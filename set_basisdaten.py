import setting
from flask import Flask
from flask import request
#import os, webbrowser, time
from flask import render_template
import setting


def basisdaten(var_beraternummer):
    fileziel=open("daten/basisdaten.txt","w")
    # schreiben in Datei für Basisdaten
    fileziel.write(request.form['form_berater']+"|"+request.form['form_mandant']+"|")
    if (request.form['loa_ns1'] != "" and request.form['loa_ts1'] != "") and (request.form['loa_ns1'] != "Nummer") :
        fileziel.write(request.form['loa_ns1']+"|"+request.form['loa_ts1']+"|")
    else:
        fileziel.write("Nummer|Lohnartenbezeichnung|")
    if (request.form['loa_nb1'] != "" and request.form['loa_tb1'] != "") and (request.form['loa_nb1'] != "Nummer"):
        fileziel.write(request.form['loa_nb1']+"|"+request.form['loa_tb1']+"|")
    else:
        fileziel.write("Nummer|Lohnartenbezeichnung|")
    fileziel.close()

def basislesen():
    filequelle=open("daten/basisdaten.txt","r")
    for x in filequelle:
        var_beraternummer,var_mandantenummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    filequelle.close()
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    return(var_beraternummer, var_mandantenummer, var_version_program, var_version_titel, var_3, var_4, var_5, var_6, var_99)

def basisleer():
    var_beraternummer = "999999"
    var_mandantenummer = "99999"
    var_3 = "Nummer"
    var_4 = "Nummer"
    var_5 = "Lohnartbezeichnung"
    var_6 = "Lohnartbezeichnung"
    var_99 = "Dummy"

    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    return(var_beraternummer, var_mandantenummer)
