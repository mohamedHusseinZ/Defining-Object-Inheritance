# from vehicle import Vehicle
class Vehicle:
    def __init__(self, color, name, model):
        self.color = color
        self.name = name
        self.model = model
    def sort(self):
        return(f"name: {self.name}, color: {self.color}, model: { self.model}") 

class Car(Vehicle):
    def __init__(self, color, name, model, speed):
        super().__init__(color, name, model)
        self.speed = speed
    def sort(self):
        return(f"{super().sort()}, speed: {self.speed}")


# Create an instance of the Car class
car1 = Car("black", "Maybach", "Mercedes", "180 km/hr")

# Call the sort method on the Car instance
print(car1.sort())



class Vehicle:
    def __init__(self, color, name, model):
        self.color = color
        self.name = name
        self.model = model

    def sort(self):
        return f"name: {self.name}, color: {self.color}, model: {self.model}"

class Car(Vehicle):
    def __init__(self, color, name, model, speed):
        super().__init__(color, name, model)
        self.speed = speed

    def sort(self):
        return f"{super().sort()}, speed: {self.speed}"

# Create an instance of the Car class
car1 = Car("black", "Maybach", "Mercedes", "180 km/hr")

# Call the sort method on the Car instance
print(car1.sort())

           
       

# class User:
#     all_users = []

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.add_user(self)

#     @classmethod
#     def add_user(cls, user):
#         cls.all_users.append(user)

#     @classmethod
#     def to_access(cls):
#         for user in cls.all_users:
#             print(f"Name: {user.name}, Age: {user.age}")

# # Create an instance of the User class
# user1 = User("Zaki", 25)

# # Access and print all users
# User.to_access()


# class Song:
#     count = 0
#     genres = []
#     artists = []
#     genre_count = {}
#     artist_count = {}

#     def __init__(self, name, artist, genre):
#         self.name = name
#         self.artist = artist
#         self.genre = genre
#         Song.add_song_to_count()
#         Song.add_to_genres(genre)
#         Song.add_to_artists(artist)
#         Song.add_to_genre_count(genre)
#         Song.add_to_artist_count(artist)

#     @classmethod
#     def add_song_to_count(cls):
#         cls.count += 1

#     @classmethod
#     def add_to_genres(cls, genre):
#         if genre not in cls.genres:
#             cls.genres.append(genre)

#     @classmethod
#     def add_to_artists(cls, artist):
#         if artist not in cls.artists:
#             cls.artists.append(artist)

#     @classmethod
#     def add_to_genre_count(cls, genre):
#         if genre in cls.genre_count:
#             cls.genre_count[genre] += 1
#         else:
#             cls.genre_count[genre] = 1

#     @classmethod
#     def add_to_artist_count(cls, artist):
#         if artist in cls.artist_count:
#             cls.artist_count[artist] += 1
#         else:
#             cls.artist_count[artist] = 1

# # Example usage:
# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# toxic = Song("Toxic", "Britney Spears", "Pop")
# thunderstruck = Song("Thunderstruck", "AC/DC", "Rock")

# print(Song.count)  # Output: 3

# print(Song.genres)  # Output: ['Rap', 'Pop', 'Rock']

# print(Song.artists)  # Output: ['Jay-Z', 'Britney Spears', 'AC/DC']

# print(Song.genre_count)  # Output: {'Rap': 1, 'Pop': 1, 'Rock': 1}

# print(Song.artist_count)  # Output: {'Jay-Z': 1, 'Britney Spears': 1, 'AC/DC': 1}




                  

# class Item:
#     count = 0
#     phones = []
#     cars = []
#     phones_count = {}
#     cars_count = {}

#     def __init__(self, *args):
#         self.name = args[0]
#         self.color = args[1]
#         self.type = args[2]
#         Item.add_to_count()
#         Item.add_to_phones(self.name)
#         Item.add_to_cars(self.name)
#         Item.add_to_count_phones(self.name)
#         Item.add_to_count_cars(self.name)

#     @classmethod
#     def add_to_count(cls):
#         cls.count += 1

#     @classmethod
#     def add_to_phones(cls, phone):
#         if phone not in cls.phones:
#             cls.phones.append(phone)

#     @classmethod
#     def add_to_cars(cls, car):
#         if car not in cls.cars:
#             cls.cars.append(car)

#     @classmethod
#     def add_to_count_phones(cls, phone):
#         if phone in cls.phones_count:
#             cls.phones_count[phone] += 1
#         else:
#             cls.phones_count[phone] = 1

#     @classmethod
#     def add_to_count_cars(cls, car):
#         if car in cls.cars_count:
#             cls.cars_count[car] += 1
#         else:
#             cls.cars_count[car] = 1

# phones = Item("iphone", "red", "smartphone")
# cars = Item("subaru", "blue", "sedan")

# # Display colors and types
# for item in [phones, cars]:
#     print(f"{item.name} - Color: {item.color}, Type: {item.type}")

# print(Item.count)
# print(Item.phones)
# print(Item.cars)
# print(Item.phones_count)
# print(Item.cars_count)


# class Student:




#     count = 0
#     names = []
#     grade = []
#     names_count ={}
#     grade_count ={}

#     def __init__(self, names, grade):
#         self.names = names
#         self.grade = grade
#         Student.add_student_to_count()
#         Student.add_names_to_count()
#         Student.add_grade_to_count()
#         Student.names_count()
#         Student.grade_count()

#     @classmethod
#     def add_sttudent_to_count(cls):
#         cls.count +=1

#     @classmethod
#     def add_names_to_count(cls, names):
#         if names not in cls.names:
#             cls.names.append(names)

#     @classmethod
#     def add_grade_to_count(cls, grade):
#         if grade not in cls.grade:
#             cls.grade.append(grade)

#     @classmethod
#     def names_count():
#         if  names in cls.names_count:
#             cls.names_count[names] +=1
#         else cls.names_count[names]  =1

#     @classmethod
#     def grade_count():
#         if grade in cls.grade_count:
#             cls.grade_count[grade]  +=1
#         else cls.grade_count[grade]  =2

# students1 = Student("maida", "siham", "zaki" "manze")
# students2 = Student("A", "B", "C","D")

# for student in [students1, students2]:
#     print(f"Names: {student.names}, Grades: {student.grades}")

# # Additional prints to show counts
# print("\nTotal Students Count:", Student.count)
# print("Unique Names:", Student.names)
# print("Unique Grades:", Student.grades)
# print("Names Count:", Student.names_count)
# print("Grades Count:", Student.grade_count)




          


     
