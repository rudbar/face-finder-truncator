from PIL import Image
import face_recognition

# получаем координаты расположения лиц на картинке
image = face_recognition.load_image_file('./images/people/group-people2.jpg')
face_locations = face_recognition.face_locations(image)


for face_location in face_locations:
    #координаты верхней, правой, нижней и левой части лица соответственно
    top, right, bottom, left = face_location

    """
    это даст нам лицо с картинки в виде массива
    с помощью которого мы сможем получить лицо 
    в виде картинке с использованием библиотеки Pillow 
    """
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    # pil_image.show()
    #сохраняем полученные лица
    pil_image.save(f'{top}.jpg')
    