from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import st7735
import digitalio
import board
import time
import sys

cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D24)
spi = board.SPI()

disp = st7735.ST7735(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    width=128,
    height=160,
    rotation=0,
    invert=False,
    )
    
# Initialize display.
disp.begin()

width = disp.width
height = disp.height
image_file = "/home/lucas/st7735-python/examples/deployrainbows.gif"

# Load an image.
print(f"Loading gif: {image_file}...")
image = Image.open(image_file)

print("Drawing gif, press Ctrl+C to exit!")

frame = 0

while True:
    try:
        image.seek(frame)
        disp.display(image.resize((width, height)))
        frame += 1
        time.sleep(0.05)

    except EOFError:
        frame = 0

"""
MESSAGE = "PEEWEE"   

disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))

draw = ImageDraw.Draw(img)

font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)

x1, y1, x2, y2 = font.getbbox(MESSAGE)
size_x = x2 - x1
size_y = y2 - y1

text_x = 160
text_y = (80 - size_y) // 2

t_start = time.time()

while True:
    x = (time.time() - t_start) * 100
    x %= (size_x + 160)
    draw.rectangle((0, 0, 160, 80), (0, 0, 0))
    draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(255, 255, 255))
    disp.display(img)

disp.begin()

img = Image.new("RGB",(WIDTH, HEIGHT), color = (0, 0, 0))
draw = ImageDraw.Draw(img)

draw.line((10, 10, WIDTH, HEIGHT), fill=(255, 255, 255))
draw.line((10, HEIGHT, WIDTH, 10), fill=(255, 255, 255))

disp.display(img)


font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)

MESSAGE = "PEEWEE"

x1, y1, x2, y2 = font.getbbox(MESSAGE)
size_x = x2 - x1
size_y = y2 - y1

text_x = 128
text_y = (160 - size_y) // 2

t_start = time.time()

while True:
    x = (time.time() - t_start) * 100
    x %= (size_x + 160)
    draw.rectangle((0, 0, 160, 80), (0, 0, 0))
    draw.text((int(text_x - x), text_y), MESSAGE, font=font, fill=(200, 40, 225))
    disp.display(img)

img = Image.new('RGB', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

# Load default font.
font = ImageFont.load_default()

# Write some text
draw.text((5, 5), "Hello World!", font=font, fill=(255, 255, 255))

# Write buffer to display hardware, must be called to make things visible on the
# display!
disp.display(img)
"""
