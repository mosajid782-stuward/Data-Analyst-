# Demonstrating Basic data type
#.......>>>>>>>
# String-Patient Name
patient_name="REbort"

#int-Patient ID
patient_id=105

#Float-Body temperature(F)
body_temp=101.4

#Bool-Is patient admitted
Is_admitted=True

#print patient Details
print("-----Patient Record-----")
print("Patient Name :",patient_name)
print("Patient ID :",patient_id)
print("Body Temperature :",body_temp,"F")
print("Admitted :",Is_admitted)

#Example use 
if Is_admitted:
    print("Status:Patient is under hospital care.")
else:
    print("Status:Patient discharged - follow up required.")
