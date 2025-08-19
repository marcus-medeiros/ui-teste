import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import pydeck as pdk

# =======================================================================
# CONFIGURAÇÃO DA PÁGINA
# st.set_page_config() deve ser o primeiro comando Streamlit no script.
# =======================================================================
st.set_page_config(
    page_title="Guia Completo Streamlit",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =======================================================================
# DADOS DE EXEMPLO (PARA GRÁFICOS, TABELAS E MAPAS)
# =======================================================================
@st.cache_data
def carregar_dados():
    # Dados para gráficos
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    # Dados para mapas
    map_data = pd.DataFrame(
        np.random.randn(200, 2) / [30, 30] + [-23.55, -46.63], # Coordenadas próximas a São Paulo
        columns=['lat', 'lon']
    )
    map_data['tooltip'] = [f"Ponto {i}" for i in range(len(map_data))]
    map_data['magnitude'] = np.random.randint(1, 100, size=len(map_data))
    
    return chart_data, map_data

chart_data, map_data = carregar_dados()


# =======================================================================
# BARRA LATERAL (SIDEBAR) PARA NAVEGAÇÃO
# =======================================================================
with st.sidebar:
    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)
    st.header("Guia Completo Streamlit")
    
    escolha_pagina = st.radio(
        "Navegue pelas seções:",
        [
            "Página Inicial",
            "Elementos de Texto",
            "Exibição de Dados",
            "Gráficos",
            "Mapas",
            "Widgets Interativos (Inputs)",
            "Layout e Contêineres",
            "Mídia",
            "Status e Progresso",
            "Otimização e Estado"
        ]
    )
    st.markdown("---")
    st.info("Esta é uma demonstração de todas as principais funcionalidades do Streamlit.")

# =======================================================================
# CONTEÚDO DAS PÁGINAS
# =======================================================================

# -----------------------------------------------------------------------
# PÁGINA INICIAL
# -----------------------------------------------------------------------
if escolha_pagina == "Página Inicial":
    st.title("📚 Bem-vindo ao Guia Completo do Streamlit")
    st.markdown("""
    Esta aplicação é um manual interativo que demonstra todas as principais funcionalidades
    da biblioteca Streamlit. Use o menu na barra lateral à esquerda para navegar pelas
    diferentes categorias de comandos.

    ### O que você encontrará aqui:
    - **Exemplos práticos** de cada função.
    - **Código-fonte** para cada exemplo, pronto para copiar e colar.
    - **Dicas** sobre quando usar cada componente.

    Vamos começar! Escolha uma seção no menu para explorar.
    """)

# -----------------------------------------------------------------------
# ELEMENTOS DE TEXTO
# -----------------------------------------------------------------------
elif escolha_pagina == "Elementos de Texto":
    st.header("🔡 Elementos de Texto")
    st.markdown("Use estes comandos para exibir texto de forma estruturada.")

    st.subheader("`st.title` e `st.header`")
    st.title("Este é um título (st.title)")
    st.header("Este é um cabeçalho (st.header)")
    st.subheader("Este é um subcabeçalho (st.subheader)")
    st.code("""
st.title("Este é um título")
st.header("Este é um cabeçalho")
st.subheader("Este é um subcabeçalho")
    """)
    st.divider()

    st.subheader("`st.markdown`, `st.text` e `st.write`")
    st.markdown("O **Markdown** permite formatação: *itálico*, `código`, [links](https://streamlit.io), etc.")
    st.text("st.text exibe texto em fonte monoespaçada, sem formatação.")
    st.write("st.write é um comando 'mágico' que renderiza quase tudo!")
    st.write({"chave": "valor", "lista": [1, 2, 3]})
    st.code("""
st.markdown("O **Markdown** permite formatação.")
st.text("st.text exibe texto em fonte monoespaçada.")
st.write("st.write renderiza quase tudo!")
    """)
    st.divider()

    st.subheader("`st.code` e `st.latex`")
    st.code("import streamlit as st\nst.write('Olá, Mundo!')", language="python")
    st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
        \sum_{k=0}^{n-1} ar^k =
        a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
    st.code(r"""
st.code('st.write("Olá, Mundo!")', language='python')
st.latex(r'a + ar + a r^2 = \sum_{k=0}^{2} ar^k')
    """)

