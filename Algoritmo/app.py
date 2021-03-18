#se crean variables
programs = []
menuSucces = True
info = []
genderList = ['No especifico','Hombre','Mujer']
numPrograms = 0
numProgramsValidate = True
numStudentsValidate = True

#funcion que recibe las notas y devuelve el promedio de notas por estudiante
def averageStudent():
    average = 0
    for j in range(1,6):
        notaValidate = True
        while notaValidate:
            try:
                average = average + float(input(f"Ingrese la nota {j}: "))
                notaValidate = False
            except:
                print('La nota debe ser un número, ingresa la nota nuevamente')
    average = average / 5
    return average
#se crea clase que se usa como plantilla para programa de admision
class Program(object):

  def __init__(self, men=0, women=0, notbinary=0, average = 0, program=0, numstudents=0):
    self.men = men
    self.women = women
    self.notbinary = notbinary
    self.average = average
    self.program = program
    self.numstudents = numstudents

  def menCount(self):
    self.men += 1
    return self.men

  def womenCount(self):
    self.women += 1
    return self.women
  
  def notbinaryCount(self):
    self.notbinary += 1
    return self.notbinary

  def students(self):
    self.numstudents += 1
    return self.numstudents

  def averageCount(self,av):
    self.average += av
    return self.average

  def setProgram(self,pr):
    self.program = pr
    return self.program

#se crean instancias clase que servira como plantilla para admisiones
program0 = Program()
program1 = Program()
program2 = Program()
program3 = Program()
program4 = Program()

#se crea clase para usar como plantilla de programa de matriculas 
class Inscription(object):
   def __init__(self, average=0,men = 0,women = 0, numstudents = 0):
        self.men = men
        self.women = women
        self.average = average
        self.numstudents = numstudents 

   def menCount(self):
        self.men += 1
        return self.men

   def womenCount(self):
        self.women += 1
        return self.women

   def ageCount(self,age):
        self.average += age
        return self.average

   def students(self):
        self.numstudents += 1
        return self.numstudents

inscription = Inscription()

