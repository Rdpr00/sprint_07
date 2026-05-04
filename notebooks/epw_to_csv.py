import pandas as pd

columnas = [
    'año', 'mes', 'dia', 'hora', 'minuto',
    'indicador_datos',
    'temp_bulbo_seco', 'temp_punto_rocio', 'humedad_relativa',
    'presion_atmosferica',
    'radiacion_extraterrestre_horizontal', 'radiacion_extraterrestre_normal',
    'radiacion_infrarroja_horizontal',
    'radiacion_solar_horizontal', 'radiacion_directa_normal',
    'radiacion_difusa_horizontal',
    'iluminancia_horizontal', 'iluminancia_directa_normal', 'iluminancia_difusa_horizontal',
    'luminancia_zenital',
    'direccion_viento', 'velocidad_viento',
    'cobertura_nubosa_total', 'cobertura_nubosa_opaca',
    'visibilidad', 'altura_techo_nubes',
    'estado_presente', 'estado_pasado',
    'agua_precipitable', 'profundidad_optica_aerosol',
    'profundidad_nieve', 'dias_desde_ultima_nevada',
    'albedo',
    'precipitacion_liquida', 'cantidad_precipitacion'
]

df = pd.read_csv('merida.epw', skiprows=8, header=None, names=columnas)

df.to_csv('merida_clima.csv', index=False)

print("✅ Conversión exitosa: merida_clima.csv")
print(f"Filas: {len(df)} | Columnas: {len(df.columns)}")
print(df[['año', 'mes', 'dia', 'hora', 'temp_bulbo_seco', 'humedad_relativa']].head())