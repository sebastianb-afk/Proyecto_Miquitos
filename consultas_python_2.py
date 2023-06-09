import psycopg2 

"""Conectarse con la base de datos, los datos de database, user, 
password y port cambian dependiendo del dispositivo en el que se guarde y 
como se guarde la base de datos."""
conexion = psycopg2.connect(database = "miquitos", user="postgres", password = "1", port=5433)
cursor = conexion.cursor()
print("conexion exitosa")


#Sentencias SQL
sql_paciente = "SELECT * FROM paciente"
sql_sexo = "SELECT * FROM sexo"
sql_seguridad_social = "SELECT * FROM seguridad_social"
sql_municipio = "SELECT * FROM municipio"
sql_departamento = "SELECT * FROM departamento"
sql_diagnosis = "SELECT * FROM diagnosis"
sql_fuente_infeccion = "SELECT * FROM fuente_infeccion"

########PACIENTE#################
cursor.execute(sql_paciente)
paciente = cursor.fetchall()
print("******PACIENTE******")
for pac in paciente:
    print("id: ", pac[0])
    print("edad: ", pac[1])
    print("viajo: ", pac[2])
    print("pais viaje: ", pac[3])
    print("pertenencia etnica: ", pac[4])
    print("estrato: ", pac[5])
    print("id seguridad social: ", pac[6])
    print("id_sexo: ", pac[7])
    print("codigo municipio: ", pac[8], "\n")

#######SEXO#############
cursor.execute(sql_sexo)
sexo = cursor.fetchall()
print("******SEXO******")
for sex in sexo:
    print("id:", sex[0])
    print("genero:", sex[1], "\n")

#####SEGURIDAD SOCIAL######
cursor.execute(sql_seguridad_social)
seguridad = cursor.fetchall()
print("******SEGURIDAD SOCIAL*******")
for seg in seguridad:
    print("tipo seguridad social: ", seg[0])
    print("id: ", seg[1], "\n")
    
####MUNICIPIO#############
cursor.execute(sql_municipio)
municipio = cursor.fetchall()
print("******MUNICIPIO******")
for mun in municipio:
    print("codigo municipio: ", mun[0])
    print("codigo departamento: ", mun[1])
    print("nombre municipio: ", mun[2], "\n")
    
#######DEPARTAMENTO###########
cursor.execute(sql_departamento)
departamento = cursor.fetchall()
print("******DEPARTAMENTO******")
for dep in departamento:
    print("codigo municipio: ", dep[0])
    print("codigo departamento: ", dep[1], "\n")
    
#######FUENTE INFECCION########
cursor.execute(sql_fuente_infeccion)
fuente_inf = cursor.fetchall()
print("******FUENTE INFECCION******")
for fun in fuente_inf:
    print("id: ", fun[0])
    print("fuente infeccion: ", fun[1], "\n")
    
#######DIAGNOSIS############
cursor.execute(sql_diagnosis)
diagnosis = cursor.fetchall()
print("******DIAGNOSIS******")
for diag in diagnosis:
    print("id paciente: ", diag[0])
    print("semana epidemiologica: ", diag[1])
    print("anio epidemiologico: ", diag[2])
    print("fecha notificacion: ", diag[3])
    print("fecha diagnosis: ", diag[4])
    print("fecha sintomas: ", diag[5])
    print("fecha exantema: ", diag[6])
    print("hospitalizacion: ", diag[7])
    print("condicion final: ", diag[8])
    print("fecha terminacion seguimiento: ", diag[9])
    print("id fuente infeccion: ", diag[10], "\n")
    
cursor.close()
conexion.close()