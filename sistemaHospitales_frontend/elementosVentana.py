from tkinter import*
from tkinter import ttk
from tkinter import PhotoImage
import tkinter.messagebox
import sistemaHospitales_backend.operaciones


class BarraMenu():
	def __init__(self,raiz):
		self.barraMenu=Menu(raiz)

		self.conectarMenu=Menu(self.barraMenu,tearoff=0)
		self.limpiarMenu=Menu(self.barraMenu,tearoff=0)
		self.ayudaMenu=Menu(self.barraMenu,tearoff=0)

	def configuracionMenu(self):

		self.conectarMenu.add_command(label="Conectar BD",command=sistemaHospitales_backend.operaciones.conectar)
		self.barraMenu.add_cascade(label="Datos", menu=self.conectarMenu)
		self.limpiarMenu.add_command(label="Medicos")
		self.barraMenu.add_cascade(label="Consulta", menu=self.consultaMedico)
	def consultaMedico(self):
		pass

class Titulo1():
	def __init__(self,raiz):
		self.frame=Frame(raiz,bg="#d3d2d2")
		
		self.labelTitulo1=Label(self.frame, text="Registro de hospitales", font=('Calibri',24,'bold'),bg="#d3d2d2",fg="#4dafe6")

		self.imagennexo=PhotoImage(file="sistemaHospitales_frontend/nexo.png")

		self.labelImagenNexo=Label(self.frame,image=self.imagennexo,bg="#d3d2d2")


		
	def configuracionTitulo(self):
		#self.frame2.pack(side=LEFT)
		#self.frame3.pack(side=RIGHT)#
		self.labelImagenNexo.pack(side=LEFT,padx=20)
	
		self.labelTitulo1.pack(anchor="w",padx=30,pady=30)
		
		self.frame.pack(fill=BOTH,expand=True)
		


class FormularioHospital():
	def __init__(self,raiz):
		self.frame=Frame(raiz,bg ="#d3d2d2")
		self.frame2=Frame(self.frame,bg ="#e9e9e9")
		self.frame3=Frame(self.frame,bg ="#d3d2d2")
		self.labelTitulo2=Label(self.frame2, text="Datos de hospital", font=("Calibri",15,'bold'),bg ="#e9e9e9",fg="#4dafe6")
		self.nombreLabel=Label(self.frame3, text="Nombre: ",bg ="#d3d2d2",fg="#6d6f70")
		


		self.localidadLabel=Label(self.frame3, text="Localidad: ",bg ="#d3d2d2",fg="#6d6f70")


		self.provLabel=Label(self.frame3, text="Provincia: ",bg ="#d3d2d2",fg="#6d6f70")


		self.calleLabel=Label(self.frame3, text="Calle: ",bg ="#d3d2d2",fg="#6d6f70")


		self.telefonoLabel=Label(self.frame3, text="Telefono: ",bg ="#d3d2d2",fg="#6d6f70")

		self.ingresoNombre = StringVar()
		self.ingresoLocalidad = StringVar()
		self.ingresoProvincia = StringVar()
		self.ingresoCalle = StringVar()
		self.ingresoTelefono = StringVar()
		
		


		# INGRESO Localidad
		

		#Ingreso Provincia
		

		#Ingreso Calle
		

		#Ingreso Telefono
		


		

	def configuracionFormulario(self):


		#self.labelTitulo2.config(text=titulo2)

		self.labelTitulo2.pack()

		self.nombreLabel.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

		self.localidadLabel.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

		self.provLabel.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)

		self.calleLabel.grid(row=6, column=0, sticky="nsew", padx=10, pady=10)

		self.telefonoLabel.grid(row=7, column=0, sticky="nsew", padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoNombre).grid(row=3, column=1, padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoLocalidad).grid(row=4, column=1, padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoProvincia).grid(row=5, column=1, padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoCalle).grid(row=6, column=1, padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoTelefono).grid(row=7, column=1, padx=10, pady=10)

		
		self.frame2.pack(expand=True,fill=X)
		self.frame3.pack()

		self.frame.pack(fill=BOTH,expand=True)
		

class FormularioPersona():
	def __init__(self,raiz):

		self.frame=Frame(raiz,bg ="#d3d2d2")

		self.frame2=Frame(self.frame,bg ="#e9e9e9")
		self.frame3=Frame(self.frame,bg ="#d3d2d2")


		

		self.dniLabel=Label(self.frame3, text="Dni: ",bg ="#d3d2d2",fg="#6d6f70")

		self.nombreLabel=Label(self.frame3, text="Nombre: ",bg ="#d3d2d2",fg="#6d6f70")
		


		self.apellidoLabel=Label(self.frame3, text="Apellido: ",bg ="#d3d2d2",fg="#6d6f70")


		self.generoLabel=Label(self.frame3, text="Genero: ",bg ="#d3d2d2",fg="#6d6f70")


		self.fechaNacLabel=Label(self.frame3, text="Nacimiento: ",bg ="#d3d2d2",fg="#6d6f70")


		self.nacionalidadLabel=Label(self.frame3, text="Nacionalidad: ",bg ="#d3d2d2",fg="#6d6f70")

		self.telefonoLabel=Label(self.frame3, text="Teléfono: ",bg ="#d3d2d2",fg="#6d6f70")

		self.telAlter=Label(self.frame3, text="Tel. alternativo: ",bg ="#d3d2d2",fg="#6d6f70")

		self.email=Label(self.frame3, text="Email: ",bg ="#d3d2d2",fg="#6d6f70")

		self.ingresoDni=StringVar()
		self.ingresoNombre=StringVar()

		self.ingresoApellido=StringVar()
		self.ingresoNombre=StringVar()
		self.ingresoGenero=StringVar()
		self.ingresoFechaNac=StringVar()
		self.ingresoNacionalidad=StringVar()
		self.ingresoTelefono=StringVar()
		self.ingresoTelAlter=StringVar()
		self.ingresoEmail=StringVar()


		


	def configuracionFormulario(self):

		#self.labelTitulo2.config(text=titulo2)

		

		self.dniLabel.grid(row=2, column=0, sticky="e", padx=4, pady=10)


		self.nombreLabel.grid(row=3, column=0, sticky="e", padx=4, pady=10)

		self.apellidoLabel.grid(row=4, column=0, sticky="e", padx=4, pady=10)

		self.generoLabel.grid(row=5, column=0, sticky="e", padx=4, pady=10)

		self.fechaNacLabel.grid(row=6, column=0, sticky="e", padx=4, pady=10)

		self.nacionalidadLabel.grid(row=2, column=2, sticky="e", padx=4, pady=10)

		self.telefonoLabel.grid(row=3, column=2, sticky="e", padx=4, pady=10)

		self.telAlter.grid(row=4, column=2, sticky="e", padx=4, pady=10)

		self.email.grid(row=5, column=2, sticky="e", padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoDni).grid(row=2, column=1, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoNombre).grid(row=3, column=1, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoApellido).grid(row=4, column=1, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoGenero).grid(row=5, column=1, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoFechaNac).grid(row=6, column=1, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoNacionalidad).grid(row=2, column=3, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoTelefono).grid(row=3, column=3, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoTelAlter).grid(row=4, column=3, padx=4, pady=10)

		Entry(self.frame3,width=15,textvariable=self.ingresoEmail).grid(row=5, column=3, padx=4, pady=10)

		

	
