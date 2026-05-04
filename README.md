# 🌤️ Análisis Exploratorio de Datos Climatológicos para Diseño Bioclimático

Este proyecto consiste en una herramienta web interactiva desarrollada con Streamlit para el análisis exploratorio de datos (EDA) enfocados en la arquitectura sustentable. El objetivo principal es transformar datos meteorológicos en información visual estratégica para la toma de decisiones en el diseño arquitectónico.

## 📌 Contexto del Proyecto
El diseño bioclimático busca optimizar el confort humano y la eficiencia energética mediante el análisis de las variables atmosféricas locales. Esta herramienta analiza cuatro pilares fundamentales:
1. Temperatura y Confort Adaptativo

   La temperatura define los requerimientos energéticos de un edificio. Este análisis se basa en el Modelo de Confort Adaptativo, el cual establece que la sensación térmica de las personas varía según el clima al que están habituadas.
    - Zona de Confort: Se define como un rango de $\pm 3.5^{\circ}C$ respecto a la temperatura neutra.
    - Impacto: Cualquier valor fuera de este rango indica la necesidad de estrategias de diseño para calentar o enfriar el espacio.
2. Humedad Relativa

   El confort higrométrico se sitúa idealmente entre el 30% y el 70%. El control de la humedad es crítico por dos razones:
    - Sensación Térmica: La humedad alta en climas cálidos limita la evaporación del sudor, provocando sofocamiento.
    - Integridad de los materiales: Niveles extremos afectan la durabilidad de materiales (como el yeso o el acero) y fomentan la proliferación de patógenos, hongos y salitre.
3. Precipitación Pluvial

El análisis de la pluviosidad acumulada permite identificar los periodos de lluvia crítica. Esta información es esencial para:Dimensionar sistemas de captación de agua pluvial.Diseñar estrategias de drenaje y protección de fachadas.

4. Régimen de Vientos
    El estudio de la dirección dominante y la velocidad del viento permite proyectar sistemas de ventilación pasiva. Esto es vital en climas cálidos y húmedos para garantizar la renovación de aire y el refrescamiento natural de los interiores.
    
Incluye por defecto datos de Mérida, Yucatán (TMYx), pero permite la carga de archivos personalizados. Sin embargo, para asegurar la compatibilidad, los datos deben seguir el formato de los archivos EPW (EnergyPlus Weather) convertidos previamente a formato CSV.Nota: La precisión del análisis depende de la calidad del archivo fuente. Se recomienda utilizar bases de datos reconocidas como Climate.OneBuilding.org.
