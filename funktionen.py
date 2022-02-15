import numpy as np
from flask import request


def basis_daten_oeffnen():
    basis_daten = open("daten/basisdaten.txt","r")
    for x in basis_daten:
        var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6,var_99=x.split("|")
        break
    basis_daten.close()
    return var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6


def basis_daten_anlegen():
    basis_daten = open("daten/basisdaten.txt","w")
    var_beraternummer="9999999"
    var_mandantennummer="99999"
    var_3="9999"
    var_4="9999"
    var_5="9999"
    var_6="9999"
    var_99="9999"
    basis_daten.write(var_beraternummer+"|"+var_mandantennummer+"|"+var_3+"|"+var_4+"|"+var_5+"|"+var_6+"|"+var_99)
    basis_daten.close()
    return var_beraternummer,var_mandantennummer,var_3,var_4,var_5,var_6

def abrechnungs_daten_lesen():
    filequelle=open("daten/abrechnungszeitraum.txt","r", encoding='utf-8')
    for x in filequelle:
        var_abrmonat,var_abrjahr=x.split("|")
        break
    filequelle.close()
    return var_abrmonat, var_abrjahr


def lohnarten_dic_lesen(lohnart):
    lohnarten_text = np.load('daten/lohnarten.npy', allow_pickle='TRUE')
    lohnarten_text = dict(lohnarten_text.item())
    lohnarten_text = lohnarten_text.get(lohnart)

    return lohnarten_text
            

def lohnarten_dic_schreiben():
    lohnarten = {}

    lz = 1
    while lz < 14:
        lohnarten["loa_ns"+str(lz)] = request.form['loa_ns'+str(lz)]
        lohnarten[request.form['loa_ns'+str(lz)]] = request.form['loa_ts'+str(lz)]
        controlle = request.form['loa_ns'+str(lz)]+request.form['loa_ts'+str(lz)]
      #  print(controlle)
        lz = lz +1

    lz = 1
    while lz < 9:
        lohnarten["loa_nb"+str(lz)] = request.form['loa_nb'+str(lz)]
        lohnarten[request.form['loa_nb'+str(lz)]] = request.form['loa_tb'+str(lz)]
        controlle = request.form['loa_nb'+str(lz)]+request.form['loa_tb'+str(lz)]
       # print(controlle)
        lz = lz +1
    
    lohnarten["konto_ggagp"] = request.form['konto_ggagp']
    lohnarten[request.form['konto_ggagp']] = request.form['kontotext_ggagp']
    lohnarten["konto_ust7"] = request.form['konto_ust7']
    lohnarten[request.form['konto_ust7']] = request.form['kontotext_ust7']
    lohnarten["konto_ust19"] = request.form['konto_ust19']
    lohnarten[request.form['konto_ust19']] = request.form['kontotext_ust19']
    
    np.save('daten/lohnarten.npy', lohnarten)
 
### Agenturprov berechnen

def agenturprov_berechnen(provbasis):
    # EUROWert auslesen
    if request.form["form_eurovorkommaagp"] == "":
        eurovorkomma = "0"
    else: 
        eurovorkomma = request.form["form_eurovorkommaagp"]
    if request.form["form_euronachkommaagp"] == "":
        euronachkomma = "00"
    elif request.form["form_euronachkommaagp"] == "0":
        euronachkomma = "00"
    elif len(request.form["form_euronachkommaagp"]) == 1:
        euronachkomma = "0"+request.form["form_euronachkommaagp"]
    else:
        euronachkomma = request.form["form_euronachkommaagp"]      

    # Prozentsaz der Provsion auslesen    
    if request.form["form_prozentvorkommaagp"] == "":
        prozentvorkomma = "0"
    else:
        prozentvorkomma = request.form["form_prozentvorkommaagp"]
    if request.form["form_prozentnachkommaagp"] == "":
        prozentnachkomma = "00"
    elif request.form["form_prozentnachkommaagp"] == "0":
        prozentnachkomma = "00"
    elif len(request.form["form_prozentnachkommaagp"]) == 1:
        prozentnachkomma = "0"+request.form["form_prozentnachkommaagp"]
    else:
        prozentnachkomma = request.form["form_prozentnachkommaagp"]

    # Provision AN-Anteil auslesen - Rest ist AG Anteil    
    if request.form['form_anteilprozentvorkommaagp'] == "":
        prozentvkAN = "0"
    else:
        prozentvkAN = request.form['form_anteilprozentvorkommaagp']

    if request.form["form_anteilprozentnachkommaagp"] == "":
        prozentnkAN = "00"
    elif request.form["form_anteilprozentnachkommaagp"] == "0":
        prozentnkAN= "00"
    elif len(request.form["form_anteilprozentnachkommaagp"]) == 1:
        prozentnkAN = "0"+request.form["form_anteilprozentnachkommaagp"]
    else:
        prozentnkAN = request.form["form_anteilprozentnachkommaagp"]

    eurowertagp = int(eurovorkomma+euronachkomma)
    eurowertagp = eurowertagp/100
#    print("Das ist der AGP Wert der erfasst wurde: "+str(eurowertagp))

    prozentagp = int(prozentvorkomma+prozentnachkomma)
    prozentagp = prozentagp/100
#    print("Das ist der AGP %Satz: "+str(prozentagp))
    
    prozentAN = int(prozentvkAN+prozentnkAN)
    prozentAN = prozentAN/100   
#    print("Das ist die AG% AN Anteil: "+str(prozentAN))
    
    provbasis=int(provbasis)
#    print("Das ist die AGP Basis: "+str(provbasis))

    agenturprov = provbasis*prozentagp/100
    agenturprov = agenturprov+eurowertagp
    agenturprov = round (agenturprov, 2)
#    print("Das ist die AGP Provison in Summe: "+str(agenturprov))

    agenturprov_AN = agenturprov*prozentAN/100
    agenturprov_AN = round (agenturprov_AN, 2)
#    print("Das ist die AGProvision AN Anteil: "+str(agenturprov_AN))

    agenturprov_AG = agenturprov-agenturprov_AN
    agenturprov_AG = round (agenturprov_AG, 2)
#    print("Das ist die AGProvision AG Anteil: "+str(agenturprov_AG))

    agenturprov_AN = agenturprov_AN*(-1)
    agenturprov_AG = agenturprov_AG*(-1)
    agenturprov = agenturprov*(-1)

    return agenturprov_AN, agenturprov_AG, prozentagp, prozentAN

def umsatzsteuer_berechnen(provbasis, ust):
    if request.form['form_steuer'] == "19":
        ust_Wert = int(provbasis)*int(ust)/100*(-1)
        ust_Wert = round (ust_Wert, 2)
        ust_Lohnart = lohnarten_dic_lesen("loa_nb8")
        ust_Konto = lohnarten_dic_lesen("konto_ust19")
    elif request.form['form_steuer'] == "7":
        ust_Wert = int(provbasis)*int(ust)/100*(-1)
        ust_Wert = round (ust_Wert, 2)
        ust_Lohnart = lohnarten_dic_lesen("loa_nb7")
        ust_Konto = lohnarten_dic_lesen("konto_ust7")
    else:
        ust_Wert = "0"
        ust_Lohnart = "0"
        ust_Konto = "0"
    return ust_Wert, ust_Lohnart, ust_Konto
