"""
Nested Lists

Given the names and grades for each student in a Physics class of N students, 
store them in a nested list and print the name(s) of any student(s) 
having the second lowest grade.

Note: If there are multiple students with the same grade, 
order their names alphabetically and print each name on a new line.

Input Format:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; 
the first line contains a student's name, 
and the second line contains their grade.

Constraints:
2 <= N <= 5
There will always be one or more students having the second lowest grade.

Output Format:
Print the name(s) of any student(s) having the second lowest grade in Physics; 
if there are multiple students, order their names alphabetically 
and print each one on a new line.

Sample Input: 
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:
Berry
Harry

Explanation:
There are 5 students in this class whose names and grades 
are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], 
                   ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. 
The second lowest grade of 37.21 belongs to both Harry and Berry, 
so we order their names alphabetically and print each name on a new line.

@author: Luísa Maria
"""
def sort_byName(alist):
    return alist[0]
    
def sort_byGrades(alist):
    return alist[1]
       
def nested_lists():
    number_entries = int(input("Number of students: "))
    students = []
    
    if(number_entries < 2 or number_entries > 5):
        return "Error!"
    
    while(number_entries > 0):
        name = input("Name: ")
        grade = float(input("Grade: "))
        
        new_student = [name, grade]
        students.append(new_student)
               
        number_entries = number_entries - 1
      
    #sort by students's names
    students.sort(key = sort_byName, reverse = False)
    
    #sort by students's grades
    students.sort(key = sort_byGrades, reverse = False)
    
    student_with_second_lowest_grade = students[1]
        
    for student in students:
        if(student[1] == student_with_second_lowest_grade[1]):
            print(student[0])
            
        
    
        
    
