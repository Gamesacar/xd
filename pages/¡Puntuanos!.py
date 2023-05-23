import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials
import gspread
st.sidebar.header("GOTY 💀💀💀")

def review_input():

    st.title("Ingresa tu review")
    #base_datos=pd.read_csv(url)
    # Recopilar la información de la review
    user = st.text_input("Usuario")
    calificacion = st.slider("Calificación (de 1 a 5)", 1, 5)
    review = st.text_area("Comentario")

    # Guardar la review en una variable de sesión
    if "reviews" in st.session_state:
        reviews = st.session_state.reviews
    if st.button("Enviar"):
        reviews={"user": user, "calificacion": calificacion, "review": review}
        st.experimental_set_query_params(**reviews)
        scope=['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]
        credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",scope)

        # Autenticar y abrir la hoja de cálculo de Google Sheets
        gc = gspread.authorize(credentials)
        # sheet=gc.create("prueba")
        # sheet.share('sajoht14@gmail.com',perm_type='user',role='writer')
        
        
        sheet = gc.open('prueba').sheet1

        # Agregar la review a la hoja de cálculo
        sheet.append_row([user, calificacion,review])

        # Mensaje de éxito
        st.success("Gracias por tu review")
        
if __name__ == '__main__':
    review_input()
