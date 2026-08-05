text=str(input("Enter ypur paragraph:")).lower()
character=len(text)
spaces=text.count(" ")
words=len(text.split())

vowels="aeiou"
vowel_count=0
for i in text:
    if i in vowels:
        vowel_count+=1

print("\n===========text analiyse===============")
print("Total character",character)
print("Total spaces:",spaces)
print("Total wors:",words)




if len(text)>0:
    print("first character (indexing):",text[0])
    print("last character (indexing:)",text[-1])

print("first 10 character (slicing):",text[:10])
print("last 10 character (slicing):",text[-10:])