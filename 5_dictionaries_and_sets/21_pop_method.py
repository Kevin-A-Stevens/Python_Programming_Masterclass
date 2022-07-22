"""
Remove items with the pop method

Because sets are unordered, you can not guarantee
what item will be removed

methods used
.pop() = removes an item from a set and returns that
item so you can do something with it
"""
from prescription_data import patients

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:
    patient = trial_patients.pop()
    print(patient)

print()
print(trial_patients)  # empty set - set()
print()

# Since the set is empty, need to create it again
trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)


