import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ─── Configuración de la página ───────────────────────────────────────────────
st.set_page_config(
    page_title='Análisis Bioclimático — Mérida',
    page_icon='🌤️',
    layout='wide'
)

st.title('🌤️ Análisis exploratorio de datos climatológicos')
st.markdown('**Mérida, Yucatán** · Datos TMYx — Climate.OneBuilding.org')
st.divider()

# ─── Carga de datos ───────────────────────────────────────────────────────────
@st.cache_data
def cargar_datos_default():
    return pd.read_csv('merida_clima.csv')

@st.cache_data
def cargar_datos_usuario(archivo):
    return pd.read_csv(archivo)

st.subheader('📂 Fuente de datos')
opcion = st.radio(
    'Selecciona el archivo a analizar:',
    options=['Archivo por defecto (Mérida, Yucatán)', 'Cargar mi propio archivo CSV'],
    horizontal=True
)

if opcion == 'Archivo por defecto (Mérida, Yucatán)':
    df = cargar_datos_default()
    st.success('Usando datos de Mérida, Yucatán — TMYx (Climate.OneBuilding.org)')
else:
    archivo = st.file_uploader(
        'Sube tu archivo CSV (debe tener el mismo formato que merida_clima.csv)',
        type='csv'
    )
    if archivo is not None:
        df = cargar_datos_usuario(archivo)
        st.success(f'Archivo cargado: **{archivo.name}** — {len(df):,} filas')
    else:
        st.warning('Sube un archivo CSV para continuar.')
        st.stop()

st.divider()

nombres_meses = {
    1: 'Ene', 2: 'Feb', 3: 'Mar', 4: 'Abr',
    5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Ago',
    9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dic'
}
df['mes_nombre'] = df['mes'].map(nombres_meses)

# ─── SECCIÓN 1: TEMPERATURA ───────────────────────────────────────────────────
st.header('🌡️ Temperatura')

# Temperatura de confort adaptativo ASHRAE 55
# Tn = 0.31 × T_media_mensual + 17.8
df_temp_mes = (
    df.groupby('mes')['temp_bulbo_seco']
    .mean()
    .reset_index()
    .rename(columns={'temp_bulbo_seco': 'temp_media'})
)
df_temp_mes['mes_nombre'] = df_temp_mes['mes'].map(nombres_meses)
df_temp_mes['T_confort'] = 0.31 * df_temp_mes['temp_media'] + 17.8
df_temp_mes['T_confort_sup'] = df_temp_mes['T_confort'] + 3.5
df_temp_mes['T_confort_inf'] = df_temp_mes['T_confort'] - 3.5

fig_temp = go.Figure()

# Box plots por mes
for mes_num in sorted(df['mes'].unique()):
    datos_mes = df[df['mes'] == mes_num]['temp_bulbo_seco']
    fig_temp.add_trace(go.Box(
        y=datos_mes,
        name=nombres_meses[mes_num],
        marker_color='#E07B54',
        showlegend=False
    ))

# Banda de confort (área sombreada)
fig_temp.add_trace(go.Scatter(
    x=df_temp_mes['mes_nombre'].tolist() + df_temp_mes['mes_nombre'].tolist()[::-1],
    y=df_temp_mes['T_confort_sup'].tolist() + df_temp_mes['T_confort_inf'].tolist()[::-1],
    fill='toself',
    fillcolor='rgba(100, 200, 150, 0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    name='Zona de confort (±3.5°C)',
    hoverinfo='skip'
))

# Línea de temperatura de confort
fig_temp.add_trace(go.Scatter(
    x=df_temp_mes['mes_nombre'],
    y=df_temp_mes['T_confort'],
    mode='lines+markers',
    name='T° confort (ASHRAE 55)',
    line=dict(color='#2ECC71', width=2, dash='dash'),
    marker=dict(size=6)
))

fig_temp.update_layout(
    title='Distribución de temperatura por mes y zona de confort adaptativo',
    xaxis_title='Mes',
    yaxis_title='Temperatura (°C)',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    height=500
)

st.plotly_chart(fig_temp, use_container_width=True)
st.caption('Zona de confort calculada con el modelo adaptativo ASHRAE 55: Tn = 0.31 × T_media_mensual + 17.8 °C (±3.5°C, 80% de aceptabilidad)')

st.subheader('🌡️ Matriz Horaria de Temperatura')

# Asegurar el orden cronológico de los meses en el eje Y
orden_meses = [nombres_meses[m] for m in range(1, 13)]

fig_heat = px.density_heatmap(
    df,
    x='hora',
    y='mes_nombre',
    z='temp_bulbo_seco',
    histfunc='avg',
    nbinsx=24,
    category_orders={'mes_nombre': orden_meses},
    color_continuous_scale='RdBu_r',
    labels={
        'hora': 'Hora del día',
        'mes_nombre': 'Mes',
        'temp_bulbo_seco': 'T° Promedio'
    }
)

