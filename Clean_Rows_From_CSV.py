from pathlib import Path # This module offers classes representing filesystem paths with semantics appropriate for different operating systems
import sys #This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter

# Read the second commandline argument which will be the source path and filename and send it to a string called Sourcefilepath
Sourcefilepath = str(sys.argv[1])

# Read the third commandline argument which will be the destination path and filename and send it to a string called Destinationfilepath
Destinationfilepath = str(sys.argv[2])

# Read the Fourth commandline argument which will be the Name of the first column send it to a string called ColumnName
ColumnName = str(sys.argv[3])

# Read the file at filepath location into a string called CSVFileContent
CSVFileContent = Path(Sourcefilepath).read_text()

# Find within the string the text "Department Family" as we know this is the column name of the first column 
position = CSVFileContent.index(ColumnName)

# open a file for writing name it the same as the original by adding one place to slashindex
textfile = open(Destinationfilepath, "w")

# write the file from the index of Department Family to the end thereby removing the header from the new file
textfile.write(CSVFileContent[position:])

# Close the new file
textfile.close()
