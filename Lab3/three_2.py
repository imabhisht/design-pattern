# concrete course
class DataStructureCourse():
    def __init__(self):
        self.fee = None

    def Fee(self):
        self.fee = 8000
 
    def available_batches(self):
        self.batches = 5
 
    def __str__(self):
        return "Data Structure Course"
 

class SoftwareEngineeringCourse():
    def __init__(self):
        self.fee = None

    def Fee(self):
        self.fee = 10000
 
    def available_batches(self):
        self.batches = 4
 
    def __str__(self):
        return "Software Development Course"
 

class CareerDevelopmentCourse():
    def __init__(self):
        self.fee = None

    def Fee(self):
        self.fee = 5000
 
    def available_batches(self):
        self.batches = 7
 
    def __str__(self):
        return "Carer Development Course"
 
 
# main method
if __name__ == "__main__":
 
    sde = SoftwareEngineeringCourse()   # object for SDE
    dsa = DataStructureCourse()   # object for DSA
    stl = CareerDevelopmentCourse()   # object for STL

    sde.Fee()
    dsa.Fee()
    stl.Fee()
 
    print(f'Name of Course: {sde} and its Fee: {sde.fee}')
    print(f'Name of Course: {stl} and its Fee: {stl.fee}')
    print(f'Name of Course: {dsa} and its Fee: {dsa.fee}')