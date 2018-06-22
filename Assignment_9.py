#Question 1

class Circle():
    radius=int(input("Enter radius of circle: "))
    def __init__(self):
     pass
    def getarea(self):
     area=3.14*self.radius*self.radius
     print("Area of circle: ", area)
    def getcircumference(self):
     cirumference=2*3.14*self.radius
     print("circumference: ",cirumference)
c=Circle()
c.getarea()
c.getcircumference()


#Question 2

class Student():
  name = input("Enter Name: ")
  roll_no = int(input("Enter Roll_no: "))
  def __init__(self):
    pass
  def display(self):
    print("Name is: " + self.name)
    print("roll_no:", self.roll_no)
s = Student()
s.display()

#Question 3

class Temprature():
  celsius=float(input("Enter temprature in celsius: "))
  fahrenhiet = float(input("Enter temprature in fahrenheit: "))
  def __init__(self):
    pass
  def convertcelsius(self):
    f=self.celsius*(9/5)+32
    print("Temprature in fahrenheit: ",f)
  def convertfahrenheit(self):
    c=(self.fahrenhiet-32)*(5/9)
    print("Temprature in celsius: ",c)
t=Temprature()
t.convertcelsius()
t.convertfahrenheit()


#Question 4

class MovieDetails():
    def __init__(self):
        pass
    def display(self,moviename,artistname,YearOfRelease,rating):
        self.m=moviename
        self.a=artistname
        self.y=YearOfRelease
        self.r=rating
        print(self.m,self.a,self.y,self.y,self.r)
    def display(self,moviename, artistname, YearOfRelease,rating):
        self.m = input("Enter Movie Name: ")
        self.a = input("Enter artist Name: ")
        self.y = input("Enter year of release: ")
        self.r = input("Enter ratings: ")
        print(self.m,self.a,self.y,self.r)
y=MovieDetails()
y.display("Jurassic World:Fallen Kingdom","J.A. Bayona","21 May 2018","4.2")
t=MovieDetails()
t.update("m","a","y","r")



#Question 5

class Expenditure():
    expense=float(input("Enter expenditure: "))
    save=float(input("Enter savings: "))
    def __init__(self):
       pass
    def display(self):
       print("expenditure is:",self.expense)
       print("Savings is: ",self.save)
    def cal_salary(self):
       total_salary =self.expense + self.save
       return total_salary
    def dis_salary(self):
        print("total salary is: ",e.cal_salary())
e=Expenditure()
e.display()
e.cal_salary()
e.dis_salary()








