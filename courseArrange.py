import json

class Course:
    def __init__(self, title: str, code: str, timeSlots: list[int], description:str = None) -> None:
        self.title: str = title
        self.code: str = code
        self.timeSlots = timeSlots 
        self.desciption = description

    def editDescription(self, desc: str) -> None:
        self.desciption = desc

 
class CourseGroup:
    def __init__(self) -> None:
        self.group: list[Course] = []
        self.timeSheet: dict = {}
        for i in range(1,5):
            self.timeSheet[i] = []
    def addCourse(self, course: Course) -> None:
        for courseInGroup in self.group:
            if course.code == courseInGroup.code:
                return
        self.group.append(course)
        slots: list[int] = course.timeSlots
        for slot in slots:
            self.timeSheet[slot].append(course)
    
    def printTimeSheet(self):
        for key in self.timeSheet:
            print(f"block {key}:", end=" ")
            for course in self.timeSheet[key]:
                print(f"[{course.code} - {course.title}]", end=" ")
            print()
            


c1 = Course("principle of programming", "COMPSCI 2SD3", [1])
c2 = Course("intro to astron", "ASTRON 1F03", [4])
c3 = Course("intro to chemical physics", "PHYS 1CC3", [1,2])

testDict = {}
testDict[1] = "dog"
testDict[2] = "cat"



McMasterCourses = CourseGroup()
McMasterCourses.addCourse(c1)
McMasterCourses.addCourse(c2)
McMasterCourses.addCourse(c3)


#with open("courseData.json", 'w') as courseDataFile:
#    json.dump([course.__dict__ for course in McMasterCourses.group], courseDataFile, indent=1)

with open('courseData.json', 'r') as courseDataFile:
    courseData = json.load(courseDataFile)

print(courseData)