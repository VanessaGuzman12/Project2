
from application import app
from flask import render_template, g, url_for
import pandas as pd
import json
import plotly 
import plotly.express as px
import sqlite3
import pandas as pd


@app.route("/")
def index():
    #Barchart disease
    database = "C:/Users/vanem/Homeworks/Project2/Project2/mortality.sqlite"
    cnx = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * FROM mortality_causes", cnx)
    graph1_df=df.groupby(["death_cause_eng"]).count().sort_values(["date_regis"],ascending=False)
    graph1_df.reset_index(inplace=True)
    fig1 = px.bar(graph1_df, x="death_cause_eng", y=['date_regis'], title = "Deaths by cause in Mexico")
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)


    #Barchart gender
    graph2_df=df.groupby(["gender"]).count().sort_values(["date_regis"],ascending=False)
    graph2_df.reset_index(inplace=True)
    fig2 = px.bar(graph2_df, x="gender", y=['date_regis'], title = "Deaths by gender in Mexico", color="gender")
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)


    #histogram age
    fig3 = px.histogram(df, x="death_age", nbins= 20,color="gender", title = "Deaths by age in Mexico")
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    #histogram Covid19
    graph4_df=df.drop(df[df.death_cause_eng!="Covid-19"].index)
    fig4 = px.histogram(graph4_df, x="death_age", nbins= 20,color="gender", title = "Deaths by Covid-19 by age in Mexico")
    graph4JSON = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)


    #histogram External causes
    graph5_df=df.drop(df[df.death_cause_eng!="External causes"].index)
    fig5 = px.histogram(graph5_df, x="death_age", nbins= 20,color="gender", title = "Deaths by External Causes by age in Mexico")
    graph5JSON = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)


    return render_template("index.html", title ="Home", graph1JSON = graph1JSON, graph2JSON = graph2JSON, graph3JSON = graph3JSON, graph4JSON = graph4JSON, graph5JSON = graph5JSON)

