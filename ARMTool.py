from flask import Flask
from flask import request
import os, webbrowser, time, csv, requests
from flask import render_template
import setting, set_basisdaten, exportmodul, importmodul
import personen, funktionen, datenbank_obj
import numpy as np


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, MetaData, Table, DATE
from sqlalchemy.sql import select 

app = Flask(__name__)


@app.route('/export_steuer.html', methods=['GET', 'POST']) # noch offen 2021-12-21
def abrechnungsdaten_exportierensteuer():
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()

    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()
    
    var_text = exportmodul.export_steuer(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)
    
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db') 
    message = engine.execute("SELECT abrechnungsdaten.id, abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger, abrechnungsdaten.artdertaetigkeit FROM abrechnungsdaten WHERE ((abrechnungsdaten.lohnart>6600 AND abrechnungsdaten.lohnart<6700) AND abrechnungsdaten.exportlodas==\"N\") ORDER BY abrechnungsdaten.PNR")
    
    return render_template('/export_steuer.html', v_text=var_text, v_bnr=var_beraternummer, tabelle=message, v_mdt=var_mandantennummer, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)

@app.route('/export_steuerliste.html', methods=['GET', 'POST']) # noch offen 2021-12-21
def abrechnungsdaten_exportierensteuerliste():
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()

    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()
    
    var_text, var_stmonat, var_stjahr = exportmodul.export_steuerliste(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)
    
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db') 
    message = engine.execute("SELECT abrechnungsdaten.id, abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger, abrechnungsdaten.artdertaetigkeit FROM abrechnungsdaten WHERE ((abrechnungsdaten.lohnart>6600 AND abrechnungsdaten.lohnart<6700) AND (abrechnungsdaten.exportlodas==\"J\" OR abrechnungsdaten.exportlohnundgehalt==\"J\") ) ORDER BY abrechnungsdaten.PNR")
    return render_template('/export_steuerliste.html', v_stmonat=var_stmonat, v_stjahr=var_stjahr, v_text=var_text, v_bnr=var_beraternummer, tabelle=message, v_mdt=var_mandantennummer, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)


@app.route('/') 
def index():
    var_kalendertag=os.path.join(time.strftime('%d.%m.%Y'))

    # Anlage SQL DB - falls nicht vorhanden
    if os.path.exists("daten/abrechnungsdaten.db"):
        pass
    else:
        engine = create_engine('sqlite:///daten/abrechnungsdaten.db')
        metadata = datenbank_obj.getdbmetadata(engine)
        abrechnungsdaten = datenbank_obj.abrechnungsdaten_dbobj(metadata)
        metadata.create_all()

    ## wenn Grunddateien nicht vorhanden, dann werden diese hier geprüft und mit Dummydaten angelegt
    if os.path.exists("daten/basisdaten.txt"):
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6 = funktionen.basis_daten_oeffnen()
    else:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6 = funktionen.basis_daten_anlegen()


    if os.path.exists("daten/abrechnungszeitraum.txt"):
        var_abrmonat, var_abrjahr = funktionen.abrechnungs_daten_lesen()
    else:
        fileziel=open("daten/abrechnungszeitraum.txt","w")
        var_abrmonat="99"
        var_abrjahr="9999"
        fileziel.write(var_abrmonat+"|"+var_abrjahr)
        fileziel.close()

    if os.path.exists("daten/PNR_Datei.txt"):
        pass
    else:
        fileziel=open("daten/PNR_Datei.txt","w", encoding='utf-8')
        fileziel.write("Arbeitnehmer importieren")
        fileziel.close()

    if os.path.exists("daten/Agentur_Datei.txt"):
        pass
    else:
        fileziel=open("daten/Agentur_Datei.txt","w", encoding='utf-8')
        fileziel.write("Agenturnummer Bezeichnung\n")
        fileziel.close()
    ### Ende Prüfung und Anlage

    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program
    
    if var_abrjahr == "9999":
        var_text = "Bitte Grundstammdaten einstellen!"
    else:
        var_text = "Alles ok"

    return render_template('index.html', v_text=var_text, v_bnr=var_beraternummer, v_mdt=var_mandantennummer, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_heute=var_kalendertag, v_version_program=var_version_program, v_version_titel=var_version_titel)

