import streamlit as st
from streamlit_gsheets import GSheetsConnection

# Google Sheet-hez való kapcsolat létrehozása
conn = st.secrets["gsheets"]
gsheets_conn = GSheetsConnection(conn["spreadsheet"], conn)

# A számláló értékének lekérdezése a Google Sheet-ből
def get_counter():
    try:
        df = gsheets_conn.read()
        counter = int(df.iloc[0, 0])
    except Exception as e:
        st.error(f"Hiba történt az adatok lekérésekor: {e}")
        counter = 0
    return counter

# A számláló értékének növelése és frissítése a Google Sheet-ben
def increase_counter(counter):
    try:
        counter += 1
        gsheets_conn.write([[counter]])
    except Exception as e:
        st.error(f"Hiba történt az adatok frissítésekor: {e}")
    return counter

# A számláló értékének lekérdezése és növelése gomb lenyomásakor
counter = get_counter()
if st.button("Lenyomás"):
    counter = increase_counter(counter)

# A számláló értékének megjelenítése
st.write(f"A gombot eddig {counter} alkalommal nyomták le.")