# -----------------------------------------------------------------------
# EXIBIÇÃO DE DADOS
# -----------------------------------------------------------------------
elif escolha_pagina == "Exibição de Dados":
    st.header("📊 Exibição de Dados")

    st.subheader("`st.dataframe`")
    st.markdown("Exibe um DataFrame interativo (ordenável, redimensionável).")
    st.dataframe(chart_data)
    st.code("st.dataframe(meu_dataframe)")
    st.divider()

    st.subheader("`st.table`")
    st.markdown("Exibe uma tabela estática.")
    st.table(chart_data.head())
    st.code("st.table(meu_dataframe.head())")
    st.divider()

    st.subheader("`st.metric`")
    st.markdown("Exibe uma métrica em destaque, ideal para dashboards.")
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperatura", "25 °C", "1.2 °C")
    col2.metric("Umidade", "76%", "-8%")
    col3.metric("Vendas (Mês)", "R$ 150.3k", "12%", delta_color="inverse")
    st.code("""
col1, col2, col3 = st.columns(3)
col1.metric("Temperatura", "25 °C", "1.2 °C")
col2.metric("Umidade", "76%", "-8%")
col3.metric("Vendas (Mês)", "R$ 150.3k", "12%", delta_color="inverse")
    """)
    st.divider()

    st.subheader("`st.json`")
    st.markdown("Exibe um objeto JSON.")
    st.json({'nome': 'Streamlit', 'versao': '1.30.0', 'ativo': True})
    st.code("st.json({'nome': 'Streamlit', 'ativo': True})")


# -----------------------------------------------------------------------
# GRÁFICOS
# -----------------------------------------------------------------------
elif escolha_pagina == "Gráficos":
    st.header("📈 Gráficos")

    st.subheader("`st.line_chart`")
    st.line_chart(chart_data)
    st.code("st.line_chart(dados)")
    st.divider()

    st.subheader("`st.area_chart`")
    st.area_chart(chart_data)
    st.code("st.area_chart(dados)")
    st.divider()
    
    st.subheader("`st.bar_chart`")
    st.bar_chart(chart_data)
    st.code("st.bar_chart(dados)")
    st.divider()

    st.subheader("`st.pyplot` (com Matplotlib)")
    st.markdown("Use para qualquer gráfico de bibliotecas como Matplotlib ou Seaborn.")
    fig, ax = plt.subplots()
    ax.hist(chart_data['a'], bins=10)
    ax.set_title("Histograma com Matplotlib")
    st.pyplot(fig)
    st.code("""
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.hist(dados['a'], bins=10)
st.pyplot(fig)
    """)
    st.divider()
    
    st.subheader("`st.plotly_chart`")
    st.markdown("Para gráficos interativos do Plotly.")
    try:
        import plotly.express as px
        fig_plotly = px.scatter(chart_data, x='a', y='b', color='c', title="Gráfico de Dispersão com Plotly")
        st.plotly_chart(fig_plotly, use_container_width=True)
    except ImportError:
        st.warning("A biblioteca Plotly não está instalada. Execute: pip install plotly")
    st.code("""
import plotly.express as px
fig = px.scatter(dados, x='a', y='b')
st.plotly_chart(fig)
    """)
    
# -----------------------------------------------------------------------
# MAPAS
# -----------------------------------------------------------------------
elif escolha_pagina == "Mapas":
    st.header("🗺️ Mapas")
    
    st.subheader("`st.map`")
    st.markdown("A forma mais simples de colocar pontos em um mapa.")
    st.map(map_data, zoom=10)
    st.code("st.map(map_data, zoom=10)")
    st.divider()
    
    st.subheader("`st.pydeck_chart`")
    st.markdown("Para mapas complexos, com camadas e alta performance.")
    
    # Definindo a visualização inicial do mapa
    view_state = pdk.ViewState(
        latitude=-23.55,
        longitude=-46.63,
        zoom=10,
        pitch=50  # Ângulo de inclinação para visualização 3D
    )
    
    # Camada de pontos
    layer = pdk.Layer(
        'ScatterplotLayer',
        data=map_data,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius='magnitude * 100',
        pickable=True
    )
    
    # Tooltip
    tooltip = {
        "html": "<b>{tooltip}</b> <br/> Magnitude: {magnitude} <br/> Posição: [{lon}, {lat}]",
        "style": {"backgroundColor": "steelblue", "color": "white"}
    }
    
    # Renderizando o mapa
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style='mapbox://styles/mapbox/light-v9',
        tooltip=tooltip
    )
    st.pydeck_chart(r)
    
    st.info("Passe o mouse sobre os pontos para ver o tooltip interativo!")
    st.code("""
import pydeck as pdk
# ... (configuração da camada e view_state)
r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip)
st.pydeck_chart(r)
    """)

