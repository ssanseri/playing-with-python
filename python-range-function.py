#!/usr/bin/env python

# print 0 (newline)... 1, 2, 3
stop = 4
for i in range(stop):  # [0..3]
    print (i)

# print a line break
print ('')

# print 3, 2, 1, 0
start = 3
stop = -1
step = -1
# when index value reaches stop value,
# the code inside the loop will not be executed
for i in range(start, stop, step):
    print (i)

# print a line break
print ('')

# print 8, 6, 4, 2
start = 8
stop = 0
step = -2
for i in range(start, stop, step):
    print (i)

    