@app.route('/import_lodas.html', methods=['GET', 'POST']) 
def abrechnungsdaten_importlodas():
    
    var_kalendertag=os.path.join(time.strftime('%d.%m.%Y'))
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()
   
    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()
    
    var_text = importmodul.lodasimport(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)
    
    return render_template('/index.html', v_text=var_text, v_bnr=var_beraternummer, v_mdt=var_mandantennummer, v_heute=var_kalendertag, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)


@app.route('/import_lug.html', methods=['GET', 'POST']) 
def abrechnungsdaten_importlug():
    var_kalendertag=os.path.join(time.strftime('%d.%m.%Y'))
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()

    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()

    var_text = importmodul.lugimport(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)

    return render_template('/index.html', v_text=var_text, v_bnr=var_beraternummer, v_mdt=var_mandantennummer, v_heute=var_kalendertag, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)

@app.route('/abrechnungsdaten.html', methods=['GET', 'POST'])
def abrechnungsdaten_erfassen():
            
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program
   
    PNR_Liste = open("daten/PNR_Datei.txt","r", encoding='utf-8')
    PNR_dropdown_list = PNR_Liste
    PNR_Liste.close

    AGNR_Liste = open("daten/Agentur_Datei.txt","r", encoding='utf-8')
    AGNR_dropdown_list = AGNR_Liste
    AGNR_Liste.close

    var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6 = funktionen.basis_daten_oeffnen()
    var_abrmonat, var_abrjahr = funktionen.abrechnungs_daten_lesen()

    personen.abrechnung_erf(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)

    return render_template('/abrechnungsdaten.html', v_bnr=var_beraternummer, v_mdt=var_mandantennummer, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel, PNR_dropdown_list=PNR_dropdown_list, AGNR_dropdown_list=AGNR_dropdown_list)

@app.route('/uebersicht.html')
def uebersicht():
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()

    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()

    engine = create_engine('sqlite:///daten/abrechnungsdaten.db') 
    message = engine.execute("SELECT abrechnungsdaten.id, abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger, abrechnungsdaten.artdertaetigkeit FROM abrechnungsdaten WHERE ((abrechnungsdaten.lohnart>6600 AND abrechnungsdaten.lohnart<9999) AND (abrechnungsdaten.exportlodas==\"N\" OR abrechnungsdaten.exportlohnundgehalt==\"N\")) ORDER BY abrechnungsdaten.PNR")


    return render_template('/uebersicht.html', v_bnr=var_beraternummer, v_mdt=var_mandantennummer, tabelle=message, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)

@app.route('/abr_del.html', methods=['GET', 'POST'])
def abrechnungsdaten_del():
    personen.abrechnungsdaten_del()
    
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    engine = create_engine('sqlite:///daten/abrechnungsdaten.db') 
    message = engine.execute("SELECT abrechnungsdaten.id, abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger, abrechnungsdaten.artdertaetigkeit FROM abrechnungsdaten WHERE ((abrechnungsdaten.lohnart>6600 AND abrechnungsdaten.lohnart<9999) AND (abrechnungsdaten.exportlodas==\"N\" OR abrechnungsdaten.exportlohnundgehalt==\"N\")) ORDER BY abrechnungsdaten.PNR")

    return render_template('/abr_del.html', v_version_program=var_version_program, v_version_titel=var_version_titel, tabelle=message)



@app.route('/export_lodas.html', methods=['GET', 'POST']) # noch offen 2021-12-21
def abrechnungsdaten_exportierenlodas():
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()

    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()
    
    var_text = exportmodul.export_lodas(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)
    
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db') 
    message = engine.execute("SELECT abrechnungsdaten.id, abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger, abrechnungsdaten.artdertaetigkeit FROM abrechnungsdaten WHERE ((abrechnungsdaten.lohnart>6600 AND abrechnungsdaten.lohnart<9999) AND abrechnungsdaten.exportlodas==\"N\") ORDER BY abrechnungsdaten.PNR")

    return render_template('/export_lodas.html', v_text=var_text, v_bnr=var_beraternummer, tabelle=message, v_mdt=var_mandantennummer, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)

