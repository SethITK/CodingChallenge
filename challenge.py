import csv
import argparse
import json

# Defines and gives a description to the argument challenge.py
parser = argparse.ArgumentParser(prog='challenge.py', 
                                 description="Filters and prints out the .tsv file in a JSON file.", 
                                 exit_on_error=True)

# Add an argument and give a help message that explains the purpouse of the (tsv) argument list.
parser.add_argument('tsv', action="store", help="Required command to filter and print out the .tsv file in a JSON file.")

# Parses the argument and returns an object with it's values.
args = parser.parse_args()

def filterWriteFile():

    # Open input2.tsv path file in read only mode.
    with open("./input/input2.tsv", "r") as inputFile:
        # Create the .json file in write only mode.
        with open("output.json", "w+") as outputFile:
            # Reading input2.tsv file with the cvs library, giving it a delimiter of tab.
            file = csv.DictReader(inputFile, delimiter='\t')

            # For in loop in file
            for line in file:
                # Dump the filtered information in the JSON file.
                json.dump(line, outputFile, indent=6)


            outputFile.close()
            inputFile.close()

    return 1


filterWriteFile()