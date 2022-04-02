from flask import Flask
from flask import request, render_template
import os, time, csv

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, MetaData, Table, DATE
from sqlalchemy.sql import select, update

import datenbank_obj, funktionen, setting
import pandas as pd
import datetime


def export_steuer(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer):
    # nur für Auswahl Monat/Jahr
    return 

def export_steuerli(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer):
    # brauche ich für Auswahl der Datensätze ggf.
    # aktuell werden alle erfassten DS exportiert, die noch nicht exportert wurden
    # unabhängig vom Erfassungsmonat
    return 


def export_steuerliste(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer):
    # der eigentliche ExcelExport bzw. 
    #    PDF Druck (geplant)
    var_stmonat=request.form["form_stmonat"]
    var_stjahr=request.form["form_stjahr"]
    
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db')
    metadata = datenbank_obj.getdbmetadata(engine)
    abrechnungsdaten = datenbank_obj.abrechnungsdaten_dbobj(metadata)
    metadata.create_all()   
    
    if var_stmonat=="01" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"01\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="02" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"02\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="03" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"03\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="04" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"04\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="05" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"05\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="06" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"06\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="07" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"07\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="08" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"08\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="09" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"09\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="10" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"10\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="11" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"11\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="12" and var_stjahr=="2022":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"12\" AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    elif var_stmonat=="01" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"01\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="02" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"02\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="03" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"03\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="04" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"04\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="05" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"05\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="06" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"06\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="07" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"07\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="08" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"08\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="09" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"09\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="10" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"10\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="11" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"11\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="12" and var_stjahr=="2023":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"12\" AND abrechnungsdaten.abrechnungsjahr==\"2023\" ", engine)
    elif var_stmonat=="01" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"01\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="02" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"02\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="03" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"03\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="04" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"04\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="05" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"05\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="06" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"06\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="07" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"07\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="08" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"08\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="09" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"09\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="10" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"10\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="11" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"11\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="12" and var_stjahr=="2024":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"12\" AND abrechnungsdaten.abrechnungsjahr==\"2024\" ", engine)
    elif var_stmonat=="01" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"01\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="02" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"02\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="03" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"03\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="04" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"04\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="05" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"05\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="06" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"06\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="07" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"07\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="08" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"08\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="09" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"09\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="10" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"10\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="11" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"11\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
    elif var_stmonat=="12" and var_stjahr=="2025":
        result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==\"12\" AND abrechnungsdaten.abrechnungsjahr==\"2025\" ", engine)
        
    else:
        var_version_titel = setting.Version_Titel
        var_version_program = setting.Version_Program
        var_text=("Zeitraum nicht verfügbar!")
        return render_template('/index.html', v_text=var_text, v_bnr=var_beraternummer, v_mdt=var_mandantennummer, v_heute="Fehler !", v_monat=var_abrmonat, v_jahr=var_abrjahr, v_version_program=var_version_program, v_version_titel=var_version_titel)

