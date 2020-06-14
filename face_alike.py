import face_recognition

image_of_tinkov = face_recognition.load_image_file('./images/known/tinkov.jpg')
tinkov_face_encoding = face_recognition.face_encodings(image_of_tinkov)[0]

unknown_image = face_recognition.load_image_file('./images/unknown/tinkov-like.png')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Сравнение двух лиц
results = face_recognition.compare_faces([tinkov_face_encoding], unknown_face_encoding)

if results[0]:
    print('Это Олег Тиньков')
else:
    print('Это не Олег Тиньков')