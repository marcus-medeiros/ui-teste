import streamlit as st
import time

# --- Configuração da Página ---
# É uma boa prática configurar o título da página e o ícone no início do script.
st.set_page_config(
    page_title="Demonstração de Menus Interativos",
    page_icon="👇",
    layout="wide",
)

# --- Título Principal ---
st.title("Guia Completo de Widgets Interativos no Streamlit")
st.markdown("""
Esta aplicação demonstra os principais widgets que você pode usar para criar menus,
barras laterais e outras formas de interação com o usuário no Streamlit.
""")

# ==============================================================================
# 1. BARRA LATERAL (SIDEBAR) - O "MENU" PRINCIPAL
# ==============================================================================

st.header("1. A Barra Lateral (`st.sidebar`)")
st.info(
    """
    A barra lateral é o local mais comum para colocar a navegação principal da sua aplicação.
    Qualquer elemento do Streamlit pode ser adicionado à sidebar usando `st.sidebar.*`.
    """
)

# Adicionando um menu de rádio na barra lateral para navegação
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    st.header("Menu de Navegação")
    
    escolha_pagina = st.radio(
        "Escolha uma seção para visualizar:",
        ("Página Inicial", "Seletores de Opções", "Entrada de Dados", "Botões e Ações"),
        key="menu_principal"
    )
    
    st.markdown("---")
    st.markdown("Feito com ❤️ pelo Streamlit.")

# ==============================================================================
# LÓGICA DE NAVEGAÇÃO BASEADA NA ESCOLHA DA SIDEBAR
# ==============================================================================

# O restante do seu app será renderizado com base na escolha feita na sidebar.
# Isso cria uma experiência de "múltiplas páginas" em um único script.

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


# --- Seção de Seletores de Opções ---
elif escolha_pagina == "Seletores de Opções":
    st.header("2. Seletores de Opções")
    st.markdown("Esses widgets permitem que o usuário escolha uma ou mais opções de uma lista.")

    st.subheader("Caixa de Seleção (`st.selectbox`)")
    st.markdown("Ideal para quando o usuário deve escolher **apenas uma opção** de uma lista suspensa.")
    
    opcao_selectbox = st.selectbox(
        'Qual é a sua linguagem de programação favorita?',
        ('Python', 'JavaScript', 'Rust', 'Go', 'C++')
    )
    st.write('Sua escolha foi:', opcao_selectbox)
    st.code("opcao = st.selectbox('Qual é a sua linguagem favorita?', ('Python', 'JavaScript'))")

    st.markdown("---")

    st.subheader("Seleção Múltipla (`st.multiselect`)")
    st.markdown("Permite que o usuário escolha **várias opções** de uma lista.")
    
    opcoes_multiselect = st.multiselect(
        'Quais tecnologias você usa no seu dia a dia?',
        ['Streamlit', 'Pandas', 'NumPy', 'Matplotlib', 'Scikit-learn', 'TensorFlow', 'PyTorch'],
        default=['Streamlit', 'Pandas']  # Opções pré-selecionadas
    )
    st.write('Você selecionou:', opcoes_multiselect)
    st.code("opcoes = st.multiselect('Quais tecnologias você usa?', ['Streamlit', 'Pandas'], default=['Streamlit'])")

    st.markdown("---")

    st.subheader("Botões de Rádio (`st.radio`)")
    st.markdown("Similar ao selectbox, mas exibe todas as opções de uma vez. Bom para listas curtas.")
    
    opcao_radio = st.radio(
        "Qual seu nível de experiência com Streamlit?",
        ('Iniciante', 'Intermediário', 'Avançado'),
        horizontal=True  # Opção para exibir na horizontal
    )
    st.write(f"Seu nível de experiência é: **{opcao_radio}**")
    st.code("opcao = st.radio('Qual seu nível?', ('Iniciante', 'Intermediário'), horizontal=True)")


