#Input 3 sides of triangle and check if it is a valid triangle or not
#If it is valid then print type of triangle - equilateral, isoceles or scalene
#side1 = 20cm
#side2 = 24cm
#side3 = 28cm



side1 = int(input(" The side1 of triangle is : "))
side2 = int(input(" The side2 of triangle is : "))
side3 = int(input(" The side3 of triangle is : "))


if side1+side2 > side3 and side2+side3 > side1 and side1+side3 > side2 :
    print(" The triangle is Valid ")
    if side1 == side2 and side2 ==side3 :
        print("EQUILATERAL TRIANGLE")

    elif side1 == side2  or side2 == side3 or side3 == side1   :
        print("ISOSCELES TRIANGLE")


    else :
        print("SCALENE TRIANGLE")
else :
    print("The traingle is invalid")