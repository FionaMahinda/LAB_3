# using a for loop
str = "This sentence has 27 chars." [::-1]

for i in str:
    print(i, end = "")

#using a function
def reverse (i):
    return i[::-1]

str = reverse ("This sentence has 27 chars.")
print(f"{str}")

#negative indexing
str = "This sentence has 27 chars."
print (str [::-1])

#join method
str = "This sentence has 27 chars."
reversedstr = "".join(reversed(str))
print(reversedstr)
