sentence=input("Enter a sentence : ")
print("="*30)
print("TEXT ANALYSIS AND TRANSFORMATION")
print("="*30)

print(f"original sentence : {sentence}")
print(f"sentence length : ",len(sentence))
print(f"First character : ",sentence[0])
print(f" last character : ",sentence[-1:])

word=input("enter a new word to add : ")

print(f"new sentence : ",sentence+ word)

new_sentence=input("enetr a new sentence : ")

if(sentence==new_sentence):
    print(f"comparison result : both sentence are same ")
else:
    print("comparison result :  both sentence are different ")

search=input("Enter a word to search : ")

if search  in sentence:
    print("search result : word found in sentence ")
else: 
    print("search result : word not found in sentence")

character=input("enter a character you want to check frequency : ")
char_frequency=sentence.count(character)

print(f"chracter frequency : {character} appears {char_frequency} times in sentence ")

pattern=input("Enter word to found : ")

found=False
for i in range(len(sentence)-len(pattern)+1):
    match=True
    for j in range(len(pattern)):
        if(sentence[i+j]!=pattern[j]):
            match=False
            break
    if match:
        found=True
        print("substring found at index ",i)
        break
if not found :
    print("Substring not found!")




old_char=input("enter a charcter you want to replace from sentence : ")
new_char=input("enter character to replace with  :")
result=""
for i in sentence:
    if(i==old_char):
        result+=new_char
    else: 
        result+=i
print(f"modified sentence : {result}")

reverse=""
for i in sentence:
    reverse=i+reverse
print(f"reverse string : {reverse}")

    
print("="*30)