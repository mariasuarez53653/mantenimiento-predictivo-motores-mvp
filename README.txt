Sistema de mantenimiento predictivo para motores eléctricos — MVP
Integrantes: Stiven Lopez Wilches y Maria José Suarez Guerra  
Programa: Ingeniería Mecatrónica  
Universidad: Universidad de Caldas

1. Problema y objetivo

El proyecto busca abordar la detección tardía de condiciones anormales en motores eléctricos, que pueden ocasionar fallas inesperadas, interrupciones en los procesos y costos de mantenimiento.

El objetivo de esta primera versión del producto mínimo viable (MVP) es desarrollar un programa en Python que permita analizar manualmente los valores de corriente y temperatura de un motor eléctrico, clasificar su estado e indicar posibles condiciones de riesgo mediante alertas y recomendaciones básicas de mantenimiento.

2. Cómo ejecutar

1. Descargar o clonar este repositorio en el computador.
2. Verificar que Python esté instalado.
3. Abrir una terminal en la carpeta donde se encuentra el archivo `main.py`.
4. Ejecutar el siguiente comando:

   ```bash
   python main.py
   ```

5. Seguir las instrucciones del menú e ingresar manualmente los valores de corriente y temperatura solicitados por el programa.

3. Dependencias

- Python 3.
- No requiere librerías externas ni instalaciones adicionales de paquetes.

4. Limitaciones actuales

Esta versión inicial presenta las siguientes limitaciones:

- Los datos deben ingresarse manualmente por el usuario.
- No tiene conexión con sensores físicos para adquirir datos directamente del motor.
- El análisis se limita a las variables de corriente y temperatura.
- La clasificación del estado del motor se basa en límites predefinidos y no considera las características particulares de cada motor.

Estas limitaciones podrán abordarse progresivamente en futuras versiones del proyecto.