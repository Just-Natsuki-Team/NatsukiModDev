init 25:
    # Allows us to define our own quit behaviour by jumping to a label on force quit, instead of defaulting to Confirm screen
    # If you touch this, or break this, I will destroy you - Blizz :)
    define config.quit_action = Function(quit_input_check)
