import this
from turtle import onclick
import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente


def Create():
    idAlteracao = st.experimental_get_query_params()
    clienteRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        clienteRecuperado = ClienteController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            id=[clienteRecuperado.id]
        )
        st.title("Alterar Cliente")
    else:
        st.title("Incluir Cliente")    

    with st.form(key="include_cliente"):
        listOccupation = ["Selecione", 
                        "Advogado",
                        "Almoxarife", 
                        "Cozinheiro", 
                        "Desenvolvedor", 
                        "Engenharia",
                        "Estudante", 
                        "Fotógrafo",
                        "Gestor",
                        "Médico",
                        "Motorista", 
                        "Músico",
                        "Policial", 
                        "Produção Industrial",
                        "Professor",
                        "Recepcionista",
                        ]
        if clienteRecuperado == None:
            input_name = st.text_input(label="Insira seu nome")
            input_age = st.number_input(label = "Insira sua idade", format="%d", step= 1)
            input_occupation = st.selectbox(label = "Selecione sua profisão", options = listOccupation )
            input_email = st.text_input(label = "Insira seu E-mail")
        else:
            input_name = st.text_input(label="Insira seu nome", value = clienteRecuperado.nome)
            input_age = st.number_input(label = "Insira sua idade", format="%d", step= 1, value = clienteRecuperado.idade) 
            input_occupation = st.selectbox(label = "Selecione sua profisão", options = listOccupation, index= listOccupation.index(clienteRecuperado.profissao))
            input_email = st.text_input(label = "Insira seu E-mail", value = clienteRecuperado.email)
        input_button_submit = st.form_submit_button("Enviar")  

    if input_button_submit:
        if clienteRecuperado == None:        
            ClienteController.Incluir(cliente.Cliente(0, input_name, input_age, input_occupation, input_email))
            st.success("Cliente incluído com sucesso!")  
        else:
            st.experimental_set_query_params()
            ClienteController.Alterar(cliente.Cliente(clienteRecuperado.id, input_name, input_age, input_occupation, input_email))
            st.success("Cliente alterado com sucesso!")    