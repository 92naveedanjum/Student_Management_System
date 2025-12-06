# --------------------------------------------------------------
# IN THE NAME OF ALLAH, THE MOST BENEFICENT, THE MOST MERCIFUL
# --------------------------------------------------------------
#                          manager.py
# --------------------------------------------------------------
from models.student import Student
from models.subject import Subject
from models.record import Record

class SystemManager:
    
    StudentsList    =   []
    SubjectsList    =   []
    RecordList      =   []
    # ---------------------------------------------------------------------------------
    def AddStudent(self, name, ID, Sec = 'A'):
        
        NewStudent  =   Student(name, ID, Sec)

        if NewStudent in self.StudentsList:
            return f"{name} is already added.\n"
        else:
            self.StudentsList.append(NewStudent)
            return f"{name} added auccessfully.\n"
    # ---------------------------------------------------------------------------------
    def AddSubject(self, name, code, credits):
        NewSubject  = Subject(name, code, credits)
        self.SubjectsList.append(NewSubject)
    # ---------------------------------------------------------------------------------
    def AddRecord(self, id, code, grade, attend):
        NewRecord  = Record(id, code, grade, attend)
        self.RecordList.append(NewRecord)
    # ---------------------------------------------------------------------------------
    def Enroll(self, id, code):
        self.AddRecord(id, code, grade = None, attend=None)
        print(f"Student with ID: {id} enrolled in subject with Code: {code} successfully.")
    # ---------------------------------------------------------------------------------
    def AddGrades(self,ID, Code, Grade):
       
        if (ID, Code) not in [(r.id, r.code) for r in self.RecordList]:
            print(f"Student with ID: {ID} with subject Code: {Code} not found in the record.")

        Index = [(r.id, r.code) for r in self.RecordList].index((ID, Code))

        self.RecordList[Index].grade = Grade            
        
        print('-'*25,'\nGrade updated successfully\n','-'*25)
    # ---------------------------------------------------------------------------------
    def MarkAttendance(self,ID, Code, Attend):

        if (ID, Code) not in [(r.id, r.code) for r in self.RecordList]:
            print(f"Student {ID} with subject {Code} not found in the record.")

        Index = [(r.id, r.code) for r in self.RecordList].index((ID, Code))

        self.RecordList[Index].attend = Attend            
        
        print('-'*25,'\nAttendance updated successfully\n','-'*25)

    # ---------------------------------------------------------------------------------
    def GenerateReport(self,ID):

        PercentAttend = lambda s: str(int(int(s.split('/')[0])/int(s.split('/')[1])*100))

        Name    =   [s.name     for s in self.StudentsList  if s.id == ID]
        Section =   [s.section  for s in self.StudentsList  if s.id == ID]
        Subjects=   [r.code     for r in self.RecordList    if r.id == ID]
        Grades  =   [r.grade    for r in self.RecordList    if r.id == ID]
        Attend  =   [r.attend   for r in self.RecordList    if r.id == ID]
        AttendPer=  [PercentAttend(r.attend)   for r in self.RecordList    if r.id == ID]
        AvgGrade=   sum(map(float,Grades))/len(Grades)

        print('-'*40)
        print(f"\tSTUDENT REPORT CARD")
        print('-'*40)

        print(f"{'ID':20}|\t{ID}")
        print(f"{'Name':20}|\t{''.join(Name)}")
        print(f"{'Section':20}|\t{''.join(Section)}")
        print(f"{'Subjects Enrolled':20}|\t{' | '.join(Subjects)}")
        print(f"{'Attendance':20}|\t{' | '.join(Attend)}")
        print(f"{'Attend (%)':20}|\t{' | '.join(AttendPer)}")
        print(f"{'Grades':20}|\t{' | '.join(Grades)}")
        print(f"{'Average Grade':20}|\t{AvgGrade:.2f} %")

        print('-'*40)

    # ---------------------------------------------------------------------------------
    def Read_Data_Files(self):

        # --- Read Students ---
        with open('data\students.txt','r') as file:
            next(file)                                  # Skip header
            for line in file:
                if not line.strip():                    # Skip empty line
                    continue
                ID, Name, Section = line.split('|')     # Read a student from file
                self.AddStudent(Name.strip(),ID.strip(),Section.strip())        # Add a student in record
                

        # --- Read Subjects ---
        with open('data\subjects.txt','r') as file:
            next(file)                                  # Skip header
            for line in file:
                if not line.strip():                    # Skip empty line
                    continue
                Code, Name, Credits = line.split('|')     # Read a student from file
                self.AddSubject(Name.strip(), Code.strip(), Credits.strip())        # Add a student in record
                

        # --- Read Record ---
        with open('data/record.txt','r') as file:
            next(file)                                  # Skip header
            for line in file:
                if not line.strip():                    # Skip empty line
                    continue
                ID, Code, Grade, Attend = line.split('|')     # Read a student from file
                self.AddRecord(ID.strip(), Code.strip(), Grade.strip(), Attend.strip())        # Add a student in record
                


    def Write_Data_Files(self):
        # --- Write Students ---
        print('\nWriting student record ...')
        with open('data/students.txt','w') as file:
            file.write(f'{'ID':10} | {'Name':15} | {'Section'}\n\n')                                  # Write header
            for s in self.StudentsList:
                file.write(f"{s.id:10} | {s.name:15} | {s.section}\n")

        print('\nWriting subjects record ...')
        # # --- Write Subjects ---
        with open('data/subjects.txt','w') as file:
            file.write(f'{'Code':10} | {'Name':15} | {'Credits'}\n\n')                                  # Write header
            for s in self.SubjectsList:
                file.write(f"{s.code:10} | {s.name:15} | {s.credits}\n")

        print('\nWriting record summary ...')
        # # --- Write Record ---
        with open('data/record.txt','w') as file:
            file.write(f'{'ID':10} | {'Code':15} | {'Grade':8} | {'Attend'}\n\n')                                  # Write header
            for r in self.RecordList:
                file.write(f"{r.id:10} | {r.code:15} | {r.grade:8} | {r.attend}\n")


    




