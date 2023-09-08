#how to use open: open(path_to_file, mode)
# which modes are there: r: Open for text file for reading text
# w: Open a text file for writing text
# s : Open a text file for appending text

#example:  f = open('the-zen-of-python.txt','r')

f = open('AOC_day1.txt', 'r')

# methods for reading text from a text file:
# read(size)
# readline()
# readlines()



# also you have to close the file when finished using it because it will still be open, when not either automatically or manually closed.
#
# Ways to do these:
# automatically:
# with open(path_to_file) as f:
#     contents = f.readlines()
#
# manually:
#
# f.close()


# Define the variable to store the lines
lines_to_append = []

# Open the text file in read mode
with open('AOC_day1.txt', 'r') as file:
    # Read the lines and append them to the variable
    for line in file:
        lines_to_append.append(line)

# Now, you can append additional lines to the variable
lines_to_append.append("This is a new line.")
lines_to_append.append("Another new line.")

# Print or do whatever you want with the appended lines
for line in lines_to_append:
    print(line, end='')

# Optionally, you can write the updated lines back to the file
with open('your_file.txt', 'a') as file:
    for line in lines_to_append:
        file.write(line)
