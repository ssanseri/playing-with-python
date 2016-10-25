# DRILL: 
# Write a program in Python 2.7 using IDLE that demonstrates the following concepts. 
# Use comments in your program to denote where you demonstrate each step. If you cannot demonstrate any of these comments, research them online first. If you still have trouble, then ask an Instructor for assistance. 
# 1. Assign an integer to a variable
# 2. Assign a string to a variable
# 3. Assign a float to a variable
# 4. Use the print function and .format() notation to print out the variable you assigned
# 5. Use each of these operators +, ­ , * , / , +=, ­= , %
# 6. Use of logical operators and, or , not
# 7. Use of conditional statements: if, elif, else
# 8. Use of a while loops
# 9. Use of a for loop
# 10. Creating a list and iterate through that list using a for loop to print each item out on a new line
# 11. Create a tuple and iterate through it using a for loop to print each item out on a new line
# 12. Defining a function that returns a string variable
# 13. Call the function you defined above and print the result to the shell
# Once this is completed, email what you wrote to an Instructor.

# 12. Defining a function that returns a string variable
def make_first_letter_of_string_capital (x):
    capital_string = x.capitalize()
    return capital_string

# 13. Call the function you defined above and print the result to the shell
print (make_first_letter_of_string_capital("hello world!"))

# 1. Assign an integer to a variable
days_of_christmas = 12

# 2. Assign a string to a variable
song_title = " Days of Christmas"
on_the = 'On the '
event = ' day of Christmas my true love sent to me:'

# 3. Assign a float to a variable
real_number = 3.14159

# 4. Use the print function and .format() notation to print out the variable you assigned
print (str(days_of_christmas) + song_title + " " + str(real_number))

# 5. Use each of these operators +, ­ , * , / , +=, ­= , %
x = 3
y = 4
print ('x = 3, y = 4')
print ('x + y = ' + str(x+y))
print ('x - y = ' + str(x-y))
print ('x * y = ' + str(x*y))
x += y
print ('x += y = ' + str(x))
x -= y
print ('x -= y = ' + str(x))
print ('x % y = ' + str(x % y))
       
# 10. Creating a list and iterate through that list using a for loop to print each item out on a new line
ordinal_names = ['first', 'second', 'third', 'fourth',
                 'fifth', 'sixth', 'seventh', 'eighth',
                 'ninth', 'tenth', 'eleventh', 'twelfth',]

# 11. Create a tuple and iterate through it using a for loop to print each item out on a new line
gifts_of_christmas = {'first' : 'a partridge in a pear tree.',
                      'second' : 'Two turtledoves',
                      'third': 'Three french hens',
                      'fourth': 'Four calling birds',
                      'fifth': 'FIVE GOLDEN RINGS',
                      'sixth': 'Six geese a-laying',
                      'seventh': 'Seven swans a-swimming',
                      'eighth': 'Eight maids a-milking',
                      'ninth': 'Nine ladies dancing',
                      'tenth': 'Ten lords a-leaping',
                      'eleventh': 'Eleven pipers piping',
                      'twelfth': 'Twelve drummers drumming',}

# 9. Use of a while loop
# Go from 1-12 on the days of Christmas
day = 1
while day <= days_of_christmas:
    # print ('On the nth day of Christmas my true love gave to me:')
    print (on_the + ordinal_names[day-1] + event)

    # 8. Use of a for loop
    # print all the gifts starting from day # going down to 1
    for gift in range(day, 0, -1):
        # to actually print the string, subtract 1 from the index because
        # lists are 0-based.
        lookup_key = ordinal_names[gift-1]

        # 7. Use of conditional statements: if, elif, else
        # 6. Use of logical operators and, or , not

        # if printing the last gift on any day except the first, put 'and'
        # before the partidge in the pear tree
        if day > 1 and gift == 1:
            print ('and ' + gifts_of_christmas[lookup_key])

        # should out FIVE GOLDEN RINGS gift
        elif gift == 5:
            print (gifts_of_christmas[lookup_key].upper() + '!')

        # print the gift normally
        else:
            print (gifts_of_christmas[lookup_key].capitalize())

        # end of for loop    
    # print a new line between each day
    print (' ')
    day += 1        
# end of while loop



