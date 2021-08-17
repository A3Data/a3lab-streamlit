import streamlit as st
import pandas as pd
from streamlit_obj.st_viz import *

"""
# My first app
## Learning streamlit

Hello **world**!

"""

df = pd.read_csv('../data/diamonds.csv')

# Inputs
col1, col2 = st.columns(2)
cut_options = list(df['cut'].unique())
with col1:
    cut = st.selectbox('Tipo de corte', cut_options, format_func = lambda x: x.lower())
min_price = col2.number_input('Preço mínimo', min_value = 300, max_value=20000)

# Filtro
df_filtered = df.loc[(df['cut'] == cut) & (df['price'] >= min_price), :]

# Tabelas e gráficos
st.dataframe(df_filtered)

st.write('## Operações de Dataframe')
df_agg = df_filtered.groupby(['clarity']).agg({'price':'mean'}).reset_index()
st.dataframe(df_agg)

st.write('## Pyplot Chart')
plot = pyplot_chart(df_filtered, 'carat', 'price', hue='clarity')
st.write(plot)

col3, col4 = st.columns(2)
alt_plot = alt_chart(df_filtered, 'carat', 'price', color='clarity')
with col3:
    st.write('## Altair Chart')
    st.altair_chart(alt_plot)


px_plot = px_chart(df_filtered, 'carat', 'price', color='clarity')
with col4:
    st.write('## Plotly Chart')
    st.plotly_chart(px_plot)