### variabler Monat aktuell nicht abfragebar - result = pd.read_sql("SELECT * FROM abrechnungsdaten WHERE abrechnungsdaten.abrechnungsmonat==var_stmonat AND abrechnungsdaten.abrechnungsjahr==\"2022\" ", engine)
    result.to_csv("export/"+var_beraternummer+"_"+var_mandantennummer+"_"+var_stmonat+"_"+var_stjahr+"_Export_Monatsauswertung_16.csv", sep=';', encoding='utf-16', index=False, mode='w') 
    result.to_csv("export/"+var_beraternummer+"_"+var_mandantennummer+"_"+var_stmonat+"_"+var_stjahr+"_Export_Monatsauswertung_8.csv", sep=';', encoding='utf-8', index=False, mode='w') 
    # Zwischendatei anlegen für Buchungsliste Agenturprovision AG Anteil
    result.to_csv("daten/ZW_Buchungsliste_AGP_AG.txt", sep='|', encoding='utf-8', index=False, header=False, mode='w') 
    result.to_csv("daten/ZW_Buchungsliste_AGP_AN.txt", sep='|', encoding='utf-8', index=False, header=False, mode='w') 

    # Quell und Zieldatei öffnen - Agenturprov AG Werte in Buchungsliste zu schreiben 
    filequelle=open("daten/ZW_Buchungsliste_AGP_AG.txt")
    fileziel=open("export/"+var_beraternummer+"_"+var_mandantennummer+"_"+var_stmonat+"_"+var_stjahr+"_AGP_AGWerte_Buchungsliste.csv","w", encoding='utf-8')

    #Beschreibung der Felder aus der Quelldatei
    #stelle 1 = Satznummer; stelle 2 = BNR; stelle 3 = Mdt; stelle 4 = PNR; stelle 5 = Lohnart; stelle 6 = LohnartText; stelle 7 = Wert; stelle 8 = Kostenstelle; stelle 9 = Kostenträger;
    #stelle 10 = Art der Tätigkeit; stelle 11 = Freitext; stelle 12 = Buchungsmonat; stelle 13 = Buchungsjahr; stelle 14 = %Agentur gesamt; stelle 15 = %Agentur AN Anteil; stelle 16 = agenturprovwert_AN; 
    #stelle 17 = agenturprovwert_AG, stelle 18 = lohnartustabzug; stelle 19 = ustwert; stelle 20 = kontoust; stelle 21 = exportlodas; stelle 22 = exportlohnundgehalt; stelle 23 = exportwiederholung; 
    #stelle 24 = exportdatum; stelle 25 = Agenturnummer
    AGP_Gegenkonto = funktionen.fibukonten_dic_lesen("konto_ggagp")
    print(AGP_Gegenkonto)
    
    #Beschreibung Exportdatei
    #AGP Gegenkonto (aus dict); Agentur (Personenkonto Rewe) wird auf 99988 gesetzt falls leer; Wert AGP AG in -; Buchungsdatum mit 01MMJJJJ; freier Text als Buchungstext 120 Zeichen ?????
    for x in filequelle:
        stelle1,stelle2,stelle3,stelle4,stelle5,stelle6,stelle7,stelle8,stelle9,stelle10,stelle11,stelle12,stelle13,stelle14,stelle15,stelle16,stelle17,stelle18,stelle19,stelle20,stelle21,stelle22,stelle23,stelle24,stelle25=x.split("|")
        stelle25 = (stelle25.strip())
        if str(stelle17) != "0.0" and str(stelle17) != "0":
            if stelle25 == "":
                stelle25 = "99988"
            fileziel.write(AGP_Gegenkonto+";"+stelle25+";"+stelle17+";01"+stelle12+stelle13+";"+stelle8+";"+stelle9+";PNR: "+stelle4+" AGP %: "+stelle14+" davon AGP AN %: "+stelle15+" Text:"+stelle11+"\n")
    filequelle.close()
    fileziel.close()

    # Quell und Zieldatei öffnen - AGP Werte um Buchungsliste zu schreiben 
    filequelle=open("daten/ZW_Buchungsliste_AGP_AN.txt")
    fileziel=open("export/"+var_beraternummer+"_"+var_mandantennummer+"_"+var_stmonat+"_"+var_stjahr+"_AGP_ANWerte_Buchungsliste.csv","w", encoding='utf-8')

   # Buchungsliste Agenturprov AN Werte schreiben
    AGP_AN_Gegenkonto = funktionen.fibukonten_dic_lesen("konto_ggagpan")
    
    #Beschreibung Exportdatei
    #AGP Gegenkonto (aus dict); Agentur (Personenkonto Rewe) wird auf 99988 gesetzt falls leer; Wert AGP AN in -; Buchungsdatum mit 01MMJJJJ; freier Text als Buchungstext 120 Zeichen ?????
    for x in filequelle:
        stelle1,stelle2,stelle3,stelle4,stelle5,stelle6,stelle7,stelle8,stelle9,stelle10,stelle11,stelle12,stelle13,stelle14,stelle15,stelle16,stelle17,stelle18,stelle19,stelle20,stelle21,stelle22,stelle23,stelle24,stelle25=x.split("|")
        stelle25 = (stelle25.strip())
        if str(stelle16) != "0.0" and str(stelle16) != "0":
            if stelle25 == "":
                stelle25 = "99988"
            fileziel.write(AGP_AN_Gegenkonto+";"+stelle25+";"+stelle16+";01"+stelle12+stelle13+";"+stelle8+";"+stelle9+";PNR: "+stelle4+" AGP %: "+stelle14+" davon AGP AN %: "+stelle15+" Text:"+stelle11+"\n")
    filequelle.close()
    fileziel.close()

    #Beschreibung der Felder aus der Quelldatei
    #stelle 1 = Satznummer; stelle 2 = BNR; stelle 3 = Mdt; stelle 4 = PNR; stelle 5 = Lohnart; stelle 6 = LohnartText; stelle 7 = Wert; stelle 8 = Kostenstelle; stelle 9 = Kostenträger;
    #stelle 10 = Art der Tätigkeit; stelle 11 = Freitext; stelle 12 = Buchungsmonat; stelle 13 = Buchungsjahr; stelle 14 = %Agentur gesamt; stelle 15 = %Agentur AN Anteil; stelle 16 = agenturprovwert_AN; 
    #stelle 17 = agenturprovwert_AG, stelle 18 = lohnartustabzug; stelle 19 = ustwert; stelle 20 = kontoust; stelle 21 = exportlodas; stelle 22 = exportlohnundgehalt; stelle 23 = exportwiederholung; 
    #stelle 24 = exportdatum; stelle 25 = Agenturnummer
    
   # Quell und Zieldatei öffnen - AGP Werte um Buchungsliste zu schreiben 
    filequelle=open("daten/ZW_Buchungsliste_AGP_AG.txt")
    fileziel=open("export/"+var_beraternummer+"_"+var_mandantennummer+"_"+var_stmonat+"_"+var_stjahr+"_AG_USt_Werte_Buchungsliste.csv","w", encoding='utf-8')

   # Buchungsliste Agenturprov AN Werte schreiben
    AG_USt_konto = funktionen.fibukonten_dic_lesen("konto_ust19")
    GG_AG_USt_konto = funktionen.fibukonten_dic_lesen("konto_ggust19") 
    
    #Beschreibung Exportdatei
    #AG USt Gegenkonto (aus dict); Agentur (Personenkonto Rewe) wird auf "unbekannt" gesetzt falls leer; Buchungsdatum mit 01MMJJJJ; freier Text als Buchungstext 120 Zeichen ?????
    for x in filequelle:
        stelle1,stelle2,stelle3,stelle4,stelle5,stelle6,stelle7,stelle8,stelle9,stelle10,stelle11,stelle12,stelle13,stelle14,stelle15,stelle16,stelle17,stelle18,stelle19,stelle20,stelle21,stelle22,stelle23,stelle24,stelle25=x.split("|")
        stelle25 = (stelle25.strip())
        if str(stelle18) == "0" and str(stelle19) != "0" and str(stelle19) != "0.0":
            if str(stelle16) != "0.0" and str(stelle16) != "0":
                if stelle25 == "":
                    stelle25 = "AG unbekannt"
            fileziel.write(AG_USt_konto+";"+GG_AG_USt_konto+";"+stelle19+";01"+stelle12+stelle13+";"+stelle8+";"+stelle9+";PNR: "+stelle4+" Agentur: "+stelle25+" Text:"+stelle11+"\n")
    filequelle.close()
    fileziel.close()

    ##################### PDF Block --------------------------- - NOCH OFFEN
    #
    ##################### komplett entfernt 
    
    if result.shape[0] != 0:
        var_text = result.shape[0]
        var_text="Es wurden "+str(var_text)+" Datensätze in die Datei Export_Steuer exportiert. Weitere Auswertungen stehen zur Verfügung."
    else:
        var_text="Es wurden keine Datensätze als Steuerwerte exportiert"

        
    return var_text, var_stmonat, var_stjahr  


 
