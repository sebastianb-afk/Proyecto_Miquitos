import dash
from dash import html
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import monosSQL as sql

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

con = Connection()
con.openConnection()
query1 = pd.read_sql_query(sql.NumberCasesPerDepartment(), con.connection)
query2 = pd.read_sql_query(sql.NumberCasesPerClass(), con.connection)
query3 = pd.read_sql_query(sql.RateCasesByGenre(), con.connection)
query4 = pd.read_sql_query(sql.AvgTimeOfDisease(), con.connection)
con.CloseConnection()

#Casos por departamento
dfCases1 = pd.DataFrame(query1, columns=["departamento", "numero_casos"])
figBarCases = px.bar(dfCases1.head(20), x = "departamento", y = "numero_casos", title = 'NÚMERO DE INFECCIÓN POR DEPARTAMENTO-BARRAS')
figPieCases = px.pie(dfCases1.head(20), values = "numero_casos", names = "departamento", title = 'NÚMERO DE INFECCIÓN POR DEPARTAMENTO-PIE')


#Casos por estrato
dfCases2 = pd.DataFrame(query2, columns = ["estrato", "numero_casos"])
figPieCasesClass = px.pie(dfCases2.head(20), values = "numero_casos", names = "estrato", title = 'NÚMERO DE INFECCIÓN POR ESTRATO-PIE')

#Numero de casos por genero
dfCases3 = pd.DataFrame(query3, columns = ["sexo","numero_casos"])
figBarCasesGenre = px.bar(dfCases3.head(20), x = "sexo", y = "numero_casos", title = 'TASA DE CONTAGIO SEGÚN GÉNERO-BARRAS')
figPieCasesGenre = px.pie(dfCases3.head(20), values = "numero_casos", names = "sexo", title = 'TASA DE CONTAGIO SEGÚN GÉNERO-PIE')

#Media de duracion segun edad
dfCases4 = pd.DataFrame(query4, columns = ["edad","promedio_duracion"])
figBarCasesTime = px.bar(dfCases4.head(20), x = "edad", y = "promedio_duracion", title = 'MEDIA DE DURACIÓN DE LA ENFERMEDAD-BARRAS')
figPieCasesTime = px.pie(dfCases4.head(20), values = "promedio_duracion", names = "edad", title = 'MEDIA DE DURACIÓN DE LA ENFERMEDAD-PIE')


app.layout= html.Div(children = [
    html.H1(children = ' miquitos Dashboard'),
    html.H2(children = ' miquitos Dashboard'),
    dcc.Graph(
        id = 'barCasesByDepartment',
        figure = figBarCases
        ),
    dcc.Graph(
        id = 'pieCasesByDepartment',
        figure = figPieCases
        ),
    dcc.Graph(
        id = 'pieCasesByClass',
        figure = figPieCasesClass
        ),
    dcc.Graph(
        id = 'barCasesByGenre',
        figure = figBarCasesGenre
        ),
    dcc.Graph(
        id = 'pieCasesByGenre',
        figure = figPieCasesGenre
        ),
    dcc.Graph(
        id = 'barCasesByTime',
        figure = figBarCasesTime
        ),
    dcc.Graph(
        id = 'pieCasesByTime',
        figure = figPieCasesTime
        ),
    ])

if __name__ == '__main__':
    app.run_server(debug = True)
