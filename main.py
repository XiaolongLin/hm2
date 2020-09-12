def getGradePoint(grade1):
  if grade1 == "A":
    gradepoint1 = 4
  elif grade1 =="A-":
    gradepoint1 = 3.67
  elif grade1 == "B+":
    gradepoint1 = 3.33
  elif grade1 == "B":
    gradepoint1 = 3
  elif grade1 == "B-":
    gradepoint1 = 2.67
  elif grade1 == "C+":
    gradepoint1 = 2,33
  elif grade1 == "C":
    gradepoint1 = 2
  elif grade1 == "D":
    gradepoint1 = 1
  else :
    gradepoint1 = 0
  return gradepoint1
def getGradePoint2(grade2):
  if grade2 == "A":
    gradepoint2 = 4
  elif grade2 =="A-":
    gradepoint2 = 3.67
  elif grade2 == "B+":
    gradepoint2 = 3.33
  elif grade2 == "B":
    gradepoin2 = 3
  elif grade2 == "B-":
    gradepoint2 = 2.67
  elif grade2 == "C+":
    gradepoint2 = 2,33
  elif grade2 == "C":
    gradepoint2 = 2
  elif grade2 == "D":
    gradepoint2 = 1
  else :
    gradepoint2 = 0
  return gradepoint2
def getGradePoin3(grade3):
 if grade3 == "A":
    gradepoint3 = 4
  elif grade3 =="A-":
    gradepoint3 = 3.67
  elif grade3 == "B+":
    gradepoint3 = 3.33
  elif grade3 == "B":
    gradepoint3 = 3
  elif grade3 == "B-":
    gradepoint3 = 2.67
  elif grade3 == "C+":
    gradepoint3 = 2,33
  elif grade3 == "C":
    gradepoint3 = 2
  elif grade3 == "D":
    gradepoint3 = 1
  else :
    gradepoint3 = 0
  return gradepoint3  
  
def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  print(f"Grade point for course 1 is: {getGradePoint(grade1)}")
  credit1 = int(credit1)
  gradepoint1 = getGradePoint(grade1)
  grade2 = input ("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  print(f"Grade point for course 2 is: {getGradePoint(grade2)}")
  credit2 = int(credit2)
  gradepoint2 = getGradePoint(grade2)
  grade3 = input ("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  print(f"Grade point for course 3 is: {getGradePoint(grade3)}")
  credit3 = int(credit3)
  gradepoint3 =getGradePoint(grade3)
  
  print(f"Your GPA is: {gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)} ")
  

   

 
if __name__ == "__main__":
 run()