# -----------------------------------------------------------------------
# WIDGETS INTERATIVOS
# -----------------------------------------------------------------------
elif escolha_pagina == "Widgets Interativos (Inputs)":
    st.header("👆 Widgets Interativos (Inputs)")

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Seleção")
        st.checkbox("Marque-me")
        st.radio("Escolha uma opção", ["A", "B", "C"])
        st.selectbox("Selecione um item", ["Maçã", "Laranja", "Banana"])
        st.multiselect("Selecione múltiplos itens", ["Python", "Streamlit", "Pandas"], default=["Streamlit"])

    with col2:
        st.subheader("Entrada de Dados")
        st.text_input("Seu nome", placeholder="Digite aqui...")
        st.number_input("Sua idade", min_value=0, max_value=120, value=25)
        st.date_input("Data de nascimento")
        st.color_picker("Escolha uma cor", "#00f900")
    
    st.divider()
    
    st.subheader("Sliders e Botões")
    st.slider("Nível de satisfação", 1, 10, 8)
    st.select_slider("Selecione uma faixa", options=['Baixo', 'Médio', 'Alto'])
    
    if st.button("Clique em mim"):
        st.success("Botão clicado!")
        
    st.download_button(
        label="Baixar dados de exemplo",
        data=chart_data.to_csv(index=False).encode('utf-8'),
        file_name='dados_exemplo.csv',
        mime='text/csv',
    )
    
    st.divider()

    st.subheader("Inputs de Arquivo e Câmera")
    st.file_uploader("Envie um arquivo")
    st.camera_input("Tire uma foto")

    st.divider()

    st.subheader("`st.form`")
    st.markdown("Agrupe widgets em um formulário para submeter todos de uma vez.")
    with st.form("meu_formulario"):
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        marcado = st.checkbox("Aceito os termos")
        
        # O botão de submissão do formulário
        submitted = st.form_submit_button("Enviar")
        if submitted:
            st.write("Formulário enviado:", "Nome:", nome, "Email:", email, "Aceito:", marcado)

# -----------------------------------------------------------------------
# LAYOUT E CONTÊINERES
# -----------------------------------------------------------------------
elif escolha_pagina == "Layout e Contêineres":
    st.header("🏗️ Layout e Contêineres")

    st.subheader("`st.columns`")
    st.markdown("Cria colunas para organizar o conteúdo lado a lado.")
    col1, col2, col3 = st.columns([2, 1, 1]) # Proporções 2:1:1
    with col1:
        st.info("Esta é a coluna 1 (mais larga).")
    with col2:
        st.info("Coluna 2.")
    with col3:
        st.info("Coluna 3.")
    st.code("""
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.info("Coluna larga.")
    """)
    st.divider()

    st.subheader("`st.tabs`")
    st.markdown("Cria abas para separar conteúdos.")
    tab1, tab2 = st.tabs(["Gráfico", "Tabela"])
    with tab1:
        st.line_chart(chart_data)
    with tab2:
        st.dataframe(chart_data)
    st.code("""
tab1, tab2 = st.tabs(["Aba 1", "Aba 2"])
with tab1:
    st.write("Conteúdo da Aba 1")
    """)
    st.divider()

    st.subheader("`st.expander`")
    st.markdown("Oculta conteúdo em uma seção expansível.")
    with st.expander("Clique para ver mais detalhes"):
        st.write("Este conteúdo estava oculto! É ótimo para informações adicionais.")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    st.code("""
with st.expander("Clique para ver"):
    st.write("Conteúdo oculto...")
    """)
    st.divider()

    st.subheader("`st.container` e `st.empty`")
    st.markdown("`st.container` cria um bloco para agrupar elementos. `st.empty` cria um espaço reservado que pode ser preenchido ou alterado depois.")
    with st.container():
        st.write("Este é um contêiner.")
        st.bar_chart(np.random.randn(50, 3))

    placeholder = st.empty()
    if st.button("Preencher o espaço vazio"):
        placeholder.success("O espaço vazio foi preenchido com esta mensagem!")
    st.code("""
placeholder = st.empty()
if st.button("Preencher"):
    placeholder.success("Pronto!")
    """)

