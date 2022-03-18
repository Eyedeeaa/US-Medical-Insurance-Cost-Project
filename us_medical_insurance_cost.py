import csv


#List for individual analysis & patient dictionary
ages = []
sex = []
bmis = []
num_children = []
smoker_status = []
region = []
insurance_cost = []
patient_data = {}


#Parse insurance CSV
with open("insurance.csv") as ic_csv:
    patient_data_dict = csv.DictReader(ic_csv)
    for row_num, row in enumerate(patient_data_dict):
        #Fill individual lists
        ages.append(int(row['age']))
        sex.append(row['sex'])
        bmis.append(float(row['bmi']))
        num_children.append(int(row['children']))
        smoker_status.append(row['smoker'])
        region.append(row['region'])
        insurance_cost.append(float(row['charges']))
        
        # Create patient dictionary
        patient_num = row_num
        patient_data.update({
            patient_num: {
                f'Patient ID': patient_num,
                'Age': row['age'],
                'Sex': row['sex'],
                'BMI': float(row['bmi']),
                'Children': int(row['children']),
                'Smoker Status': row['smoker'],
                'Region': row['region'],
                'Insurance Cost': float(row['charges'])
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

num_northwest = len(northwest)
num_northeast = len(northeast)
num_southwest = len(southwest)
num_southeast = len(southeast)


# Find male to female ratio
def m_to_f_ratio(lst):
    male = 0
    female = 0
    for sex in lst:
        if sex == 'male':
            male += 1
        else:
            female += 1
    return male, female

male_count, female_count = m_to_f_ratio(sex)

#Classify BMI rating

under_weight_range = []
health_weight_range = []
over_weight_range = []
obese_range = {'Class-1': [], 'Class-2': [], 'Class-3': []}

def sort_bmi(dict):
    for patient in dict.values():
        patient_bmi = patient['BMI']
        if patient_bmi < 18.5:
            under_weight_range.append(patient)
        elif patient_bmi >= 18.5 and patient_bmi < 25:
            health_weight_range.append(patient)
        elif patient_bmi >= 25 and patient_bmi < 30:
            over_weight_range.append(patient)
        else:
            if patient_bmi > 30 and patient_bmi < 35:
                obese_range['Class-1'].append(patient)
            elif patient_bmi >= 35 and patient_bmi < 40:
                obese_range['Class-2'].append(patient)
            else:
                obese_range['Class-3'].append(patient)


sort_bmi(patient_data)

#Smoker VS Non-Smoker Ratio
smokers = []
non_smokers = []
def sort_by_smoker_status(dict):
    for patient in dict.values():
        if patient['Smoker Status'] == "yes":
            smokers.append(patient)
        else:
            non_smokers.append(patient)

sort_by_smoker_status(patient_data)
print(len(non_smokers))


