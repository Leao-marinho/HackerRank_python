# -*- coding: utf-8 -*-
"""
Finding the percentage

You have a record of N students. Each record contains the student's name, 
and their percent marks in Maths, Physics and Chemistry. 
The marks can be floating values. The user enters some integer N
followed by the names and marks for N students. 
You are required to save the record in a dictionary data type. 
The user then enters a student's name. 
Output the average percentage marks obtained by that student, 
correct to two decimal places.

Input Format:
The first line contains the integer N, the number of students. 
The next N lines contains the name and marks obtained by that student 
separated by a space. The final line contains 
the name of a particular student previously listed.

Constraints:
    2 <= N <= 10
    0 <= Marks <= 100

Output Format:
Print one line: The average of the marks obtained 
by the particular student correct to 2 decimal places.

Sample Input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output:
56.00

Explanation:
Marks for Malika are {52,56,60}  whose average is 52+56+60 / 3 = 56


@author: Luísa Maria Mesquita
"""

def calculate_media(name, adict):
    marks = adict[name]
    marks = [float(mark) for mark in marks]
    
    sum_ = sum(marks)
    
    media = round(sum_/3, 2)
    
    return media
    
    
def finding_percentage():
    n = int(input("Number of entries: "))
    
    if(n < 2 or n > 100):
        return "Error!"
    
    adict = {}
    
    while(n >= 0):
        name_and_marks = input()
        
        name_and_marks = name_and_marks.split(" ")
        
        if(n == 0):
            name = name_and_marks[0]
            media = calculate_media(name, adict)
            return ("{:.2f}".format(media))
        
        if(len(name_and_marks) != 4):
            return "Error!"
        
        if(float(name_and_marks[1]) < 0 or float(name_and_marks[1]) > 100):
            return "Error!"
        if(float(name_and_marks[2]) < 0 or float(name_and_marks[2]) > 100):
            return "Error!"
        if(float(name_and_marks[3]) < 0 or float(name_and_marks[3]) > 100):
            return "Error!"
        
        adict[name_and_marks[0]] = [name_and_marks[1], name_and_marks[2], name_and_marks[3]]
        
        n = n - 1
        
        
        
