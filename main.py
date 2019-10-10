from PIL import Image

IMAGE = Image.open("monro.jpg")     # Исходное изображение
PIXELS = 100                        # Величина смещения

red, green, blue, = IMAGE.split()

# Смещаем красный канал

coordinates_red_1 = (PIXELS, 0, red.width, red.height)
cropped_red_1 = red.crop(coordinates_red_1)

coordinates_red_2 = (PIXELS/2, 0, red.width - PIXELS/2, red.height)
cropped_red_2 = red.crop(coordinates_red_2)

image_red = Image.blend(cropped_red_1, cropped_red_2, 0.5)

# Смещаем синий канал

coordinates_blue_1 = (0, 0, blue.width - PIXELS, blue.height)
cropped_blue_1 = blue.crop(coordinates_blue_1)

coordinates_blue_2 = (PIXELS/2, 0, blue.width - PIXELS/2, blue.height)
cropped_blue_2 = blue.crop(coordinates_blue_2)

image_blue = Image.blend(cropped_blue_1, cropped_blue_2, 0.5)

# Обрезаем зелёный канал

coordinates_green = (PIXELS/2, 0, green.width - PIXELS/2, green.height)
cropped_green = green.crop(coordinates_green)

# Объединяем все три картинки в одну

new_image = Image.merge("RGB", (image_red, image_blue, cropped_green))
new_image.thumbnail((500, 500))      # Нарезаем аватарку
new_image.save("final_image.jpg")
