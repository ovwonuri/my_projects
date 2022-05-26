class Student:
    # [assignment] Skeleton class. Add your code here
    # def __init__(self):
    # pass

    # init method or constructor
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    # change_name function
    # this is a set method
    def change_name(self, name):
        self.name = name

    # change_age function
    # this is a set method
    def change_age(self, age):
        self.age = int(age)

    # add_track function
    # this is also a set method
    def add_track(self, tracks):
        self.tracks = tracks

    # get_score function
    # this is a get method
    def get_score(self):
        return self.score

    # def get_age(self):
    # return self.age


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34.9)
Bob.add_track("UI/UX")

print(Bob.get_score())
# print(Bob.get_age())
