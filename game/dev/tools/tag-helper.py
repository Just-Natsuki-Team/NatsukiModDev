# This helper script will take a file input, apply {w} tags based on the dialogue tag pattern in use, and return the {w}-tagged output.
# This saves having to insert tags manually, and helps reduce untagged dialogue having to be correct.
# For best results, only insert blocks of dialogue - do not add logic (I.E conditions), as this runs the risk of accidental replacement!

import os

target_file_and_path = os.path.join(os.path.dirname(__file__), "dialogue.txt")

if os.path.isfile(target_file_and_path):

    # Load in from source file
    source_file = open(target_file_and_path, "r")
    content = source_file.read()
    source_file.close()

    # Perform replacements
    content = content\
        .replace("... ", "...{w=0.3} ")\
        .replace(". ", ".{w=0.2} ")\
        .replace("? ", "?{w=0.2} ")\
        .replace("! ", "!{w=0.2} ")\
        .replace("- ", "-{w=0.1} ")\
        .replace(", ", ",{w=0.1} ")\
        .replace("; ", ";{w=0.1} ")

    # Write back
    destination_file = open(target_file_and_path, "w")
    destination_file.write(content)
    destination_file.close()
    print("Done! Remember to check dialogue before committing.")

else:
    # No source file found; create and return
    new_source_file = open(target_file_and_path)
    new_source_file.close()
    print(f"Target file {target_file_and_path} not found and was created instead, insert dialogue to tag and retry.")