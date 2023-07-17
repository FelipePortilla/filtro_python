import coree
import os
from datetime import datetime

diccCitas = {}
def LoadInfocitas():
    global diccCitas
    if (coree.checkFile("citas.json")):
        diccCitas = coree.LoadInfo("citas.json")
    else:
        coree.crearInfo("citas.json",diccCitas)

def MainMenu():
    os.system("clear") or os.system('cls')
    isCliRun = True
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','ADMINISTRACION DE CITAS',' '))
    print('+','-'*55,'+')
    print("1. Registrar cita")
    print("2. Buscar cita")
    print("3. Editar cita")
    print("4. Eliminar cita")
    print("5. Regresar menu principal")
    opcion =int(input(":)_"))
    if (opcion == 1):
        os.system("clear") or os.system('cls')
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','REGISTRAR PACIENTE',' '))
        print('+','-'*55,'+')
        citaMedicaNumero = str((len(diccCitas)+1))
        nombrePaciente = input("Agrega el nombre del paciente: ").upper()
        while True:
            fecha_str = input("Ingresa fecha en el formato dd-mm-yyyy: ")
            try:
                fecha = datetime.strptime(fecha_str,"%d-%m-%Y").date()
                break
            except ValueError:
                print("Formato que ingreso es incorrecto.Ingrese nuevamente")
        fechaFinal=fecha.strftime("%d-%m-%Y")
        while True:
            hora_str = input("Ingresa hora en el formato HH:MM ")
            try:
                hora = datetime.strptime(hora_str,"%H:%M").time()
                break
            except ValueError:
                print("Formato que ingreso es incorrecto")
        horaFinal=hora.strftime("%H:%M")
        print(horaFinal)
        os.system('pause')
        while True:
            os.system("clear") or os.system('cls')
            print("MOTIVO DE CONSULTA")
            print("1.Dolor abdominal")
            print("2.Fractura")
            print("3.Fiebre y vomito")
            print("4.Otro(Description)")
            opcion=int(input("Ingresar opcion: "))
            if(opcion==1):
                motivo="DOLOR DE ABDOMINAL"
                break
            if(opcion==2):
                motivo="FRACTURA"
                break
            if(opcion==3):
                motivo="FIEBRE Y VOMITO"
                break
            if(opcion==4):
                motivo=input("Ingresa breve descripción: ")
                break
        paciente={
            "Cita #":citaMedicaNumero,
            "Nombre":nombrePaciente,
            "Fecha":fechaFinal,
            "Hora":horaFinal,
            "Motivo":motivo
        }
        diccCitas.update({f'{citaMedicaNumero}':paciente})
        coree.crearInfo('citas.json',diccCitas)
    if (opcion == 2):
        os.system('clear') and os.system('cls')
        busquedaPaciente=[]
        busquedaFecha=[]
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','BUSCAR PACIENTE',' '))
        print('+','-'*55,'+')
        print("Elige opcion para buscar al paciente:")
        print("1.Nombre del paciente")
        print("2.Fecha de la cita")
        opcion=int(input("Ingresar opcion: "))
        if(opcion==1):
            nombrePaciente=input("Ingresa nombre del paciente: ").upper()
            for item in diccCitas:
                if nombrePaciente in diccCitas[item].get('Nombre'):
                    busquedaPaciente.append(diccCitas[item])
            for i,item in enumerate(busquedaPaciente):
                print(f"{i+1}:{item}")
            os.system('pause') and os.system('sleep 8')
        if(opcion==2):
            fechaBuscar=input("Ingresa fecha de la cita: ").upper()
            for item in diccCitas:
                if fechaBuscar in diccCitas[item].get('Fecha'):
                    busquedaFecha.append(diccCitas[item])
            print(busquedaFecha)
            for i,item in enumerate(busquedaFecha):
                print(f"{i+1}:{item}")
            os.system('pause') and os.system('sleep 8')
            # se esperaa un momento y elprograma lo envia al inicio
    if (opcion == 3):
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDITAR CITA',' '))
        print('+','-'*55,'+')
        print("Ingresar nombre,fecha de cita del paciente. ")
        nombrePaciente=input("Ingresa nombre del paciente: ").upper()
        fechaBuscar=input("Ingresa fecha de la cita: ").upper()
        for item in diccCitas:
            if (nombrePaciente in diccCitas[item].get('Nombre') and fechaBuscar in diccCitas[item].get('Fecha') ):
                print(f"El paciente es: {nombrePaciente}")
                nombreModificar= input("Desea modificar el nombre o Enter para continuar: ").upper() or diccCitas[item].get('Nombre')
                fechaModificar = input("Desea modificar la fecha( formato dd-mm-yyyy) o Enter para continuar: ").upper() or diccCitas[item].get('Fecha')
                horaModificar= input("Desea modificar la hora (formato HH:MM) o Enter para continuar: ").upper() or diccCitas[item].get('Hora')
                paciente={
                    "Nombre":nombreModificar,
                    "Fecha":fechaModificar,
                    "Hora":horaModificar,
                }
                diccCitas.update({f'{diccCitas[item].get("Cita #")}':paciente})
                coree.crearInfo('citas.json',diccCitas)
                break
    if (opcion == 4):
        print('+','-'*55,'+')
        print("|{:^16}{}{:^15}|".format(' ','EDITAR CITA',' '))
        print('+','-'*55,'+')
        print("Ingresar nombre,fecha y  de cita del paciente. ")
        nombrePaciente=input("Ingresa nombre del paciente: ").upper()
        fechaBuscar=input("Ingresa fecha de la cita: ").upper()
        for i,item in enumerate(diccCitas):
            if (nombrePaciente in diccCitas[item].get('Nombre') and fechaBuscar in diccCitas[item].get('Fecha') ):
                print(diccCitas)
                diccCitas.pop(item)
                print(diccCitas)
                coree.EditarData('citas.json',diccCitas)
                break
        print("No se encontro paciente")
    if (opcion == 5):
        isCliRun=False
    if(isCliRun):
        MainMenu()

