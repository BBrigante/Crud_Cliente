from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
import Controllers.ClienteController as ClienteController
import pandas as pd
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente

st.sidebar.title('menu')

Page_cliente = st.sidebar.selectbox('Cliente', ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

if Page_cliente == 'Consultar':
    PageListCliente.List()

if Page_cliente == 'Incluir':
    PageCreateCliente.Create()
    

