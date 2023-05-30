from unittest import main
import streamlit as st;
import Controllers.ClienteController as ClienteController
import Pages.Cliente.Create as PageCreateCliente

def List():
    paramId = st.experimental_get_query_params()
    if paramId.get("id") == None:
        st.experimental_set_query_params() 
        st.title("Clientes")        
        st.write("")       
        colms = st.columns((1,2,2,3,3,2.5,2))
        campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'E-mail', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.subheader(campo_nome)            
        
        st.write("")       
        for x, item in enumerate(ClienteController.SelecionarTodos()):
            col1, col2, col3, col4, col5, col6, col7 = st.columns((1,2,2,3,3,2.5,2))   
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            col5.write(item.email)
           
            button_space_excluir = col6.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.id))
           
            button_space_alterar = col7.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar'+ str(item.id))

            if on_click_excluir:
                ClienteController.Excluir(item.id)  
                button_space_excluir.button(
                'Excluído', 'btnExcluido'+ str(item.id))

            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.id]
                )
                st.experimental_rerun()
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateCliente.Create()
            

