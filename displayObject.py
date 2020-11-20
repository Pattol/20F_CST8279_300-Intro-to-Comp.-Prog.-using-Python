from gfxhat import lcd,  fonts, backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar


def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayObject(obj,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(obj)
    draw.text((x,y), obj, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    backlight.set_all(255, 155, 155)
    backlight.show() 



# for x in range(128):
#     for y in range(64):
#         pixel = image.getpixel((x, y))
#         lcd.set_pixel(x, y, pixel)

lcd.show()

def Games(x=63,y=50):
    lcd.set_pixel(x, y, 1)
    backlight.show()
    lcd.show()

f1 =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,0,0,
0,1,1,0,0,0,0,0,0,0,0,0,0,0]
lcd.show()

pm =[0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,
1,1,1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,0
,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0]


x = 0
if x in f1:
   x = 64
   x-= 1
   lcd.set_pixel(x, y, 1)
   lcd.show()

else:
  print()

y=0
if y in pm:
   y = 64
   y -= 1
   lcd.set_pixel(x, y, 1)
   lcd.show
else:
    print()