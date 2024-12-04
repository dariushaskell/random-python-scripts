from PIL import Image

image = Image.open("pic.png")
image = image.convert("RGBA")

data = image.getdata()
new_data = []
for item in data:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:
        new_data.append((0, 0, 0, item[3]))
    else:
        new_data.append(item)

image.putdata(new_data)

image.save("pic_edit.png")
