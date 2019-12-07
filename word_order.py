"""
Word Order

You are given n words. Some words may repeat. 
For each word, output its number of occurrences. 
The output order should correspond with the input order of appearance 
of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
    1 <= n <= 10**5
    The sum of the lengths of all the words do not exceed 10**6
    All the words are composed of lowercase English letters only.

Input Format:
The first line contains the integer, n.
The next n lines each contain a word.

Output Format:
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences 
for each distinct word according to their appearance in the input.

Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
3
2 1 1

Explanation:
There are 3 distinct words. Here, "bcdef" appears twice in the input 
at the first and last positions. 
The other words appear once each. 
The order of the first appearances are "bcdef", "abcdefg" and "bcde" 
which corresponds to the output.

@author: Luísa Maria Mesquita
"""
def count(astring, alist):
    count = 0
    for i in range(0, len(alist)):
        if(alist[i] == astring):
            count = count + 1
    return count
    
def word_order():
    n = int(input("Number of entries: "))
    
    words = {}   
    alist = []
    
    #creates a list with all the words
    while(n > 0):
        word = input("Word: ")
        
        alist.append(word)
        
        n = n - 1
    
    # creates a dictionary with the words as key 
    # and, as key, the number of occurrences for each distinct word 
    # according to their appearance in the input 
    for i in range(0, len(alist)):
        words[alist[i]] = count(alist[i], alist)
        
    # prints on the first line the number of distinct words from the input
    # prints on the scond line the keys of dictionary "words" 
    result = ""
    for item in list(words.items()):
        result = result + str(item[1]) + " "
        
    print(len(words.items()))
    print(result)
        
    
