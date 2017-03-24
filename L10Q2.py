#-------------------------------------------
# 
# Program: L10Q2.py
#Purpose:To take a height value from the user and create a image that displays three different stripes with various colors
#-------------------------------------------
from PIL import Image
# a function to print out the first red stripe
def first_stripe(height,image):
    for y in range(0,height):
         red_color = 0
         for x in range(0, 256):
             image.putpixel((x,y),(red_color,0,0))
             red_color = red_color +1




# A function to print out the second green stripe
def second_stripe(height,image):
    new_color = (0,255,0)
    for y in range((height*2),(height*4)):
        for x in range(0, 256):
            image.putpixel((x,y), new_color)




# A function to print out the third blue stripe
def third_stripe(height,image):
     for y in range(int((height/2)*3),(int((height*2)+(height / 2)))):
         blue_color = 255
         for x in range(0, 256):
            image.putpixel((x,y), (0,0,blue_color))
            blue_color = blue_color - 1

#Main function
def draw_stripes():

    #Asking for the Height of the canvas
    value = int(input("Please enter the overall height: "))
    print(value)




    #Calculating the heights of each stripe
    stripe1_height = int(value * 0.4)
    stripe2_height = int(value * 0.2)
    stripe3_height = int(value * 0.4)
    print(stripe2_height,stripe3_height,stripe1_height)

      # Creating the canvas to work with
    width = 256
    height = value
    size = (width, height)
    picture = Image.new('RGB', size, 'white')

    #Calling the other functions and printing the image
    first_stripe(stripe1_height,picture)
    second_stripe(stripe2_height,picture)
    third_stripe(stripe3_height,picture)
    picture.show()





#Calling the Main function
draw_stripes()
