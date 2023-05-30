import streamlit as st;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd

def List():
    st.title("Clientes")
    costumerList = []

    for item in ClienteController.SelecionarTodos():
        costumerList.append([item.nome, item.idade, item.profissao, item.email])

    df = pd.DataFrame(
        costumerList,
        columns = ['Nome', 'Idade', 'Profissao', 'Email']
    )

    st.table(df)