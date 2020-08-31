
note1 = "The If clause can be executed by first typing if, then the conditions, then a colon, then 4 spaces, then finally the command"
note2 = "You can write more than one command to be executed under the if statement as long as it is separted and has 4 lines as well"
note3 = "The command line can have 3, 4, 5, or more spaces. However, this needs to be identical for any following commands.\nIf you use 6 spaces instead of 4, then the following statements also need to contain 6 spaces"
note4 = "You can write an independent line of code that will always execute regardless of the If clause as long as it does not have any spaces."
note5 = "The if clause can contain more than two conditions by using the elif function in between"
note6 = "The elif function can be written several times"
note7 = "Alternatively, instead of writing multiple elif lines, the if statement can be written under the else statement"


print(note1)

a = 1
b = 2
if a < b:
    print('a is less than b\n')


print(note2)



a = 1
b = 2
if a < b:
    print('a is less than b')
    print('yes, Im sure that a is less than b')


print ("\n")
print(note3)



a = 1
b = 2
if a < b:
    print('a is less than b')
    print('Yes, I am sure that a is less than b\n')



print(note4)



# in this cell, c is greater than d so the if clause is not fulfilled
# as a result the print statement in the clause will not show
# however, the separate line of code will still appear
c = 3
d = 2
if c < d:
    print('a is less than b')
print('I exist no matter what\n')



print(note5)



# In this cell there are three categories. Positive, negative, and neither a.k.a zero
# Using the elif statement, it is possible to create a condition for more than just two possibilities
c = -4

if c < 0:
    print("c is a negative number")
elif c == 0:
    print("c is equal to zero")
else:
    print("c is a positive number")

# %%

print(note6)

# %%

# as mentione dbefore, the elif can be written more than once
# this allows statements which can apply to virtually any number of conditions
e = 100

if e < 10:
    print("e is a single digit integer")
elif e < 100:
    print("e is a two-digit integer")
elif e < 1000:
    print("e is a three-digit integer")

# %%

print(note7)

# %%

# In this cell there are 3 different statements which can be true
# instead of repeating elif, the if clause was used several times within the else statement

f = -128
print("f is equal to:")
print(f)
if f < 0 and f > -10:
    print("f is a single digit negative integer")
else:
    if f <= -10 and f > -100:
        print("f is a two digit negative integer")
    else:
        if f <= -100 and f > -1000:
            print("f is a three digit negative integer")
