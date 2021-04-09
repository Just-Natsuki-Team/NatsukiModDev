#well here goes nothing..

init python:

    class Natsuki_displayable(renpy.Displayable):

        def __init__(self, body=None, outfit=None, face=None, eyes=None, eyebrows=None, mouth=None):

            super(Natsuki_displayable, self).__init__()
            
            if body == None : body = "mod_assets/natsuki/empty.png"
            if outfit == None : outfit = "mod_assets/natsuki/empty.png"
            if face == None : face = "mod_assets/natsuki/empty.png"
            if eyes == None : eyes = "mod_assets/natsuki/empty.png"
            if eyebrows == None : eyebrows = "mod_assets/natsuki/empty.png"
            if mouth == None : mouth = "mod_assets/natsuki/empty.png"

            self.body = body
            self.outfit = outfit
            self.face = face
            self.eyes = eyes
            self.eyebrows = eyebrows
            self.mouth = mouth
            
            self.child = Null()
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):
            

            self.child = im.Composite(
                (1280, 720),
                (0, 0), self.body,
                (0, 0), self.outfit,
                (0, 0), self.face,
                (0, 0), self.eyes,
                (0, 0), self.eyebrows,
                (0, 0), self.mouth)
            self.child = Flatten(self.child)

            t = Transform(child=self.child)
            child_render = renpy.render(t, width, height, st, at)
            self.width, self.height = child_render.get_size()


            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (0, 0))

            # Return the render.
            return render

        def visit(self):
            return [ self.child ]