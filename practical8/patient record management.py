class patients(object):
    def __init__(self,name,age,date_admission,medical_history):
        self.name=name
        self.age=age
        self.date=date_admission
        self.history=medical_history
    def print_details(self):
        print('name:',self.name,'age:',self.age,'date of last admission:',self.date,'medical history:',self.history)

patient=patients(name='Amy',age=22,date_admission='20240412',medical_history='nothing')
patient.print_details()