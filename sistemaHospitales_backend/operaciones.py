from tkinter import*
import tkinter.messagebox
import sqlite3
import sistemaHospitales_frontend.pantallaPrincipal
import mysql.connector

# pantalla.ejecutar()


def conectar():
    try:
        try:
            conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
            cursor=conexion.cursor()
            crear_bd="CREATE DATABASE BD_Hospital"
            cursor.execute(crear_bd)
            #conexion1 = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin')
        except:
            print("la bd llamada bd_Hospital ha sido creada anteriormente")
        try:
            conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
            cursor=conexion.cursor()
            crear_tabla_hospitales='''
                CREATE TABLE Hospitales (
                    Id INTEGER AUTO_INCREMENT PRIMARY KEY ,
                    Nombre VARCHAR(50), 
                    Localidad VARCHAR(50), 
                    Provincia VARCHAR(50), 
                    Calle VARCHAR(50), 
                    Telefono VARCHAR (50)
                )
            '''
            cursor.execute(crear_tabla_hospitales)
        except:
            print("ya existe la tabla hospitales")

        
        try:
            conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
            cursor=conexion.cursor()
            crear_tabla_personas='''
                CREATE TABLE personas (
                    Dni INT(8) ,
                    Nombre VARCHAR(50), 
                    Apellido VARCHAR(50), 
                    Genero VARCHAR(50), 
                    Nacimiento VARCHAR(50), 
                    Nacionalidad VARCHAR(50),
                    Telefono VARCHAR (50),
                    TelAlter VARCHAR (50),
                    Email VARCHAR (50),
                    PRIMARY KEY (Dni)
                    
                )
            '''
            cursor.execute(crear_tabla_personas)
        except:
            print("ya existe la tabla personas")
        #Id_hospital INT UNIQUE,
                #FOREIGN KEY (Id_hospital) REFERENCES hospitales(Id)
        
        #
        try:
            conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
            cursor=conexion.cursor()
            crear_tabla_medicos='''
                CREATE TABLE medicos (
                    Dni INT,
                    PRIMARY KEY (Dni),
                    FOREIGN KEY (Dni) REFERENCES personas(Dni) ON DELETE CASCADE

                )
            '''
            cursor.execute(crear_tabla_medicos)

        except:
            print("ya existe la tabla medicos")

        conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
        cursor=conexion.cursor()
        crear_tabla_pacientes='''
            CREATE TABLE pacientes (
                Dni INT PRIMARY KEY,
                Fecha_ingreso VARCHAR (50),
                Fecha_egreso VARCHAR (50)
            )
        '''
        cursor.execute(crear_tabla_pacientes)
        #try:
        conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
        cursor=conexion.cursor()
        crear_tabla_hospitales_medicos='''
            CREATE TABLE Hospitales_Medicos (
                Id_hospital INT,
                Dni_medico INT,
                PRIMARY KEY (Id_hospital,Dni_medico),
                FOREIGN KEY (Id_hospital) REFERENCES hospitales(Id) ON DELETE CASCADE,
                FOREIGN KEY (Dni_medico) REFERENCES medicos(Dni) ON DELETE CASCADE

            )
        '''
        cursor.execute(crear_tabla_hospitales_medicos)

        conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
        cursor=conexion.cursor()
        crear_tabla_pacientes_medicos='''
            CREATE TABLE Pacientes_Medicos (
                Dni_medico INT,
                Dni_paciente INT,
                PRIMARY KEY (Dni_medico,Dni_paciente),
                FOREIGN KEY (Dni_medico) REFERENCES medicos(Dni) ON DELETE CASCADE,
                FOREIGN KEY (Dni_paciente) REFERENCES pacientes(Dni) ON DELETE CASCADE
            )
        '''
        cursor.execute(crear_tabla_pacientes_medicos)

        conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
        cursor=conexion.cursor()
        crear_tabla_especialidades='''
            CREATE TABLE especialidades (
                Id INTEGER AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR (50),
                Descripcion VARCHAR (50),
                Dni_medico INT,
                FOREIGN KEY (Dni_medico) REFERENCES medicos(Dni) ON DELETE CASCADE
                
            )
        '''
        cursor.execute(crear_tabla_especialidades)

        conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
        cursor=conexion.cursor()
        crear_tabla_enfermedades='''
            CREATE TABLE enfermedades (
                Id INTEGER AUTO_INCREMENT PRIMARY KEY,
                Nombre VARCHAR (50),
                Descripcion VARCHAR (50)
                
            )
        '''

        cursor.execute(crear_tabla_enfermedades)


        conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
        cursor=conexion.cursor()
        crear_tabla_paciente_enfermedad='''
            CREATE TABLE paciente_enfermedad (
                Id_enfermedad INT,
                Dni_paciente INT,
                PRIMARY KEY (Id_enfermedad,Dni_paciente),
                FOREIGN KEY (Dni_paciente) REFERENCES pacientes(Dni) ON DELETE CASCADE,
                FOREIGN KEY (Id_enfermedad) REFERENCES enfermedades(Id) ON DELETE CASCADE
                
            )
        '''

        cursor.execute(crear_tabla_paciente_enfermedad)

        tkinter.messagebox.showinfo("Info","BBDD llamada bd_hospital creada con éxito")

    except:

        tkinter.messagebox.showinfo("Info", "BBDD llamada bd_hospital creada anteriormente")

