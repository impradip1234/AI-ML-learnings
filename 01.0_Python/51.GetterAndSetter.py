class Student:
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name
    def set_name(self, name):
        if len(name) > 0:
            self._name = name
        else:
            print("Invalid name")
# correct usage
sol = Student("Aadi")
print(sol.get_name())         # Aadi
sol.set_name("pradip yadav")
print(sol.get_name())         # pradip yadav