import streamlit as st
import pandas as pd

# Dados de exemplo (substitua pelos seus dados reais)
dados_pedidos = {
    'Cliente': ['Cliente1', 'Cliente2', 'Cliente3'],
    'Pedido': ['Mesa de Jantar', 'Guarda-roupa', 'Cama'],
    'Status': ['Em andamento', 'Concluído', 'Em andamento']
}

dados_evolucao = {
    'Pedido': ['Mesa de Jantar', 'Guarda-roupa', 'Cama'],
    'Progresso': [30, 100, 50]
}

df_pedidos = pd.DataFrame(dados_pedidos)
df_evolucao = pd.DataFrame(dados_evolucao)

# Página principal para exibir a lista de pedidos
st.title('Acompanhamento de Pedidos de Marcenaria')

# Sidebar para seleção de cliente
cliente_selecionado = st.sidebar.selectbox('Selecione um Cliente:', df_pedidos['Cliente'].unique())

# Filtra os pedidos do cliente selecionado
pedidos_cliente = df_pedidos[df_pedidos['Cliente'] == cliente_selecionado]

# Exibe a tabela de pedidos do cliente
st.subheader(f'Pedidos de {cliente_selecionado}:')
st.table(pedidos_cliente)

# Página para analisar a evolução do pedido
st.title('Análise de Evolução do Pedido')

# Sidebar para seleção de pedido
pedido_selecionado = st.sidebar.selectbox('Selecione um Pedido:', pedidos_cliente['Pedido'])

# Filtra a evolução do pedido selecionado
evolucao_pedido = df_evolucao[df_evolucao['Pedido'] == pedido_selecionado]

# Exibe o gráfico de evolução do pedido
st.subheader(f'Evolução do Pedido: {pedido_selecionado}')
st.bar_chart(evolucao_pedido.set_index('Pedido'))

# Você pode adicionar mais funcionalidades, gráficos e interatividade conforme necessário.