def altaHospital(Nombre,Localidad,Provincia,Calle,Telefono):
    conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
    cursor=conexion.cursor()
    sql='''INSERT INTO hospitales (NOMBRE, LOCALIDAD, PROVINCIA, CALLE, TELEFONO) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(Nombre,Localidad,Provincia,Calle,Telefono)
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

def busca_hospital(nombre_hospital):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql = "SELECT * FROM bd_hospital.hospitales WHERE NOMBRE = {}".format(nombre_hospital)
    cur.execute(sql)
    nombreX = cur.fetchall()
    cur.close()     
    return nombreX 
def mostrar_todo():
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cursor = conexion.cursor()
    sql = "SELECT * FROM bd_hospital.hospitales " 
    cursor.execute(sql)
    registro = cursor.fetchall()
    return registro

def elimina_hospital(codigo):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''DELETE FROM bd_hospital.hospitales WHERE ID = {}'''.format(codigo)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

    # cursor.execute('''
    #     INSERT INTO Paciente (Dni,Nombre,Apellido,Genero,Nacimiento,Telefono,TelAlter,Email,Id_hospital) VALUES (23221345,"GGRR","Apellido","Genero","Nacimiento","Telefono","TelAlter","Email","Id_hospital")
    # ''')

    # cursor.execute('''
    #     INSERT INTO Paciente (Dni,Nombre,Apellido,Genero,Nacimiento,Telefono,TelAlter,Email,Id_hospital) VALUES (23455678,"blalbla","Apellido","Genero","Nacimiento","Telefono","TelAlter","Email",1)
    # ''')

    # conexion.commit()
    # #

    # consulta=cursor.execute('''
    #     SELECT Paciente.Nombre,Hospital.Nombre FROM Paciente INNER JOIN Hospital ON Hospital.Id = Paciente.Id_hospital 
    # ''')
    # print(consulta.fetchall())
    #         #
def altaMedico(Dni,Nombre,Apellido,Genero,FechaNac,Nacionalidad,Telefono,TelAlter,Email):


    conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
    cursor=conexion.cursor()
        
    sql='''INSERT INTO personas (Dni,Nombre,Apellido,Genero,Nacimiento,Nacionalidad,Telefono,TelAlter,Email) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}','{}')'''.format(Dni,Nombre,Apellido,Genero,FechaNac,Nacionalidad,Telefono,TelAlter,Email)
    cursor.execute(sql)
    sql2='''INSERT INTO medicos (Dni) 
        VALUES('{}')'''.format(Dni)
    cursor.execute(sql2)

    conexion.commit()
    conexion.close()

def busca_medico(nombre_medico):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql = "SELECT * FROM bd_hospital.personas INNER JOIN bd_hospital.medicos ON bd_hospital.personas.Dni = bd_hospital.medicos.Dni WHERE bd_hospital.personas.Nombre = {}".format(nombre_medico)
    cur.execute(sql)
    nombreX = cur.fetchall()
    cur.close()     
    return nombreX 
def mostrar_medico():
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cursor = conexion.cursor()
    sql1 = "SELECT * FROM bd_hospital.personas INNER JOIN bd_hospital.medicos ON bd_hospital.personas.Dni = bd_hospital.medicos.Dni "
    
    cursor.execute(sql1)
    registro = cursor.fetchall()
    #print(registro)
    #print(registro[0])
    return registro

