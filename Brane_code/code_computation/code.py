#!/usr/bin/env python3

# Imports
import os
import sys
import yaml
import pandas as pd
import matplotlib.pyplot as plt



def read(name: str) -> str:
    """
        Reads the given file in the distributed filesystem and returns its contents.
    """

    # Once again we wrap the reading in a try/catch so we may catch any errors
    try:
        # Open the file and read the content
        with open(f"/data/{name}.txt", "r") as f:
            content = f.read()
        store=pd.read_csv("/data/store.csv")
        store.dropna(axis=0, how='any',inplace=True)
        store.to_csv(f"/data/{name}_new.csv")
        # Return the string
        return content

    # Catch file errors
    except IOError as e:
        # Return the error message
        return f"ERROR: {e} ({e.errno})"



# The entrypoint of the script
if __name__ == "__main__":
    # Make sure that at least one argument is given, that is either 'write' or 'read'
    if len(sys.argv) != 2 or (sys.argv[1] != "write" and sys.argv[1] != "read"):
        print(f"Usage: {sys.argv[0]} write|read")
        exit(1)

    # If it checks out, call the appropriate function
    command = sys.argv[1]
    if command == "write":
        # Write the file and print the error code
        print(yaml.dump({ "code": write(os.environ["NAME"], os.environ["CONTENTS"]) }))
    else:
        # Read the file and print the contents
        print(yaml.dump({ "contents": read(os.environ["NAME"]) }))

    # Done!

