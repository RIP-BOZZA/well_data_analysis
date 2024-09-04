import pandas as pd
import sqlite3


def migrate_data(path) ->None:
    data_frame = pd.read_excel(path)
    annual_data = data_frame.groupby('API WELL  NUMBER').agg({
                "OIL":'sum','GAS':'sum','BRINE':'sum'
                }).reset_index()

    data_base = sqlite3.connect('well_data.db')
    connection = data_base.cursor()
    connection.execute(' CREATE TABLE IF NOT EXISTS well_data ( api_well_number \
                        TEXT PRIMARY KEY,oil INTEGER,gas INTEGER,brine INTEGER)')
    for index,row in annual_data.iterrows():
        connection.execute('INSERT OR REPLACE INTO well_data (api_well_number ,oil ,gas ,brine) \
                           VALUES (?,?,?,?)',(str(row['API WELL  NUMBER']), int(row['OIL']), int(row['GAS']), int(row['BRINE'])))
    data_base.commit()
    data_base.close()
    return "success"


print(migrate_data('./20210309_2020_1 - 4 (1) (1).xls'))
