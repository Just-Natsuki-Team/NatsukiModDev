init python in jn_poems:

    class JNPoem:
        __init__(
            reference_name,
            display_name,
            unlocked,
            poem
        ):
            self.reference_name = reference_name
            self.display_name = display_name
            self.poem = poem
            self.unlocked = False