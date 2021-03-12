python early:
    def dummy(*args, **kwargs):
        """
        Dummy function. Does absolutely nothing
        """
        return

    renpy.execution.check_infinite_loop = dummy
