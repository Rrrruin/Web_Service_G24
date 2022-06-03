#!/usr/bin/env python3

# Imports
import os
import sys
import yaml
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# The functions
def write(name: str, contents: str) -> int:
    """
        Writes a given string to the distributed filesystem.
    """

    # We wrap the writing in a try/catch so we may catch any errors
    try:
        # Open the file and write the content
        with open(f"/data/{name}.txt", "w") as f:
            f.write(contents)
        store=pd.read_csv("/data/store_new.csv")
        correlation = df_comb.corr()

        # Generate a mask for the upper triangle
        mask = np.zeros_like(correlation, dtype=bool)
        mask[np.triu_indices_from(mask)] = True

        # Set up the matplotlib figure
        f, ax = plt.subplots(figsize=(12, 15))

        # Draw the heatmap with the mask and correct aspect ratio
        sns.heatmap(correlation, mask=mask, vmax=.3, square=True, linewidths=.5,     cbar_kws={"shrink": .5}, ax=ax)
        plt.savefig('/data/cor.jpg')
	
        # Return 0 (i.e., "success")
        return 0

    # Catch file errors
    except IOError as e:
        # Return the non-zero exit code that they define
        return e.errno




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

