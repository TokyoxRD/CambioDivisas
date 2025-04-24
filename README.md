README: Cambio de Divisas
Descripción
Este proyecto es un programa en Python que permite realizar conversiones entre diferentes monedas utilizando tasas de cambio predefinidas. El usuario puede seleccionar entre varias opciones de conversión y proporcionar la cantidad que desea convertir. El programa calcula el resultado y lo muestra en pantalla.


Funcionalidades
Conversión entre las siguientes monedas:
USD a EUR
EUR a USD
DOP a USD
USD a DOP
EUR a DOP
DOP a EUR
Validación de opciones ingresadas por el usuario.
Cálculo  utilizando tasas de cambio predefinidas y no cambiables.


Mejoras Realizadas
Mejoras en la experiencia del usuario:

Se agregó un mensaje para manejar opciones no válidas.
Los resultados de las conversiones se formatearon para mostrar dos decimales, mejorando la presentación.

Cómo Usar
Ejecuta el programa en un entorno de Python.
Sigue las instrucciones en pantalla:
Selecciona una opción de conversión ingresando el número correspondiente.
Ingresa la cantidad que deseas convertir.
El programa mostrará el resultado de la conversión.

Estructura del Código
Diccionario exchange_rates: Contiene las tasas de cambio entre las monedas.
Función convert_currency: Realiza el cálculo de la conversion.
Menú de opciones: Permite al usuario seleccionar la conversión deseada.
Condicionales: Ejecutan la lógica de conversión según la opción seleccionada.

Requisitos
python 3.13.2
