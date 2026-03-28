# Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

Words=["apple","banana","kiwi","cherry","mango"]
length_info={}
for i in Words:
    length_info[i]=len(i)
print(length_info)