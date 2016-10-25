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

def searchPeople(personsName):
    # Looks up the name in the epic dictionary
    try:
        # Tries the following lines of texts, and if
        # there are no errors then it runs
        personsInfo = epic_programmer_dict[personsName]
        print ('Name: ' + personsName.title())
        print ('Email: ' + personsInfo[0])
        print ('Number: ' + str(personsInfo[1]))

    except:
        # If there are errors, then this code gets run.
        print ('No information found for that name')

userWantsMore = True
while userWantsMore == True:
    # Ask user to input person's name
    # raw_input() in python 2.x has been replaced by input() in python 3.x
    personsName = input('Please enter a name: ').lower()

    # Run our new function searchPeople with what was typed in
    searchPeople(personsName)
    userWantsMore = False

    # See if user wants to search again
    searchAgain = input('Search again? (y/n)')

    # Look at what they reply and act accordingly
    if searchAgain == 'y':
        # userWantsMore stays as True so loop repeats
        userWantsMore = True
    elif searchAgain == 'n':
        # userWantsMore turns to False to stop loop
        userWantsMore = False
    else:
        # user inputs an invalid response, so we quit anyway
        print ("I don't understand what you mean, quitting")
        userWantsMore = False
        

print (epic_programmer_dict)

print (personsName)


