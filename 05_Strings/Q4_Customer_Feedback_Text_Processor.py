username=input("Enter username : ")
feedback=input("Enter customer feedback : ")

exclaimation_count=0
dot_count=0
coma_count=0
alphabets_count=0
uppercase_count=0
lowercase_count=0
space_count=0
digit_count=0
vowel_count=0
consonant_count=0
sp_character_count=0
upper_consonant_count=0
lower_consonant_count=0
upper_vowel_count=0
lower_vowel_count=0
total_length=0
# product_count=0

length=len(feedback)

first_character=feedback[0]
last_character=feedback[-1:]
words=feedback.split()
first_word=words[0]
last_word=words[-1]
striped=feedback.strip()
feedback_lower=feedback.lower()
feedback_upper=feedback.upper()
title_case=feedback.title()
capitalized=feedback.capitalize()
currency_convert=feedback.replace("Rs.","₹")
exclaimation_replace=feedback.replace("!",".")
product_find=feedback_lower.find("product")
last_product_find=feedback_lower.rfind("product")
good_find=feedback_lower.find("good")
bad_find=feedback_lower.find("bad")

for i in feedback:
    if(i=="!"):
        exclaimation_count+=1
    elif(i=="."):
        dot_count+=1
    elif(i==","):
        coma_count+=1

the_count=feedback_lower.count("the")
product_count=feedback_lower.count("product")

total_words=len(words)
longest=words[0]
shortest=words[0]
for word in words:
    if len(word)>len(longest):
        longest =word
    if len(word)<len(shortest):
        shortest=word

for word in words:
    total_length+=len(word)
average=total_length/total_words

for i in feedback:
    if('A'<=i <='Z'):

        alphabets_count+=1
        uppercase_count+=1
        if i in "AEIOU":
            upper_vowel_count+=1
        else:
            upper_consonant_count+=1

    elif('a'<=i <='z'):
        alphabets_count+=1
        lowercase_count+=1
        if i in "aeiou":
            lower_vowel_count+=1
        else:
            lower_consonant_count+=1
    
    

        
    elif("0"<=i <="9"):
        digit_count+=1
    elif(i==" "):
        space_count+=1
    else:
        sp_character_count+=1

vowel_count=upper_vowel_count+lower_vowel_count
consonant_count=lower_consonant_count+upper_consonant_count

start_with_the=feedback.lower().startswith("the")
end_with_dot=feedback.endswith(".")

refund = "refund" in feedback.lower()

excellent="excellent" in feedback.lower()


print("="*30)
print("CUSTOMER FEEDBACK REPORT")
print("="*30)

print(f"\n username : {username}")

print(f"original feedback : {feedback}\n")

print("-"*30)

print(f"length : {length}")
print(f"first character : {first_character}")
print(f"last character : {last_character}")
print(f"first word : {first_word}")
print(f"last word : {last_word}\n")

print("-"*30)

print("cleaned feedback \n")
print(f"trimmed : {striped}")
print(f"lower case : {feedback_lower}")
print(f"upper case : {feedback_upper}")
print(f"title case  :{title_case}")
print(f"capitalized : {capitalized}")
print(f"currency updated : {currency_convert}")
print(f"exclaimation update  :{exclaimation_replace}\n")

print("-"*30)

print("SEARCH REPORT ")
print(f"first'product' : {product_find}")
print(f"last 'product' : {last_product_find}")

print(f"first 'good' : {good_find}")
print(f"first 'bad' : {bad_find}\n")

print("-"*30)

print(f"\n count report")

print(f"! count : {exclaimation_count}")
print(f". count : {dot_count}")
print(f", count  : {coma_count}")
print(f"'the' count : {the_count}")
print(f"'product' count : {product_count}\n")

print("-"*30)

print("WORD ANALYSIS ")
print(f"Total words : {total_words}")
print(f"longest word : {longest}")
print(f"shortest word : {shortest}")
print(f"average word length : {average}")

print("-"*30)

print("\n CHARACTER STATISTICS")

print(f"alphabets : {alphabets_count}")
print(f"lower case : {lowercase_count}")
print(f"upper case : {uppercase_count}")
print(f"digit : {digit_count}")
print(f"vowels : {vowel_count}")
print(f"consonant : {consonant_count}")
print(f"space :  {space_count}")
print(f"special character : {sp_character_count}")

print("-"*30)

print("\nVALIDATION")

print(f"starts with 'The' : {start_with_the}")
print(f"end with .  : {end_with_dot}")
print(f"contains 'refund' : {refund}")
print(f"contains  'excellent' : {excellent}")











