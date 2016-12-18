class Employee:
    'Common base class for all employees'
    # https://www.tutorialspoint.com/python/python_classes_objects.htm
    empCount = 0 #varijabla klasna sherovana kroz sve instance(objekte) klase

    def __init__(self, name, salary): #prva metoda __init__ - konstruktor klase koju pajton poziva kada se kreira nova instanca klase
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # ostale metode klase se deklarisu kao normalne Funkcije - python sam dodaje SELF kao prvi argument
    #ne treba SELf ubacivati kada se poziva metoda
    #!!!!SELF u klasama mora
    #  da postoji kao metoda-funkcija koja za razliku od normalnih funkcija i odnosi se na sam taj objekat koji
    #se instancira kasnije u aplikaciji
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

#!!!kreiranje instancnih objekata - da bi se kreirao objekat-instanca klase poziva se ime klase i unose argumenti koji se nalaze u __init__ metodi
"This would create first object of Employee class"
emp1 = Employee( "Zara", 2000 )
"This would create second object of Employee class"
emp2 = Employee( "Manni", 5000 )

#pristupanje atributima u klasi - koristimo TACKA operator EMPLOYEE.EMPCOUNT
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)