class FormularioMedico(FormularioPersona):
		"""docstring for ClassName"""
		def __init__(self,raiz):
			super().__init__(raiz)

			self.labelTitulo2=Label(self.frame2, text="Datos de medico", font=("Calibri",15,'bold'),bg ="#e9e9e9",fg="#4dafe6")
			
			

		def configuracionFormularioMedico(self):

			self.labelTitulo2.pack()
			

			self.frame2.pack(expand=True,fill=X)
			self.frame3.pack()

			self.frame.pack(fill=X)




class FormularioPaciente(FormularioPersona):
		"""docstring for ClassName"""
		def __init__(self,raiz):
			super().__init__(raiz)

			self.labelTitulo2=Label(self.frame2, text="Datos de paciente", font=("Calibri",15,'bold'),bg ="#e9e9e9",fg="#4dafe6")
			
			

		def configuracionFormularioPaciente(self):

			self.labelTitulo2.pack()
			


			self.frame2.pack(expand=True,fill=X)
			self.frame3.pack()

			self.frame.pack(fill=BOTH,expand=True)



				
class FormularioEspecialidad():
	def __init__(self,raiz):
		self.frame=Frame(raiz,bg ="#d3d2d2")
		self.frame2=Frame(self.frame,bg ="#e9e9e9")
		self.frame3=Frame(self.frame,bg ="#d3d2d2")
		self.labelTitulo2=Label(self.frame2, text="Datos de especialidad", font=("Calibri",15,'bold'),bg ="#e9e9e9",fg="#4dafe6")

		self.nombreLabel=Label(self.frame3, text="Nombre: ",bg ="#d3d2d2",fg="#6d6f70")
		


		self.dniMedicoLabel=Label(self.frame3, text="Dni Medico: ",bg ="#d3d2d2",fg="#6d6f70")


		self.descLabel=Label(self.frame3, text="Descripcion: ",bg ="#d3d2d2",fg="#6d6f70")


		

		self.ingresoNombre = StringVar()
		self.ingresoDniMedico = StringVar()
		self.ingresoDesc = StringVar()

		
	

	def configuracionFormulario(self):


		#self.labelTitulo2.config(text=titulo2)

		self.labelTitulo2.pack()

		self.nombreLabel.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

		self.dniMedicoLabel.grid(row=4, column=0, sticky="nsew", padx=10, pady=10)

		self.descLabel.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoNombre).grid(row=3, column=1, padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoDniMedico).grid(row=4, column=1, padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoDesc).grid(row=5, column=1, padx=10, pady=10)

		
		self.frame2.pack(expand=True,fill=X)
		self.frame3.pack()

		self.frame.pack(fill=BOTH,expand=True)
		

			
class FormularioEnfermedad():
	def __init__(self,raiz):
		self.frame=Frame(raiz,bg ="#d3d2d2")
		self.frame2=Frame(self.frame,bg ="#e9e9e9")
		self.frame3=Frame(self.frame,bg ="#d3d2d2")
		self.labelTitulo2=Label(self.frame2, text="Datos de enfermedad", font=("Calibri",15,'bold'),bg ="#e9e9e9",fg="#4dafe6")

		self.nombreLabel=Label(self.frame3, text="Nombre: ",bg ="#d3d2d2",fg="#6d6f70")
		


		


		self.descLabel=Label(self.frame3, text="Descripcion: ",bg ="#d3d2d2",fg="#6d6f70")
		

		self.ingresoNombre = StringVar()

		self.ingresoDesc = StringVar()

		
	

	def configuracionFormulario(self):


		#self.labelTitulo2.config(text=titulo2)

		self.labelTitulo2.pack()

		self.nombreLabel.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)

		self.descLabel.grid(row=5, column=0, sticky="nsew", padx=10, pady=10)

		Entry(self.frame3,textvariable=self.ingresoNombre).grid(row=3, column=1, padx=10, pady=10)


		Entry(self.frame3,textvariable=self.ingresoDesc).grid(row=5, column=1, padx=10, pady=10)

		
		self.frame2.pack(expand=True,fill=X)
		self.frame3.pack()

		self.frame.pack(fill=BOTH,expand=True)

		

