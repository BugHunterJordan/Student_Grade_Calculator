##Jordan Pangrazzi
##CIT129-1002
##8/4/25
#3 hours
#Create a program that based upon the number of students gets their name & test scores, then displays their grades based upon their score. Also displays the highest grade out of all the tests


def getStudents():   #define function to get the number of students
    numStudents = int(input("Enter the number of students (1 to 50 students): "))  #ask user to enter number of students(1-50)
    while numStudents < 1 or numStudents > 50: #if not 1-50 students
        numStudents = int(input("Invalid entry - Enter number between 1-50: "))  #display error message, while loop to ask to input proper value
    return numStudents #assigns num (called inside main) value to getStudents()

def getScores(numStudents, name, score):  #define function w/ 3 parameters to get name and score for the set of students
    for x in range(numStudents):
        n = input("Enter student's name: ")   #ask user to input name
        s = float(input("Enter student's test score: "))  #ask user to input test score
        name.append(n)  #each time user adds a new students name it goes to end of the name list
        score.append(s)  #each time user adds a new score it goes to the end of the score list

def getHighest(score):  #define function w/ 1 parameter for highest score
    return max(score)  #assigns highest (called inside main) value to getHighest()

def getGrade(numStudents, name, score, highest, grade):  #define the function w/ 5 parameters & determine letter grade 
    for g in range(numStudents):
        s = score[g]   
        if s >= highest - 10:
            grading = "A"  #Make grade A when score is >= best score - 10
        elif s >= highest - 20:
            grading = "B"  #Make grade B when score is >= best score - 20
        elif s >= highest - 30:
            grading = "C"  #Make grade C when score is >= best score -30
        elif s >= highest - 40:
            grading = "D"  #Make grade D when score is >= best score - 40
        else:
            grading = "F"  #Make grade F for any other scores 
        grade.append(grading)  #each grade gets added to the end of the grade list

def displayData(numStudents, name, score, grade, highest): #define function to display the data, w/ 5 parameters
    print("\n***Grade Report***")
    print("\nName", "\t", "Score", "\t", "Grade")  #display this column to align with the users data below to make it presentable
    for g in range(numStudents):  
        print(name[g], "\t", format(score[g], '.2f'), "\t", grade[g]) #displays the values of it's parameters in list format
    print("\nThe highest test score: ", format(highest, '.2f'))  #display the highest test score of any given by the user
    

def main():  #define main function in order to call and execute functions inside of main
    num = getStudents()   #store the return value from inside getStudents function

    name = []  #initialize a list for names entered by the user
    score = []  #initialize a list for scores entered by the user
    grade = []  #initialize a list for grades that were calculated based upon the scores provided

    getScores(num, name, score) #call the getScores function with matching parameters

    highest = getHighest(score)  #store the return value from inside getHighest function
   
    getGrade(num, name, score, highest, grade)  #call the getGrade function with matching parameters

    displayData(num, name, score, grade, highest) #call the displayData function with matching parameters

main()  #call the main function otherwise nothing will run
