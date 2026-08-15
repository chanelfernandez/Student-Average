print("")
print("Student Information")
print("")
name = str(input("Enter your Name: "))
snum = int(input("Enter your Student Number: "))
YnS = str(input("Enter your Year and Section: "))

print("")
print ('GRADE SUBJECT')
print("")
print ("Enter your Grades per Subject")

sub1 = int(input("English : "))
sub2 = int(input("Science : "))
sub3 = int(input("Filipino : "))
sub4 = int(input("Mathematics : "))
sub5 = int(input("Social Studies : "))
sub6 = int(input("Arts : "))

def calculate_average(sub1, sub2, sub3, sub4, sub5, sub6):
    """
    
    Returns:
        float: The average score
    """
    total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
    average = total / 6
    return average

average = calculate_average(sub1, sub2, sub3, sub4, sub5, sub6)
print(f"Average: {average}")

if average < 70:
    print("You failed!")
else:
    print("You passed!")