# -----------------------------------------------------------------------
# MÍDIA
# -----------------------------------------------------------------------
elif escolha_pagina == "Mídia":
    st.header("🖼️ Mídia")

    st.subheader("`st.image`")
    st.image("https://storage.googleapis.com/streamlit-public-media/gallery/cat.jpg",
             caption="Um gato fofo. Imagem de exemplo do Streamlit.", width=300)
    st.code("st.image(url, caption='Legenda', width=300)")
    st.divider()

    st.subheader("`st.audio`")
    st.audio("https://storage.googleapis.com/streamlit-public-media/gallery/B_T_V_2020-09-08.mp3")
    st.code("st.audio(url_do_audio)")
    st.divider()
    
    st.subheader("`st.video`")
    st.video("https://storage.googleapis.com/streamlit-public-media/gallery/cat-rolling.mp4")
    st.code("st.video(url_do_video)")
    
# -----------------------------------------------------------------------
# STATUS E PROGRESSO
# -----------------------------------------------------------------------
elif escolha_pagina == "Status e Progresso":
    st.header("⏳ Status e Progresso")

    st.subheader("Barras de Progresso e Spinners")
    if st.button("Iniciar processo demorado"):
        st.toast("Começando!")
        progress_bar = st.progress(0, text="Aguarde...")
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1, text=f"Processando item {i+1}...")
        progress_bar.empty()
        st.success("Processo concluído!")

    with st.spinner('Esperando por algo...'):
        time.sleep(2)
    st.write("Algo aconteceu!")
    
    with st.status("Detalhes do processo...", expanded=True) as status:
        st.write("Procurando por arquivos...")
        time.sleep(1)
        st.write("Encontrado 10 arquivos.")
        time.sleep(1)
        st.write("Processo finalizado.")
        status.update(label="Download completo!", state="complete")

    st.subheader("Mensagens de Alerta")
    st.success("Esta é uma mensagem de sucesso.")
    st.info("Esta é uma mensagem informativa.")
    st.warning("Esta é uma mensagem de aviso.")
    st.error("Esta é uma mensagem de erro.")
    
    try:
        x = 1 / 0
    except Exception as e:
        st.exception(e)
        
    st.subheader("Animações divertidas")
    col1, col2 = st.columns(2)
    if col1.button("Mostrar balões 🎈"):
        st.balloons()
    if col2.button("Mostrar neve ❄️"):
        st.snow()

# -----------------------------------------------------------------------
# OTIMIZAÇÃO E ESTADO
# -----------------------------------------------------------------------
elif escolha_pagina == "Otimização e Estado":
    st.header("⚡ Otimização e Gerenciamento de Estado")

    st.subheader("`st.cache_data` e `st.cache_resource`")
    st.markdown("""
    - `st.cache_data`: Usado para armazenar em cache resultados de funções que retornam dados (DataFrames, JSON, etc.). O Streamlit verifica os parâmetros da função e o conteúdo do corpo da função para decidir se re-executa.
    - `st.cache_resource`: Usado para armazenar em cache recursos globais que não devem ser recriados a cada execução (conexões com banco de dados, modelos de ML).
    """)
    st.code("""
@st.cache_data
def carregar_dataframe(url):
    # Código para carregar dados
    return df

@st.cache_resource
def carregar_modelo_ml():
    # Código para carregar um modelo pesado
    return modelo
    """)
    st.info("Já estamos usando `@st.cache_data` na função `carregar_dados()` no topo deste script!")

    st.divider()

    st.subheader("`st.session_state`")
    st.markdown("Um objeto tipo dicionário para armazenar o estado da sessão entre as interações do usuário.")

    # Inicializa o contador no estado da sessão se ele não existir
    if 'contador' not in st.session_state:
        st.session_state.contador = 0

    st.write("Valor atual do contador:", st.session_state.contador)
    
    col1, col2 = st.columns(2)
    if col1.button("Incrementar +1"):
        st.session_state.contador += 1
        st.rerun() # Opcional, força o rerrodar imediato

    if col2.button("Resetar contador"):
        st.session_state.contador = 0
        st.rerun()
    
    st.code("""
if 'contador' not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar"):
    st.session_state.contador += 1
    """)