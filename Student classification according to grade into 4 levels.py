def classify_student(grade):
    if 90 <= grade <= 100:
        return "(Excellent)"
    elif 75 <= grade < 90:
        return "(Very Good)"
    elif 60 <= grade < 75:
        return "(Good)"
    else:
        return "(Poor)"


grade = int(input("enter your grade: "))
print(f"Your classification: {classify_student(grade)}")