@app.route('/export_lug.html', methods=['GET', 'POST'])
def abrechnungsdaten_exportierenlug():

    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()

    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()
    
    var_text = exportmodul.export_lohnundgehalt(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)
    
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db') 
    message = engine.execute("SELECT abrechnungsdaten.id, abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger, abrechnungsdaten.artdertaetigkeit FROM abrechnungsdaten WHERE ((abrechnungsdaten.lohnart>6600 AND abrechnungsdaten.lohnart<9999) AND abrechnungsdaten.exportlohnundgehalt==\"N\") ORDER BY abrechnungsdaten.PNR")
    return render_template('/export_lug.html', v_text=var_text, v_bnr=var_beraternummer, tabelle=message, v_mdt=var_mandantennummer, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)
    
    ##### Export komplett nach csv
@app.route('/export_csv.html')
def export_csv():
    var_kalendertag=os.path.join(time.strftime('%d.%m.%Y'))
    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()

    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()

    var_text = exportmodul.export_csv(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer)

    return render_template('/index.html', v_text=var_text, v_bnr=var_beraternummer, v_mdt=var_mandantennummer, v_heute=var_kalendertag, v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)




####### Ergänzung erforderlich 
# Basisdaten stimmen nicht, durch Anlage eines dict sind es zu viele Stellen
# macht aber keinen Fehler aktuell
#############################################################################
@app.route('/basisdaten.html', methods=['POST', 'GET'])
def basisdaten():
##############################################################
### Anlage der Stammdaten (Konfiguration) für die Erfassung
### Beraternummer, Mandant und Lohnarten mit Text
##############################################################
    if os.path.exists("daten/abrechnungszeitraum.txt"):
        filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
        for x in filequelle:
            var_abrmonat,var_abrjahr=x.split("|")
            break
        filequelle.close()
    else:
        fileziel=open("daten/abrechnungszeitraum.txt","w")
        var_abrmonat="99"
        var_abrjahr="9999"
        fileziel.write(var_abrmonat+"|"+var_abrjahr)
        fileziel.close()
    

    if os.path.exists("daten/basisdaten.txt"):
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6 = funktionen.basis_daten_oeffnen()
    else:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6 = funktionen.basis_daten_anlegen()
        
    if request.method == 'POST':
        fileziel=open("daten/abrechnungszeitraum.txt","w")
        var_abrmonat=request.form['form_abrmonat']
        var_abrjahr=request.form['form_abrjahr']
        fileziel.write(var_abrmonat+"|"+var_abrjahr)
        fileziel.close()



        fileziel=open("daten/basisdaten.txt","w")
        # schreiben in Datei für Basisdaten
        fileziel.write(request.form['form_berater']+"|"+request.form['form_mandant']+"|")
        if (request.form['loa_ns1'] != "" and request.form['loa_ts1'] != "") and (request.form['loa_ns1'] != "Nummer") :
            fileziel.write(request.form['loa_ns1']+"|"+request.form['loa_ts1']+"|")
            # dict für lohnarten
            funktionen.lohnarten_dic_schreiben()
### ggf. noch prüfen  ob es überhaupt else geben kann !!!!!!!!!!!!!
        else:
            fileziel.write("Nummer|Lohnartenbezeichnung|")
        if (request.form['loa_nb1'] != "" and request.form['loa_tb1'] != "") and (request.form['loa_nb1'] != "Nummer"):
            fileziel.write(request.form['loa_nb1']+"|"+request.form['loa_tb1']+"|")
        else:
            fileziel.write("Nummer|Lohnartenbezeichnung|")
        fileziel.close()
    else:
        pass

    filequelle=open("daten/basisdaten.txt","r")
    for x in filequelle:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    filequelle.close()

    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    return render_template('basisdaten.html', v_bnr=var_beraternummer, v_mdt=var_mandantennummer, 
    v_version_program=var_version_program, v_version_titel=var_version_titel, v_sn1=var_3, v_st1=var_4, 
    v_bn1=var_5,v_bt1=var_6, v_bt5=var_99)

