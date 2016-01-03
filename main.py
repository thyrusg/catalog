import argparse

parser = argparse.ArgumentParser()

# Argument for the filename the user can specify
parser.add_argument("name", help="Name of the document", type=str, default=None)

# Argument for indexing option
parser.add_argument("-i", "--index", help="Search the current directory for specified file types and add to DB")

# Argument for searching DB of documents
parser.add_argument("-s", "--search", help="Search DB for the name and return some information")

parser.add_argument("-o", "--open", help="Open up the document in the OS's default application")

args = parser.parse_args()

# Execute the index option
if args.index:
    print "Indexing the directory"

# Execute the search option
if args.search:
    print "Searching for the file"

# Execute the open option
if args.open:
    print "Opening the file"