def elimina_medico(codigo):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''DELETE FROM bd_hospital.medicos WHERE Dni = {}'''.format(codigo)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

def altaPaciente(Dni,Nombre,Apellido,Genero,FechaNac,Nacionalidad,Telefono,TelAlter,Email):


    conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
    cursor=conexion.cursor()
        
    sql='''INSERT INTO personas (Dni,Nombre,Apellido,Genero,Nacimiento,Nacionalidad,Telefono,TelAlter,Email) 
        VALUES('{}', '{}','{}', '{}','{}','{}','{}','{}','{}')'''.format(Dni,Nombre,Apellido,Genero,FechaNac,Nacionalidad,Telefono,TelAlter,Email)
    cursor.execute(sql)
    sql2='''INSERT INTO pacientes (Dni) 
        VALUES('{}')'''.format(Dni)
    cursor.execute(sql2)


    conexion.commit()
    conexion.close()

def busca_paciente(nombre_paciente):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql = "SELECT * FROM bd_hospital.personas INNER JOIN bd_hospital.pacientes ON bd_hospital.personas.Dni = bd_hospital.pacientes.Dni WHERE bd_hospital.personas.Nombre = {}".format(nombre_paciente)
    cur.execute(sql)
    nombreX = cur.fetchall()
    cur.close()     
    return nombreX 
def mostrar_paciente():
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cursor = conexion.cursor()
    sql1 = "SELECT * FROM bd_hospital.personas INNER JOIN bd_hospital.pacientes ON bd_hospital.personas.Dni = bd_hospital.pacientes.Dni "
    
    cursor.execute(sql1)
    registro = cursor.fetchall()
    #print(registro)
    #print(registro[0])
    return registro

def elimina_paciente(codigo):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''DELETE FROM bd_hospital.pacientes WHERE Dni = {}'''.format(codigo)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

def altaEspecialidad(Nombre,Descripcion,DniMedico):


    conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
    cursor=conexion.cursor()
        
    sql='''INSERT INTO especialidades (Nombre,Descripcion,Dni_medico) 
        VALUES('{}', '{}','{}')'''.format(Nombre,Descripcion,DniMedico)
    cursor.execute(sql)

    conexion.commit()
    conexion.close()

def busca_especialidad(nombre_especialidad):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql = "SELECT * FROM bd_hospital.especialidades WHERE Nombre = {}".format(nombre_especialidad)
    cur.execute(sql)
    nombreX = cur.fetchall()
    cur.close()     
    return nombreX 
def mostrar_especialidad():
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cursor = conexion.cursor()
    sql1 = "SELECT * FROM bd_hospital.especialidades "
    
    cursor.execute(sql1)
    registro = cursor.fetchall()
    #print(registro)
    #print(registro[0])
    return registro

def elimina_especialidad(codigo):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''DELETE FROM bd_hospital.especialidades WHERE Id = {}'''.format(codigo)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

def altaEnfermedad(Nombre,Descripcion):


    conexion = mysql.connector.connect( host='localhost',database ='bd_hospital', user = 'root', password ='admin',port='3306')
    cursor=conexion.cursor()
        
    sql='''INSERT INTO bd_hospital.enfermedades (Nombre,Descripcion) 
        VALUES('{}', '{}')'''.format(Nombre,Descripcion)
    cursor.execute(sql)

    conexion.commit()
    conexion.close()

def busca_enfermedad(nombre_enfermedad):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql = "SELECT * FROM bd_hospital.enfermedades WHERE Nombre = {}".format(nombre_enfermedad)
    cur.execute(sql)
    nombreX = cur.fetchall()
    cur.close()     
    return nombreX 
def mostrar_enfermedad():
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cursor = conexion.cursor()
    sql1 = "SELECT * FROM bd_hospital.enfermedades "
    
    cursor.execute(sql1)
    registro = cursor.fetchall()
    #print(registro)
    #print(registro[0])
    return registro

def elimina_enfermedad(codigo):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''DELETE FROM bd_hospital.enfermedades WHERE Id = {}'''.format(codigo)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

