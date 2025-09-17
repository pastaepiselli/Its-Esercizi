from dottore import Dottore
from paziente import Paziente
class Fattura:
    
    fatture: int
    salary: int

    def __init__(self, doctor: Dottore, patient: list[Paziente]) -> None:
        self.doctor = doctor
        self.patient = patient
        if doctor.isAValidDoctor():
            self.fatture = len(patient)
            self.salary = 0
        else:
            self.fatture = None
            self.patient = None
            self.salary = None
        
    def getSalary(self) -> int:
        self.salary = self.doctor.getParcel() * len(self.patient)
        return self.salary

    def getFatture(self) -> int:
        self.fatture = len(self.patient)
        return self.fatture

    def addPatient(self, newPatient: Paziente) -> None:
        self.patient.append(newPatient) 

        self.getFatture() # aggiorno le fatture
        self.getSalary( ) # aggiorno il salario

        print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato aggiunto il paziente {newPatient.getIdCode()}")
    
    def removePatient(self, idCode: str) -> None:
        for patient in self.patient:
            if patient.getIdCode() == idCode:
                self.patient.remove(patient)
        
        self.getFatture()
        self.getSalary()

        print(f"Alla lista del Dottor {self.doctor.getLastName()} è stato rimosso il paziente {idCode}")