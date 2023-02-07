f = open('Grades_2016.txt', 'r').read()
grades = eval(f)


# sort houses that are in Circle/Crescent
grades_list = []
for i in range(len(grades)):
  if grades[i][1] == "Form IV" or grades[i][1] == "Form III":
    grades_list.append(grades[i])
sorted_houses = sorted(grades_list)

#functions
#create dictionary with houses as keys, values set to 0
def create_house_dict(list):
  house_dict = {}
  for element in list:
    house_dict[element[3]] = []
  return house_dict

#function to calculate average GPA
def calculate(gradesList):
  total = 0
  average = 0
  for element in gradesList:
    if element == "A+":
      total = total + 4.3
    elif element == "A":
      total = total + 4.0
    elif element == "A-":
      total = total + 3.7
    elif element == "B+":
      total = total + 3.3
    elif element == "B":
      total = total + 3.0
    elif element == "B-":
      total = total + 2.7
    elif element == "C+":
      total = total + 2.3
    elif element == "C":
      total = total + 2.0
    elif element == "C-":
      total = total + 1.7
    elif element == "D":
      total = total + 1.0
    elif element == "D-":
      total = total + 0.7
    elif element == "F":
      total += 0.0
  average = total/len(gradesList)
  return average

#Chivers
house_dict = create_house_dict(sorted_houses)
for element in sorted_houses:
  for house in house_dict:
    if element[3] == house:
      house_dict[house].append(element[4])
def chivers():
  chiversHouses = house_dict
  for house in chiversHouses:
    chiversHouses[house] = calculate(chiversHouses[house])
  house_list = list(zip(chiversHouses.values(), chiversHouses.keys()))
  house_list = sorted(house_list)
  print("Drum roll for Chivers Cup awardees...\n")
  print(f"The house with the highest average GPA goes to {house_list[10][1]} with an average GPA of {house_list[10][0]:.5}!")
  print(f"The house with the second highest average GPA goes to {house_list[9][1]} with an average GPA of {house_list[9][0]:.5}!")
  print(f"The house with the third highest average GPA goes to {house_list[8][1]} with an average GPA of {house_list[8][0]:.5}!")
#call function
chivers()

#Green
house_dict2 = create_house_dict(sorted_houses)
for element in sorted_houses:
  for house in house_dict2:
    if element[3] == house:
      house_dict2[house].append(element[4])
def green():
  fall = create_house_dict(sorted_houses)
  spring = create_house_dict(sorted_houses)
  diff = create_house_dict(sorted_houses)
  house_dict2 = create_house_dict(sorted_houses)
  for element in sorted_houses:
    for house in house_dict2:
      if element[3] == house:
        if element[2] == "T1":
          fall[house].append(element[4])
        elif element[2] == "T3":
          spring[house].append(element[4])
  for house in fall:
    fall[house] = calculate(fall[house])
  for house in spring:
    spring[house] = calculate(spring[house])
  for house in diff:
    diff[house] = spring[house]-fall[house]
  diff_list = list(zip(diff.values(), diff.keys()))
  diff_list = sorted(diff_list)
  #print(diff_list)
  print("\nDrum roll for Green Cup...\n")
  print(f"The Green Cup goes to {diff_list[10][1]} with an increase of {diff_list[10][0]:.4}!")
  print(f"The house with the second highest increase in average GPA goes to {diff_list[9][1]} with an increase of {diff_list[9][0]:.4}!")
  print(f"The house with the second highest increase in average GPA goes to {diff_list[8][1]} with an increase of {diff_list[8][0]:.4}!")
#call function
green()

#High Honors, Dean's List
#Checking GPA for High Honors qualifications
def hh():
  if element[4] == "A+" or element[4] == "A" or element[4] == "A-":
    for grade in values:
      if element[4] == grade:
        element[4] = values[grade]
    print(element[0], element[1], element[2], element[3], element[4])

#Checking GPA for Deans' List qualifications
def dl():
  if element[4] == "B+":
    for grade in values:
      if element[4] == grade:
        element[4] = values[grade]
    print(element[0], element[1], element[2], element[3], element[4]) 

values = {"A+":4.3, "A":4.0,"A-":3.7, "B+":3.3, "B":3.0, "B-":2.7, "C+":2.3, "C":2.0, "C-":1.7, "D":1.0, "D-":0.7, "F":0.0}

print("\nHigh Honors (GPA for the term > 3.6) and Deans' List (GPA for the term is between 3.2 and 3.6) awardees: ")

while True:
  listType = input("\nFor High Honors , type in 'HH'. For Deans' List, type in 'DL' . ")
  if listType.upper() == "HH" or listType.upper() == "DL":
    break
  
while True:
  term = input("Which term? (1, 2 or 3) ")
  if term == "1" or term == "2" or term == "3":
    break

if listType.upper() == "HH":
  if term == "1":
    for element in grades:
      if element[2] == "T1":
        hh()
  if term == "2":
    for element in grades:
      if element[2] == "T2":
        hh()   
  if term == "3":
    for element in grades:
      if element[2] == "T3":
        hh()
elif listType.upper() == "DL":
  if term == "1":
    for element in grades:
      if element[2] == "T1":
        dl()
  if term == "2":
    for element in grades:
      if element[2] == "T2":
        dl()    
  if term == "3":
    for element in grades:
      if element[2] == "T3":
        dl()




