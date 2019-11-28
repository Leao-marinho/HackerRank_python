"""
Minion Game

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules:
 - Both players are given the same string, S.
 - Both players have to make substrings using the letters of the string S.
 - Stuart has to make words starting with consonants.
 - Kevin has to make words starting with vowels.
 - The game ends when both players have made all possible substrings.

Scoring:
 - A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:
                    BANANA
    
    STUART              KEVIN 
WORDS   SCORE        WORDS  SCORE
  B       1            A       3
  N       2            AN      2
  BA      1            ANA     2
  NA      2            ANAN    1
  BAN     1            ANANA   1
  NAN     1
  BANA    1
  NANA    1
  BANAN   1
  BANANA  1
  TOTAL   12           TOTAL   9
  
Your task is to determine the winner of the game and their score.

Input Format:
A single line of input containing the string S.
Note: The string S will contain only uppercase letters: [A - Z].

Constraints:
0 < len(S) <= 10**6

Output Format:
Print one line: the name of the winner and their score separated by a space.
If the game is a draw, print Draw.

Sample Input:
BANANA

Sample Output:
Stuart 12

Note :
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.


@author: Luísa Maria
"""
def find_substrings(word):
    substrings = []
    copy_word = word
    j = 1
    while(len(copy_word) != 0):
        for i in range(0, len(copy_word)):
            substrings.append(copy_word[:i+1])
        copy_word = word[j:]
        j = j + 1 
    return substrings  

def minion_game():
    VOWELS = ["A", "E", "I", "O", "U"]
    kevin_substrings = []
    stuart_substrings = []
    kevin_score = 0
    stuart_score = 0
    s = input("Word: ")
    
    if(len(s) < 0 or len(s) > 10**6):
        return "Error!"
    
    #finding the substrings 
    all_substrings = find_substrings(s)

    for substring in all_substrings:
        if(substring[0] in VOWELS):
            #substrings starting with a vowel
            kevin_substrings.append(substring)
        else:
            #substrings starting with a consonant
            stuart_substrings.append(substring)

    #calculating the scores
    kevin_score = len(kevin_substrings)
    stuart_score = len(stuart_substrings)
    
    #printing the result
    if(kevin_score > stuart_score):
        print("Kevin "+ str(kevin_score))
    elif(stuart_score > kevin_score):
        print("Stuart "+ str(stuart_score))
    elif(stuart_score == kevin_score):
        print("Draw")
        
    