from flask import Flask
from flask import request
import os, time

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, MetaData, Table, DATE
from sqlalchemy.sql import select, update

import datenbank_obj, funktionen
import numpy as np


def abrechnung_erf(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantennummer):
    
# anlage Datenbank - falls nicht vorhanden
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db')
    metadata = datenbank_obj.getdbmetadata(engine)
    abrechnungsdaten = datenbank_obj.abrechnungsdaten_dbobj(metadata)
    metadata.create_all()

    if request.method == 'POST':

    # Ohne Steuer
        if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommaos'] == "" and request.form["form_euronachkommaos"] == ""):
            pass
        else:
            if request.form["form_eurovorkommaos"] == "":
                setvorkomma = "0"
            else:
                setvorkomma = request.form["form_eurovorkommaos"]
            if request.form["form_euronachkommaos"] == "":
                setnachkomma = "00"
            elif request.form["form_euronachkommaos"] == "0":
                setnachkomma = "00"
            elif len(request.form["form_euronachkommaos"]) == 1:
                setnachkomma = "0"+request.form["form_euronachkommaos"]
            else:
                setnachkomma = request.form["form_euronachkommaos"]
            
            provbasis = int(setvorkomma+setnachkomma)
            provbasis = provbasis/100
                     
            if request.form['form_prozentvorkommaagp'] == "" and request.form["form_prozentnachkommaagp"] == "" and request.form["form_eurovorkommaagp"] == "" and request.form["form_euronachkommaagp"] == "":
                agenturprov_AN = 0
                agenturprov_AG = 0
                agenturprov = 0
                prozentagp = 0
                prozentAN = 0
                
            else:
                agenturprov_AN, agenturprov_AG, prozentagp, prozentAN= funktionen.agenturprov_berechnen(provbasis)

            if request.form['form_steuer'] == "19":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
            elif request.form['form_steuer'] == "7":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
            else:
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)

            lohnart=funktionen.lohnarten_dic_lesen("loa_ns1")
            lohnart=str(lohnart)
            lohnart_text = funktionen.lohnarten_dic_lesen(lohnart)      
 
            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnart, lohnart_text=lohnart_text, wert=setvorkomma+"."+setnachkomma, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent=prozentagp, agenturprovprozent_AN=prozentAN, agenturprovwert_AN=agenturprov_AN, agenturprovwert_AG=agenturprov_AG,
                                                            lohnartustabzug=ust_Lohnart, ustwert=ust_Wert, kontoust=ust_Konto, exportlodas="N",
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)
############ ok

    # Pauschalsteuer 15%
        if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommap15'] == "" and request.form['form_euronachkommap15'] == ""):
            pass
        else:
            if request.form["form_eurovorkommap15"] == "":
                setvorkomma = "0"
            else:
                setvorkomma = request.form["form_eurovorkommap15"]
            if request.form["form_euronachkommap15"] == "":
                setnachkomma = "00"
            
            elif request.form["form_euronachkommap15"] == "0":
                setnachkomma = "00"
            elif len(request.form["form_euronachkommap15"]) == 1:
                setnachkomma = "0"+request.form["form_euronachkommap15"]
            else:
                setnachkomma = request.form["form_euronachkommap15"]

            #Berechnung Prov
            provbasis = int(setvorkomma+setnachkomma)
            provbasis = provbasis/100

            if request.form['form_prozentvorkommaagp'] == "" and request.form["form_prozentnachkommaagp"] == "":
                agenturprov_AN = 0
                agenturprov_AG = 0
                agenturprov = 0
                prozentagp = 0
                prozentAN = 0
                print("Du hast keine Provision eingegeben")

            else:
                agenturprov_AN, agenturprov_AG, prozentagp, prozentAN= funktionen.agenturprov_berechnen(provbasis)

            # berechnung steuer und soli
            pauschbrutto=setvorkomma+setnachkomma
            pauschbrutto=int(pauschbrutto)
            pauschbrutto=pauschbrutto/100
            pauschsteuer=pauschbrutto*15/100
            pauschsteuer = round (pauschsteuer, 2)
            pauschsoli=pauschsteuer*5.5/100
            pauschsoli = round (pauschsoli, 2)
            pauschsteuer = "-"+(str(pauschsteuer))
            pauschsoli = "-"+(str(pauschsoli))
            # Ende Berechnung

            #Berechnung UST 
            if request.form['form_steuer'] == "19":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
                
            elif request.form['form_steuer'] == "7":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
            else:
                ust = "0"
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)


            lohnart=funktionen.lohnarten_dic_lesen("loa_ns3")
            lohnart=str(lohnart)
            lohnart_text = funktionen.lohnarten_dic_lesen(lohnart)      

            lohnartp15=funktionen.lohnarten_dic_lesen("loa_nb1")
            lohnartp15=str(lohnartp15)
            lohnart_textp15 = funktionen.lohnarten_dic_lesen(lohnartp15)      
 
            lohnartsoli=funktionen.lohnarten_dic_lesen("loa_nb3")
            lohnartsoli=str(lohnartsoli)
            lohnart_textsoli = funktionen.lohnarten_dic_lesen(lohnartsoli)  

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnart, lohnart_text=lohnart_text, wert=setvorkomma+"."+setnachkomma, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent=prozentagp, agenturprovprozent_AN=prozentAN, agenturprovwert_AN=agenturprov_AN, agenturprovwert_AG=agenturprov_AG,
                                                            lohnartustabzug=ust_Lohnart, ustwert=ust_Wert, kontoust=ust_Konto, exportlodas="N",
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)
            
            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnartp15, lohnart_text=lohnart_textp15, wert=pauschsteuer, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N",
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)
            
            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnartsoli, lohnart_text=lohnart_textsoli, wert=pauschsoli, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N",
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)


