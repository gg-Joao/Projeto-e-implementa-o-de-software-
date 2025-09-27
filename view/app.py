import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import streamlit as st
from controller.item_controller import ItemController


controller = ItemController()

st.title("📦 Cadastro de Itens")

# Formulário para adicionar item
st.subheader("Adicionar Novo Item")
with st.form("form_item"):
    descricao = st.text_input("Descrição")
    quantidade = st.number_input("Quantidade", min_value=1, step=1)
    submitted = st.form_submit_button("Salvar")

    if submitted:
        if descricao.strip() != "":
            controller.criarItem(descricao, quantidade)
            st.success("Item cadastrado com sucesso!")
        else:
            st.warning("A descrição não pode estar vazia.")

# Listagem de itens
st.subheader("Itens Cadastrados")
itens = controller.obterTodosOsItens()

if itens:
    for item in itens:
        st.write(f"🔹 **ID:** {item.id} | **Descrição:** {item.descricao} | **Quantidade:** {item.quantidade}")
else:
    st.info("Nenhum item cadastrado ainda.")
