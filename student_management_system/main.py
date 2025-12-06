# --------------------------------------------------------------
# IN THE NAME OF ALLAH, THE MOST BENEFICENT, THE MOST MERCIFUL
# --------------------------------------------------------------
#                          main.py
# --------------------------------------------------------------
# Author: Naveed Anjum (PhD Student / Reg # 577607)
# Course: AI-853 Advanced Programming in Python
# Assignment-2: Student Management System (Dec, 2025)
# --------------------------------------------------------------

import os
import random
from models.student import Student
from models.subject import Subject
from models.manager import SystemManager

def DisplayUserMenu():
    # Clear screen
    os.system('cls')

    print('')
    print(f"                W E L C O M E   T O\n")
    print(f"S T U D E N T   M A N A G E M E N T   S Y S T E M")
    print('-' * 50 + '\n')
    print('\n\nNote: A default data is already stored.\n\n')

    CLI = [
        '1. Add Student\n',
        '2. Add Subject\n',
        '3. Enroll Student\n',
        '4. Add Grade\n',
        '5. Mark Attendance\n',
        '6. View Student Report\n',
        '7. View All Students\n',
        '8. Exit\n\n']

    print(*CLI, sep = '\n')

def main():

    DisplayUserMenu()
    
    DrawLine = lambda L=25: print('-'*L,end='\n')

    SMS = SystemManager()

    SMS.Read_Data_Files()

    while True:
        # Ask user to select one
        try:
            User_Input = int(input("\nYour choice ( 1 ~ 8 ) ?\t\t"))
        except ValueError:
            print('Invalid input. Enter again.')
            continue
        # ---------------------------------------------------------------------------------
        # Action as per user input
        # ---------------------------------------------------------------------------------
        if User_Input == 1:     # Add Student

            print('\n' + '-'*60)

            Name =   input(f"\n{'Enter student name (e.g. Ali)':40}:\t")
            id   =   input(f"\n{'Enter student ID (e.g. 2001)':40}:\t")
            Sec  =   input(f"\n{'Enter student Section (e.g. RAI-25)':40}:\t")

            print('\n' + '-'*60)

            SMS.AddStudent(Name, id, Sec)

            print(f"\nStudent addedd successfully.")
            
            print('\n' + '-'*60)
        # ---------------------------------------------------------------------------------
        elif User_Input == 2:   # Add Subject

            print('\n' + '-'*60)

            Name    = input(f"\n{'Enter subject name (e.g. Python)':40}:\t")
            Code    = input(f"\n{'Enter subject code (e.g. CSE-548)':40}:\t")
            Credits = input(f"\n{'Enter subject credit hours (e.g. 3)':40}:\t")

            print('\n' + '-'*60)

            SMS.AddSubject(Name, Code, Credits)

            print(f"\nSubject addedd successfully.")
            
            print('\n' + '-'*60)
        # ---------------------------------------------------------------------------------
        elif User_Input == 3:   # Enroll course


            DrawLine(), print(*[f"| {s.id:10} | {s.name}" for s in SMS.StudentsList],sep='\n')
            DrawLine(), print(*[f"| {s.code:10} | {s.name}" for s in SMS.SubjectsList],sep='\n')
            DrawLine()

            try:    
                ID, Code = input('Enter student ID and subject code e.g. 1002, CSE-848 : ').split(",")
                ID   = ID.strip()
                Code = Code.strip()
            except ValueError:
                print("Invalid input. Try again.")
                continue

            if ID not in [s.id for s in SMS.StudentsList]:
                print(f"Student {ID} is not added. Please add the student first.")
                continue

            if Code not in [s.code for s in SMS.SubjectsList]:
                print(f"Subject {Code} is not added. Please add the subject first.")
                continue

            if (ID, Code) in [(r.id, r.code) for r in SMS.RecordList]:
                print(f"Student {ID} is already enrolled in {Code}.")
                continue

            SMS.Enroll(ID, Code)
        # ---------------------------------------------------------------------------------
        elif User_Input == 4:           # Add grade

            DrawLine()
            print('\nHere is the previous record of grades\n')
            print(f'{'ID'}\t|\t{'CODE'}\t|\t{'GRADE'}\t|\n')
            print(*[(f'{r.id}\t|\t{r.code}\t|\t{r.grade}\t|\n') for r in SMS.RecordList])
            DrawLine()

            try:
                ID, Code, Grade = input("Enter sutdent id, subject code, grade (e.g. 1002, EE-826, 50):\t").split(",")
                SMS.AddGrades(ID.strip(),Code.strip(),Grade.strip())
            except ValueError:
                print("Invalid input. Try again.")
                continue
        # ---------------------------------------------------------------------------------
        elif User_Input == 5:           # Add attendance

            DrawLine()
            print('\nHere is the previous record of attendance\n')
            print(f'{'ID'}\t|\t{'CODE'}\t|\t{'ATTEND'} |\n')
            print(*[(f'{r.id}\t|\t{r.code}\t|\t{r.attend} |\n') for r in SMS.RecordList])
            DrawLine()

            try:
                ID, Code, Attend = input("Enter sutdent id, subject code, attendance (e.g. 1002, EE-826, 10/15):\t").split(",")
                SMS.MarkAttendance(ID.strip(),Code.strip(),Attend.strip())
            except ValueError:
                print("Invalid input. Try again.")
                continue

        # ---------------------------------------------------------------------------------
        elif User_Input == 6: # Show report

            DrawLine()
            print('\nHere is the list of students\n')
            print(f'{'ID'}\t|\t{'Name'}\t|\n')
            print(*[(f'{s.id}\t|\t{s.name}\t|\n') for s in SMS.StudentsList])
            DrawLine()

            try:
                ID  =   input("Enter sutdent id (e.g. 1002):\t").strip()
            except ValueError:
                print("Invalid input. Try again.")
                continue

            SMS.GenerateReport(ID)

        # ---------------------------------------------------------------------------------
        elif User_Input == 7:

            print('-'*36)
            print(f"|\t{'COMPLETE RECORD':27}|")
            print('-'*36)
            print(f"| {'ID':5}| {'CODE':11}| {'GRADE':5}| {'ATTEND':6}|")
            print('-'*36)
            for r in SMS.RecordList:
                print(f"| {r.id:5}| {r.code:11}| {r.grade:5}| {r.attend:6}|")
                
            print('-'*36)
        # ---------------------------------------------------------------------------------
        elif User_Input == 8:

            print('\nSaving updated data ...')

            SMS.Write_Data_Files()

            print('\nExiting ...')


            break
        # ---------------------------------------------------------------------------------
        else:
            continue


if __name__ == "__main__":
    main()
