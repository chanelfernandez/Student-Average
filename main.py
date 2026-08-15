def calculate_average(sub1, sub2, sub3, sub4, sub5, sub6):
    """
    Calculate the average of 6 subjects.
    
    Args:
        sub1, sub2, sub3, sub4, sub5, sub6: Score for each subject
    
    Returns:
        float: The average score
    """
    total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
    average = total / 6
    return average

print(f"Average: {average}")

if average < 70:
    print("You failed!")
else:
    print("You passed!")