#using new keyword to create an object of string is not a practice

name = "sai eswar"

print(name.lower());
print(name.upper());
print(name.islower());
print(name.isupper());
print(name.startswith("E"));
print(name.endswith("R"));
print(name.startswith("e"));
print(name.endswith("r"));
# print(name.concatinate("kumar")); #concat is not present in python
print(name.title());
print(""" 


""")
name1 = "Sai"
print(name1.isalpha());
print(name1.isalnum());
print(name1.isdecimal());

paragraph = "       hai this is eswar from github      "
print(paragraph.strip(), "\"remove \\white space\"")

test1 = "hai this is eswar"
print(test1.replace("i", "w") , "replace the characters")

test2 = "hairaibe"
print(test2.split("i"), "splitting")
print("-".join(test2), "joining")
print(test2.find("r"))


print(len(test2), "finding the length") # finding the length of the string
print("rai" in test2)  # finding character or substring present in string

print(test2[0]);    #finding first index character
print(test2[len(test2)-1]); #finding last index character 