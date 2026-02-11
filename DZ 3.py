import random


# класс работы
class Job:
    def __init__(self, name: str = "test_job", salary: float = 1):
        self.name = name
        self.salary = salary

    def set_name(self, name: str):
        self.name = name

    def set_salary(self, salary: float):
        self.salary = salary


# новый класс дома
class House:
    def __init__(self, name: str = "home", comfort: int = 50, cost: float = 100):
        self.name = name
        self.comfort = comfort
        self.cost = cost

    def upgrade(self):
        self.comfort += 10
        self.cost += 50


# класс человека
class Human:
    def __init__(self, name: str = "name", job: Job = None,
                 home: House = None, car=None, money: float = 0):
        self.name = name
        self.job = job
        self.home = home
        self.happiness = 100
        self.satiety = 100
        self.car = car
        self.money = money

    def set_name(self, name: str):
        self.name = name

    def set_home(self, home: House):
        self.home = home

    def set_car(self, car):
        self.car = car

    def set_job(self, job: Job):
        self.job = job

    def eat(self):
        self.satiety += 10

    def work(self):
        if self.job:
            self.money += self.job.salary

    # взаимодействие с домом
    def relax(self):
        if self.home:
            self.happiness += self.home.comfort * 0.1

    def improve_home(self):
        if self.home and self.money >= self.home.cost:
            self.money -= self.home.cost
            self.home.upgrade()


# работы
programmist = Job("programmist", 3000)
futbolist = Job("futbolist", 2000)
dizayner = Job("dizayner", 2500)

# дома
mardakan = House("mardakan_dacha", 70, 200)
badamdar = House("badamdar_dacha", 60, 150)
may28 = House("28may", 80, 300)

# люди
Farkhad = Human("Farkhad", programmist, mardakan, "MB_Maybach", 250)
Vidadi = Human("Vidadi", futbolist, badamdar, "07_peredok", 150)
Aysu = Human("Aysu", dizayner, may28, "Porsche", 250)

people_list = [Farkhad, Vidadi, Aysu]

# действия
Farkhad.eat()
Farkhad.work()
Farkhad.relax()
Farkhad.improve_home()

programmist.set_salary(4000)
programmist.set_name("developer")

# вывод информации
for person in people_list:
    print("Job:")
    print("   Name:", person.job.name)
    print("   Salary:", person.job.salary)

    print("Human:")
    print("   Name:", person.name)
    print("   Job:", person.job.name, "(", person.job.salary, ")")
    print("   Home:", person.home.name)
    print("   Home comfort:", person.home.comfort)
    print("   Car:", person.car)
    print("   Happiness:", person.happiness)
    print("   Satiety:", person.satiety)
    print("   Money:", person.money)
    print()
