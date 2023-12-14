>>> from PIL import Image
>>> img=Image.open("C:/Users/Leonid/Desktop/image_12.jpg")
>>> img.mode
'RGB'
>>> img1 = img.convert("RGBA")
>>> img1.mode
'RGBA'
>>> img1.show()
