import face_recognition
from PIL import Image, ImageDraw

image_of_megan = face_recognition.load_image_file('./images/known/megan_fox.jpg')
megan_face_encoding = face_recognition.face_encodings(image_of_megan)[0]

image_of_shia = face_recognition.load_image_file('./images/known/shia_labeouf.jpg')
shia_face_encoding = face_recognition.face_encodings(image_of_shia)[0]

# Создаем массив с кодировками и именами
known_face_encodings = [
    megan_face_encoding,
    shia_face_encoding
]

known_face_names = [
    "Megan Fox",
    "Shia Labeouf"
]

# Загрузка тестового изображния на котором будут искаться закодированные лица
test_image = face_recognition.load_image_file('./images/people/megan_fox_lebaf.jpg')

# Нахождение лиц на тестовом изображении
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Конвертируем изображние в формат PIL, чтобы была возможность рисовать на изображении
pil_image = Image.fromarray(test_image)

# Создаем экземпляр ImageDraw, чтобы рисовать на изображении
draw = ImageDraw.Draw(pil_image)

# Проходимся циклом по лицам в тестовом изображении (test_image)
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Неопознанный человек"

    # Если кодировки совпадают
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    
    # Рисуем квадрат
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,0))

    # Рисуем прямоугольник для имени
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0,0,0), outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

# Удаляем экземпляр ImageDraw, чтобы не засорял память
del draw

# Выводим изображение
pil_image.show()

# Сохраняем полученного изображение в текущую папку
pil_image.save('recognized.jpg')