# Gage abzgl. Betriebsausgaben
        if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommaab'] == "" and request.form['form_euronachkommaab'] == ""):
            pass
        else:
            if request.form["form_eurovorkommaab"] == "":
                setvorkomma = "0"
            else:
                setvorkomma = request.form["form_eurovorkommaab"]
            if request.form["form_euronachkommaab"] == "":
                setnachkomma = "00"
            
            elif request.form["form_euronachkommaab"] == "0":
                setnachkomma = "00"
            elif len(request.form["form_euronachkommaab"]) == 1:
                setnachkomma = "0"+request.form["form_euronachkommaab"]
            else:
                setnachkomma = request.form["form_euronachkommaab"]

            #Berechnung Prov
            provbasis = int(setvorkomma+setnachkomma)
            provbasis = provbasis/100

            if request.form['form_prozentvorkommaagp'] == "" and request.form["form_prozentnachkommaagp"] == "":
                agenturprov_AN = 0
                agenturprov_AG = 0
                agenturprov = 0
                prozentagp = 0
                prozentAN = 0
                
            else:
                agenturprov_AN, agenturprov_AG, prozentagp, prozentAN= funktionen.agenturprov_berechnen(provbasis)

            # berechnung steuer und soli
            pauschbrutto=setvorkomma+setnachkomma
            pauschbrutto=int(pauschbrutto)
            pauschbrutto=pauschbrutto/100
            pauschsteuer=pauschbrutto*30/100
            pauschsteuer = round (pauschsteuer, 2)
            pauschsoli=pauschsteuer*5.5/100
            pauschsoli = round (pauschsoli, 2)
            pauschsteuer = "-"+(str(pauschsteuer))
            pauschsoli = "-"+(str(pauschsoli))
            # Ende Berechnung

            # Berechnung UST 
            if request.form['form_steuer'] == "19":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
                
            elif request.form['form_steuer'] == "7":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
            else:
                ust = "0"
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)


            lohnart=funktionen.lohnarten_dic_lesen("loa_ns5")
            lohnart=str(lohnart)
            lohnart_text = funktionen.lohnarten_dic_lesen(lohnart)      

            lohnartp30=funktionen.lohnarten_dic_lesen("loa_nb2")
            lohnartp30=str(lohnartp30)
            lohnart_textp30 = funktionen.lohnarten_dic_lesen(lohnartp30)      
 
            lohnartsoli=funktionen.lohnarten_dic_lesen("loa_nb3")
            lohnartsoli=str(lohnartsoli)
            lohnart_textsoli = funktionen.lohnarten_dic_lesen(lohnartsoli)  

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnart, lohnart_text=lohnart_text, wert=setvorkomma+"."+setnachkomma, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent=prozentagp, agenturprovprozent_AN=prozentAN, agenturprovwert_AN=agenturprov_AN, agenturprovwert_AG=agenturprov_AG,
                                                            lohnartustabzug=ust_Lohnart, ustwert=ust_Wert, kontoust=ust_Konto, exportlodas="N",
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnartp30, lohnart_text=lohnart_textp30, wert=pauschsteuer, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N", 
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnartsoli, lohnart_text=lohnart_textsoli, wert=pauschsoli, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N",
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

