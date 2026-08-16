print("==" * 30)
print("Student Information")
print("==" * 30)
name = str(input("Enter your Name: "))
snum = str(input("Enter your Student Number: "))
YnS = str(input("Enter your Year and Section: "))

print("==" * 30)
print ('GRADE SUBJECT')
print("==" * 30)
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
    remark = "You failed!"
else:
    remark = "You passed!"


print("\n")
print("=" * 60)
print("                 STUDENT GRADE CARD")
print("=" * 60)

print(f"Name           : {name}")
print(f"Student Number : {snum}")
print(f"Year & Section : {YnS}")

print("-" * 60)
print("SUBJECTS AND GRADES")
print("-" * 60)

print(f"English         : {sub1}")
print(f"Science         : {sub2}")
print(f"Filipino        : {sub3}")
print(f"Mathematics     : {sub4}")
print(f"Social Studies  : {sub5}")
print(f"Arts            : {sub6}")

print("-" * 60)
print(f"Average         : {average:.2f}")
print(f"Remarks         : {remark}")