class Botones():
	"""docstring for Botones"""
	def __init__(self, raiz, pantallaHospital, pantallaMedico, pantallaPaciente,pantallaEspecialidad,pantallaEnfermedad,pantallaPersonal):
		self.frame=Frame(raiz,bg="#d3d2d2")
		
		
		self.boton1=Button(self.frame,text="Datos de hospital",command=pantallaHospital,bg ="#d3d2d2",fg="#2d3d9b")
		

		self.boton2=Button(self.frame,text="Datos de médico", command=pantallaMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton3=Button(self.frame,text="Datos de paciente",command=pantallaPaciente,bg ="#d3d2d2",fg="#2d3d9b")
		self.boton4=Button(self.frame,text="Datos de enfermedad", command=pantallaEnfermedad,bg ="#d3d2d2",fg="#2d3d9b")
		self.boton5=Button(self.frame,text="Datos de especialidad", command=pantallaEspecialidad,bg ="#d3d2d2",fg="#2d3d9b")
		self.boton6=Button(self.frame,bg ="#d3d2d2",fg="#2d3d9b")

		
	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
		self.boton2.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
		self.boton3.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
		self.boton4.grid(row=2, column=2, sticky="nsew", padx=10, pady=10)
		self.boton5.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
		self.boton6.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		self.frame.pack(fill=BOTH)

class BotonesABM():
	"""docstring for Botones"""
	def __init__(self, raiz, formulario, tabla):
		self.frame=Frame(raiz,bg="#2d3d9b")
		self.raiz = raiz
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		
		self.tabla=tabla
		self.formulario=formulario
		self.ingresoNombre, self.ingresoLocalidad, self.ingresoProvincia, self.ingresoCalle, self.ingresoTelefono = self.formulario.ingresoNombre, self.formulario.ingresoLocalidad, self.formulario.ingresoProvincia, self.formulario.ingresoCalle, self.formulario.ingresoTelefono

		


		self.boton1=Button(self.frame2,text="Alta",command=self.altaHospital,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarHospital,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton3=Button(self.frame2,text="Limpiar",command=self.limpiar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton4=Button(self.frame2,text="Eliminar",command=self.eliminar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton6=Button(self.frame2,text="Consulta",command=self.consultaMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarTodo,bg ="#d3d2d2",fg="#2d3d9b")


		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False

	def consultaMedico(self):
		filaHospital = self.tabla.contenido.selection()

		codigo= self.tabla.contenido.item(filaHospital[0],"text")

		item=self.tabla.contenido.item(filaHospital[0])
		nombre_hospital=item['values'][0]
		print(nombre_hospital)
		ventanaSecundaria=VentanaSecundariaMedico_hospital(self.raiz,codigo,nombre_hospital)
		ventanaSecundaria.configuracion()
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton3.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

		self.boton4.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

		self.boton6.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
		


	def altaHospital(self):
		
		
			
		if self.borrarVentana==True:
			self.tabla.contenido.delete(*self.tabla.contenido.get_children())
			self.borrarVentana=False
		sistemaHospitales_backend.operaciones.altaHospital(self.ingresoNombre.get(), self.ingresoLocalidad.get(), self.ingresoProvincia.get(), self.ingresoCalle.get(), self.ingresoTelefono.get())
		self.tabla.agregar_datos(self.ingresoNombre.get(), self.ingresoLocalidad.get(), self.ingresoProvincia.get(), self.ingresoCalle.get(), self.ingresoTelefono.get())

	def buscarHospital(self):

		
		
		self.borrarVentana=True
		nombre_hospital = self.nombreBuscado.get()
		nombre_hospital = str("'" + nombre_hospital + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_hospital(nombre_hospital)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		
		for dato in nombre_buscado:
		    #print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5]))
	def mostrarTodo(self):
	
		self.borrarVentana=True
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_todo()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5]))
	def limpiar(self):
		
	
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		self.formulario.ingresoNombre.set('')
		self.formulario.ingresoLocalidad.set('')
		self.formulario.ingresoProvincia.set('')
		self.formulario.ingresoCalle.set('')
		self.formulario.ingresoTelefono.set('')

	def eliminar(self):
		
		
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		print(codigo)
		self.tabla.contenido.delete(fila)
			     
		sistemaHospitales_backend.operaciones.elimina_hospital(codigo)
			



class BotonesMedicos():
	"""docstring for Botones"""
	def __init__(self, raiz, formulario,tabla):
		self.frame=Frame(raiz,bg="#2d3d9b")
		self.raiz = raiz
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		self.formulario=formulario


		self.ingresoDni,self.ingresoNombre, self.ingresoApellido, self.ingresoGenero, self.ingresoFechaNac, self.ingresoNacionalidad , self.ingresoTelefono, self.ingresoTelAlter, self.ingresoEmail= self.formulario.ingresoDni,self.formulario.ingresoNombre, self.formulario.ingresoApellido, self.formulario.ingresoGenero, self.formulario.ingresoFechaNac, self.formulario.ingresoNacionalidad, self.formulario.ingresoTelefono, self.formulario.ingresoTelAlter, self.formulario.ingresoEmail
		self.tabla = tabla
		self.boton1=Button(self.frame2,text="Alta",command=self.altaMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton3=Button(self.frame2,text="Limpiar",command=self.limpiar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton4=Button(self.frame2,text="Eliminar",command=self.eliminar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton6=Button(self.frame2,text="Añadir hospital",command=self.añadirHospitales,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarTodo,bg ="#d3d2d2",fg="#2d3d9b")


		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton3.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

		self.boton4.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.boton6.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
	
	

	def altaMedico(self):
		ingresoDni=self.ingresoDni.get()
		if len(ingresoDni) == 8 and ingresoDni.isdigit():
			if self.borrarVentana==True:
				self.tabla.contenido.delete(*self.tabla.contenido.get_children())
				self.borrarVentana=False
			sistemaHospitales_backend.operaciones.altaMedico(self.ingresoDni.get(), self.ingresoNombre.get(), self.ingresoApellido.get(), self.ingresoGenero.get(), self.ingresoFechaNac.get(), self.ingresoNacionalidad.get(), self.ingresoTelefono.get(), self.ingresoTelAlter.get(), self.ingresoEmail.get())
			self.tabla.agregar_datos(self.ingresoDni.get(), self.ingresoNombre.get(), self.ingresoApellido.get(), self.ingresoGenero.get(), self.ingresoFechaNac.get(), self.ingresoNacionalidad.get(), self.ingresoTelefono.get(), self.ingresoTelAlter.get(), self.ingresoEmail.get())
		else:
			tkinter.messagebox.showerror("Error","Ingrese en DNI ocho digitos")
	def buscarMedico(self):
		self.borrarVentana=True
		nombre_medico = self.nombreBuscado.get()
		nombre_medico = str("'" + nombre_medico + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_medico(nombre_medico)
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		
		for dato in nombre_buscado:
		    print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))
	def limpiar(self):
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		self.formulario.ingresoDni.set('')
		self.formulario.ingresoNombre.set('')
		self.formulario.ingresoApellido.set('')
		self.formulario.ingresoGenero.set('')
		self.formulario.ingresoFechaNac.set('')
		self.formulario.ingresoNacionalidad.set('')
		self.formulario.ingresoTelefono.set('')
		self.formulario.ingresoTelAlter.set('')
		self.formulario.ingresoEmail.set('')
		self.formulario.ingresoIdHospital.set('')


	def eliminar(self):
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		print(codigo)
		self.tabla.contenido.delete(fila)
			     
		sistemaHospitales_backend.operaciones.elimina_medico(codigo)
	def mostrarTodo(self):
		self.borrarVentana=True
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_medico()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))

	def añadirHospitales(self):
		filaMedico = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(filaMedico[0],"text")
		ventanaSecundaria=VentanaSecundariaHospitales(self.raiz,codigo)
		ventanaSecundaria.configuracion()


class BotonesPacientes():
	"""docstring for Botones"""
	def __init__(self, raiz, formulario,tabla):
		self.frame=Frame(raiz,bg="#2d3d9b")
		self.raiz = raiz
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		self.formulario=formulario


		self.ingresoDni,self.ingresoNombre, self.ingresoApellido, self.ingresoGenero, self.ingresoFechaNac, self.ingresoNacionalidad , self.ingresoTelefono, self.ingresoTelAlter, self.ingresoEmail = self.formulario.ingresoDni,self.formulario.ingresoNombre, self.formulario.ingresoApellido, self.formulario.ingresoGenero, self.formulario.ingresoFechaNac, self.formulario.ingresoNacionalidad, self.formulario.ingresoTelefono, self.formulario.ingresoTelAlter, self.formulario.ingresoEmail
		self.tabla = tabla
		self.boton1=Button(self.frame2,text="Alta",command=self.altaPaciente,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarPaciente,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton3=Button(self.frame2,text="Limpiar",command=self.limpiar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton4=Button(self.frame2,text="Eliminar",command=self.eliminar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarPaciente,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton6=Button(self.frame2,text="Añadir enfermedades",command=self.añadirEnfermedades,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton7=Button(self.frame2,text="Añadir medico",command=self.añadirMedicos,bg ="#d3d2d2",fg="#2d3d9b")


		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton3.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

		self.boton4.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.boton6.grid(row=1, column=3, sticky="nsew", padx=10, pady=10)

		self.boton7.grid(row=1, column=4, sticky="nsew", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
	
	

	def altaPaciente(self):
		if self.borrarVentana==True:
			self.tabla.contenido.delete(*self.tabla.contenido.get_children())
			self.borrarVentana=False
		sistemaHospitales_backend.operaciones.altaPaciente(self.ingresoDni.get(), self.ingresoNombre.get(), self.ingresoApellido.get(), self.ingresoGenero.get(), self.ingresoFechaNac.get(), self.ingresoNacionalidad.get(), self.ingresoTelefono.get(), self.ingresoTelAlter.get(), self.ingresoEmail.get())
		self.tabla.agregar_datos(self.ingresoDni.get(), self.ingresoNombre.get(), self.ingresoApellido.get(), self.ingresoGenero.get(), self.ingresoFechaNac.get(), self.ingresoNacionalidad.get(), self.ingresoTelefono.get(), self.ingresoTelAlter.get(), self.ingresoEmail.get())

	def buscarPaciente(self):
		self.borrarVentana=True
		nombre_medico = self.nombreBuscado.get()
		nombre_medico = str("'" + nombre_medico + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_paciente(nombre_medico)
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		
		for dato in nombre_buscado:
		    print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))
	def limpiar(self):
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		self.formulario.ingresoDni.set('')
		self.formulario.ingresoNombre.set('')
		self.formulario.ingresoApellido.set('')
		self.formulario.ingresoGenero.set('')
		self.formulario.ingresoFechaNac.set('')
		self.formulario.ingresoNacionalidad.set('')
		self.formulario.ingresoTelefono.set('')
		self.formulario.ingresoTelAlter.set('')
		self.formulario.ingresoEmail.set('')
	

	def eliminar(self):
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		print(codigo)
		self.tabla.contenido.delete(fila)
			     
		sistemaHospitales_backend.operaciones.elimina_paciente(codigo)
	def mostrarPaciente(self):
		self.borrarVentana=True
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_paciente()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))
	
	def añadirEnfermedades(self):
		filaPaciente = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(filaPaciente[0],"text")
		ventanaSecundaria=VentanaSecundariaEnfermedades(self.raiz,codigo)
		ventanaSecundaria.configuracion()

	def añadirMedicos(self):
		filaPaciente = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(filaPaciente[0],"text")
		ventanaSecundaria=VentanaSecundariaAñadirMedico(self.raiz,codigo)
		ventanaSecundaria.configuracion()
	

class BotonesEnfermedades():
	"""docstring for Botones"""
	def __init__(self, raiz, formulario,tabla):
		self.frame=Frame(raiz,bg="#2d3d9b")
		self.raiz = raiz
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		self.formulario=formulario


		self.ingresoNombre,self.ingresoDesc= self.formulario.ingresoNombre, self.formulario.ingresoDesc
		self.tabla = tabla
		self.boton1=Button(self.frame2,text="Alta",command=self.altaEnfermedad,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarEnfermedad,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton3=Button(self.frame2,text="Limpiar",command=self.limpiar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton4=Button(self.frame2,text="Eliminar",command=self.eliminar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarEnfermedad,bg ="#d3d2d2",fg="#2d3d9b")


		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton3.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

		self.boton4.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
	
	
	def altaEnfermedad(self):
		
		
			
		if self.borrarVentana==True:
			self.tabla.contenido.delete(*self.tabla.contenido.get_children())
			self.borrarVentana=False
		sistemaHospitales_backend.operaciones.altaEnfermedad(self.ingresoNombre.get(), self.ingresoDesc.get())
		self.tabla.agregar_datos(self.ingresoNombre.get(), self.ingresoDesc.get())

	def buscarEnfermedad(self):

		
		
		self.borrarVentana=True
		nombre_enfermedad = self.nombreBuscado.get()
		nombre_enfermedad = str("'" + nombre_enfermedad + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_enfermedad(nombre_enfermedad)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		
		for dato in nombre_buscado:
		    #print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2]))
	def mostrarEnfermedad(self):
	
		self.borrarVentana=True
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_enfermedad()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2]))
	def limpiar(self):
		
	
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		self.formulario.ingresoNombre.set('')
		self.formulario.ingresoLocalidad.set('')
		self.formulario.ingresoProvincia.set('')
		self.formulario.ingresoCalle.set('')
		self.formulario.ingresoTelefono.set('')

	def eliminar(self):
		
		
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		print(codigo)
		self.tabla.contenido.delete(fila)
			     
		sistemaHospitales_backend.operaciones.elimina_enfermedad(codigo)

class BotonesEspecialidades():
	"""docstring for Botones"""
	def __init__(self, raiz, formulario,tabla):
		self.frame=Frame(raiz,bg="#2d3d9b")
		self.raiz = raiz
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		self.formulario=formulario


		self.ingresoNombre,self.ingresoDesc,self.ingresoDniMedico= self.formulario.ingresoNombre, self.formulario.ingresoDesc,self.formulario.ingresoDniMedico
		self.tabla = tabla
		self.boton1=Button(self.frame2,text="Alta",command=self.altaEspecialidad,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarEspecialidad,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton3=Button(self.frame2,text="Limpiar",command=self.limpiar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton4=Button(self.frame2,text="Eliminar",command=self.eliminar,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarEspecialidad,bg ="#d3d2d2",fg="#2d3d9b")


		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton3.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

		self.boton4.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
	
	
	def altaEspecialidad(self):
		
		
			
		if self.borrarVentana==True:
			self.tabla.contenido.delete(*self.tabla.contenido.get_children())
			self.borrarVentana=False
		sistemaHospitales_backend.operaciones.altaEspecialidad(self.ingresoNombre.get(), self.ingresoDesc.get(), self.ingresoDniMedico.get())
		self.tabla.agregar_datos(self.ingresoNombre.get(), self.ingresoDesc.get(), self.ingresoDniMedico.get())

	def buscarEspecialidad(self):

		
		
		self.borrarVentana=True
		nombre_especialidad = self.nombreBuscado.get()
		nombre_especialidad = str("'" + nombre_especialidad + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_especialidad(nombre_especialidad)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		
		for dato in nombre_buscado:
		    #print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3]))
	def mostrarEspecialidad(self):
	
		self.borrarVentana=True
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_especialidad()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3]))
	def limpiar(self):
		
	
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		self.formulario.ingresoNombre.set('')
		self.formulario.ingresoDesc.set('')
		self.formulario.ingresoDniMedico.set('')


	def eliminar(self):
		
		
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		print(codigo)
		self.tabla.contenido.delete(fila)
			     
		sistemaHospitales_backend.operaciones.elimina_especialidad(codigo)
class Tabla():
	"""docstring for Tabla"""
	def __init__(self,raiz):

	
		self.frame = Frame(raiz,bg="pink")

		self.contenido = ttk.Treeview(self.frame, height=21)

	def configuracionTabla(self):
		self.contenido.grid(column=0, row=0)
		ladox = Scrollbar(self.frame, orient = HORIZONTAL, command= self.contenido.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = Scrollbar(self.frame, orient =VERTICAL, command = self.contenido.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.contenido.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

		self.contenido['columns'] = ('Nombre', 'Localidad', 'Provincia', 'Calle', 'Telefono')

		self.contenido.column('#0', minwidth=100, width=120, anchor='center')
		self.contenido.column('Nombre', minwidth=100, width=130 , anchor='center')
		self.contenido.column('Localidad', minwidth=100, width=120, anchor='center' )
		self.contenido.column('Provincia', minwidth=100, width=120 , anchor='center')
		self.contenido.column('Calle', minwidth=100, width=105, anchor='center')
		self.contenido.column('Telefono', minwidth=100, width=105, anchor='center')

		self.contenido.heading('#0', text='Codigo', anchor ='center')
		self.contenido.heading('Nombre', text='Nombre', anchor ='center')
		self.contenido.heading('Localidad', text='Localidad', anchor ='center')
		self.contenido.heading('Provincia', text='Provincia', anchor ='center')
		self.contenido.heading('Calle', text='Calle', anchor ='center')
		self.contenido.heading('Telefono', text='Telefono', anchor ='center')

		self.contenido.bind("<<TreeviewSelect>>", self.obtener_fila) 
		self.frame.pack(side=RIGHT)
	def obtener_fila(self, event):
		current_item = self.contenido.focus()
		if not current_item:
			return
		data = self.contenido.item(current_item)
		self.nombre_borar = data['values'][0]
	def agregar_datos(self, ingresoNombre, ingresoLocalidad, ingresoProvincia, ingresoCalle, ingresoTelefono):
		self.contenido.get_children()
		ingresoNombre = ingresoNombre
		ingresoLocalidad = ingresoLocalidad
		ingresoProvincia = ingresoProvincia
		ingresoCalle = ingresoCalle
		ingresoTelefono = ingresoTelefono
		datos = (ingresoNombre, ingresoLocalidad, ingresoProvincia, ingresoCalle,ingresoTelefono)
		#if codigo and nombre and modelo and precio and cantidad !='':        
		self.contenido.insert('','end',values=datos)
		#self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)



class TablaMedicos():
	"""docstring for Tabla"""
	def __init__(self,raiz):

	
		self.frame = Frame(raiz,bg="pink")

		self.contenido = ttk.Treeview(self.frame, height=21)

	def configuracionTabla(self):
		self.contenido.grid(column=0, row=0)
		ladox = Scrollbar(self.frame, orient = HORIZONTAL, command= self.contenido.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = Scrollbar(self.frame, orient =VERTICAL, command = self.contenido.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.contenido.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

		self.contenido['columns'] = ( 'Nombre', 'Apellido', 'Genero', 'Nacimiento','Nacionalidad','Telefono','TelAlter','Email')

		self.contenido.column('#0', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nombre', minwidth=60, width=60, anchor='center' )
		self.contenido.column('Apellido', minwidth=60, width=60 , anchor='center')
		self.contenido.column('Genero', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacimiento', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacionalidad', minwidth=60, width=70, anchor='center')
		self.contenido.column('Telefono', minwidth=60, width=60, anchor='center')
		self.contenido.column('TelAlter', minwidth=60, width=60, anchor='center')
		self.contenido.column('Email', minwidth=60, width=60, anchor='center')

		self.contenido.heading('#0', text='Dni', anchor ='center')
		self.contenido.heading('Nombre', text='Nombre', anchor ='center')
		self.contenido.heading('Apellido', text='Apellido', anchor ='center')
		self.contenido.heading('Genero', text='Genero', anchor ='center')
		self.contenido.heading('Nacimiento', text='Nacimiento', anchor ='center')
		self.contenido.heading('Nacionalidad', text='Nacionalidad', anchor ='center')
		self.contenido.heading('Telefono', text='Telefono', anchor ='center')
		self.contenido.heading('TelAlter', text='TelAlter', anchor ='center')
		self.contenido.heading('Email', text='Email', anchor ='center')
		

		self.contenido.bind("<<TreeviewSelect>>", self.obtener_fila) 
		self.frame.pack(side=RIGHT)
	def obtener_fila(self, event):
		current_item = self.contenido.focus()
		if not current_item:
			return
		data = self.contenido.item(current_item)
		self.nombre_borar = data['values'][0]
	def agregar_datos(self, ingresoDni,ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail):
		self.contenido.get_children()
		ingresoDni = ingresoDni
		ingresoNombre = ingresoNombre
		ingresoApellido = ingresoApellido
		ingresoGenero = ingresoGenero
		ingresoFechaNac = ingresoFechaNac
		ingresoNacionalidad = ingresoNacionalidad
		ingresoTelefono = ingresoTelefono
		ingresoTelAlter = ingresoTelAlter
		ingresoEmail = ingresoEmail
		
		datos = (ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail)
		#if codigo and nombre and modelo and precio and cantidad !='':        
		self.contenido.insert('','end',text=ingresoDni,values=datos)
		#self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)

class TablaPaciente():
	"""docstring for Tabla"""
	def __init__(self,raiz):

	
		self.frame = Frame(raiz,bg="pink")

		self.contenido = ttk.Treeview(self.frame, height=21)

	def configuracionTabla(self):
		self.contenido.grid(column=0, row=0)
		ladox = Scrollbar(self.frame, orient = HORIZONTAL, command= self.contenido.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = Scrollbar(self.frame, orient =VERTICAL, command = self.contenido.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.contenido.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

		self.contenido['columns'] = ( 'Nombre', 'Apellido', 'Genero', 'Nacimiento','Nacionalidad','Telefono','TelAlter','Email')

		self.contenido.column('#0', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nombre', minwidth=60, width=60, anchor='center' )
		self.contenido.column('Apellido', minwidth=60, width=60 , anchor='center')
		self.contenido.column('Genero', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacimiento', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacionalidad', minwidth=60, width=70, anchor='center')
		self.contenido.column('Telefono', minwidth=60, width=60, anchor='center')
		self.contenido.column('TelAlter', minwidth=60, width=60, anchor='center')
		self.contenido.column('Email', minwidth=60, width=60, anchor='center')

		self.contenido.heading('#0', text='Dni', anchor ='center')
		self.contenido.heading('Nombre', text='Nombre', anchor ='center')
		self.contenido.heading('Apellido', text='Apellido', anchor ='center')
		self.contenido.heading('Genero', text='Genero', anchor ='center')
		self.contenido.heading('Nacimiento', text='Nacimiento', anchor ='center')
		self.contenido.heading('Nacionalidad', text='Nacionalidad', anchor ='center')
		self.contenido.heading('Telefono', text='Telefono', anchor ='center')
		self.contenido.heading('TelAlter', text='TelAlter', anchor ='center')
		self.contenido.heading('Email', text='Email', anchor ='center')


		self.contenido.bind("<<TreeviewSelect>>", self.obtener_fila) 
		self.frame.pack(side=RIGHT)
	def obtener_fila(self, event):
		current_item = self.contenido.focus()
		if not current_item:
			return
		data = self.contenido.item(current_item)
		self.nombre_borar = data['values'][0]
	def agregar_datos(self, ingresoDni,ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail):
		self.contenido.get_children()
		ingresoDni = ingresoDni
		ingresoNombre = ingresoNombre
		ingresoApellido = ingresoApellido
		ingresoGenero = ingresoGenero
		ingresoFechaNac = ingresoFechaNac
		ingresoNacionalidad = ingresoNacionalidad
		ingresoTelefono = ingresoTelefono
		ingresoTelAlter = ingresoTelAlter
		ingresoEmail = ingresoEmail
		
		datos = (ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail)
		#if codigo and nombre and modelo and precio and cantidad !='':        
		self.contenido.insert('','end',text=ingresoDni,values=datos)
		#self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)

		
class TablaEspecialidad():
	"""docstring for Tabla"""
	def __init__(self,raiz):

	
		self.frame = Frame(raiz,bg="pink")

		self.contenido = ttk.Treeview(self.frame, height=16)

	def configuracionTabla(self):
		self.contenido.grid(column=0, row=0)
		ladox = Scrollbar(self.frame, orient = HORIZONTAL, command= self.contenido.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = Scrollbar(self.frame, orient =VERTICAL, command = self.contenido.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.contenido.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

		self.contenido['columns'] = ( 'Nombre','DniMedico','Descripcion')

		self.contenido.column('#0', minwidth=100, width=100, anchor='center')
		self.contenido.column('Nombre', minwidth=100, width=100, anchor='center' )
		self.contenido.column('DniMedico', minwidth=100, width=100 , anchor='center')
		self.contenido.column('Descripcion', minwidth=100, width=100, anchor='center')
		
		self.contenido.heading('#0', text='Id', anchor ='center')
		self.contenido.heading('Nombre', text='Nombre', anchor ='center')
		self.contenido.heading('DniMedico', text='DniMedico', anchor ='center')
		self.contenido.heading('Descripcion', text='Descripcion', anchor ='center')



		self.contenido.bind("<<TreeviewSelect>>", self.obtener_fila) 
		self.frame.pack(side=RIGHT)
	def obtener_fila(self, event):
		current_item = self.contenido.focus()
		if not current_item:
			return
		data = self.contenido.item(current_item)
		self.nombre_borar = data['values'][0]
	def agregar_datos(self, ingresoNombre, ingresoDesc, ingresoDniMedico):
		self.contenido.get_children()
		ingresoNombre = ingresoNombre
		ingresoDesc = ingresoDesc
		ingresoDniMedico = ingresoDniMedico
		datos = (ingresoNombre, ingresoDesc, ingresoDniMedico)
		#if codigo and nombre and modelo and precio and cantidad !='':        
		self.contenido.insert('','end',values=datos)
		#self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)

class TablaEnfermedad():
	"""docstring for Tabla"""
	def __init__(self,raiz):

	
		self.frame = Frame(raiz,bg="pink")

		self.contenido = ttk.Treeview(self.frame, height=16)

	def configuracionTabla(self):
		self.contenido.grid(column=0, row=0)
		ladox = Scrollbar(self.frame, orient = HORIZONTAL, command= self.contenido.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = Scrollbar(self.frame, orient =VERTICAL, command = self.contenido.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.contenido.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

		self.contenido['columns'] = ( 'Nombre','Descripcion')

		self.contenido.column('#0', minwidth=100, width=100, anchor='center')
		self.contenido.column('Nombre', minwidth=100, width=100, anchor='center' )
		self.contenido.column('Descripcion', minwidth=100, width=200, anchor='center')
		
		self.contenido.heading('#0', text='Id', anchor ='center')
		self.contenido.heading('Nombre', text='Nombre', anchor ='center')
		self.contenido.heading('Descripcion', text='Descripcion', anchor ='center')



		self.contenido.bind("<<TreeviewSelect>>", self.obtener_fila) 
		self.frame.pack(side=RIGHT)
	def obtener_fila(self, event):
		current_item = self.contenido.focus()
		if not current_item:
			return
		data = self.contenido.item(current_item)
		self.nombre_borar = data['values'][0]
	def agregar_datos(self, ingresoNombre, ingresoDescripcion):
		self.contenido.get_children()
		ingresoNombre = ingresoNombre
		ingresoDescripcion = ingresoDescripcion
		datos = (ingresoNombre, ingresoDescripcion)
		#if codigo and nombre and modelo and precio and cantidad !='':        
		self.contenido.insert('','end',values=datos)
		#self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)

class TablaHospitales_medicos():

	def __init__(self,raiz):

	
		self.frame = Frame(raiz,bg="pink")

		self.contenido = ttk.Treeview(self.frame, height=21)

	def configuracionTabla(self):
		self.contenido.grid(column=0, row=0)
		ladox = Scrollbar(self.frame, orient = HORIZONTAL, command= self.contenido.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = Scrollbar(self.frame, orient =VERTICAL, command = self.contenido.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.contenido.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

		self.contenido['columns'] = ( 'Nombre', 'Apellido', 'Genero', 'Nacimiento','Nacionalidad','Telefono','TelAlter','Email','Id_hospital')

		self.contenido.column('#0', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nombre', minwidth=60, width=60, anchor='center' )
		self.contenido.column('Apellido', minwidth=60, width=60 , anchor='center')
		self.contenido.column('Genero', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacimiento', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacionalidad', minwidth=60, width=70, anchor='center')
		self.contenido.column('Telefono', minwidth=60, width=60, anchor='center')
		self.contenido.column('TelAlter', minwidth=60, width=60, anchor='center')
		self.contenido.column('Email', minwidth=60, width=60, anchor='center')
		self.contenido.column('Id_hospital', minwidth=60, width=60, anchor='center')

		self.contenido.heading('#0', text='Dni', anchor ='center')
		self.contenido.heading('Nombre', text='Nombre', anchor ='center')
		self.contenido.heading('Apellido', text='Apellido', anchor ='center')
		self.contenido.heading('Genero', text='Genero', anchor ='center')
		self.contenido.heading('Nacimiento', text='Nacimiento', anchor ='center')
		self.contenido.heading('Nacionalidad', text='Nacionalidad', anchor ='center')
		self.contenido.heading('Telefono', text='Telefono', anchor ='center')
		self.contenido.heading('TelAlter', text='TelAlter', anchor ='center')
		self.contenido.heading('Email', text='Email', anchor ='center')
		self.contenido.heading('Id_hospital', text='Id_hospital', anchor ='center')
		

		self.contenido.bind("<<TreeviewSelect>>", self.obtener_fila) 
		self.frame.pack(side=RIGHT)
	def obtener_fila(self, event):
		current_item = self.contenido.focus()
		if not current_item:
			return
		data = self.contenido.item(current_item)
		self.nombre_borar = data['values'][0]
	def agregar_datos(self, ingresoDni,ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail,id_hospital):
		self.contenido.get_children()
		ingresoDni = ingresoDni
		ingresoNombre = ingresoNombre
		ingresoApellido = ingresoApellido
		ingresoGenero = ingresoGenero
		ingresoFechaNac = ingresoFechaNac
		ingresoNacionalidad = ingresoNacionalidad
		ingresoTelefono = ingresoTelefono
		ingresoTelAlter = ingresoTelAlter
		ingresoEmail = ingresoEmail
		id_hospital = id_hospital
		
		datos = (ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail,id_hospital)
		#if codigo and nombre and modelo and precio and cantidad !='':        
		self.contenido.insert('','end',text=ingresoDni,values=datos)
		#self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)

class TablaHospitales_pacientes():

	def __init__(self,raiz):

	
		self.frame = Frame(raiz,bg="pink")

		self.contenido = ttk.Treeview(self.frame, height=21)

	def configuracionTabla(self):
		self.contenido.grid(column=0, row=0)
		ladox = Scrollbar(self.frame, orient = HORIZONTAL, command= self.contenido.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = Scrollbar(self.frame, orient =VERTICAL, command = self.contenido.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.contenido.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)

		self.contenido['columns'] = ( 'Nombre', 'Apellido', 'Genero', 'Nacimiento','Nacionalidad','Telefono','TelAlter','Email','Id_hospital')

		self.contenido.column('#0', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nombre', minwidth=60, width=60, anchor='center' )
		self.contenido.column('Apellido', minwidth=60, width=60 , anchor='center')
		self.contenido.column('Genero', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacimiento', minwidth=60, width=60, anchor='center')
		self.contenido.column('Nacionalidad', minwidth=60, width=70, anchor='center')
		self.contenido.column('Telefono', minwidth=60, width=60, anchor='center')
		self.contenido.column('TelAlter', minwidth=60, width=60, anchor='center')
		self.contenido.column('Email', minwidth=60, width=60, anchor='center')
		self.contenido.column('Id_hospital', minwidth=60, width=60, anchor='center')

		self.contenido.heading('#0', text='Dni', anchor ='center')
		self.contenido.heading('Nombre', text='Nombre', anchor ='center')
		self.contenido.heading('Apellido', text='Apellido', anchor ='center')
		self.contenido.heading('Genero', text='Genero', anchor ='center')
		self.contenido.heading('Nacimiento', text='Nacimiento', anchor ='center')
		self.contenido.heading('Nacionalidad', text='Nacionalidad', anchor ='center')
		self.contenido.heading('Telefono', text='Telefono', anchor ='center')
		self.contenido.heading('TelAlter', text='TelAlter', anchor ='center')
		self.contenido.heading('Email', text='Email', anchor ='center')
		self.contenido.heading('Id_hospital', text='Id_hospital', anchor ='center')
		

		self.contenido.bind("<<TreeviewSelect>>", self.obtener_fila) 
		self.frame.pack(side=RIGHT)
	def obtener_fila(self, event):
		current_item = self.contenido.focus()
		if not current_item:
			return
		data = self.contenido.item(current_item)
		self.nombre_borar = data['values'][0]
	def agregar_datos(self, ingresoDni,ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail,id_hospital):
		self.contenido.get_children()
		ingresoDni = ingresoDni
		ingresoNombre = ingresoNombre
		ingresoApellido = ingresoApellido
		ingresoGenero = ingresoGenero
		ingresoFechaNac = ingresoFechaNac
		ingresoNacionalidad = ingresoNacionalidad
		ingresoTelefono = ingresoTelefono
		ingresoTelAlter = ingresoTelAlter
		ingresoEmail = ingresoEmail
		id_hospital = id_hospital
		
		datos = (ingresoNombre, ingresoApellido, ingresoGenero, ingresoFechaNac, ingresoNacionalidad,ingresoTelefono,ingresoTelAlter,ingresoEmail,id_hospital)
		#if codigo and nombre and modelo and precio and cantidad !='':        
		self.contenido.insert('','end',text=ingresoDni,values=datos)
		#self.base_datos.inserta_producto(codigo, nombre, modelo, precio, cantidad)


class VentanaSecundariaEnfermedades():
	"""docstring for VentanaSecundariaEnfermedades"""
	def __init__(self, raiz,codigoPaciente):
		
		self.contenedor=Toplevel(raiz)
		self.tablaEnfermedad=TablaEnfermedad(self.contenedor)
		codigoPaciente=codigoPaciente

		self.botonesSecundarios=BotonesSecundarios(self.contenedor,self.tablaEnfermedad,codigoPaciente)
	def configuracion(self):
		
		self.contenedor.title("Añadir enfermedades")
		self.contenedor.focus()
		self.contenedor.grab_set()
		
		self.tablaEnfermedad.configuracionTabla()
		registro = sistemaHospitales_backend.operaciones.mostrar_enfermedad()
		self.botonesSecundarios.configuracionBotones()
		for dato in registro:                      
			self.tablaEnfermedad.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2]))

class BotonesSecundarios():
	"""docstring for BotonesSecundarios"""
	def __init__(self, contenedor,tabla,codigoPaciente):
		self.frame=Frame(contenedor,bg="#2d3d9b")
		self.contenedor = contenedor
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		
		self.codigoPaciente=codigoPaciente
		self.tabla = tabla
		self.boton1=Button(self.frame2,text="Añadir",command=self.añadirEnfermedad,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarEnfermedad,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarEnfermedad,bg ="#d3d2d2",fg="#2d3d9b")


		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
	def añadirEnfermedad(self):
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		sistemaHospitales_backend.operaciones.añadirEnfermedad(codigo,self.codigoPaciente)

	def buscarEnfermedad(self):
		nombre_enfermedad = self.nombreBuscado.get()
		nombre_enfermedad = str("'" + nombre_enfermedad + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_enfermedad(nombre_enfermedad)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())

		print(nombre_buscado)
		
		for dato in nombre_buscado:
		    print((dato[0],dato[1],dato[2]) )                  
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2]))
	def mostrarEnfermedad(self):
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_enfermedad()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2]))

class VentanaSecundariaHospitales():
	"""docstring for VentanaSecundariaHospitales"""
	def __init__(self, raiz,codigoHospital):
		
		self.contenedor=Toplevel(raiz)
		self.tablaHospital=Tabla(self.contenedor)
		codigoHospital=codigoHospital

		self.botonesSecundarios=BotonesSecundariosHospitales(self.contenedor,self.tablaHospital,codigoHospital)
	def configuracion(self):
		
		self.contenedor.title("Añadir hospitales")
		self.contenedor.focus()
		self.contenedor.grab_set()
		
		self.tablaHospital.configuracionTabla()
		registro = sistemaHospitales_backend.operaciones.mostrar_todo()
		self.botonesSecundarios.configuracionBotones()
		for dato in registro:                      
			self.tablaHospital.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2]))

class BotonesSecundariosHospitales():
	"""docstring for BotonesSecundarios"""
	def __init__(self, contenedor,tabla,codigoHospital):
		self.frame=Frame(contenedor,bg="#2d3d9b")
		self.contenedor = contenedor
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		
		self.codigoHospital=codigoHospital
		self.tabla = tabla
		self.boton1=Button(self.frame2,text="Añadir",command=self.añadirHospital,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarHospital,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarTodo,bg ="#d3d2d2",fg="#2d3d9b")



		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
	def añadirHospital(self):
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		sistemaHospitales_backend.operaciones.añadirHospital(codigo,self.codigoHospital)

	def buscarHospital(self):
			
		nombre_hospital = self.nombreBuscado.get()
		nombre_hospital = str("'" + nombre_hospital + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_hospital(nombre_hospital)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		
		for dato in nombre_buscado:
		    #print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3]))
	def mostrarTodo(self):
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_todo()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5]))	
		
class VentanaSecundariaMedicos():
	"""docstring for VentanaSecundariaHospitales"""
	def __init__(self, raiz,dniMedico):
		
		self.contenedor=Toplevel(raiz)
		self.tablaMedico=TablaMedicos(self.contenedor)
		dniMedico=dniMedico

		self.botonesSecundarios=BotonesSecundariosMedicos(self.contenedor,self.tablaMedico,dniMedico)
	def configuracion(self):
		
		self.contenedor.title("Añadir hospitales")
		self.contenedor.focus()
		self.contenedor.grab_set()
		
		self.tablaMedico.configuracionTabla()
		registro = sistemaHospitales_backend.operaciones.mostrar_medico()
		self.botonesSecundarios.configuracionBotones()
		for dato in registro:                      
			self.tablaMedico.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2]))

class BotonesSecundariosMedicos():
	"""docstring for BotonesSecundarios"""
	def __init__(self, contenedor,tabla,codigoHospital):
		self.frame=Frame(contenedor,bg="#2d3d9b")
		self.contenedor = contenedor
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		
		self.codigoHospital=codigoHospital
		self.tabla = tabla

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarMedico,bg ="#d3d2d2",fg="#2d3d9b")



		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)
		

	def configuracionBotones(self):

		

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()

	def buscarMedico(self):
			
		nombre_medico = self.nombreBuscado.get()
		nombre_medico = str("'" + nombre_medico + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_medico(nombre_medico)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		print(nombre_buscado)
		for dato in nombre_buscado:
		    print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))
	def mostrarMedico(self):
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_medico()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))

