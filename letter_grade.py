Write a fruitful python function which computes and returns a letter grade based on a percentage grade. The percentage grade is the single parameter of this function and should be a number between 0 and 100.  Your function should return an error message if the value of the argument is not within this range. The assignment of the letter grade should be based on the table in the syllabus of this course.  

Note that this involves both conditional execution and functions.

def grade(x):
    score = (x)
    
    if score>100.0 or score<0.0:
        return "Please only enter a numeric value between 0 and 100, example 90% enter grade(90)"
    elif score>=95.0:
        return "A"
    elif score>=90.0:
        return "A-"
    elif score>=86.0:
        return "B+"
    elif score>=83.0:
        return "B"
    elif score>=80.0:
        return "B-"
    elif score >= 76.0:
        return "C+"
    elif score >= 73.0:
        return "C"
    elif score>=70.0:
        return "C-"
    elif score>=65.0:
        return "D+"
    elif score >= 60.0:
        return "D"
    elif 0.0== score < 60.0:
        return "F"
    else:
        return "Please only enter a numeric value between 0 and 100, example 90% enter grade(90)"
        
# can also be void and provide results by printing

def grade(x):
    score = (x)
    
    if score>100.0 or score<0.0:
        print("Please only enter a numeric value between 0 and 100, example 90% enter grade(90)")
    elif score>=95.0:
        print("A")
    elif score>=90.0:
        print("A-")
    elif score>=86.0:
        print("B+")
    elif score>=83.0:
        print("B")
    elif score>=80.0:
        print("B-")
    elif score >= 76.0:
        print("C+")
    elif score >= 73.0:
        print("C")
    elif score>=70.0:
        print("C-")
    elif score>=65.0:
        print("D+")
    elif score >= 60.0:
        print("D")
    elif 0.0== score < 60.0:
        print ("F")
    else:
        return "Please only enter a numeric value between 0 and 100, example 90% enter grade(90)"
  
