from PIL import Image

# image = Image.new('RGB', (250, 250), (0, 0, 0))
# image.save('pillow/black.png')

white = Image.open('pillow/white.png')
black = Image.open('pillow/black.png')
size = black.size
white.paste(black, (size[0] // 2, size[1] // 2))
white.save('pillow/pasted.png')

red = Image.open('pillow/red.png')
new_width = int(input("Please enter new width\n"))
width, height = red.size
new_height = height * new_width // width
red = red.resize((new_width, new_height))
red.save('pillow/red_resized.png')

nature = Image.open('pillow/nature.jpg')
px = nature.load()
nature_wb = Image.new('RGB', nature.size)
for i in range(nature.size[0]):
    for j in range(nature.size[1]):
        grey = (px[i, j][0] + px[i, j][1] + px[i, j][2]) // 3
        nature_wb.putpixel((i, j), (grey, grey, grey))
nature_wb.save('pillow/nature_wb.jpg')

