#Author: Duaa
#Date: November 19, 2019
#Grade Display

int_gradeOne = (int)(input("Enter your first best mark: "))
int_gradeTwo = (int)(input("Enter your second best mark: "))
int_gradeThree = (int)(input("Enter your third best mark: "))
int_gradeFour = (int)(input("Enter your fourth best mark: "))
int_gradeFive = (int)(input("Enter your fifth best mark: "))
int_gradeSix = (int)(input("Enter your sixth best mark: "))

average = (int_gradeOne + int_gradeTwo + int_gradeThree + int_gradeFour + int_gradeFive + int_gradeSix) / 6

if average >= 80 and average <= 100:
    print("Excellent-Honours")
elif average >= 65 and average <= 79:
    print("Good")
elif average >= 50 and average <= 64:
    print("Fair")
else:
    print("Poor")
