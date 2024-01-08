from tkinter import*
import tkinter.messagebox
import sistemaHospitales_frontend.elementosVentana
import sistemaHospitales_backend.operaciones
class Pantalla():
	"""docstring for ClassName"""
	def __init__(self):
		# 1. Ventana o raiz
		
		self.raiz=Tk()
		
		self.menu= sistemaHospitales_frontend.elementosVentana.BarraMenu(self.raiz)
		self.titulo1= sistemaHospitales_frontend.elementosVentana.Titulo1(self.raiz)
		self.tabla=sistemaHospitales_frontend.elementosVentana.Tabla(self.raiz)
		
		self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)
		
		self.formulario= sistemaHospitales_frontend.elementosVentana.FormularioHospital(self.raiz)		
		
		self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesABM(self.raiz,self.formulario,self.tabla)
	def configuracion(self):

		self.raiz.title("Registro de hospitales")

		self.menu.configuracionMenu()


		self.titulo1.configuracionTitulo()

		self.tabla.configuracionTabla()
		
		self.botones.configuracionBotones()
		
		self.formulario.configuracionFormulario()

		


		self.botonesABM.configuracionBotones()


		
		
		self.raiz.config(menu=self.menu.barraMenu)

	def pantallaHospital(self):
		try:
			self.formulario.frame.destroy()
			#self.botonesABM.frame.destroy()
			self.tabla.frame.destroy()
			self.botones.frame.destroy()
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)




			self.botonesABM.frame.destroy()		

			self.botonesMedicos.frame.destroy()
			self.formulario= sistemaHospitales_frontend.elementosVentana.FormularioHospital(self.raiz)		
			self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesABM(self.raiz,self.formulario,self.tabla)

			self.tabla=sistemaHospitales_frontend.elementosVentana.Tabla(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.formulario.configuracionFormulario()
			self.botonesABM.configuracionBotones()
		except:
			self.formulario.frame.destroy()
			self.botones.frame.destroy()
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)
			self.formulario= sistemaHospitales_frontend.elementosVentana.FormularioHospital(self.raiz)
			self.botonesABM.frame.destroy()	
			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.Tabla(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesABM(self.raiz,self.formulario,self.tabla)
			self.formulario.configuracionFormulario()
			
			self.botonesABM.configuracionBotones()
	def pantallaMedico(self):
		#self.formulario.frame.destroy()
		try:
			self.formulario.frame.destroy()
			self.botonesABM.frame.destroy()
			self.botonesMedicos.frame.destroy()
			self.botones.frame.destroy()
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaMedicos(self.raiz)
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioMedico(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.formulario.configuracionFormulario()
			self.formulario.configuracionFormularioMedico()

			self.botonesMedicos= sistemaHospitales_frontend.elementosVentana.BotonesMedicos(self.raiz,self.formulario,self.tabla)
			self.botonesMedicos.configuracionBotones()
		except:

			self.formulario.frame.destroy()
			self.formulario= sistemaHospitales_frontend.elementosVentana.FormularioMedico(self.raiz)
			self.botonesABM.frame.destroy()	
			self.botones.frame.destroy()	
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaMedicos(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesMedicos(self.raiz,self.formulario,self.tabla)
			self.formulario.configuracionFormulario()
			self.formulario.configuracionFormularioMedico()
			self.botonesABM.configuracionBotones()
	def pantallaPaciente(self):
		#self.formulario.frame.destroy()
		try:
			self.formulario.frame.destroy()
			self.botonesABM.frame.destroy()
			self.botonesMedicos.frame.destroy()
			self.botones.frame.destroy()
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz,self.formulario,self.tabla)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaPaciente(self.raiz)
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioPaciente(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.formulario.configuracionFormulario()
			self.formulario.configuracionFormularioPaciente()

			self.botonesPacientes= sistemaHospitales_frontend.elementosVentana.BotonesPacientes(self.raiz,self.formulario,self.tabla)
			self.botonesPacientes.configuracionBotones()
		except:

			self.formulario.frame.destroy()
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioPaciente(self.raiz)
			self.botonesABM.frame.destroy()	
			self.botones.frame.destroy()	
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaPaciente(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesPacientes(self.raiz,self.formulario,self.tabla)
			self.formulario.configuracionFormulario()
			self.formulario.configuracionFormularioPaciente()
			self.botonesABM.configuracionBotones()
		
	def pantallaEspecialidad(self):
		#self.formulario.frame.destroy()
		try:
			self.formulario.frame.destroy()
			self.botonesABM.frame.destroy()
			self.botonesMedicos.frame.destroy()
			self.botones.frame.destroy()
			self.botones= sistemaHospitales_frontend.elementosVentana.BotonesEspecialidades(self.raiz,self.formulario,self.tabla)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaEspecialidad(self.raiz)
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioEspecialidad(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.formulario.configuracionFormulario()
			
		except:

			self.formulario.frame.destroy()
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioEspecialidad(self.raiz)
			self.botonesABM.frame.destroy()	
			self.botones.frame.destroy()	
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaEspecialidad(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesEspecialidades(self.raiz,self.formulario,self.tabla)
			self.formulario.configuracionFormulario()

			self.botonesABM.configuracionBotones()

	def pantallaEnfermedad(self):
		#self.formulario.frame.destroy()
		try:
			self.formulario.frame.destroy()
			self.botonesABM.frame.destroy()
			self.botonesMedicos.frame.destroy()
			self.botones.frame.destroy()
			self.botones= sistemaHospitales_frontend.elementosVentana.BotonesPacientes(self.raiz, self.formulario, self.tabla)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaEnfermedad(self.raiz)
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioEnfermedad(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.formulario.configuracionFormulario()
			self.botonesMedicos= sistemaHospitales_frontend.elementosVentana.BotonesEnfermedades(self.raiz,self.formulario,self.tabla)
			self.botonesMedicos.configuracionBotones()
		except:

			self.formulario.frame.destroy()
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioEnfermedad(self.raiz)
			self.botonesABM.frame.destroy()	
			self.botones.frame.destroy()	
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaEnfermedad(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesEnfermedades(self.raiz,self.formulario,self.tabla)
			self.formulario.configuracionFormulario()
			self.botonesABM.configuracionBotones()

	def pantallaPersonal(self):
		#self.formulario.frame.destroy()
		try:
			self.formulario.frame.destroy()
			self.botonesABM.frame.destroy()
			self.botonesMedicos.frame.destroy()
			self.botones.frame.destroy()
			self.botones= sistemaHospitales_frontend.elementosVentana.BotonesPacientes(self.raiz,self.formulario,self.tabla)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaMedicos(self.raiz)
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioPaciente(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.formulario.configuracionFormulario()
			self.formulario.configuracionFormularioPaciente()

			self.botonesMedicos= sistemaHospitales_frontend.elementosVentana.BotonesMedicos(self.raiz,self.formulario,self.tabla)
			self.botonesMedicos.configuracionBotones()
		except:

			self.formulario.frame.destroy()
			self.formulario=sistemaHospitales_frontend.elementosVentana.FormularioPaciente(self.raiz)
			self.botonesABM.frame.destroy()	
			self.botones.frame.destroy()	
			self.botones= sistemaHospitales_frontend.elementosVentana.Botones(self.raiz, self.pantallaHospital, self.pantallaMedico, self.pantallaPaciente, self.pantallaEspecialidad, self.pantallaEnfermedad, self.pantallaPersonal)

			self.tabla.frame.destroy()
			self.tabla=sistemaHospitales_frontend.elementosVentana.TablaMedicos(self.raiz)
			self.tabla.configuracionTabla()
			self.botones.configuracionBotones()
			self.botonesABM= sistemaHospitales_frontend.elementosVentana.BotonesMedicos(self.raiz,self.formulario,self.tabla)
			self.formulario.configuracionFormulario()
			self.formulario.configuracionFormularioPaciente()
			self.botonesABM.configuracionBotones()
	def salir():
	    salir=tkinter.messagebox.askquestion("Desea salir ?","¿Desea salir de la aplicación?")
	    if salir=="yes":
	        raiz.destroy()

	    return

	def ejecutar(self):
		self.configuracion()
		self.raiz.mainloop()


	#def ejecutar(self):
		
		# def conectar():
		#     conexion=sqlite3.connect("BD_hospital")
		#     cursor=conexion.cursor()

		#     try:
		#         cursor.execute('''
		#             CREATE TABLE Hospital (
		#             Nombre VARCHAR(50) PRIMARY KEY, 
		#             Localidad VARCHAR(50), 
		#             Provincia VARCHAR(50), 
		#             Calle VARCHAR(50), 
		#             Telefono VARCHAR (50))
		#             ''')
		#         conexion.commit()
		#         conexion.close()
		#         tkinter.messagebox.showinfo("Info","Tabla Hospital creada")

		#     except:
		#         tkinter.messagebox.showerror("Error","Ya se ha creado antes la tabla Hospital")


		# def salir():
		#     salir=tkinter.messagebox.askquestion("Desea salir ?","¿Desea salir de la aplicación?")
		#     if salir=="yes":
		#         raiz.destroy()

    	# 	return