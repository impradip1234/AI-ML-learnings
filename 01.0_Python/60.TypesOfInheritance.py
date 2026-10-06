#01: single level inheritance....
class Animals:
    def __init__(self,name):
        self.name=name
class Dog(Animals):
    def __init__(self,sound,name):
        self.sound=sound
        super().__init__(name)

dog1=Dog("bhau .. bhau","sheru")
print(dog1.name,dog1.sound)

#02: Multi Level inheritance.......
class School:
    def __init__(self,schoolname):
        self.schoolname=schoolname
class Students(School):
    def __init__(self,Roll,schoolname):
        self.Roll=Roll
        super().__init__(schoolname)
class Badmas(Students):
    def __init__(self,level,schoolname,Roll):
        self.level=level
        super().__init__(Roll,schoolname)

Badmas1=Badmas("Extream","Pradip",2438317)
print(f"{Badmas1.schoolname} is a badmas bachha, having roll number {Badmas1.Roll} and doing {Badmas1.level} level Badmashi")

#03: Multiple inheritance.......

class Youtuber:
    def __init__(self,YoutubeChanal):
        self.YoutubeChanal=YoutubeChanal
class Teacher:
    def __init__(self,name):
        self.name=name

class YoutubeTeacher(Youtuber,Teacher):
    def __init__(self,name,YoutubeChanal):
        Youtuber.__init__(self,YoutubeChanal)
        Teacher.__init__(self,name)
YutubeTeacher1=YoutubeTeacher("Pradip","BigDreams")
print(f"{YoutubeTeacher.name} is a good youtube teacher, whose chanal name is : {YoutubeTeacher.YoutubeChanal}")
