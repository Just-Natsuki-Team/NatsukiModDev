init python in jn_threading:
    import store
    import store.jn_utils as jn_utils
    import threading
    import uuid

    def fire_and_forget(function, args=()):
        """
        Creates and starts a new, untracked background thread given a function and args that runs without blocking execution.
        This will not return a result, therefore only use this for things like void functions where no return is expected/needed.

        IN:
            - function - the function to call in the new thread
            - args - parameters to be passed to
        """

        if not callable(function):
            raise TypeError("function given is not a callable object")
            return

        if not isinstance(args, tuple) and not isinstance(args, list):
            raise TypeError("arguments must be given in tuple or list format")
            return

        if isinstance(args, list):
            args = tuple(args)

        try:
            thread = threading.Thread(name=uuid.uuid4(), target=function, args=args)
            thread.daemon = True
            thread.start()

        except:
            jn_utils.log(message="Failed to launch thread for function {0} with args {1}".format(function, args), logseverity=jn_utils.SEVERITY_ERR)
