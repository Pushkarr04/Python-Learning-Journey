name=input("Enter username : ")
sentence=input("Enter a sentence :")


alphabets =0
digit=0
space=0
sp_character=0
count=0
vowel=0
consonant=0
uppercase=0
lowercase=0
for i in sentence:
    count+=1
print(f"lenghth : {count}")
print("first character : ",sentence[0:1])
print("last character : ",sentence[-1:])
print("\nfirst five  character : ",sentence[0:5])
print("last five character : ",sentence[-5:])

for i in sentence:
    if('A'<=i <='Z' or 'a'<=i <='z'):
        alphabets+=1
        if i in "AEIOUaeiou":
            vowel+=1
        else:
            consonant+=1
    
        if("A"<=i <="Z"):
            uppercase+=1
        else:
            lowercase+=1

        
    elif("0"<=i <="9"):
        digit+=1
    elif(i==" "):
        space+=1
    else:
        sp_character+=1

    


    

print(f"\nalphabets : {alphabets}")
print(f"Digit : {digit}")
print(f"space : {space}")
print(f"special character : {sp_character}\n")

print(f"vowels : {vowel}")
print(f"consonant  : {consonant}\n")

print(f"uppercase : {uppercase}")
print(f"lowercase : {lowercase}")