# Betriebsausgabenabzug bei Gage
        if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommaba'] == "" and request.form['form_euronachkommaba'] == ""):
            pass
        else:
            if request.form["form_eurovorkommaba"] == "":
                setvorkomma = "0"
            else:
                setvorkomma = request.form["form_eurovorkommaba"]
            if request.form["form_euronachkommaba"] == "":
                setnachkomma = "00"
            elif request.form["form_euronachkommaba"] == "0":
                setnachkomma = "00"
            elif len(request.form["form_euronachkommaba"]) == 1:
                setnachkomma = "0"+request.form["form_euronachkommaba"]
            else:
                setnachkomma = request.form["form_euronachkommaba"]

            lohnart=funktionen.lohnarten_dic_lesen("loa_ns6")
            lohnart=str(lohnart)
            lohnart_text = funktionen.lohnarten_dic_lesen(lohnart)  

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnart, lohnart_text=lohnart_text, wert=setvorkomma+"."+setnachkomma, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr,
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N",
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

# Gage Nettovereinbarung 
        if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommanetto'] == "" and request.form['form_euronachkommanetto'] == ""):
            pass
        else:
            if request.form["form_eurovorkommanetto"] == "":
                setvorkomma = "0"
            else:
                setvorkomma = request.form["form_eurovorkommanetto"]
            if request.form["form_euronachkommanetto"] == "":
                setnachkomma = "00"
            elif request.form["form_euronachkommanetto"] == "0":
                setnachkomma = "00"
            elif len(request.form["form_euronachkommanetto"]) == 1:
                setnachkomma = "0"+request.form["form_euronachkommanetto"]
            else:
                setnachkomma = request.form["form_euronachkommanetto"]

            #Berechnung Prov
            provbasis = int(setvorkomma+setnachkomma)
            provbasis = provbasis/100

            if request.form['form_prozentvorkommaagp'] == "" and request.form["form_prozentnachkommaagp"] == "":
                agenturprov_AN = 0
                agenturprov_AG = 0
                agenturprov = 0
                prozentagp = 0
                prozentAN = 0
                print("Du hast keine Provision eingegeben")

            else:
                agenturprov_AN, agenturprov_AG, prozentagp, prozentAN= funktionen.agenturprov_berechnen(provbasis)

            # berechnung steuer und soli
            pauschbrutto=setvorkomma+setnachkomma
            pauschbrutto=int(pauschbrutto)
            pauschbrutto=pauschbrutto/100
            pauschsteuer=pauschbrutto*17.82/100
            pauschsteuer = round (pauschsteuer, 2)
            pauschsoli=pauschbrutto*0.98/100
            pauschsoli = round (pauschsoli, 2)
            pauschverrechnung = pauschsteuer+pauschsoli
            pauschsteuer = "-"+(str(pauschsteuer))
            pauschsoli = "-"+(str(pauschsoli))

            # Berechnung UST 
            if request.form['form_steuer'] == "19":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
                
            elif request.form['form_steuer'] == "7":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
            else:
                ust = "0"
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)

            lohnart=funktionen.lohnarten_dic_lesen("loa_ns8")
            lohnart=str(lohnart)
            lohnart_text = funktionen.lohnarten_dic_lesen(lohnart)      
            
            lohnartv=funktionen.lohnarten_dic_lesen("loa_ns10")
            lohnartv=str(lohnartv)
            lohnart_textv = funktionen.lohnarten_dic_lesen(lohnartv)      

            lohnartp17=funktionen.lohnarten_dic_lesen("loa_nb4")
            lohnartp17=str(lohnartp17)
            lohnart_textp17 = funktionen.lohnarten_dic_lesen(lohnartp17)      
 
            lohnartsoli5=funktionen.lohnarten_dic_lesen("loa_nb5")
            lohnartsoli5=str(lohnartsoli5)
            lohnart_textsoli5 = funktionen.lohnarten_dic_lesen(lohnartsoli5)  
                       
            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnart, lohnart_text=lohnart_text, wert=setvorkomma+"."+setnachkomma, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent=prozentagp, agenturprovprozent_AN=prozentAN, agenturprovwert_AN=agenturprov_AN, agenturprovwert_AG=agenturprov_AG, 
                                                            lohnartustabzug=ust_Lohnart, ustwert=ust_Wert, kontoust=ust_Konto, exportlodas="N", 
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnartv, lohnart_text=lohnart_textv, wert=str(pauschverrechnung), 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr,
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N", 
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnartp17, lohnart_text=lohnart_textp17, wert=pauschsteuer, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N", 
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnartsoli5, lohnart_text=lohnart_textsoli5, wert=pauschsoli, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent="0", agenturprovprozent_AN="0", agenturprovwert_AN="0", agenturprovwert_AG="0",
                                                            lohnartustabzug="0", ustwert="0", kontoust="0", exportlodas="N", 
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)


