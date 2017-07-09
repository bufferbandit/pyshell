# Small python shell by @bufferbandit

blockstarts = ("if","else","def","class","with","for","try","except","while")
inblock = False                             # We're not in a block yet
prefix = "Py >>> "                          # Initialize the prefix
with open("client","w") as c:c.write('')    # Clean out the file on a new run
while 1:                                    # Start the loop
    i = input(prefix)                       # Set input
    c = open(".commands","a")               # Open the (hidden) command file
    if i.startswith(blockstarts) :          # Checks if block starts
        inblock = True                      # We're in a block now
        prefix =  " "*len(prefix) +  "    " # Prefix get's changed to indentation
        c.write(i + "\n")                   # Block start get's written
        c.close()                           # Close file
    elif not inblock:                       # If we're not in a block...
        try:                                # Try to execute a command
            c.write(i + "\n")               # Write a new line
            c.close()                       # Close file
            exec(open(".commands").read())  # Execute the command
            with open(".commands","w") as c:# Open the file
                c.write('')                 # And clean it out 
            continue                        # Continue the loop
        except Exception as e:              # Catch exceptions and print them nicely
            print("[!] Error: {}".format(e))# Print the error in a nice format
            with open(".commands","w") as c:# Open the file
                c.write('')                 # And clean it out
    elif inblock:                           # If we're in a block   
        if i == "":                         # See if we did hit enter
            prefix = "Py >>> "              # Re-initialize the prefix
            inblock = False                 # We're not in the block anymore
        else:                               # If not hit enter...       
            c.write("    " + i + "\n")      # Write file with indentation
            c.close()                       # Close file
            exec(open(".commands").read())  # So now we can execute whole of the block
            with open(".commands","w") as c:# Open the file
                c.write('')                 # And clean it out

                
