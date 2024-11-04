#imagewriter.py

img = open("testimage.ppm","w")

img.write("P6") #magic number
img.write("640 480") # width and height
img.write("255") # Max colour depth

for pixel in range(640):


img.close()
