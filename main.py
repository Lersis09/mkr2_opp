from PIL import Image

# завантаження зображення
img = Image.open(r"plains.jpg")
img.mode
'RGB'

# зміна формату зображення
img1 = img.convert("RGBA")
img1.mode
'RGBA'

# виведення зображення
img1.show()

# збереження зображення
img1.save(r"plains_1.jpg")