-------------------------------------------------------------------------------------------------
Btw I'm not an english speaker, but every thing in this "proyect" will be in English language.
The deal is that I'll be learning Python and English in the same way and I'll try to do my best. 
(I'm using an online course by Nate Gentile so far).

Today is Saturday 30th (2023)
-------------------------------------------------------------------------------------------------

# Input and using "int" in there.

## An example of this is:

num_x = int(input("Put x number here: "))
num_y = int(input("Put y number here: "))
print(num_x + num_y)

# We use "int" in input because we want to use integer number for this. The opposite of "str"
inputs and this is something like "rule"? because if we don't use "int" we'll got:

"TypeError: unsupported operand type(s) for +: 'int' and 'str'." 

# In another test I'm using "max" and "min" tho the the maximum number of the user's inputs:

num_1 = int(input("Put the first number: "))
num_2 = int(input("Put the second number: "))
num_3 = int(input("Put the third number: "))

print(max(num_1, num_2, num_3))
print(min(num_1, num_2, num_3))

# Well, now I just have learned how to use "{}".format

Definition and Usage. The format() method formats the specified value(s)and insert them inside
the string's placeholder. The placeholder is defined using curly brackets: {}.

´num_1 = int(input("Put the first number: "))
num_2 = int(input("Put the second number: "))
num_3 = int(input("Put the third number: "))

print("The largest number between {}, {} and {}, is: {}".format(num_1, num_2, num_3, 
                                                                max(num_1, num_2, num_3)))

Output:

  Put the first number: 23
  Put the second number: 122
  Put the third number: 3
  The largest number between 23, 122 and 3, is: 122´










