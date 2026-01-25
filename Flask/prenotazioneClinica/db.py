from ClinicHub import ClinicHub
from DiagnosticExam import DiagnosticExam
from MedicalVisit import MedicalVisit

# Creazione del sistema di gestione prenotazioni
ch: ClinicHub = ClinicHub()

# Prenotazione di tipo MedicalVisit
visit = MedicalVisit(
    booking_id="BK-101",
    patient_name="Mario Rossi",
    doctor="Dr. Bianchi",
    department="Cardiologia",
    date="2026-02-10",
    time="10:00",
    status="scheduled",
    visit_reason="Controllo annuale",
    first_time=True
)

# Prenotazione di tipo DiagnosticExam
exam = DiagnosticExam(
    booking_id="BK-102",
    patient_name="Giulia Verdi",
    doctor="Dr. Neri",
    department="Radiologia",
    date="2026-02-11",
    time="09:15",
    status="scheduled",
    exam_type="RMN",
    requires_fasting=True
)

# Inserimento nel ClinicHub
ch.add(visit)
ch.add(exam)
