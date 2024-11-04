#imagewriter.py

img = open("testimage.ppm","w")

img.write("P3") #magic number
img.write("640 480 ") # width and height
img.write("255 ") # Max colour depth

for row in range(480):
    for pixel in range(640):
    img.write("255 0 0 ")


img.close()
