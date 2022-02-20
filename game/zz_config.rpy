init 10000 python:
    # Allows us to define our own quit behaviour by jumping to a label on force quit, instead of defaulting to Confirm screen
    # If you touch this, or break this, I will destroy you - Blizz :)
    config.quit_action = Jump("jn_quit_action")