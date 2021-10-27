import csv
import json


def ToJson(programPath, profilePath, jsonPath):

    data = {}

    with open(profilePath, encoding='utf-8') as csvf:   #reader1 stores student profile info
        reader1 = csv.DictReader(csvf)
        
                
        for row in reader1:     #runs for each student to store the student profile
            key1 = row['student_username']
            student = {}        #student dict contains all the student info
            student["campus"] = row['campus_identifier']
            student["gpa"] = float(row['gpa'])
            student["email"] = row['email']
            student["first_name"] = row['first_name']
            student["last_name"] = row['last_name']
            student["username"] = row['student_username']

            record = {}         #record dict contains student and program info both

            with open(programPath, encoding='utf-8') as csvf2:  #reader2 stores student program info
                reader2 = csv.DictReader(csvf2)
                
                plan = {}
                programs = {}
                programList = []            #stores all programs for a student
                for row2 in reader2:        #checks all records in program info file
                    key2 = row2['student_username']
                    if key2 == key1:        
                        programList.append(row2['program_identifier'])

                programs['programs'] = programList
                plan['plan'] = programs

                record['plan'] = programs
                record['student'] = student
                
                data[key1] = record
                

    with open(jsonPath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def main():
    profilePath = r'C:\Users\zainab.hasnain\Desktop\StudentRecord\student_profile.csv'
    jsonPath = r'C:\Users\zainab.hasnain\Desktop\StudentRecord\student.json'
    programPath = r'C:\Users\zainab.hasnain\Desktop\StudentRecord\student_program.csv'
    ToJson(programPath, profilePath, jsonPath)

main()