fig_heat.update_layout(
    title='Promedio de temperatura por hora y mes (°C)',
    xaxis=dict(tickmode='linear', tick0=0, dtick=1), # Muestra todas las horas (0-23)
    yaxis_title=None,
    height=500
)

st.plotly_chart(fig_heat, use_container_width=True)
st.caption('Análisis de intensidad térmica horaria: permite identificar visualmente las horas de mayor calor durante el año.')

st.divider()

# ─── SECCIÓN 2: HUMEDAD ───────────────────────────────────────────────────────
st.header('💧 Humedad')

fig_hum = go.Figure()

# Box plots de humedad por mes
for mes_num in sorted(df['mes'].unique()):
    datos_mes = df[df['mes'] == mes_num]['humedad_relativa']
    fig_hum.add_trace(go.Box(
        y=datos_mes,
        name=nombres_meses[mes_num],
        marker_color='#5B9BD5',
        showlegend=False
    ))

# Banda de confort de humedad (30% - 70%)
meses_orden = [nombres_meses[m] for m in sorted(df['mes'].unique())]

fig_hum.add_trace(go.Scatter(
    x=meses_orden + meses_orden[::-1],
    y=[70] * 12 + [30] * 12,
    fill='toself',
    fillcolor='rgba(100, 180, 255, 0.15)',
    line=dict(color='rgba(255,255,255,0)'),
    name='Zona de confort (30–70%)',
    hoverinfo='skip'
))

# Líneas de límite de confort
fig_hum.add_hline(y=70, line_dash='dash', line_color='#3498DB',
                annotation_text='Límite superior 70%', annotation_position='top right')
fig_hum.add_hline(y=30, line_dash='dash', line_color='#3498DB',
                annotation_text='Límite inferior 30%', annotation_position='bottom right')

fig_hum.update_layout(
    title='Distribución de humedad relativa por mes y zona de confort',
    xaxis_title='Mes',
    yaxis_title='Humedad relativa (%)',
    yaxis=dict(range=[0, 105]),
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
    height=500
)

st.plotly_chart(fig_hum, use_container_width=True)
st.caption('Zona de confort de humedad relativa: 30% – 70% según ASHRAE 55.')

st.divider()

# ─── SECCIÓN 3: PRECIPITACIÓN ─────────────────────────────────────────────────
st.header('🌧️ Precipitación')

df_precip = (
    df.groupby('mes')['precipitacion_liquida']
    .sum()
    .reset_index()
    .rename(columns={'precipitacion_liquida': 'precip_total'})
)
df_precip['mes_nombre'] = df_precip['mes'].map(nombres_meses)

fig_precip = px.bar(
    df_precip,
    x='mes_nombre',
    y='precip_total',
    title='Precipitación acumulada por mes',
    labels={
        'mes_nombre': 'Mes',
        'precip_total': 'Precipitación (mm)'
    },
    color='precip_total',
    color_continuous_scale='Blues',
    text_auto='.1f'
)
fig_precip.update_layout(
    coloraxis_showscale=False,
    height=450
)
fig_precip.update_traces(textposition='outside')

st.plotly_chart(fig_precip, use_container_width=True)
st.caption('Precipitación acumulada total por mes (mm).')

st.divider()

# ─── SECCIÓN 4: VIENTO ────────────────────────────────────────────────────────
st.header('💨 Viento')

# Clasificar dirección del viento en rumbos
def direccion_a_rumbo(grados):
    rumbos = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
              'S', 'SSO', 'SO', 'OSO', 'O', 'ONO', 'NO', 'NNO']
    idx = round(grados / 22.5) % 16
    return rumbos[idx]

df_viento = df[df['velocidad_viento'] > 0].copy()
df_viento['rumbo'] = df_viento['direccion_viento'].apply(direccion_a_rumbo)

# Clasificar velocidad en rangos
bins = [0, 1.5, 3.3, 5.5, 8, 100]
labels = ['< 1.5 m/s', '1.5–3.3 m/s', '3.3–5.5 m/s', '5.5–8 m/s', '> 8 m/s']
df_viento['rango_velocidad'] = pd.cut(df_viento['velocidad_viento'], bins=bins, labels=labels)

df_rosa = (
    df_viento.groupby(['rumbo', 'rango_velocidad'], observed=True)
    .size()
    .reset_index(name='frecuencia')
)

fig_rosa = px.bar_polar(
    df_rosa,
    r='frecuencia',
    theta='rumbo',
    color='rango_velocidad',
    title='Rosa de los vientos — Mérida, Yucatán',
    color_discrete_sequence=px.colors.sequential.Blues_r,
    template='plotly_white'
)
fig_rosa.update_layout(
    legend_title='Velocidad del viento',
    height=550
)

st.plotly_chart(fig_rosa, use_container_width=True)
st.caption('Rosa de los vientos construida a partir de frecuencia horaria por dirección y velocidad.')