# --- Seção de Entrada de Dados ---
elif escolha_pagina == "Entrada de Dados":
    st.header("3. Widgets de Entrada de Dados")
    st.markdown("Use estes widgets para coletar informações do usuário.")

    st.subheader("Entrada de Texto (`st.text_input`)")
    nome_usuario = st.text_input("Qual é o seu nome?", "Visitante")
    st.write(f"Olá, {nome_usuario}!")
    st.code("nome = st.text_input('Qual é o seu nome?', 'Visitante')")

    st.markdown("---")

    st.subheader("Entrada Numérica (`st.number_input`)")
    idade = st.number_input("Insira sua idade:", min_value=0, max_value=120, value=25, step=1)
    st.write(f"Você tem {idade} anos.")
    st.code("idade = st.number_input('Insira sua idade:', min_value=0, value=25)")

    st.markdown("---")

    st.subheader("Slider (`st.slider`)")
    st.markdown("Para selecionar um valor dentro de um intervalo.")
    
    nivel_satisfacao = st.slider(
        "Qual o seu nível de satisfação com este guia? (de 1 a 10)",
        min_value=1,
        max_value=10,
        value=8,
        help="1 = Nada Satisfeito, 10 = Totalmente Satisfeito"
    )
    st.write(f"Nível de satisfação selecionado: {nivel_satisfacao}")
    st.code("nivel = st.slider('Qual seu nível de satisfação?', 1, 10, 8)")
    
# --- Seção de Botões e Ações ---
elif escolha_pagina == "Botões e Ações":
    st.header("4. Botões e Ações")
    st.markdown("Use botões para disparar ações ou eventos na sua aplicação.")

    st.subheader("Botão (`st.button`)")
    st.markdown("Executa uma ação quando clicado. O código dentro do `if` só roda após o clique.")

    if st.button("Clique aqui para ver uma mágica!"):
        st.balloons()
        st.success("Mágica realizada com sucesso!")
    st.code("""
if st.button('Clique aqui'):
    st.balloons()
""")

    st.markdown("---")

    st.subheader("Checkbox (`st.checkbox`)")
    st.markdown("Use para ligar ou desligar uma opção. O estado (marcado/desmarcado) é mantido.")
    
    if st.checkbox("Mostrar código-fonte desta seção"):
        st.code("""
if st.checkbox("Mostrar código-fonte"):
    st.code("...")
""")

    st.markdown("---")
    
    st.subheader("Abas (`st.tabs`)")
    st.markdown("Uma forma moderna de organizar conteúdo em seções, sem recarregar a página.")
    
    tab1, tab2, tab3 = st.tabs(["📈 Gráfico", "🗃️ Dados", "🖼️ Imagem"])

    with tab1:
        st.header("Um gráfico de exemplo")
        st.line_chart([10, 20, 15, 25, 30, 20, 40])

    with tab2:
        st.header("Uma tabela de dados")
        st.dataframe({
            'Coluna A': [1, 2, 3, 4],
            'Coluna B': [10, 20, 30, 40]
        })

    with tab3:
        st.header("Uma imagem aleatória")
        st.image("https://picsum.photos/400/300", caption="Imagem gerada aleatoriamente")
        
    st.code("""
tab1, tab2 = st.tabs(["Gráfico", "Dados"])

with tab1:
    st.line_chart(...)

with tab2:
    st.dataframe(...)
""")

    st.markdown("---")
    st.subheader("Expansor (`st.expander`)")
    st.markdown("Use para ocultar conteúdo que não precisa ser visto o tempo todo.")

    with st.expander("Clique aqui para ver mais detalhes"):
        st.write("""
        Esta é uma área de conteúdo que só aparece quando o usuário clica no expansor.
        É muito útil para tutoriais, seções de ajuda ou informações secundárias que podem
        poluir a interface se estiverem sempre visíveis.
        """)
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50)

    st.code("""
with st.expander("Clique para ver mais"):
    st.write("Conteúdo oculto...")
""")