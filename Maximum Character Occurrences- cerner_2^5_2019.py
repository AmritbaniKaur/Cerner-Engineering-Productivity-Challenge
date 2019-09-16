#cerner_2^5_2019

def maxCharOccurrences(string1, string2, charToFind):
   count1 = string1.count(charToFind)
   count2 = string2.count(charToFind)
   if(count1 > count2):
       print(string1)
   else:
       print(string2)

string1 = "Cerner"
string2 = "Cerner Corporation"
charToFind = "C"

maxCharOccurrences(string1, string2, charToFind)

