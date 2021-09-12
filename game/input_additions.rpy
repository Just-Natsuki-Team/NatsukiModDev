# Original Paste code and Sub-Selections v2 by LegendKiller21
# Copy, Cut, Select All, and Original Markers for Sub-Selections and Sub-Selections v2 optimizations by LordBaaa

init 1 python:
    config.keymap['input_paste'] = ['ctrl_K_v']
    config.keymap['input_copy'] = ['ctrl_K_c']
    config.keymap['input_cut'] = ['ctrl_K_x']
    config.keymap['input_select_all'] = ['ctrl_K_a']
    config.keymap['input_move_select_left'] = ['ctrl_K_LEFT', 'ctrl_repeat_K_LEFT']
    config.keymap['input_move_select_right'] = ['ctrl_K_RIGHT', 'ctrl_repeat_K_RIGHT']

init 999 python:
    import pygame

    setattr(renpy.display.behavior.Input, 'select_start_pos', None)
    setattr(renpy.display.behavior.Input, 'select_end_pos', 0)
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
            self.select_start_pos = self.caret_pos
            self.select_end_pos = self.caret_pos

        if self.select_end_pos <= 0:
            return
        self.select_end_pos -= 1

    def move_selected_right(self):
        if self.select_start_pos is None:
            self.select_start_pos = self.caret_pos
            self.select_end_pos = self.caret_pos

        if self.select_end_pos >= len(self.content)-2:
            return
        self.select_end_pos += 1

    def render_selected_markers(self):
        text_wo_markers = get_content_wo_markers(self) #DEBUG:

        if self.select_start_pos is None:
            self.update_text(text_wo_markers, self.editable, check_size = True)

        mark1_pos = self.select_start_pos
        mark2_pos = self.select_end_pos

        if mark1_pos > mark2_pos:
            mark1_pos, mark2_pos = mark2_pos, mark1_pos

        text_w_markers = text_wo_markers[:mark1_pos]+"\u231C"+text_wo_markers[mark1_pos:mark2_pos]+"\u231F"+text_wo_markers[mark2_pos:]

        self.update_text(text_w_markers, self.editable, check_size = True)

    def get_content_wo_markers(self):
        content = self.content
        content = content.replace("\u231C", '')
        content = content.replace("\u231F", '')

        return content


    setattr(renpy.display.behavior.Input, 'move_selected_left', move_selected_left)
    setattr(renpy.display.behavior.Input, 'move_selected_right', move_selected_right)
    setattr(renpy.display.behavior.Input, 'render_selected_markers', render_selected_markers)

    map_event = renpy.display.behavior.map_event

    def event_ov(self, ev, x, y, st):
        self.old_caret_pos = self.caret_pos

        if not self.editable:
            return None

        l = len(self.content)

        raw_text = None

        if map_event(ev, "input_backspace"):

            if self.content and self.caret_pos > 0:
                content = self.content[0:self.caret_pos-1] + self.content[self.caret_pos:l]
                self.caret_pos -= 1
                self.update_text(content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()

        elif map_event(ev, "input_enter"):

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
            self.render_selected_markers()

        elif map_event(ev, "input_move_select_right"):
            self.move_selected_right()
            self.render_selected_markers()

        elif ev.type == pygame.TEXTEDITING:
            self.update_text(self.content, self.editable, check_size=True)

            raise renpy.display.core.IgnoreEvent()

        elif ev.type == pygame.TEXTINPUT:
            self.edit_text = ""
            raw_text = ev.text

        elif ev.type == pygame.KEYDOWN:
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

            if self.content and self.caret_pos < l:
                if (
                    (self.start_marker_pos == 0 and self.caret_pos != self.start_marker_pos)
                    or (self.end_marker_pos == l and self.caret_pos != self.end_marker_pos-1)
                    or (self.caret_pos != self.start_marker_pos and self.caret_pos != self.end_marker_pos)
                    or not (self.start_marker_is_set and self.end_marker_is_set)
                ):
                    content = self.content[0:self.caret_pos] + self.content[self.caret_pos+1:l]
                    if self.start_marker_pos < self.caret_pos <= self.end_marker_pos:
                        self.end_marker_pos -=1
                    elif self.caret_pos < self.start_marker_pos:
                        self.start_marker_pos -=1
                        self.end_marker_pos -=1

                    self.update_text(content, self.editable)

                    if self.start_marker_pos == self.end_marker_pos-1:
                        content = list(self.remove_marker_text(self.content))
                        self.reset_marker_values()
                        self.caret_pos -= 1
                        content = "".join(content)
                        self.update_text(content, self.editable)

            renpy.display.render.redraw(self, 0)
            raise renpy.display.core.IgnoreEvent()


    setattr(renpy.display.behavior.Input, 'event', event_ov)
