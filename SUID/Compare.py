#Work!
import argparse

print("file compare with Wordlist")

#params parser
parser = argparse.ArgumentParser(description="Compare two files Line by Line.")
parser.add_argument("-f", "--file1", help="First file to compare", required = True)
parser.add_argument("-w", "--Wordlist", help="Second file to compare", required = True)
args = parser.parse_args()


# Open Files and Read contents
with open(args.file1, "r") as f, open(args.Wordlist, "r") as w:
    lines1 = f.readlines()
    lines2 = w.readlines()

# Compare contents

for line1 in lines1:
    line1 = line1.strip()
    for line2 in lines2:
        line2 = line2.strip()
        if line1 == line2:
            print(f"Found !  {line1} == {line2}")