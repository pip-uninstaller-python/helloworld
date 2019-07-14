# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#convert user input to value and save the result
def cipher(code):
    
    result = []
    for letter in code:
        key = ord(letter) +97
        result.append(key)
    print(result)
   
    decipher(result)
     
           

#convert value back to character
def decipher(result):
    finish = ""
    
    for number in result:
        unkey = int(number)
        unkey = chr(unkey-97)
        finish = finish + unkey    
    print(finish)
        


def main():
    
    code = input("Enter the string you want encrypt: ")
    cipher(code)
  
main()