## NEU 31.03.2022
#############################################################################
@app.route('/basis_an.html', methods=['POST', 'GET'])
def basis_an():
##############################################################
### Anlage der AN_Stammdaten für die Erfassung
##############################################################
        
    if request.method == 'POST':
        fileziel=open("daten/PNR_Datei.txt","a", encoding='utf-8')
        var_name=request.form['form_name']
        var_vname=request.form['form_vname']
        var_vpnr=request.form['form_pnr']
        fileziel.writelines(var_vpnr+" "+var_name+", "+var_vname+"\n")
        fileziel.close()
    else:
        pass

    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    return render_template('basis_an.html', v_version_program=var_version_program, v_version_titel=var_version_titel)

## NEU 31.03.2022
#############################################################################
@app.route('/basis_fibu.html', methods=['POST', 'GET'])
def basis_fibu():
##############################################################
### Anlage der Fibukonten für die Erfassung
##############################################################
    if os.path.exists("daten/fibukonten.npy"):
        konto_ggagp = funktionen.fibukonten_dic_lesen("konto_ggagp")
        konto_ggagpan = funktionen.fibukonten_dic_lesen("konto_ggagpan")
        konto_ust7 = funktionen.fibukonten_dic_lesen("konto_ust7")
        konto_ust19 = funktionen.fibukonten_dic_lesen("konto_ust19")
        konto_ggust19 = funktionen.fibukonten_dic_lesen("konto_ggust19")
    else:
        konto_ggagp = "Kontonummer erfassen"
        konto_ggagpan = "Kontonummer erfassen"
        konto_ust7 = "Kontonummer erfassen"
        konto_ust19 = "Kontonummer erfassen"
        konto_ggust19 = "Kontonummer erfassen"
        
    if request.method == 'POST':
        funktionen.fibukonten_dic_schreiben()
        if os.path.exists("daten/fibukonten.npy"):
            konto_ggagp = funktionen.fibukonten_dic_lesen("konto_ggagp")
            konto_ggagpan = funktionen.fibukonten_dic_lesen("konto_ggagpan")
            konto_ust7 = funktionen.fibukonten_dic_lesen("konto_ust7")
            konto_ust19 = funktionen.fibukonten_dic_lesen("konto_ust19")
            konto_ggust19 = funktionen.fibukonten_dic_lesen("konto_ggust19")
        else:
            konto_ggagp = "Kontonummer erfassen"
            konto_ggagpan = "Kontonummer erfassen"
            konto_ust7 = "Kontonummer erfassen"
            konto_ust19 = "Kontonummer erfassen"
            konto_ggust19 = "Kontonummer erfassen"

    else:
        pass


    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    return render_template('basis_fibu.html', v_version_program=var_version_program, v_version_titel=var_version_titel, v_konto_ggagp = konto_ggagp, v_konto_ggagpan = konto_ggagpan, v_konto_ust7 = konto_ust7, v_konto_ust19 = konto_ust19, v_konto_ggust19 = konto_ggust19)

## NEU 24.07.20222
#############################################################################
@app.route('/basis_agentur.html', methods=['POST', 'GET'])
def basis_agentur():
##############################################################
### Anlage der Agentur_Stammdaten für die Erfassung
##############################################################

    if request.method == 'POST':
        fileziel=open("daten/Agentur_Datei.txt","a", encoding='utf-8')
        var_bezeichnung=request.form['form_bezeichnung']
        var_agenturnr=request.form['form_agenturnr']
        fileziel.writelines(var_agenturnr+" "+var_bezeichnung+"\n")
        fileziel.close()
    else:
        pass

    var_version_titel = setting.Version_Titel
    var_version_program = setting.Version_Program

    return render_template('basis_agentur.html', v_version_program=var_version_program, v_version_titel=var_version_titel)




webbrowser.open('http://'+setting.Flask_Server_Name)
if __name__ =='__main__':
    app.run(port=17102, debug=False)