def añadirEnfermedad(codigo,dniPaciente):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''INSERT INTO bd_hospital.paciente_enfermedad (Id_enfermedad,Dni_paciente) 
        VALUES('{}', '{}')'''.format(codigo,dniPaciente)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

def añadirHospital(codigo,dniMedico):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''INSERT INTO bd_hospital.hospitales_medicos (Id_hospital,Dni_medico) 
        VALUES('{}', '{}')'''.format(codigo,dniMedico)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

def añadirMedico(dniPaciente,dniMedico):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql='''INSERT INTO bd_hospital.pacientes_medicos (Dni_medico,Dni_paciente) 
        VALUES('{}', '{}')'''.format(dniMedico,dniPaciente)
    cur.execute(sql)
    conexion.commit()    
    cur.close()

def busca_medico_hospital(id_hospital):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql = '''SELECT bd_hospital.personas.Dni,
    bd_hospital.personas.Nombre, 
    bd_hospital.personas.Apellido,
    bd_hospital.personas.Genero,
    bd_hospital.personas.Nacimiento,
    bd_hospital.personas.Nacionalidad,
    bd_hospital.personas.Telefono,
    bd_hospital.personas.TelAlter,
    bd_hospital.personas.Email,
    bd_hospital.hospitales_medicos.Id_hospital 
    FROM bd_hospital.personas 
    INNER JOIN bd_hospital.medicos 
    ON bd_hospital.personas.Dni = bd_hospital.medicos.Dni 
    INNER JOIN bd_hospital.hospitales_medicos 
    ON bd_hospital.hospitales_medicos.Dni_medico = bd_hospital.medicos.Dni 
    WHERE bd_hospital.hospitales_medicos.Id_hospital = {}'''.format(id_hospital)
    cur.execute(sql)
    nombreX = cur.fetchall()
    cur.close()     
    return nombreX 

def busca_medico_hospital_por_nombre(nombre_medico,id_hospital):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()

    print(nombre_medico,id_hospital)
    sql = '''
        SELECT
            bd_hospital.personas.Dni,
            bd_hospital.personas.Nombre,
            bd_hospital.personas.Apellido,
            bd_hospital.personas.Genero,
            bd_hospital.personas.Nacimiento,
            bd_hospital.personas.Nacionalidad,
            bd_hospital.personas.Telefono,
            bd_hospital.personas.TelAlter,
            bd_hospital.personas.Email,
            bd_hospital.hospitales_medicos.Id_hospital
        FROM
            bd_hospital.personas
        INNER JOIN
            bd_hospital.medicos ON bd_hospital.personas.Dni = bd_hospital.medicos.Dni
        INNER JOIN
            bd_hospital.hospitales_medicos ON bd_hospital.hospitales_medicos.Dni_medico = bd_hospital.medicos.Dni
        WHERE
            bd_hospital.personas.Nombre = {}
            AND bd_hospital.hospitales_medicos.Id_hospital = {}
            '''.format(nombre_medico,id_hospital)
    cur.execute(sql)
    nombreX = cur.fetchall()

    print(nombreX)
    cur.close()     
    return nombreX 

def busca_paciente_hospital(id_hospital):
    conexion = mysql.connector.connect( host='localhost',user = 'root',password ='admin',port='3306')
    cur = conexion.cursor()
    sql = '''
    SELECT 
        bd_hospital.personas.Dni,
        bd_hospital.personas.Nombre,
        bd_hospital.personas.Apellido,
        bd_hospital.personas.Genero,
        bd_hospital.personas.Nacimiento,
        bd_hospital.personas.Nacionalidad,
        bd_hospital.personas.Telefono,
        bd_hospital.personas.TelAlter,
        bd_hospital.personas.Email,
        bd_hospital.hospitales_medicos.Id_hospital 
        
    FROM bd_hospital.personas 
    INNER JOIN 
        bd_hospital.pacientes 
        ON bd_hospital.personas.Dni = bd_hospital.pacientes.Dni 
    INNER JOIN 
        bd_hospital.pacientes_medicos 
        ON bd_hospital.pacientes_medicos.Dni_paciente = bd_hospital.pacientes.Dni
    INNER JOIN 
        bd_hospital.hospitales_medicos 
        ON bd_hospital.pacientes_medicos.Dni_medico = bd_hospital.hospitales_medicos.Dni_medico
        WHERE bd_hospital.hospitales_medicos.Id_hospital = {}'''.format(id_hospital)
    cur.execute(sql)
    nombreX = cur.fetchall()
    print(nombreX)
    cur.close()     
    return nombreX 