def export_csv(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer):
    
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db')
    metadata = datenbank_obj.getdbmetadata(engine)
    abrechnungsdaten = datenbank_obj.abrechnungsdaten_dbobj(metadata)
    metadata.create_all()

    result = pd.read_sql("SELECT * FROM abrechnungsdaten", engine)
    result.to_csv("export/"+var_beraternummer+"_"+var_mandantennummer+"_"+var_abrmonat+"_"+var_abrjahr+"_Export.csv", sep=';', encoding='utf-16', index=False, mode='w') 
    if result.shape[0] != 0:
        var_text = result.shape[0]
        var_text="Es wurden "+str(var_text)+" Datensätze als csv Daten exportiert."
    else:
        var_text="Es wurden keine Datensätze als csv Daten exportiert"

    # Export alle DS nach Excel

    return var_text

## sollte nach vielen anpassungen nicht mehr funktionieren - ungeprüft
def export_lohnundgehalt(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantenummer):

    engine = create_engine('sqlite:///daten/abrechnungsdaten.db')
    metadata = datenbank_obj.getdbmetadata(engine)
    abrechnungsdaten = datenbank_obj.abrechnungsdaten_dbobj(metadata)
    metadata.create_all()

    if request.method == 'POST':
        neuedatei = open("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"LuG.txt", "w")
        neuedatei.write(var_beraternummer+";"+var_mandantenummer+";"+var_abrmonat+"/"+var_abrjahr+"\n")
        neuedatei.close()
        
        # Export der Lohnarten und Nettobe/abzüge 
        result = pd.read_sql("SELECT abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.exportlohnundgehalt==\"N\" ", engine)
        result.to_csv("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"LuG.txt", sep=';', encoding='utf-8', index=False, header=False, mode='a') 

        ### NEU AGP und UST auch in LUG Datei
        # Export der USt in Zwischendatei
        result = pd.read_sql('SELECT abrechnungsdaten.PNR, abrechnungsdaten.lohnartustabzug, abrechnungsdaten.ustwert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.ustwert != "0" AND abrechnungsdaten.exportlohnundgehalt==\"N\" ', engine)
        result.to_csv("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"LuG.txt", sep=';', encoding='utf-8', index=False, header=False, mode='a') 
        
        # Export der Agenturprovision in Zwischendatei
        result = pd.read_sql('SELECT abrechnungsdaten.PNR, abrechnungsdaten.agenturprovwert_AN, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.agenturprovwert_AN != "0" AND abrechnungsdaten.exportlohnundgehalt==\"N\" ', engine)
        result.to_csv("daten/ZW_LuG_AGP.txt", sep='|', encoding='utf-8', index=False, header=False, mode='w') 

        ############
        # Quell und Zieldatei öffnen - AGP Werte um Lohnart einzufügen 
        filequelle=open("daten/ZW_LuG_AGP.txt")
        fileziel=open("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"LuG.txt","a", encoding='utf-8')
        
        #Beschreibung der Felder aus der Quelldatei
        #stelle 1 = PNR; stelle 2 = Wert; stelle 3 = Kostenstelle; stelle 4 = Kostentraeger 
        AGP_Lohnart = funktionen.lohnarten_dic_lesen("loa_nb6")
        for x in filequelle:
            stelle1,stelle2,stelle3,stelle4=x.split("|")
            stelle4 = (stelle4.strip())
#            stelle2 = stelle2.replace(".", ",") 
            fileziel.write(stelle1+";"+AGP_Lohnart+";"+stelle2+";"+stelle3+";"+stelle4+"\n")

        filequelle.close()
        fileziel.close()

       
        hdatum = datetime.datetime.now()
        hdatum = hdatum.strftime("%d.%m.%Y")
        conn = engine.connect()                          
        abrechnungsdatenupdate = abrechnungsdaten.update().where(abrechnungsdaten.c.exportlohnundgehalt=="N").values(exportlohnundgehalt="J", exportlodas="X", exportwiederholung="X", abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, exportdatum=str(hdatum))
        conn.execute(abrechnungsdatenupdate)
        abrechnungsdatenupdate = abrechnungsdaten.select()
        conn.execute(abrechnungsdatenupdate).fetchall()
        
        if result.shape[0] != 0:
            var_text = result.shape[0]
            var_text="Es wurden "+str(var_text)+" Datensätze für Lohn und Gehalt exportiert."

            filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
            for x in filequelle:
                var_abrmonat,var_abrjahr=x.split("|")
                break
            var_abrmonat = int(var_abrmonat)+1
            if var_abrmonat < 10:
                var_abrmonat = str(var_abrmonat)
                var_abrmonat = "0"+var_abrmonat
            else:
                var_abrmonat = str(var_abrmonat)
            
            if var_abrmonat == "13":
                var_abrmonat = "01"
                var_abrjahr = int(var_abrjahr)+1
                var_abrjahr = str(var_abrjahr)
            filequelle=open("daten/abrechnungszeitraum.txt","w")
            filequelle.write(var_abrmonat+"|"+var_abrjahr)       
            filequelle.close()
        else:
            var_text="Es wurden keine Datensätze für Lohn und Gehalt exportiert"
            pass
    else:
        var_text="Es werden die Datensätze der Monatsübersicht für Lohn und Gehalt exportiert"
        pass

    return var_text


### Export Lodas in Funktion aktuell 2022-02-14 mit AGP und USt
### Tabellen auf Netto und Brutto geändert 
### NEU* 20220402 USt wenn AG übernimmt - LOA 0 in SQL DB
### USt wenn AN trägt Nettoabzug in SQl DB
def export_lodas(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantenummer):

    engine = create_engine('sqlite:///daten/abrechnungsdaten.db')
    metadata = datenbank_obj.getdbmetadata(engine)
    abrechnungsdaten = datenbank_obj.abrechnungsdaten_dbobj(metadata)
    metadata.create_all()

    if request.method == 'POST':
        if os.path.exists("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"_Lodas.txt"):
        ## Datei öffnen und Daten werden angehangen
            fileziel=open("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"_Lodas.txt","a")
            fileziel.write("\n* Stunden zur Abrechnung von Mitarbeitern\n")
            fileziel.write("[Bewegungsdaten]\n")
            
        else:
        ## Datei neu öffnen und Kopfdaten schreiben
            fileziel=open("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"_Lodas.txt","w")
        # schreiben in Lodas Importdatei
            fileziel.write("[Allgemein]\nZiel=LODAS\nVersion_SST=1.0\nBeraterNr=")
            fileziel.write(var_beraternummer)
            fileziel.write("\nMandantenNr=")
            fileziel.write(var_mandantenummer)
            fileziel.write("\nDatumsformat=JJJJ-MM-TT")
            fileziel.write("\nStringbegrenzer='")
            fileziel.write("\n\n* LEGENDE:\n* Datei erzeugt mit Tool ARMTool\n* AP: Andreé Rosenkranz; andree@rosenkranz.one\n\n")
            fileziel.write("* Satzbeschreibungen zur Übergabe von Bewegungsdaten für Mitarbeiter\n[Satzbeschreibung]\n")
#            fileziel.write("\n10;u_lod_bwd_buchung_brutto;abrechnung_zeitraum#bwd;pnr#bwd;la_eigene#bwd;brutto_fest_bez#bwd;kostenstelle#bwd;kostentraeger#bwd;")
 #           fileziel.write("\n11;u_lod_bwd_buchung_netto;abrechnung_zeitraum#bwd;pnr#bwd;nba_nr#bwd;netto_betrag#bwd;")
            fileziel.write("\n10;u_lod_bwd_buchung_standard;abrechnung_zeitraum#bwd;pnr#bwd;la_eigene#bwd;bs_nr#bwd;bs_wert_butab#bwd;kostenstelle#bwd;kostentraeger#bwd;")

            fileziel.write("\n\n")
            fileziel.write("* Werte zur Abrechnung von Mitarbeitern\n\n")
            fileziel.write("[Bewegungsdaten]\n\n")
 
# Export der USt in Zwischendatei
# Neu*  20220401 ohne USt AG    result = pd.read_sql('SELECT abrechnungsdaten.PNR, abrechnungsdaten.lohnartustabzug, abrechnungsdaten.ustwert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.ustwert != "0" AND abrechnungsdaten.exportlodas==\"N\" ', engine)
        result = pd.read_sql('SELECT abrechnungsdaten.PNR, abrechnungsdaten.lohnartustabzug, abrechnungsdaten.ustwert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.lohnartustabzug != "0" AND abrechnungsdaten.exportlodas==\"N\" ', engine)
        result.to_csv("daten/ZW_Lodas_USt.txt", sep='|', encoding='utf-8', index=False, header=False, mode='w') 
# Export der Agenturprovision AN in Zwischendatei
        result = pd.read_sql('SELECT abrechnungsdaten.PNR, abrechnungsdaten.agenturprovwert_AN, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.agenturprovwert_AN != "0" AND abrechnungsdaten.exportlodas==\"N\" ', engine)
        result.to_csv("daten/ZW_Lodas_AGP_AN.txt", sep='|', encoding='utf-8', index=False, header=False, mode='w')
# Export der Agenturprovision AG in Zwischendatei
        result = pd.read_sql('SELECT abrechnungsdaten.PNR, abrechnungsdaten.agenturprovwert_AG, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.agenturprovwert_AG != "0" AND abrechnungsdaten.exportlodas==\"N\" ', engine)
        result.to_csv("daten/ZW_Lodas_AGP_AG.txt", sep='|', encoding='utf-8', index=False, header=False, mode='w')
 # Export der Lohnarten und Nettobe/abzüge                                                                                                                                                 
        result = pd.read_sql('SELECT abrechnungsdaten.PNR, abrechnungsdaten.lohnart, abrechnungsdaten.wert, abrechnungsdaten.kostenstelle, abrechnungsdaten.kostentraeger FROM abrechnungsdaten WHERE abrechnungsdaten.exportlodas==\"N\" ', engine)
        result.to_csv("daten/ZW_Lodas.txt", sep='|', encoding='utf-8', index=False, header=False, mode='w') 

        ############
        # Quell und Zieldatei öffnen - AGP Werte
        filequelle=open("daten/ZW_Lodas_AGP_AN.txt")
        fileziel=open("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"_Lodas.txt","a", encoding='utf-8')
        
        #Beschreibung der Felder aus der Quelldatei
        #stelle 1 = PNR; stelle 2 = Wert; stelle 3 = Kostenstelle; stelle 4 = Kostentraeger 
        AGP_Lohnart = funktionen.lohnarten_dic_lesen("loa_nb6")
        for x in filequelle:
            stelle1,stelle2,stelle3,stelle4=x.split("|")
            stelle4 = (stelle4.strip())
            var_bs = "3"
            stelle2 = stelle2.replace(".", ",") 
#            fileziel.write("11;"+var_abrjahr+"-"+var_abrmonat+"-01;"+stelle1+";"+AGP_Lohnart+";"+stelle2+";"+stelle3+";"+stelle4+";\n")
            fileziel.write("10;"+var_abrjahr+"-"+var_abrmonat+"-01;"+stelle1+";"+AGP_Lohnart+";"+var_bs+";"+stelle2+";"+stelle3+";"+stelle4+";\n")

        filequelle.close()
        fileziel.close()

        ############
        # Quell und Zieldatei öffnen - USt Werte
        filequelle=open("daten/ZW_Lodas_Ust.txt")
        fileziel=open("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"_Lodas.txt","a", encoding='utf-8')
        
      #Beschreibung der Felder aus der Quelldatei
      #stelle 1 = PNR; stelle 2 = Lohnart; stelle 3 = Wert; stelle 4 = Kostenstelle; stelle 5 = Kostentraeger
        for x in filequelle:
            stelle1,stelle2,stelle3,stelle4,stelle5=x.split("|")
            stelle5 = (stelle5.strip())
            if int(stelle2) > 8999:
                var_bs = "3"
                var_sa = "11"

            else:
                var_bs = "2"
                var_sa = "10"
            stelle3 = stelle3.replace(".", ",") 
#            fileziel.write(var_sa+";"+var_abrjahr+"-"+var_abrmonat+"-01;"+stelle1+";"+stelle2+";"+stelle3+";"+stelle4+";"+stelle5+";\n")
            fileziel.write("10;"+var_abrjahr+"-"+var_abrmonat+"-01;"+stelle1+";"+stelle2+";"+var_bs+";"+stelle3+";"+stelle4+";"+stelle5+";\n")

        filequelle.close()
        fileziel.close()

        filequelle=open("daten/ZW_Lodas.txt")
        fileziel=open("export/"+var_beraternummer+"_"+var_mandantenummer+"_"+var_abrmonat+"_"+var_abrjahr+"_Lodas.txt","a", encoding='utf-8')
        
        #Beschreibung der Felder aus der Quelldatei
        #stelle 1 = PNR; stelle 2 = Lohnart; stelle 3 = Wert; stelle 4 = Kostenstelle; stelle 5 = Kostentraeger
        for x in filequelle:
            stelle1,stelle2,stelle3,stelle4,stelle5=x.split("|")
            stelle5 = (stelle5.strip())
            if int(stelle2) > 8999:
                var_bs = "3"
                var_sa = "11"
            else:
                var_bs = "2"
                var_sa = "10"

            stelle3 = stelle3.replace(".", ",") 

#            fileziel.write(var_sa+";"+var_abrjahr+"-"+var_abrmonat+"-01;"+stelle1+";"+stelle2+";"+stelle3+";"+stelle4+";"+stelle5+";\n")
            fileziel.write("10;"+var_abrjahr+"-"+var_abrmonat+"-01;"+stelle1+";"+stelle2+";"+var_bs+";"+stelle3+";"+stelle4+";"+stelle5+";\n")

        fileziel.write("\n\n[Hinweisdaten]\n\nDaten uebernommen aus Erfassungstool ARMTool\nfuer die korrekte Berechnung saemtlicher Werte ist allein der Anwender verantwortlich!\n")
        #Dateien schließen	
        filequelle.close()
        fileziel.close()

        ######################        
        hdatum = datetime.datetime.now()
        hdatum = hdatum.strftime("%d.%m.%Y")
        conn = engine.connect()                               
        abrechnungsdatenupdate = abrechnungsdaten.update().where(abrechnungsdaten.c.exportlodas=="N").values(exportlohnundgehalt="X", exportlodas="J", exportwiederholung="X", abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, exportdatum=str(hdatum))
        conn.execute(abrechnungsdatenupdate)
        abrechnungsdatenupdate = abrechnungsdaten.select()
        conn.execute(abrechnungsdatenupdate).fetchall()
        
        if result.shape[0] != 0:
            var_text = result.shape[0]
            var_text="Es wurden "+str(var_text)+" Datensätze für Lodas exportiert."

            filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
            for x in filequelle:
                var_abrmonat,var_abrjahr=x.split("|")
                break
            var_abrmonat = int(var_abrmonat)+1
            if var_abrmonat < 10:
                var_abrmonat = str(var_abrmonat)
                var_abrmonat = "0"+var_abrmonat
            else:
                var_abrmonat = str(var_abrmonat)
            
            if var_abrmonat == "13":
                var_abrmonat = "01"
                var_abrjahr = int(var_abrjahr)+1
                var_abrjahr = str(var_abrjahr)
            filequelle=open("daten/abrechnungszeitraum.txt","w")
            filequelle.write(var_abrmonat+"|"+var_abrjahr)       
            filequelle.close()
            pass
        else:
            var_text="Es wurden keine Datensätze für Lodas exportiert"
            pass
    else:
        var_text="Es werden die Datensätze der Monatsübersicht für Lodas exportiert"
        pass

    return var_text