class VentanaSecundariaMedico_hospital():
	"""docstring for VentanaSecundariaHospitales"""
	def __init__(self, raiz,idHospital,nombre_hospital):
		
		self.contenedor=Toplevel(raiz)
		self.tablaMedico_hospital=TablaHospitales_medicos(self.contenedor)
		self.idHospital=idHospital
		self.nombre_hospital=nombre_hospital

		self.botonesSecundarios=BotonesSecundariosMedico_hospital(self.contenedor,self.tablaMedico_hospital,idHospital,self.nombre_hospital)
	def configuracion(self):
		
		self.contenedor.title(f"Consultar sobre hospital {self.nombre_hospital}")
		self.contenedor.focus()
		self.contenedor.grab_set()
		
		self.tablaMedico_hospital.configuracionTabla()
		registro = sistemaHospitales_backend.operaciones.busca_medico_hospital(self.idHospital)
		#print(registro)
		self.botonesSecundarios.configuracionBotones()
		for dato in registro:                      
			self.tablaMedico_hospital.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9]))

class BotonesSecundariosMedico_hospital():
	"""docstring for BotonesSecundarios"""
	def __init__(self, contenedor,tabla,codigoHospital,nombre_hospital):
		self.frame=Frame(contenedor,bg="#2d3d9b")
		self.contenedor = contenedor
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		
		self.codigoHospital=codigoHospital
		self.nombre_hospital=nombre_hospital
		self.tabla = tabla

		self.boton1=Button(self.frame2,text="Medicos",command=self.mostrarMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton3=Button(self.frame2,text="Pacientes",command=self.mostrarPaciente,bg ="#d3d2d2",fg="#2d3d9b")

		#self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarMedico,bg ="#d3d2d2",fg="#2d3d9b")



		self.titulo=Label(self.frame1, text=f"Consulta del hospital {self.nombre_hospital}",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)
		

	def configuracionBotones(self):

		

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
		self.boton3.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)



		#self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()

	def buscarMedico(self):
			
		nombre_medico = self.nombreBuscado.get()
		nombre_medico = str("'" + nombre_medico + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_medico_hospital_por_nombre(nombre_medico,self.codigoHospital)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		print(nombre_buscado)
		for dato in nombre_buscado:
		    #print((dato[0],dato[1],dato[2],dato[3],dato[4],dato[5]))                   
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9]))
	def mostrarMedico(self):
		#self.tabla.configuracionTabla()
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.busca_medico_hospital(self.codigoHospital)
		#print(registro)
		#self.botonesSecundarios.configuracionBotones()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9]))
	def mostrarPaciente(self):

		self.tabla.frame.destroy()

		self.tabla=TablaHospitales_pacientes(self.contenedor)
		self.tabla.configuracionTabla()

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.busca_paciente_hospital(self.codigoHospital)
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8],dato[9]))


