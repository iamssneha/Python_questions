#input - Marks of 5 subjects
#output - Grade

sub1 = int(input("Enter subject 1 :"))
sub2 = int(input())
sub3 = int(input())
sub4 = int(input())
sub5 = int(input())
total = sub1+sub2+sub3+sub4+sub5
print("total == 500")

if total>=400 and total <=500:
    print("Grade: A")
elif total>=300 and total<400:
    print("Grade: B")
elif total>=200 and total<300:
    print("Grade: C")
elif total>=100 and total<200:
    print("Grade: D")

else:
    print("Grade: F")