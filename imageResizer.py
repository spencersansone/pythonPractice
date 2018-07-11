import PIL
from PIL import Image

filename =input("Enter image filename: ")
i = Image.open(filename)
print(
"""
Current Info
============
Width: {}
Length: {}
""".format(i.size[0],i.size[1])
)

width = int(input("Enter new width: "))
length = int(input("Enter new height: "))
newFilename = input("Enter new filename: ")

i.resize((width,length), Image.ANTIALIAS).save(newFilename)


