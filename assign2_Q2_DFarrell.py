assignment1 = input("Enter grade for assignment 1: ")
assignment2 = input("Enter grade for assignment 2: ")
exam1 = input("Enter grade for exam 1: ")
exam2 = input("Enter grade for exam 2: ")

assignAvg = (float(assignment1) + float(assignment2))/2
examAvg = (float(exam1) + float(exam2))/2

finalGrade = ((assignAvg * (40/100)) + (examAvg * (60/100)))

finalGradeFormatted = "{:.2f}".format(finalGrade)

print("Final Grade: " + finalGradeFormatted)