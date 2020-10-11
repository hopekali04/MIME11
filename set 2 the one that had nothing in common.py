horizontal = ["Hello my name is Hope Kalitera","What’s New In Python 3.9,In addition to the standard library","there is a growing collection of several thousand components", "pydoc — Documentation generator and online help system", "unittest — Unit testing framework",'A Path represents a path that is hierarchical and composed of a sequence of directory and file name elements separated by a special separator or delimiter','Accessing a file using an empty path is equivalent to accessing the default directory of the file system']
vertical2 = ["This-line-has-no-spaces-it","What’s New In Python 3.9","Documentation generator and online help system"]
output = set(horizontal) & set(vertical2)
if output == set():
    print ('This sets have nothing in common')
else :
    print ("ok")
print (output)
