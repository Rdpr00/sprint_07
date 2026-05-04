# Sprint 7 - Tripleten

El presente proyecto crea una página web para un análisis exploratorio de datos (EDA) con enfoque en datos climatólogicos para su uso en arquitectura. 

Para este tipo de análisis hay cuatro variables atmosféricas principales a analizar: temperatura, humedad, precipitación y vientos.

Primeramente, la temperatura nos dicta los requerimentos energéticos que necesitamos en nuestro diseño, es decir, si necesitamos enfriar o calentar el espacio. Esto se determina tomando como temperatura base la **temperatura de confort adaptativo**. Esta temperatura expresa el valor en el cual una persona de un determinado lugar se encuentra en confort térmico. Este confort cambia de región a región debido a que las personas se aclimatan a los climas en los cuales se desenvuelven, por eso el nombre de adaptativo. A partir de este valor, se toma un rango de {\pm 3.5°C}, el cual nos da la Zona de confort térmico. Cualquier valor fuera de este rango es indicativo del requerimento energético del proyecto.

De manera similar, el ser humano se encuentra en confort higromético cuando la humedad relativa en el ambiente se encuentra dentro del rango de 30 a 70%. Es importante conocer el valor de la humedad por dos principales razones: 
- La humedad potencia las sensaciones térmicas, especialmente cuando hace calor. El ser humano naturalmente suda para refrescarse en estos ambientes, sin embargo, si la humedad en e propio ambiente es alta, el sudor propiciara una sensación de sofocamiento.
- Los materiales de la construcción. Existen materiales (como el yeso) que son extremadamente sensibles a la humedad, y que pueden propiciar no solo el desprendimiento de los acabados o recubrimientos, sino tambien el deterioro de estructuras de acero y la proliferación de hongos y salitre.

Por su parte, la precipitación nos permite conocer el dato de cuales son los meses de lluvia. Con estos datos se pueden proponer sistemas de capatción de agua en función de la cantidad de lluvia registrada.

Finalmente, conocer la dirección dominante de los vientos, así como su velocidad, nos permite diseñar sistemas de ventilación pasiva optimos para refrescar el ambiente y renovar el aire, especialmente en climas cálidos y húmedos.

El proyecto contiene por default datos de una estación meteorológica de Yucatán. Sin embargo, con el fin de que sea una página reutilizable, se agrega la opción de cargar datos propios. Es importante que estos datos sean originalmente EPW y posteriormente convertidos a csv. 
