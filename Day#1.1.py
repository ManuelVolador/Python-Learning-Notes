num_1 = int(input("Put the first number: "))
num_2 = int(input("Put the second number: "))
num_3 = int(input("Put the third number: "))

print("The largest number between {}, {} and {}, is {}, and the smallest is: {}".format(num_1, num_2, num_3,
                                                                max(num_1, num_2, num_3),
                                                                min(num_1, num_2, num_3)))

fahrenheit = int(input("Put fahrenheit here: "))
celsius = (fahrenheit-32)*5/9
print("°{} fahrenheit equals to:{}° celsius".format(fahrenheit, celsius))


pesos = float(input("Put your pesos quantity here: "))
conversion = float(input("Put the standard conversion to dollars"))
dollars = (pesos/conversion)
print("your pesos quantity is {}, and will be converted using the conversion of {}, that equals to {} dollars"
      .format(pesos, conversion, dollars))

