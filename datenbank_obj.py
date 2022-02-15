
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, MetaData, Table, DATE


def abrechnungsdaten_dbobj(metadata): 
    abrechnungsdaten = Table('abrechnungsdaten', metadata,
    Column('id', Integer, primary_key=True),
    Column('beraternummer', Text),
    Column('mandantennummer', Text),
    Column('PNR', Text),
    Column('lohnart', Text),
    Column('lohnart_text', Text),
    Column('wert', Text),
    Column('kostenstelle', Text),
    Column('kostentraeger', Text),
    Column('artdertaetigkeit', Text),
    Column('freitext', Text),
    Column('abrechnungsmonat', Text),
    Column('abrechnungsjahr', Text),
    Column('agenturprovprozent', Text),
    Column('agenturprovprozent_AN', Text),
    Column('agenturprovwert_AN', Text),
    Column('agenturprovwert_AG', Text),
    Column('lohnartustabzug', Text),
    Column('ustwert',Text),
    Column('kontoust', Text),
    Column('exportlodas', Text),
    Column('exportlohnundgehalt', Text),
    Column('exportwiederholung', Text),
    Column('exportdatum', Text)
    )
    return abrechnungsdaten

def getdbmetadata(engine):

    metadata = MetaData()
    metadata.bind = engine

    return metadata