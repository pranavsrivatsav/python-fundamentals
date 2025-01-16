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

#------------------------------------------------

#write into a file 
#if file exists - (override existing content) - will clear and write content
with open("demoFile.txt", 'w') as file:
    file.write("Demo insertion")

#if file does not exist, will create new file and write into it
with open("demoFile1.txt", 'w') as file:
    file.write("Demo insertion")

#------------------------------------------------

#append into a file
with open("demoFile.txt", 'a') as file:
    file.write("\nAppending content")

#------------------------------------------------

#read and write access to a file using r+
#but it will not create a new file if it does not exist
with open("demoFile.txt", 'r+') as file:
    #in r+ mode - write operations will be done over the existing file

    #currently because of the above appending - the demo file content will be
    # "Demo insertion\nAppending content"

    file.write("Overriding content")
    
    #Now the demo file content will be "Overriding contentpending content"
    
    #There is one more concept in play here, file pointer position

    currentPosition = file.tell()
    print(currentPosition) #18, but why 18?
    #As we ask the file to write the content, the file pointer position is initially from 0, and as it starts writing the content, the position will keep moving based on the character, some characters might need more than one byte, since ours is a simple words containing alphabets "Overriding content" - which has a length of 18, the current file position is at 18

    #And now if we do a read operation, guess what is the output?
    content = file.read()
    print(content) #pending content 
    #because the pointer is now at the position 18

    #so to read the file properly, let's move the pointer position back to the start of the file (i.e 0)
    file.seek(0)
    content = file.read()
    print(content) #Overriding contentpending content

#note: in w mode, the file will be cleared and overwritten
with open("demoFile.txt", 'w') as file:
    file.write("Demo insertion")
