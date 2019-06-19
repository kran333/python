class Person:
    def getGender(self,gender):
        if gender == "Male":
            obj = Male()
            obj.getGender()
        elif gender == "Female":
            obj = Female()
            obj.getGender()
        else:
            print "No Match found"
class Male(Person):
    def getGender(self):
        print "Male"

class Female(Person):
    def getGender(self):
        print "Female"
obj = Person()
obj.getGender("Female")