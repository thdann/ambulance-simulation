class EmergencyCall():
    properties = {
        'id': int,
        'patient': int,
        'time': float
    }

    def __init__(self, patient):
        print("init(EmergencyCall())")
        self.id = 1, 
        self.patient = patient.id, 
        self.time = patient.incident_time_hour
        print("EmergencyCall created " + str(self.id) + "with patient: " + str(self.patient))


    def action(self):
        print("EmergencyCall.action()")

        # trigga ambulance to patient departure. Vad behöver vi då?
        # Är ambulance ledig? - skicka den. 
        # patienten (dess loaction iaf) hela objektet?