class VentanaSecundariaAñadirMedico():
	"""docstring for VentanaSecundariaEnfermedades"""
	def __init__(self, raiz,codigoMedico):
		
		self.contenedor=Toplevel(raiz)
		self.tablaMedicos=TablaMedicos(self.contenedor)
		codigoMedico=codigoMedico

		self.botonesSecundarios=BotonesSecundariosAñadirMedico(self.contenedor,self.tablaMedicos,codigoMedico)
	def configuracion(self):
		
		self.contenedor.title("Añadir medicos")
		self.contenedor.focus()
		self.contenedor.grab_set()
		
		self.tablaMedicos.configuracionTabla()
		registro = sistemaHospitales_backend.operaciones.mostrar_medico()
		self.botonesSecundarios.configuracionBotones()
		for dato in registro:                      
			self.tablaMedicos.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7],dato[8]))

class BotonesSecundariosAñadirMedico():
	"""docstring for BotonesSecundarios"""
	def __init__(self, contenedor,tabla,codigoMedico):
		self.frame=Frame(contenedor,bg="#2d3d9b")
		self.contenedor = contenedor
		self.frame1=Frame(self.frame,bg="#d3d2d2")
		self.frame2=Frame(self.frame,bg="#2d3d9b")
		self.frame3=Frame(self.frame,bg="#2d3d9b")
		
		self.codigoMedico=codigoMedico
		self.tabla = tabla
		self.boton1=Button(self.frame2,text="Añadir",command=self.añadirMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton2=Button(self.frame3,text="Buscar por nombre",command=self.buscarMedico,bg ="#d3d2d2",fg="#2d3d9b")

		self.boton5=Button(self.frame3,text="Mostrar datos de MYSQL",command=self.mostrarMedico,bg ="#d3d2d2",fg="#2d3d9b")


		self.titulo=Label(self.frame1, text="Control",font=("Calibri",15),bg ="#2d3d9b",fg="#d3d2d2")

		self.nombreBuscado = StringVar()
		self.nombreBuscado = Entry(self.frame3)

		self.borrarVentana = False
		

	def configuracionBotones(self):

		self.boton1.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

		self.boton2.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

		self.boton5.grid(row=3, column=0, columnspan=2 , sticky="n", padx=10, pady=10)

		self.nombreBuscado.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)

		self.titulo.pack()

		self.frame.pack(fill=BOTH)
		self.frame1.pack()
		self.frame2.pack()
		self.frame3.pack()
	def añadirMedico(self):
		fila = self.tabla.contenido.selection()
		codigo= self.tabla.contenido.item(fila[0],"text")
		sistemaHospitales_backend.operaciones.añadirMedico(self.codigoMedico,codigo)

	def buscarMedico(self):
		nombre_medico = self.nombreBuscado.get()
		nombre_medico = str("'" + nombre_medico + "'")
		nombre_buscado = sistemaHospitales_backend.operaciones.busca_medico(nombre_medico)

		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		
		for dato in nombre_buscado:
		    #print((dato[0],dato[1],dato[2]) )                  
		    self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7]))
	def mostrarMedico(self):
		self.tabla.contenido.delete(*self.tabla.contenido.get_children())
		registro = sistemaHospitales_backend.operaciones.mostrar_medico()
		for dato in registro:                      
			self.tabla.contenido.insert('',"end", text=dato[0] , values=(dato[1],dato[2],dato[3],dato[4],dato[5],dato[6],dato[7]))
