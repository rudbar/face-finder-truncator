import face_recognition

image = face_recognition.load_image_file('./images/people/group-people1.jpg')
face_locations = face_recognition.face_locations(image)

# Массив, содержащий координаты каждого лица на картинке 
#print(face_locations)

# Количество людей на заданной картинке
print(f'На этой картинке {len(face_locations)} человека')