# Gage Nettovereinbarung bis 250 EURO
        if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommanetto2'] == "" and request.form['form_euronachkommanetto2'] == ""):
            pass
        else:
            if request.form["form_eurovorkommanetto2"] == "":
                setvorkomma = "0"
            else:
                setvorkomma = request.form["form_eurovorkommanetto2"]
            if request.form["form_euronachkommanetto2"] == "":
                setnachkomma = "00"
            elif request.form["form_euronachkommanetto2"] == "0":
                setnachkomma = "00"
            elif len(request.form["form_euronachkommanetto2"]) == 1:
                setnachkomma = "0"+request.form["form_euronachkommanetto2"]
            else:
                setnachkomma = request.form["form_euronachkommanetto2"]
               
            #Berechnung Prov
            provbasis = int(setvorkomma+setnachkomma)
            provbasis = provbasis/100

            if request.form['form_prozentvorkommaagp'] == "" and request.form["form_prozentnachkommaagp"] == "":
                agenturprov_AN = 0
                agenturprov_AG = 0
                agenturprov = 0
                prozentagp = 0
                prozentAN = 0
                print("Du hast keine Provision eingegeben")

            else:
                agenturprov_AN, agenturprov_AG, prozentagp, prozentAN= funktionen.agenturprov_berechnen(provbasis)

            # Berechnung UST 
            if request.form['form_steuer'] == "19":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
                
            elif request.form['form_steuer'] == "7":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
            else:
                ust = "0"
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)

            lohnart=funktionen.lohnarten_dic_lesen("loa_ns11")
            lohnart=str(lohnart)
            lohnart_text = funktionen.lohnarten_dic_lesen(lohnart)      
            
            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnart, lohnart_text=lohnart_text, wert=setvorkomma+"."+setnachkomma, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent=prozentagp, agenturprovprozent_AN=prozentAN, agenturprovwert_AN=agenturprov_AN, agenturprovwert_AG=agenturprov_AG, 
                                                            lohnartustabzug=ust_Lohnart, ustwert=ust_Wert, kontoust=ust_Konto, exportlodas="N", 
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)
           

