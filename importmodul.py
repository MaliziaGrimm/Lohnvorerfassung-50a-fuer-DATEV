#  
# Tool zum Import von Stammdaten aus Lodas / LuG nach ARMTool
# DalyReport Arbeitnehmer mit Quelle Lodas wird verarbeitet
# DalyReport Arbeitnehmer mit Wuelle Lohn und Gehalt wird verarbeitet
# Stand 24.12.2021
#

import os, time 
from shutil import copyfile


def lodasimport(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantenummer):
    Datum = os.path.join(time.strftime('%Y%m%d_%H%M'))

    if os.path.exists("daten/Arbeitnehmer.txt"):

        if os.path.exists("daten/PNR_Datei.txt"):
            os.rename("daten/PNR_Datei.txt","daten/"+(Datum)+"PNR_Datei.sic")  
            
        else:
            pass
    # Quell und Zieldatei öffnen

        filequelle=open("daten/Arbeitnehmer.txt")
        fileziel=open("daten/PNR_Datei.txt","w", encoding='utf-8')
        fileziel.write("\n")

        #Beschreibung der Felder aus der Quelldatei
        #stelle 1 = Satznummer; stelle 2 = BNR; stelle 3 = Mandantenummer; stelle 4 = MM/JJJJ Abrechnungsmonat, stelle 5 = PNR; 
        #stelle 6 = Name*; stelle 7 = Vorname*; stelle 8 = strasse*; stelle 9 = Hausnummer*; stelle 10 = Ort; stelle 11 = PLZ*;
        #stelle 12 = Eintritt; stelle 13 = Austritt; stelle 14 = NameMandant; stelle 15 = PLZMandant; stelle 16 = OrtMandant;
        #stelle 17 = StrasseMandant; stelle 18 = LandMandant; stelle 19 = Dummy

        for x in filequelle:
            stelle1,stelle2,stelle3,stelle4,stelle5,stelle6,stelle7,stelle8,stelle9,stelle10,stelle11,stelle12,stelle13,stelle14,stelle15,stelle16,stelle17,stelle18,stelle19=x.split(";")
            stelle19 = (stelle19.strip())
            fileziel.write(stelle5+" "+stelle6+", "+stelle7+"\n")

        #Dateien schließen	
        filequelle.close()
        fileziel.close()
  
        #Quelldatei sichern, umbennen mit Zeitstempel
        os.rename("daten/Arbeitnehmer.txt","daten/"+(Datum)+"Arbeitnehmer.sic")
        var_text="Es wurden Personaldaten übernommen."
    else:
        var_text="FEHLER: Es wurden keine Personaldaten aus LODAS übernommen!"
        pass

    return var_text


def lugimport(var_abrmonat, var_abrjahr, var_beraternummer, var_mandantenummer):
    Datum = os.path.join(time.strftime('%Y%m%d_%H%M'))
    if os.path.exists("daten/Arbeitnehmer.txt"):

        if os.path.exists("daten/PNR_Datei.txt"):
            os.rename("daten/PNR_Datei.txt","daten/"+(Datum)+"PNR_Datei.sic")  
        else:
            pass
    # Quell und Zieldatei öffnen

        filequelle=open("daten/Arbeitnehmer.txt")
        fileziel=open("daten/PNR_Datei.txt","w", encoding='utf-8')
        fileziel.write("\n")

        #Beschreibung der Felder aus der Quelldatei
        #stelle 1 = Satznummer; stelle 2 = BNR; stelle 3 = Mandantenummer; stelle 4 = JJJJ/MM Abrechnungsmonat, stelle 5 = PNR*; 
        #stelle 6 = Name, Vorname* ; stelle 7 = PLZ; stelle 8 = Ort; stelle 9 = Strasse, Hausnummer; stelle 10 = Alter; stelle 11 = Geschlecht des 
        #Mitarbeiters lang; stelle 12 = Geburtsdatum;  stelle 13 = Vertragsform; stelle 14 = Eintritt; stelle 15 = Austritt;
        #stelle 16 = Betriebszugehörigkeit; stelle 17 = IBAN der Mitarbeiterbankverbindung;
        #stelle 18 = BIC der Mitarbeiterbankverbindung; stelle 19 = Bankbezeichnung; stelle 20=  Arbeitnehmertyp - lang;
        #stelle 21 = Name des Beschäftigungsbetriebes; stelle 22 = Straße bzw. Postfach; stelle 23 = Postleitzahl;
        #stelle 24 = Ort; stelle 25 = Nationalitätskennzeichen der Mandantenadresse;stelle 26 = Dummy

        for x in filequelle:
            stelle1,stelle2,stelle3,stelle4,stelle5,stelle6,stelle7,stelle8,stelle9,stelle10,stelle11,stelle12,stelle13,stelle14,stelle15,stelle16,stelle17,stelle18,stelle19,stelle20,stelle21,stelle22,stelle23,stelle24,stelle25,stelle26=x.split(";")
            stelle26 = (stelle26.strip())
            fileziel.write(stelle5+" "+stelle6+"\n")

        #Dateien schließen	
        filequelle.close()
        fileziel.close()
  
        #Quelldatei sichern, umbennen mit Zeitstempel
        os.rename("daten/Arbeitnehmer.txt","daten/"+(Datum)+"Arbeitnehmer.sic")
        var_text="Es wurden Personaldaten übernommen."
    else:
        var_text="FEHLER: Es wurden keine Personaldaten aus Lohn und Gehalt übernommen!"
        pass
 
    return var_text