"""
Checking to see if two or more lists have members in common
"""
horizontal = ["Hello my name is Hope Kalitera","What’s New In Python 3.9,In addition to the standard library","there is a growing collection of several thousand components", "pydoc — Documentation generator and online help system", "unittest — Unit testing framework",'A Path represents a path that is hierarchical and composed of a sequence of directory and file name elements separated by a special separator or delimiter','Accessing a file using an empty path is equivalent to accessing the default directory of the file system']
vertical = ["Hello my name is Hope Kalitera", "addition to the standard library", "there is a growing collection of several thousand components", "Documentation generator and online help  system", "unittest Unit testing framework"]
####sets
"""horizontal and verical are our variables, which contain our lists
to get the common members in our lists they must be sets
so as in venn diagrams the point of interception contains the common members in the sets
so is our variable |output| so the & sign is inputed to you know what
to clarify the similarity between or among the sets
"""
output = set(horizontal) & set (vertical)
print (f"The common sentences in our vertical file and horizontal file are, {output}")
print ("\n")
#to get number of members in our output
number = (len(output))
print ("Number of members in output", number)
og_number = (len(vertical))
print ("number of members in vertical", og_number)
#og_number is the number of members in vertical
unique_members = og_number - number
print (f"Members that are not similar to the other list or set = {unique_members}")

