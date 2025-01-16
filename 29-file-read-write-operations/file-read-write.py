"""
- file operations using open method: 
    - Modes of file operations:
        - read (r)
        - write (w) - override existing content
        - append (a)
        - read and write (r+)

- close file using close method: close

- methods to operate on a file
    - read
    - write
    - writeline

- using with for file operations: To automatically handle closing of the file
"""

#------------------------------------------------
# read a file
file = open("demoFile.txt", 'r')
content = file.read()
print(content)
file.close()


# read a file line by line
file = open("demoFile.txt", 'r')
for line in file:
    print(line.strip()) #strip removes trailing new line
file.close()

# read specific number of characters
file = open("demoFile.txt", 'r')
content = file.read(10)
print(content)
file.close()

# write into a file (override existing content)
with open("C:\\Users\\PranavSrivatsavC\\Documents\\Learning\\GenAI-course\\file1.txt.txt", 'w') as file:
    file.write("Demo insertion")

# # write into a file (override existing content)
# with open("demoFile1.txt", 'w') as file:
#     file.write("Demo insertion")


