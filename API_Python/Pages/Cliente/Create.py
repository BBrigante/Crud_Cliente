import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente


st.title("Incluir Cliente")

def Create():
    with st.form(key="include_cliente"):
        input_name = st.text_input(label="Insira seu nome")
        input_age = st.number_input(label = "Insira sua idade", format="%d", step= 1)
        input_occupation = st.selectbox("Selecione sua profisão", ["Desenvolvedor", "Médico", "Professor", "Advogado", "Policial", "Estudante"])
        input_email = st.text_input(label = "Insira seu E-mail")
        input_button_submit = st.form_submit_button("Enviar")  
        
    if input_button_submit:

        ClienteController.Incluir(cliente.Cliente(0, input_name, input_age, input_occupation, input_email))
        st.success("Cadastro realizado com sucesso!")  