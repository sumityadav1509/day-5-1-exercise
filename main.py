# total=0
# for number in range(1,101):
#  total+=number

# print(total) 
# sum_of_even_number=0
# for number in range(1,101):
#   if number%2==0:
#     # print(number) 
#     sum_of_even_number+=number 


# print(f"The sum of all numbers that are even is :{sum_of_even_number}")
  
  # Fizz Buzz Code : 

for number in range(1,19) :
  # Mistake was made here as i had forgot to check that both the conditions should be true at the intitial start rather than towards the end.
  if number%3==0 and number%5==0:
     print("FizzBuzz")
  elif number%5==0:
     print("Buzz")   
  elif number%3==0:
      print("Fizz") 
  else:
    print(number)    
    
    
        