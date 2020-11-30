from gfxhat import lcd, fonts, backlight
from PIL import Image, ImageFont, ImageDraw
from click import getchar


def clearScreen(lcd):
    lcd.clear()
    lcd.show()


def displayText(text, lcd, x, y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x, y), text, 1, font)
    for x1 in range(x, x + w):
        for y1 in range(y, y + h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    backlight.set_all(255, 155, 155)
    backlight.show()

    lcd.show()


def Games(x=63, y=50):
    lcd.set_pixel(x, y, 1)
    backlight.show()
    lcd.show()

    P = True
    while P:
        c = getchar()

        if (c == '\x1b[A'):
            if (y == 0):
                y = 64
            y -= 1
            lcd.set_pixel(x, y, 1)
            lcd.show()

        elif (c == '\x1b[B'):
            if (y == 63):
                y = -1
            y += 1
            lcd.set_pixel(x, y, 1)
            lcd.show()

        elif (c == '\x1b[C'):
            if (x == 127):
                x = -1
            x += 1
            lcd.set_pixel(x, y, 1)
            lcd.show()

        elif (c == '\x1b[D'):
            if (x == 0):
                x = 128
            x -= 1
            lcd.set_pixel(x, y, 1)
            lcd.show()

        elif (c == "s"):
            clearScreen(lcd)

        elif (c == "q"):
            p = False
            displayText('END THE GAME', lcd, 53, 15)


displayText('ETCH A SKETCH', lcd, 20, 15)
c = getchar()
clearScreen(lcd)

Games()
c = getchar()
clearScreen(lcd)