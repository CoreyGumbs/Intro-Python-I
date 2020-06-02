"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
def readFile(x):
    #open file with read flag
    file = open(x, 'r')

    #read lines in file and loop
    for line in file.readlines():
        #print out each line
        print(line)

    #close file
    file.close()

#call func
readFile('foo.txt')

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
def createFile(file, lines):
    newFile = open(file, 'w+')
    newFile.writelines(lines);
    newFile.close()

myLines = ["This is bar.txt \n", "Hello, world! \n", "My name is Corey Gumbs. \n", "I like coding. \n"]

createFile('bar.txt', myLines)
readFile('bar.txt');