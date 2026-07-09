class Person:
    def __init__(self,name,age,**kwargs):
        self.name = name
        self.age = age
        super().__init__(**kwargs)
    
    def introduce(self):
        print(f"Introducing you {self.name}")

    def display_basic_info(self):
        print("PERSON DETAILS")
        print("---------------")
        print(f"Name: {self.name}\nAge: {self.age}")

class Student(Person):
    def __init__(self,roll_no,course,**kwargs):
        self.roll_no = roll_no
        self.course = course
        super().__init__(**kwargs)

    def study(self):
        print(f"{self.name} studies {self.course}")

    def submit_assignment(self):
        print(f"{self.name} submits assignment")

    def attend_class(self):
        print(f"{self.name} attends class")


class Employee(Person):
    def __init__(self,employee_id,department,**kwargs):
        self.employee_id = employee_id
        self.department = department
        super().__init__(**kwargs)

    def work(self):
        print(f"{self.name} works in {self.department} department")

    def mark_attendance(self):
        print(f"{self.name} marks attendance")

    def display_department(self):
        print(f"Department: {self.department}")

class Manager(Employee):
    def __init__(self,team_size,**kwargs):
        self.team_size = team_size
        super().__init__(**kwargs)

    def conduct_meeting(self):
        print(f"{self.name} conducts meeting")

    def assign_task(self):
        print(f"{self.name} assigns task")

    def evaluate_employee(self):
        print(f"{self.name} with team of {self.team_size} size evaluates employees")

class GraduateStudent(Student):
    def __init__(self,research_topic,**kwargs):
        self.research_topic = research_topic
        super().__init__(**kwargs)

    def do_research(self):
        print(f"{self.name} does research on {self.research_topic}")

    def publish_paper(self):
        print(f"{self.name} publishes research papers")

    def present_seminar(self):
        print(f"{self.name} presents a seminar")

class ProjectGuide(GraduateStudent,Manager):
    def __init__(self,project_name,**kwargs):
        self.project_name = project_name
        super().__init__(**kwargs)

    def introduce(self):
        print(
            f"I am {self.name}. "
            f"I work in the {self.department} department, "
            f"specialize in {self.research_topic}, "
            f"and guide the project '{self.project_name}'."
        )

    def guide_students(self):
        print(f"{self.name} guides students")

    def review_project(self):
        print(f"{self.name} reviews projects")

    def approve_project(self):
        print(f"{self.name} approves projects")

    def display_profile(self):
        print("DISPLAYING PROFILE")
        print("-------------------")
        Person.display_basic_info(self)
        print(f"Roll no: {self.roll_no}")
        print(f"Course: {self.course}")
        print(f"Employee ID: {self.employee_id}")
        Employee.display_department(self)
        print(f"Team size: {self.team_size}")
        print(f"Research Topic: {self.research_topic}")
        print(f"Project name: {self.project_name}")
        
    def daily_routine(self):
        self.mark_attendance()
        self.study()
        self.do_research()
        self.conduct_meeting()
        self.guide_students()

guide = ProjectGuide(name = "Hemant", age = 40, roll_no =1,course ="BSC",employee_id = 100,department="HR",team_size = 11,research_topic = "Data Structures and Algorithms",project_name = "DSA Learning Portal")

guide.introduce()
guide.work()
guide.review_project()
guide.display_profile()
guide.daily_routine()


print("\nMethod Resolution Order")
print("-----------------------")

for cls in ProjectGuide.mro():
    print(cls.__name__)
