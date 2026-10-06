# . Ask the user for a string and print:
    # • All unique characters
    # • The count of unique characters

str=input("enter a string : ")
print("all unique characters: ")
for i in str:
    print(i)

#count of string unique characters
s = "hello"
freq = {}

for i in s:
    freq[i] = freq.get(i, 0) + 1

for key in freq:
    if freq[key] == 1:
        print(key)