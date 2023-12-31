-------------------------------------------------------------------------------------------------
**Today is Saturday 30th (2023)**

Btw I'm not an english speaker, but every thing in this "proyect" will be in English language.
The deal is that I'll be learning Python and English in the same way and I'll try to do my best. 
(I'm using an online course by Nate Gentile so far).


-------------------------------------------------------------------------------------------------

# Input and using "int" in there.

**An example of this is:**
```
num_x = int(input("Put x number here: "))
num_y = int(input("Put y number here: "))
print(num_x + num_y)
```

**I just learned that putting up "int" in input is necessary to the execution of the code,if it uses integers.The opposite of "str" inputs and this is something like a "rule"? because if we don't use "int" we'll got:**
```
"TypeError: unsupported operand type(s) for +: 'int' and 'str'."
```

## In another test I'm using "max" and "min" tho the the maximum number of the user's inputs:
```
num_1 = int(input("Put the first number: "))
num_2 = int(input("Put the second number: "))
num_3 = int(input("Put the third number: "))

print(max(num_1, num_2, num_3))
print(min(num_1, num_2, num_3))
```

## Well, now I just have learned how to use "{}".format

Definition and Usage. The format() method formats the specified value(s)and insert them inside
the string's placeholder. The placeholder is defined using curly brackets: {}.

```
num_1 = int(input("Put the first number: "))
num_2 = int(input("Put the second number: "))
num_3 = int(input("Put the third number: "))

print("The largest number between {}, {} and {}, is {}, and the smallest is: {}"
                                                               .format(num_1, num_2, num_3,
                                                                max(num_1, num_2, num_3),
                                                                min(num_1, num_2, num_3)))
Output:

Put the first number: 52517
Put the second number: 1
Put the third number: 762
The largest number between 52517, 1 and 762, is 52517, and the smallest is: 1
```
## Now I just made a Fahrenheit => Celsius converter

```
fahrenheit = int(input("Put fahrenheit here: "))
celsius = (fahrenheit-32)*5/9
print("{}° fahrenheit equals to:{}° celsius".format(fahrenheit, celsius)

Output:

Put fahrenheit here: 10
°10 fahrenheit equals to:-12.222222222222221° celsius
```
## Pesos ==> Dollars converter

**Now I'm using "float" because is needed to make the operation possible. (integers can't be used to money conversion if you want exact values)**
```
pesos = float(input("Put your pesos quantity here: "))
conversion = float(input("Put the standard conversion to dollars"))
dollars = (pesos*conversion)

print("your pesos quantity is {}, and will be converted using
the conversion of {}, that equals to {} dollars"
.format(pesos, conversion, dollars))

Output:

Put your pesos quantity here: 50000
Put the standard conversion to dollars3800
your pesos quantity is 50000.0, and will be converted using
the conversion of 3800.0, that equals to 13.157894736842104 dollars

```









