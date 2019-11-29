"""
Validating Credit Card Numbers

You and Fredrick are good friends. Yesterday, 
Fredrick received N credit cards from ABCD Bank. 
He wants to verify whether his credit card numbers are valid or not. 
You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4,5 or 6. (rule1)
► It must contain exactly 16 digits. (rule2)
► It must only consist of digits (0-9). (rule3)
► It may have digits in groups of 4, separated by one hyphen "-". (rule4)
► It must NOT use any other separator like ' ' , '_', etc. (rule5)
► It must NOT have 4 or more consecutive repeated digits. (rule6)

Examples:
Valid Credit Card Numbers:
4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers:
42536258796157867       #17 digits in card number → Invalid 
4424444424442444        #Consecutive digits are repeating 4 or more times → 
                        Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

Input Format:
The first line of input contains an integer N.
The next N lines contain credit card numbers.

Constraints:
    0 < N < 100

Output Format:
Print 'Valid' if the credit card number is valid. 
Otherwise, print 'Invalid'. Do not print the quotes.

Sample Input:
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output:
Valid
Valid
Invalid
Valid
Invalid
Invalid

Explanation:
4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234-567-8912-3456 : Invalid, because the card number is not divided 
                      into equal groups of 4.
4123356789123456 : Valid
5133-3367-8912-3456 : Invalid, consecutive digits  is repeating  times.
5123 - 4567 - 8912 - 3456 : Invalid, because space '  ' and - are used 
                            as separators.
                            
@author: Luísa Maria
"""
#returns True if starts with a 4,5 or 6
def rule1(astring):
    if(astring[0] == "4" or astring[0] == "5" or astring[0] == "6"):
        return True
    return False
    
#returns True if astring contains exactly number_digits digits
def rule2(astring, number_digits):
    count = 0
    if("-" in astring):
        for i in range(0, len(astring)):
            if(astring[i] != "-"):
                count = count + 1
        if(count == number_digits):
            return True
        return False
    else:
        count = len(astring)
        if(count == number_digits):
            return True
        return False
           
#returns True if only consists of digits (0-9)
def rule3(astring):
    result = False
    for digit in astring:
        if(digit.isdecimal() == False):
            continue
        elif(int(digit) >= 0 or int(digit) <= 9):
            result = True
        else:
            result = False
    return result

#returns True if it has digits in groups of 4, separated by one hyphen "-"
def rule4(astring):
    list_groups = astring.split("-")
    for group in list_groups:
        if(rule2(group, 4) == False):
            return False
    return True
        
    
#retruns True if does not use any other separator like ' ' , '_', etc
def rule5(astring):
    if(rule4(astring) == True):
        for i in range(-1, len(astring), 5):
            if(i == -1):
                continue
            elif(astring[i] != "-"):
                return False
            return True
        return True
    
#returns True if does not have 4 or more consecutive repeated digits
def rule6(astring):
    new_astring = astring.split("-")
    new_astring = "".join(new_astring)
    for i in range(0, len(new_astring)):
        for j in range(i+1, len(new_astring)):
            for k in range(j+1, len(new_astring)):
                for n in range(k+1, len(new_astring)):
                    if(new_astring[i] == new_astring[j] 
                        and new_astring[j] == new_astring[k]
                        and new_astring[k] == new_astring[n]):
                        return False
                    break
                break
            break
    return True
  
def number_with_hifen(astring):
    if("-" in astring):
        return True
    return False
    
def validating_credit_card_numbers():
    number_entries = int(input("Number of credit cards: "))
    
    if(number_entries <= 0 or number_entries >= 100):
        return "Error!"
    
    while(number_entries > 0):
        credit_card_number = input("Credit card number: ")
        
        if(number_with_hifen(credit_card_number)):
            if(rule1(credit_card_number) 
            and rule2(credit_card_number, 16)
            and rule3(credit_card_number)
            and rule4(credit_card_number)
            and rule5(credit_card_number)
            and rule6(credit_card_number)):
                print("Valid")
            else:
                print("Invalid")
        else:
            if(rule1(credit_card_number) 
            and rule2(credit_card_number, 16)
            and rule3(credit_card_number)
            and rule6(credit_card_number)):
                print("Valid")
            else:
                print("Invalid")
        
        number_entries = number_entries - 1








