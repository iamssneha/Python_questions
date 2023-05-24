# Take three int values from user and print greatest and smallest among them.
# value1 = 12
# value2 = 10
# value3 = 15

value1 = int(input("Enter the value1 is :  "))
value2 = int(input("Enter the value2 is :  "))
value3 = int(input("Enter the value3 is :  "))

if value1> value2 and value1>value3 : 
    print("GREATEST NUMBER", value1)
if value1< value2 and value1< value3 : 
    print("SMALLEST", value1)

if value2> value1 and value2>value3: 
    print("GREATEST NUMBER", value2)
if value2< value1 and value2< value3 : 
    print("SMALLEST", value2)

if value3> value2 and value3>value1 : 
    print("GREATEST NUMBER", value3)
if value3< value2 and value3< value1 : 
    print("SMALLEST", value3)




