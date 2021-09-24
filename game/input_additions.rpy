# Original Paste code and Sub-Selections v2 by LegendKiller21
# Copy, Cut, Select All, and Original Markers for Sub-Selections and Sub-Selections v2 optimizations by LordBaaa

init 1 python:
    config.keymap['input_paste'] = ['ctrl_K_v']
    config.keymap['input_copy'] = ['ctrl_K_c']
    config.keymap['input_cut'] = ['ctrl_K_x']
    config.keymap['input_select_all'] = ['ctrl_K_a']
    config.keymap['input_move_select_left'] = ['ctrl_K_LEFT', 'ctrl_repeat_K_LEFT']
    config.keymap['input_move_select_right'] = ['ctrl_K_RIGHT', 'ctrl_repeat_K_RIGHT']
    config.keymap['input_move_select_home'] = ['ctrl_K_HOME']
    config.keymap['input_move_select_end'] = ['ctrl_K_END']

init 999 python:
    import pygame
    pygame.scrap.init()
    #no idea why but pygame.scrap.get_init apparently doesn't exist... is renpy's pygame that outdated?

    setattr(renpy.display.behavior.Input, 'select_start_pos', None)
    setattr(renpy.display.behavior.Input, 'select_end_pos', 0)
    setattr(renpy.display.behavior.Input, 'select_last_end_pos', 0)
    setattr(renpy.display.behavior.Input, 'select_start_char', "\u231C")
    setattr(renpy.display.behavior.Input, 'select_end_char', "\u231F")

    def get_selected(self):
        start_pos = self.select_start_pos
        end_pos = self.select_end_pos

        if not(start_pos and end_pos):
            return ""


        if start_pos == end_pos:
            selected = ""

        elif start_pos > end_pos:
            selected = self.content[end_pos:start_pos]

        elif start_pos < end_pos:
            selected = self.content[start_pos:end_pos]

        return selected

    def move_selected_left(self):
        if self.select_start_pos is None:
            if self.caret_pos <= 0:
                return

            self.select_start_pos = self.caret_pos
            self.select_end_pos = self.caret_pos

        if self.select_end_pos <= 0:
            return

        self.select_end_pos -= 1
        self.caret_pos = self.select_end_pos

    def move_selected_right(self):
        if self.select_start_pos is None:
            if self.caret_pos >= len(get_content_wo_markers(self)):
                return

            self.select_start_pos = self.caret_pos
            self.select_end_pos = self.caret_pos

        if self.select_end_pos >= len(get_content_wo_markers(self)):
            return

        self.select_end_pos += 1
        self.caret_pos = self.select_end_pos

    def move_selected_home(self):
        if self.caret_pos <= 0:
            return

        if self.select_start_pos is None:
            self.select_start_pos = self.caret_pos

        self.select_end_pos = 0
        self.caret_pos = self.select_end_pos

    def move_selected_end(self):
        if self.caret_pos >= len(get_content_wo_markers(self)):
            return

        if self.select_start_pos is None:
            self.select_start_pos = self.caret_pos

        self.select_end_pos = len(get_content_wo_markers(self))
        self.caret_pos = self.select_end_pos

    def render_selected_markers(self):
        text_wo_markers = get_content_wo_markers(self)

        if self.select_start_pos is None:
            self.update_text(text_wo_markers, self.editable, check_size = True)

        mark1_pos = self.select_start_pos
        mark2_pos = self.select_end_pos

        if mark1_pos > mark2_pos:
            mark1_pos, mark2_pos = mark2_pos, mark1_pos

        text_w_markers = text_wo_markers[:mark1_pos]+"\u231C"+text_wo_markers[mark1_pos:mark2_pos]+"\u231F"+text_wo_markers[mark2_pos:]

        self.update_text(text_w_markers, self.editable, check_size = True)

    def get_content_wo_markers(self):#FIXME:pls, my brain mush from this
        if self.select_start_pos is None:
            return self.content

        mark1_pos = self.select_start_pos
        mark2_pos = self.select_last_end_pos

        if mark1_pos > mark2_pos:
            mark1_pos, mark2_pos = mark2_pos, mark1_pos

        return self.content[:mark1_pos]+self.content[mark1_pos+1:mark2_pos+1]+self.content[mark2_pos+2:]

    def remove_selected_markers(self):
        if self.select_start_pos is None:
            return

        text_wo_markers = get_content_wo_markers(self)
        self.select_start_pos = None
        self.update_text(text_wo_markers, self.editable, check_size = True)

    def caret_relative2markers(self):
        pos = 0
        if self.select_start_pos < self.caret_pos:
            pos += 1

        if self.select_end_pos < self.caret_pos:
            pos += 1

        return pos

    setattr(renpy.display.behavior.Input, 'move_selected_left', move_selected_left)
    setattr(renpy.display.behavior.Input, 'move_selected_right', move_selected_right)
    setattr(renpy.display.behavior.Input, 'move_selected_home', move_selected_home)
    setattr(renpy.display.behavior.Input, 'move_selected_end', move_selected_end)
    setattr(renpy.display.behavior.Input, 'render_selected_markers', render_selected_markers)
    setattr(renpy.display.behavior.Input, 'remove_selected_markers', remove_selected_markers)

    map_event = renpy.display.behavior.map_event

    def event_ov(self, ev, x, y, st):
        self.old_caret_pos = self.caret_pos

        if not self.editable:
            return None

        l = len(self.content)

        raw_text = None

        if map_event(ev, "input_backspace"):
            self.remove_selected_markers()

            if self.content and self.caret_pos > 0:
                content = self.content[0:self.caret_pos-1] + self.content[self.caret_pos:l]
                self.caret_pos -= 1
                self.update_text(content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_enter"):
            self.remove_selected_markers()

            content = self.content

            if self.edit_text:
                content = content[0:self.caret_pos] + self.edit_text + self.content[self.caret_pos:]

            if self.value:
                return self.value.enter()

            if not self.changed:
                return content

        elif map_event(ev, "input_left"):
            if self.caret_pos > 0:
                self.caret_pos -= 1
                self.update_text(self.content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_right"):
            if self.caret_pos < l:
                self.caret_pos += 1
                self.update_text(self.content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_delete"):
            self.remove_selected_markers()

            if self.caret_pos < l:
                content = self.content[0:self.caret_pos] + self.content[self.caret_pos+1:l]
                self.update_text(content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_home"):
            self.caret_pos = 0
            self.update_text(self.content, self.editable)
            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_end"):
            self.caret_pos = l
            self.update_text(self.content, self.editable)
            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_move_select_left"):
            self.move_selected_left()

        elif map_event(ev, "input_move_select_right"):
            self.move_selected_right()

        elif map_event(ev, "input_move_select_home"):
            self.move_selected_home()

        elif map_event(ev, "input_move_select_end"):
            self.move_selected_end()

        elif map_event(ev, "input_copy"):
            pass

        elif ev.type == pygame.TEXTEDITING:
            self.update_text(self.content, self.editable, check_size=True)

            raise renpy.display.core.IgnoreEvent()

        elif ev.type == pygame.TEXTINPUT:
            self.edit_text = ""
            raw_text = ev.text

        elif ev.type == pygame.KEYDOWN:
            self.remove_selected_markers()

            if ev.unicode and ord(ev.unicode[0]) >= 32:
                raw_text = ev.unicode
            elif renpy.display.interface.text_event_in_queue():
                raw_text = ''

        if raw_text is not None:

            text = ""

            for c in raw_text:

                if self.allow and c not in self.allow:
                    continue
                if self.exclude and c in self.exclude:
                    continue

                text += c

            if self.length:
                remaining = self.length - len(self.content)
                text = text[:remaining]

            if text:

                content = self.content[0:self.caret_pos] + text + self.content[self.caret_pos:l]
                self.caret_pos += len(text)

                self.update_text(content, self.editable, check_size=True)

            raise renpy.display.core.IgnoreEvent()

        if not self.select_start_pos is None:
            self.render_selected_markers()
        self.select_last_end_pos = self.select_end_pos

    setattr(renpy.display.behavior.Input, 'event', event_ov)
