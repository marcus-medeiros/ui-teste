import streamlit as st
import pandas as pd
import numpy as np
import time

# --- Configuração da Página ---
st.set_page_config(
    page_title="Demonstração de Menus Interativos",
    page_icon="📊",
    layout="wide",
)

# --- Título Principal ---
st.title("Guia Completo de Widgets Interativos no Streamlit - MVM")
st.markdown("""
Esta aplicação demonstra os principais widgets que você pode usar para criar menus,
barras laterais e outras formas de interação com o usuário no Streamlit.
""")

# ==============================================================================
# 1. BARRA LATERAL (SIDEBAR) - O "MENU" PRINCIPAL
# ==============================================================================
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    st.header("Menu de Navegação")
    
    escolha_pagina = st.radio(
        "Escolha uma seção para visualizar:",
        ("Página Inicial", "Seletores de Opções", "Entrada de Dados", "Botões, Ações e Gráficos"),
        key="menu_principal"
    )
    
    st.markdown("---")
    st.markdown("Feito com ❤️ pelo Streamlit.")

# ==============================================================================
# PREPARAÇÃO DOS DADOS PARA OS GRÁFICOS
# ==============================================================================
# Criando um DataFrame de exemplo com o Pandas para usar nos gráficos
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Criando dados para o mapa
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-23.55, -46.63], # Coordenadas próximas a São Paulo
    columns=['lat', 'lon']
)


# ==============================================================================
# LÓGICA DE NAVEGAÇÃO BASEADA NA ESCOLHA DA SIDEBAR
# ==============================================================================

if escolha_pagina == "Página Inicial":
    st.header("Bem-vindo(a) à Página Inicial!")
    st.markdown(
        """
        Use o menu na barra lateral à esquerda para navegar entre as diferentes
        demonstrações de widgets interativos. Cada seção explicará um tipo diferente
        de funcionalidade que você pode usar para criar menus e interagir com seus usuários.
        """
    )
    st.image("https://storage.googleapis.com/streamlit-public-media/animation/share-feat-1.gif")

elif escolha_pagina == "Seletores de Opções":
    st.header("2. Seletores de Opções")
    st.markdown("Esses widgets permitem que o usuário escolha uma ou mais opções de uma lista.")

    st.subheader("Caixa de Seleção (`st.selectbox`)")
    opcao_selectbox = st.selectbox(
        'Qual é a sua linguagem de programação favorita?',
        ('Python', 'JavaScript', 'Rust', 'Go', 'C++')
    )
    st.write('Sua escolha foi:', opcao_selectbox)

    st.subheader("Seleção Múltipla (`st.multiselect`)")
    opcoes_multiselect = st.multiselect(
        'Quais tecnologias você usa no seu dia a dia?',
        ['Streamlit', 'Pandas', 'NumPy', 'Matplotlib', 'Scikit-learn', 'TensorFlow', 'PyTorch'],
        default=['Streamlit', 'Pandas']
    )
    st.write('Você selecionou:', opcoes_multiselect)
    
    st.subheader("Botões de Rádio (`st.radio`)")
    opcao_radio = st.radio(
        "Qual seu nível de experiência com Streamlit?",
        ('Iniciante', 'Intermediário', 'Avançado'),
        horizontal=True
    )
    st.write(f"Seu nível de experiência é: **{opcao_radio}**")

elif escolha_pagina == "Entrada de Dados":
    st.header("3. Widgets de Entrada de Dados")
    st.markdown("Use estes widgets para coletar informações do usuário.")

    st.subheader("Entrada de Texto (`st.text_input`)")
    nome_usuario = st.text_input("Qual é o seu nome?", "Visitante")
    st.write(f"Olá, {nome_usuario}!")

    st.subheader("Entrada Numérica (`st.number_input`)")
    idade = st.number_input("Insira sua idade:", min_value=0, max_value=120, value=25, step=1)
    st.write(f"Você tem {idade} anos.")

    st.subheader("Slider (`st.slider`)")
    nivel_satisfacao = st.slider(
        "Qual o seu nível de satisfação com este guia? (de 1 a 10)",
        min_value=1, max_value=10, value=8
    )
    st.write(f"Nível de satisfação selecionado: {nivel_satisfacao}")
    
# --- Seção de Botões, Ações e Gráficos ---
elif escolha_pagina == "Botões, Ações e Gráficos":
    st.header("4. Botões, Ações e Gráficos")
    st.markdown("Use botões para disparar ações e abas para organizar conteúdo, como gráficos.")

    st.subheader("Abas (`st.tabs`) com Múltiplos Gráficos")
    st.info("As abas são perfeitas para organizar diferentes visualizações de dados.")
    
    # Renomeando as abas para serem mais descritivas
    tab_graficos, tab_acoes, tab_organizadores = st.tabs(["📊 Todos os Gráficos", "🚀 Ações", "🗂️ Organizadores"])

    with tab_graficos:
        st.header("Galeria de Gráficos Nativos do Streamlit")
        st.markdown("Estes são os principais tipos de gráficos que você pode criar diretamente com o Streamlit.")
        
        # 1. Gráfico de Linha
        st.subheader("Gráfico de Linha (`st.line_chart`)")
        st.line_chart(chart_data)
        st.code("st.line_chart(data)")

        # 2. Gráfico de Área
        st.subheader("Gráfico de Área (`st.area_chart`)")
        st.area_chart(chart_data)
        st.code("st.area_chart(data)")

        # 3. Gráfico de Barras
        st.subheader("Gráfico de Barras (`st.bar_chart`)")
        st.bar_chart(chart_data)
        st.code("st.bar_chart(data)")
        
        # 4. Gráfico de Dispersão (usando st.pyplot)
        st.subheader("Gráfico de Dispersão (`st.pyplot`)")
        st.markdown("Para gráficos mais customizados, como o de dispersão, usamos bibliotecas como Matplotlib.")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.scatter(chart_data['a'], chart_data['b'])
        st.pyplot(fig)
        st.code("""
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(data['a'], data['b'])
st.pyplot(fig)
""")
        
        # 5. Mapa
        st.subheader("Mapa (`st.map`)")
        st.markdown("Perfeito para visualizar dados geográficos com latitude e longitude.")
        st.map(map_data)
        st.code("st.map(map_data)")


    with tab_acoes:
        st.header("Disparando Ações")
        
        st.subheader("Botão (`st.button`)")
        if st.button("Clique aqui para ver uma mágica!"):
            st.balloons()
            st.success("Mágica realizada com sucesso!")

        st.subheader("Checkbox (`st.checkbox`)")
        if st.checkbox("Mostrar mensagem secreta"):
            st.warning("Você encontrou a mensagem secreta! ✨")

    with tab_organizadores:
        st.header("Organizando Conteúdo")
        
        st.subheader("Expansor (`st.expander`)")
        with st.expander("Clique aqui para ver mais detalhes"):
            st.write("""
            Esta é uma área de conteúdo que só aparece quando o usuário clica.
            É muito útil para seções de ajuda ou informações secundárias.
            """)
            st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50)

        st.subheader("Colunas (`st.columns`)")
        st.markdown("Divida a tela em colunas para organizar melhor os elementos.")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("Esta é a primeira coluna.")
            st.button("Botão 1")

        with col2:
            st.info("Esta é a segunda coluna.")
            st.button("Botão 2")

        with col3:
            st.info("Esta é a terceira coluna.")
            st.button("Botão 3")