# Gage ohne Steuer wg DBA

        if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommadba'] == "" and request.form['form_euronachkommadba'] == ""):
            pass
        else:
            if request.form["form_eurovorkommadba"] == "":
                setvorkomma = "0"
            else:
                setvorkomma = request.form["form_eurovorkommadba"]
            if request.form["form_euronachkommadba"] == "":
                setnachkomma = "00"
            elif request.form["form_euronachkommadba"] == "0":
                setnachkomma = "00"
            elif len(request.form["form_euronachkommadba"]) == 1:
                setnachkomma = "0"+request.form["form_euronachkommadba"]
            else:
                setnachkomma = request.form["form_euronachkommadba"]

               
            #Berechnung Prov
            provbasis = int(setvorkomma+setnachkomma)
            provbasis = provbasis/100

            if request.form['form_prozentvorkommaagp'] == "" and request.form["form_prozentnachkommaagp"] == "":
                agenturprov_AN = 0
                agenturprov_AG = 0
                agenturprov = 0
                prozentagp = 0
                prozentAN = 0
                print("Du hast keine Provision eingegeben")

            else:
                agenturprov_AN, agenturprov_AG, prozentagp, prozentAN= funktionen.agenturprov_berechnen(provbasis)

            # Berechnung UST 
            if request.form['form_steuer'] == "19":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
                
            elif request.form['form_steuer'] == "7":
                ust = request.form['form_steuer']
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)
            else:
                ust = "0"
                ust_Wert, ust_Lohnart, ust_Konto  = funktionen.umsatzsteuer_berechnen(provbasis, ust)

            lohnart=funktionen.lohnarten_dic_lesen("loa_ns13")
            lohnart=str(lohnart)
            lohnart_text = funktionen.lohnarten_dic_lesen(lohnart)      
            
            insert_daten = abrechnungsdaten.insert().values(beraternummer=var_beraternummer, mandantennummer=var_mandantennummer, PNR=request.form['form_personalnummer'], lohnart=lohnart, lohnart_text=lohnart_text, wert=setvorkomma+"."+setnachkomma, 
                                                            kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
                                                            artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat, abrechnungsjahr=var_abrjahr, 
                                                            agenturprovprozent=prozentagp, agenturprovprozent_AN=prozentAN, agenturprovwert_AN=agenturprov_AN, agenturprovwert_AG=agenturprov_AG, 
                                                            lohnartustabzug=ust_Lohnart, ustwert=ust_Wert, kontoust=ust_Konto, exportlodas="N", 
                                                            exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            engine.execute(insert_daten)

            #insert_daten = abrechnungsdaten.insert().values(PNR=request.form['form_personalnummer'], lohnart=request.form["form_gehaltdba"], wert=setvorkomma+"."+setnachkomma,
            #                                               kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
            #                                               artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat,
            #                                               abrechnungsjahr=var_abrjahr, exportlodas="N", exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
            #


# Agenturprovision

    #    if request.form['form_personalnummer'] == "Auswahl" or (request.form['form_eurovorkommaagp'] == "" and request.form['form_euronachkommaagp'] == ""):
    #        pass
    #    else:
    #        if request.form["form_eurovorkommaagp"] == "":
    #            setvorkomma = "0"
    #        else:
    #            setvorkomma = request.form["form_eurovorkommaagp"]
    #        if request.form["form_euronachkommaagp"] == "":
    #            setnachkomma = "00"
    #        elif request.form["form_euronachkommaagp"] == "0":
    #            setnachkomma = "00"
    #        elif len(request.form["form_euronachkommaagp"]) == 1:
    #            setnachkomma = "0"+request.form["form_euronachkommaagp"]
    #        else:
    #            setnachkomma = request.form["form_euronachkommaagp"]
    #        # war mal drin request.form["form_gehaltagp"]

    #        insert_daten = abrechnungsdaten.insert().values(PNR=request.form['form_personalnummer'], lohnart="9606", wert=setvorkomma+"."+setnachkomma, 
    #                                                        kostenstelle=request.form["form_kostenstelle"], kostentraeger=request.form["form_kostentraeger"], 
    #                                                        artdertaetigkeit=request.form["form_abrtyp"], freitext=request.form["form_freiertext"], abrechnungsmonat=var_abrmonat,
    #                                                        abrechnungsjahr=var_abrjahr, exportlodas="N", exportlohnundgehalt="N", exportwiederholung="N", exportdatum="00.00.0000")
    #        engine.execute(insert_daten)

    #else:
        
    #    pass
    
    return 


def abrechnungsdaten_del():
    # anlage Datenbank - falls nicht vorhanden
    engine = create_engine('sqlite:///daten/abrechnungsdaten.db')
    metadata = datenbank_obj.getdbmetadata(engine)
    abrechnungsdaten = datenbank_obj.abrechnungsdaten_dbobj(metadata)
    metadata.create_all()

    ####
    ## if .. noch einbauen, damit nur DS gelöscht werden können die auch aktuell sind! #abrechnungsdaten.c.exportlodas=="N" and
    ## and klappt nicht - löscht dann alle mit beiden Bedingungen

    if request.method == 'POST':
        loeschen_daten = abrechnungsdaten.delete().where(abrechnungsdaten.c.id==request.form['form_id'])
        engine.execute(loeschen_daten)
        loeschen_daten = abrechnungsdaten.select()
        engine.execute(loeschen_daten).fetchall
#        notification.notify(title = "ARMTools", message = f"Es wurde der Datensatz\nmit der ID: "+request.form['form_id']+"\ngelöscht!\n")

    else:
        
        pass
    return