#programa principal
while menuSucces:
    menu = input("¿Qué desea hacer? - admision(admi) - matrícula(matri): ")
    if menu == "admi":
        menuSucces = False
        while numProgramsValidate:
            
            try:
                numPrograms = int(input("Ingrese el  número de programas que desea registrar (Maximo 5): "))
            except ValueError:
                print('Debe ingresar un número y este debe ser menor o igual a 5')
            else:
                if numPrograms <= 5:
                    numProgramsValidate = False
                    for i in range(numPrograms):
                        nameProgram = input(f'Ingrese el nombre del programa academico {i+1}: ') 
                        programs.append(nameProgram)
                    while numStudentsValidate:
                        try:    
                            numStudents = int(input('Ingrese el número de estudiantes: '))
                            numStudentsValidate = False
                        except:
                            print('Debe ingresar un numero para la cantidad de estudiantes')
                    
                    for i in range(numStudents):
                        numProgramSelectValidate = True
                        genderValidate = True
                        count = 0
                        print('\n')
                        print('########## PROGRAMAS ##########')
                        for i in programs:
                            print(' '+str(count) + '-' + i)
                            count+=1
                        print('###############################')
                        print('\n')
                        while numProgramSelectValidate:
                            try:
                                programStudent = int(input('Seleccione el número del programa academico al que pertenece el estudiante a registrar en la lista anterior: '))
                                if programStudent > 4:
                                    numProgramSelectValidate = True
                                    print('El numero debe corresponder a uno de los programas en el menu anterior')
                                elif programStudent <= 4:
                                    numProgramSelectValidate = False
                            except:
                                print('Debe ingresar un numero y debe estar en el menu anterior')
                        nameStudent = input('Ingrese el nombre del estudiante: ')
                        note = averageStudent()
                        count2 = 0
                        print('\n')
                        print('########## GÉNERO ##########')
                        for i in genderList:
                            print(' '+str(count2) + '-' + i)
                            count2+=1
                        print('###############################')
                        print('\n')
                        while genderValidate:
                            try:
                                gender = int(input('Seleccione el número del género del estudiante de la lista anterior: '))
                                if gender > 2:
                                    genderValidate = True
                                    print('El numero debe corresponder a uno de los géneros en el menu anterior')
                                elif gender <= 2:
                                    genderValidate = False
                            except:
                                print('Debe ingresar un numero y debe estar en el menu anterior')
                        info.append({'name':nameStudent,'program':programStudent, 'average':note, 'gender':gender})
                        if programStudent == 0:
                            program0.setProgram(programStudent)
                            program0.students()
                            program0.averageCount(note)
                            if gender == 0:
                                program0.notbinaryCount()
                            if gender == 1:
                                program0.menCount()
                            if gender == 2:
                                program0.womenCount()
                        if programStudent == 1:
                            program1.setProgram(programStudent)
                            program1.students()
                            program1.averageCount(note)
                            if gender == 0:
                                program1.notbinaryCount()
                            if gender == 1:
                                program1.menCount()
                            if gender == 2:
                                program1.womenCount()
                        if programStudent == 2:
                            program2.setProgram(programStudent)
                            program2.students()
                            program2.averageCount(note)
                            if gender == 0:
                                program2.notbinaryCount()
                            if gender == 1:
                                program2.menCount()
                            if gender == 2:
                                program2.womenCount()
                        if programStudent == 3:
                            program3.setProgram(programStudent)
                            program3.students()
                            program3.averageCount(note)
                            if gender == 0:
                                program3.notbinaryCount()
                            if gender == 1:
                                program3.menCount()
                            if gender == 2:
                                program3.womenCount()
                        if programStudent == 4:
                            program4.setProgram(programStudent)
                            program4.students()
                            program4.averageCount(note)
                            if gender == 0:
                                program4.notbinaryCount()
                            if gender == 1:
                                program4.menCount()
                            if gender == 2:
                                program4.womenCount()
                    print('\n')
                    print('-------------------  Información Global de programas registrados -------------------------------------- \n')
                    if program0.numstudents > 0:
                        programName = programs[program0.program]
                        print(f'###################### {programName.upper()} ######################')
                        print(f'El número de estudiantes en el programa {programName} es: {program0.numstudents}')
                        print(f'El promedio de notas del programa {programName} es: {program0.average/program0.numstudents}')
                        print(f'El número de hombres en el programa {programName} es: {program0.men}')
                        print(f'El número de mujeres en el programa {programName} es: {program0.women}')
                        print(f'El número de personas con otra orientación sexual en el programa {programName} es: {program0.notbinary} \n')
                    if program1.numstudents > 0:
                        programName = programs[program1.program]
                        print(f'###################### {programName.upper()} ######################')
                        print(f'El número de estudiantes en el programa {programName} es: {program1.numstudents}')
                        print(f'El promedio de notas del programa {programName} es: {program1.average/program1.numstudents}')
                        print(f'El número de hombres en el programa {programName} es: {program1.men}')
                        print(f'El número de mujeres en el programa {programName} es: {program1.women}')
                        print(f'El número de personas con otra orientación sexual en el programa {programName} es: {program1.notbinary} \n')
                    if program2.numstudents > 0:
                        programName = programs[program2.program]
                        print(f'###################### {programName.upper()} ######################')
                        print(f'El número de estudiantes en el programa {programName} es: {program2.numstudents}')
                        print(f'El promedio de notas del programa {programName} es: {program2.average/program2.numstudents}')
                        print(f'El número de hombres en el programa {programName} es: {program2.men}')
                        print(f'El número de mujeres en el programa {programName} es: {program2.women}')
                        print(f'El número de personas con otra orientación sexual en el programa {programName} es: {program2.notbinary} \n')
                    if program3.numstudents > 0:
                        programName = programs[program3.program]
                        print(f'###################### {programName.upper()} ######################')
                        print(f'El número de estudiantes en el programa {programName} es: {program3.numstudents}')
                        print(f'El promedio de notas del programa {programName} es: {program3.average/program3.numstudents}')
                        print(f'El número de hombres en el programa {programName} es: {program3.men}')
                        print(f'El número de mujeres en el programa {programName} es: {program3.women}')
                        print(f'El número de personas con otra orientación sexual en el programa {programName} es: {program3.notbinary} \n')
                    if program4.numstudents > 0:
                        programName = programs[program4.program]
                        print(f'###################### {programName.upper()} ######################')
                        print(f'El número de estudiantes en el programa {programName} es: {program4.numstudents}')
                        print(f'El promedio de notas del programa {programName} es: {program4.average/program4.numstudents}')
                        print(f'El número de hombres en el programa {programName} es: {program4.men}')
                        print(f'El número de mujeres en el programa {programName} es: {program4.women}')
                        print(f'El número de personas con otra orientación sexual en el programa {programName} es: {program4.notbinary} \n')

                    print('-------------------  Información de Estudiantes registrados -------------------------------------- \n')

                    for i in info:
                        name = i['name']
                        gender = genderList[i['gender']]
                        program = programs[i['program']]
                        average = i['average']
                        print(f'Nombre: {name} | sexo: {gender} | Pograma: {program} | Promedio: {average} ')
                    print('\n')
                    print('-------------------  Fin del programa  --------------------------------------------------------------')
                else:
                    numProgramsValidate = True      
            finally:
                if numPrograms > 5:
                    print('Ingrese nuevamente el numero de programas')
                if type(numPrograms) not in (int,float):    
                    print('######### Ejecute nuevamente el Programa #########')
            

    elif menu=="matri":
        menuSucces = False
        stop = True
        age = 0
        while stop:
            ageValidate = True
            sexValidate = True
            while ageValidate:
                try:
                    age = int(input('Ingrese la edad Del estudiante: ')) 
                    inscription.ageCount(age)
                except ValueError:
                    print('La edad debe ser númerica, ingrese la edad nuevamente')
                else:
                    ageValidate = False 
            while sexValidate:       
                sex = input("Ingrese el sexo del estudiante (h - H) - Hombre  (m - M) - Mujer: ")
                if sex == "m" or sex == "M":
                    inscription.womenCount()
                    sexValidate = False
                elif sex == "h" or sex == "H":
                    inscription.menCount()  
                    sexValidate = False  
                else:
                    print('El sexo debe corresponder a algunas de las opciones anteriores, ingrese el sexo nuevamente.')
            stopAdmission = input("si desea parar de matricular ingrese 0, de lo contrario cualquier tecla para continuar: ")
            inscription.students()
            if stopAdmission == '0':
                print('\n')
                print('------------------  Información de estudiantes matriculados  ------------------------')
                print('\n')
                break
        
        averageAge = inscription.average/inscription.numstudents
        print(f"Número de estudiantes matriculados: {inscription.numstudents}")
        print(f"Promedio de edad de matriculados: {averageAge}")
        print(f"Número de mujeres matriculadas: {inscription.women}")
        print(f"Número de hombre matriculados: {inscription.men}")
        print('\n')
        print('------------------  El programa ha terminado  ------------------------')
    else:
        menuSucces = True