# -*- coding: utf-8 -*-
#CodeAcademy PythonPractice and woring out Sept21th2018
"""
@Author Cassie
"""

text1="a spoonfull of sugar"
word1="sugar"
mywords = text1.split(" ")
#print(mywords)

def censor(t, w):
  words =t.split(" ")
  for j in words:
      if ( j == w): 
        censor_word = "*" * len(w)
  censor_text = ' '.join(words)
  return print(censor_text.replace(w, censor_word))
  

result1 = censor(text1, word1)      
result2 = censor("the rain in Spain falls mainly on the plain", "rain")

#the Solution!!  my way works too
def censor2(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result

solution_result = censor2("the rain in Spain", "rain")#does work!!
print ("The solution result is :" + solution_result)

 
#removes odd numbers from a list?? 
def count1(sequence, item):
  ct = 0
  for i in sequence:
    if (i == item):
      ct += 1
  
  return ct
#counts the number of odd numbers, prints 8
print(count1([1,2,1,1,1,1,1,1,1], 1))


def purify(my_list):
  new_list = my_list
  for i in new_list:
    if(i % 2 == 1):
      new_list.remove(i)

  return new_list

numbers_list = [1,2,3,4,5,6,7,8,9,10]
other_list = [4,5,4]   
print(purify(numbers_list))
print(purify(other_list))   

#The solution  - this finds even numbers and puts them into a new list 
def purify(lst):
    res = []
    for ele in lst:
        if ele % 2 == 0:
            res.append(ele)
    return res

#Next exercice function to multi all the list elements eg 4*5*8=100
def product(product_lst):
  results_product = 1
  for element in product_lst:
    if (element >= 1):
      results_product = results_product * element 
            
  return results_product

prod_list = [4,5,5]
print(prod_list[0])
print(product(prod_list))
#solution
def product(list):
  total = 1
  for num in list:
    total = total * num
  return total
#remove duplicate item from a list
  
def remove_duplicates(dup_list):
  new_list2 = []
  for item in dup_list:  
    if (item not in new_list2):
      new_list2.append(item)
        
  return new_list2

print(remove_duplicates([1,4,55,55,4,1]))

# find the medium in a list, if even number add the two centre numbers /2 
list1= [4,2,5,3,1]
list2=[1,6,3,4,5,2]
list3=[4,5,5,4]
def median(a_list):
  a_list.sort()
  length = len(a_list)
  if(length%2 == 0):
    a = int(length/2)
    median = float(a_list[a] + a_list[a - 1])/2
    return median
  else:
    median = 0
    median = int(length / 2)
    
    return a_list[median]

print(median(list1))# should give median of 3
print(median(list2))# should give median of 3.5
print(median(list3))# should give mediam of 4.5


#statistics function practice code academy tutorial
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades_input):
  for grade in grades_input:
    print (grade)
    
def grades_sum(scores):
  sum = 0.0
  for num in scores:
    sum = sum + num
    
  return sum

res = grades_sum(grades)
print(res) 

def grades_average(grades_input):
  sum = grades_sum(grades_input)
  ave = sum / float(len(grades_input))
  return ave

result = grades_average(grades)
print(result)
#to check the variance in the students scores:how much do they vary from the average?  
def grades_variance(scores):
  average = float(grades_average(scores))
  variance = 0
  for score in scores:
    score =  float(average - score)**2
    variance = variance + score
  result = variance / len(scores) 
  return result
  
print(grades_variance(grades))

#standard diviation is the square root of the variance calculated by raising the number to the one-half power

def grades_std_deviation(variance):
  result = float(variance ** 0.5)
  return result 

variance = (grades_variance(grades))
  
print ("GRADES")  
print_grades(grades)
print(grades_sum(grades)) 
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))


