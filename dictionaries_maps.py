"""
Dictionaries and Maps

Given n names and phone numbers, assemble a phone book 
that maps friends' names to their respective phone numbers. 
You will then be given an unknown number of names to query your phone book for. 
For each name queried, print the associated entry 
from your phone book on a new line in the form name=phoneNumber; 
if an entry for name is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input Format:
The first line contains an integer, n, denoting the number of entries 
in the phone book.
Each of the n subsequent lines describes an entry 
in the form of 2 space-separated values on a single line. 
The first value is a friend's name, and the second value 
is an 8-digit phone number.

After the n lines of phone book entries, 
there are an unknown number of lines of queries. 
Each line (query) contains a name to look up, 
and you must continue reading lines until there is no more input.

Note: Names consist of lowercase English alphabetic letters 
and are first names only.

Constraints:
    1 <= n <= 10**5
    1 <= queries <= 10*5
    
Output Format:
On a new line for each query, 
print Not found if the name has no corresponding entry in the phone book; 
otherwise, print the full name and phoneNumber in the format name=phoneNumber.

Sample Input:
3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output:
sam=99912222
Not found
harry=12299933

Explanation:
We add the following n=3 (Key,Value) pairs to our map so it looks like this:

    phoneNumber = {(sam, 99912222), (tom, 11122222), (harry, 12299933)}

We then process each query and print key=value 
if the queried key is found in the map; otherwise, we print Not found.

Query 0: sam
Sam is one of the keys in our dictionary, so we print sam=99912222.

Query 1: edward
Edward is not one of the keys in our dictionary, so we print Not found.

Query 2: harry
Harry is one of the keys in our dictionary, so we print harry=12299933.

@author: Luísa Maria
"""
def count(astring):
    number = int(astring)
    count = 0    
    while(number > 0):
        count = count + 1
        number = number // 10        
    return count

def search(name, adict):
    for item in adict.items():
        if(item[0] == name):
            return True
    return False
              
def dictionaries_maps():
    number_entries = int(input("Number of entries: "))
    number_queries = number_entries
    phoneNumber = {}

    if(number_entries < 1 or number_entries >= 10**5):
        return "Error!"
    
    while(number_entries > 0):
        entry = input("Name and phone number: ")
        entry_tuple = tuple(entry.split(" "))
        
        if(count(entry_tuple[1]) != 8):
            return "Error!"
        
        phoneNumber[entry_tuple[0]] = entry_tuple[1]
    
        number_entries = number_entries - 1
        
    while(number_queries > 0):
        query = input("Name to search for: ")
        if(search(query, phoneNumber) == True):
            print(query + "=" + phoneNumber[query])
        else:
            print("Not found")   
        number_queries = number_queries - 1 
   
