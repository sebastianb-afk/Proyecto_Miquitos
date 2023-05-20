def NumberCasesPerDepartment():
    return """SELECT d.nombre_departamento as departamento, count(p.id) as numero_casos
              FROM departamento d inner join municipio m on (d.codigo_departamento = m.codigo_departamento_departamento)
					inner join paciente p on (p.codigo_municipio_municipio = m.codigo_municipio)
              GROUP BY departamento
              ORDER BY numero_casos DESC
            """

def NumberCasesPerClass():
    return """SELECT estrato, count(id) as numero_casos
              FROM paciente
              GROUP BY estrato
              ORDER BY numero_casos DESC;
           """

def RateCasesByGenre():
    return """SELECT s.sexo, count(p.id) as numero_casos
              FROM sexo s inner join paciente p on (s.id = p.id_sexo)
              GROUP BY sexo
              ORDER BY numero_casos DESC;
           """

def AvgTimeOfDisease():
    return """SELECT p.edad as edad, avg(d.fecha_terminacion_seguimiento - d.fecha_exantema) as promedio_duracion
              FROM paciente p inner join  diagnosis d on (p.id = d.id_paciente)
              GROUP BY edad
              ORDER BY promedio_duracion DESC;
           """
