# Marks input by students 

student_scores=input("Input a list of student scores").split()  
# print(len(student_scores))
# Forgot to use the split function upwards as it is required to split the data to be placed inside a list below.
for n in range(0,len(student_scores)):
  student_scores[n]=int(student_scores[n]) 

print(student_scores) 
highest_score=0
for score in student_scores:
  
  if score>highest_score:
    highest_score=score 
    print(f"The highest score is : {highest_score}")
