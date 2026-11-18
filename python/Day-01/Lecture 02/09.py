#Program -Validate account Number (User-Defined Function)
def is_valid_patient_id(patient_id_str):
    min_length=5
    max_length=10
    if len(patient_id_str) >= min_length and len(patient_id_str) <= max_length:
        return True
    else:
        return False
    
# sample patient IDs
patient1="P-101"
patient2="1234"
patient3="P-101-ABCDE"
#print the validation results....
patient1="P-101"
print(f"'{patient1}' is valid : {is_valid_patient_id(patient1)}")
print(f"'{patient2}' is valid : {is_valid_patient_id(patient2)}")
print(f"'{patient3}' is valid : {is_valid_patient_id(patient3)}")
