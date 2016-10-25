# This program will grab information such as telephone numbers,
# email addresses, etc. by inputting a name into the console.

# First, we will create a dictionary so that we can easily handle
# information such as telephone numbers and email addresses being
# attached to someone's name.

# Now, let's start by making a new file, adding the dictionary
# and checking that the dictionary works properly:

# Our epic programmer dict from before
epic_programmer_dict = {
    'tim berners-lee' : ['tbl@gmail.com', 111],
    'guido van rossum' : ['gvr@gmail.com', 222],
    'linus torvalds': ['lt@gmail.com', 333],
    'larry page': ['lp@gmail.com', 444],
    'sergey brin': ['sb@gmail.com', 555],
    }
print (epic_programmer_dict)

# raw_input() in python 2.x has been replaced by input() in python 3.x
personsName = input('Please enter a name: ').lower()
print (personsName)

try:
    # Tries the following lines of texts, and if
    # there are no errors then it runs
    personsInfo = epic_programmer_dict[personsName]
    print (personsInfo)

except:
    # If there are errors, then this code gets run.
    print ('No information found for that name')
