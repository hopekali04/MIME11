"""
Checking to see if two or more lists have members in common
"""
horizontal = ["Hello my name is Hope Kalitera","What’s New In Python 3.9,In addition to the standard library","there is a growing collection of several thousand components", "pydoc — Documentation generator and online help system", "unittest — Unit testing framework",'A Path represents a path that is hierarchical and composed of a sequence of directory and file name elements separated by a special separator or delimiter','Accessing a file using an empty path is equivalent to accessing the default directory of the file system']
vertical = ["Hello my name is Hope Kalitera", "addition to the standard library", "there is a growing collection of several thousand components", "Documentation generator and online help  system", "unittest Unit testing framework"]
vertical2 = ["This-line-has-no-spaces-it","What’s New In Python 3.9","Documentation generator and online help system"]
vertical3 = ["Hello my name is Hope Kalitera", "addition to the standard library", "there is a growing collection of several thousand components", "Documentation generator and online help  system", "unittest Unit testing framework"]
output = set(horizontal) & set (vertical)
print (f"The common sentences in our vertical file and horizontal file are, {output}")
output2 = set(horizontal) & set (vertical2)
if output2 == set():
    print ("horinzontal and vertical2",'have nothing in common')
else :
    print (f"The common sentences in our Second vertical file and horizontal file are, {output2}")
output3 = set(horizontal) & set (vertical3)
print (f"The common sentences in our Third vertical file and horizontal file are, {output3}")
print ("\n")
#to get number of members in our output
number = (len(output))
number2 = (len(output2))
number3 = (len(output3))
print ("Number of members in output", number)
print ("Number of members in common2", number2)
print ("Number of members in common3", number3)
og_number = (len(vertical))
og_number2 = (len(vertical2))
og_number3 = (len(vertical3))
print ("number of members in vertical", og_number)
print ("number of members in vertical", og_number)
print ("number of members in vertical", og_number)
#og_number is the number of members in vertical
unique_members = og_number - number
unique_members2 = og_number2 - number
unique_members3 = og_number3 - number
print (f"Members that are not similar to the other list or set = {unique_members}")
print (f"Members that are not similar to the other list or set = {unique_members2}")
print (f"Members that are not similar to the other list or set = {unique_members3}")

