import csv


#List for individual analysis & patient dictionary
ages = []
sex = []
bmis = []
num_children = []
region = []
insurance_cost = []
patient_data = {}


#Parse insurance CSV
with open("insurance.csv") as ic_csv:
    patient_data_dict = csv.DictReader(ic_csv)
    for row in patient_data_dict:
        #Fill individual lists
        ages.append(int(row['age']))
        sex.append(row['sex'])
        bmis.append(float(row['bmi']))
        num_children.append(int(row['children']))
        region.append(row['region'])
        insurance_cost.append(float(row['charges']))



# Fill patient dictionary
for item in range(len(ages)):
    patient_num = item
    patient_data.update({
        patient_num: {
        f'Patient ID': patient_num,
        'Age': ages[item],
        'Sex': sex[item],
        'BMI': bmis[item],
        'Children': num_children[item],
        'Region': region[item],
        'Insurance Cost': insurance_cost[item]
        }
    })


#Function to find averages
def find_avg(lst):
    return sum(lst) / len(lst)

# Averages
avg_age = int(find_avg(ages))
avg_bmi = round(find_avg(bmis), 2)
avg_children = int(find_avg(num_children))
avg_insurance_cost = round(find_avg(insurance_cost), 2)


#Sort and count patients by region
northwest = []
northeast = []
southwest = []
southeast = []

def sort_region(patients):

    for patient in patients:
        if patients[patient]['Region'] == 'northwest':
            northwest.append(patients[patient])
        elif patients[patient]['Region'] == 'northeast':
            northeast.append(patients[patient])
        elif patients[patient]['Region'] == 'southwest':
            southwest.append(patients[patient])
        else:
            southeast.append(patients[patient])

sort_region(patient_data)

