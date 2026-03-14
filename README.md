# EDA_vehicle_add_sell
Este proyecto consiste en el desarrollo de una aplicación web interactiva para el análisis exploratorio de datos (EDA) relacionados con la venta de vehículos usados en Estados Unidos.

La aplicación fue construida utilizando Streamlit, lo que permite crear interfaces web simples e interactivas directamente desde Python. A través de esta herramienta, los usuarios pueden visualizar y analizar diferentes aspectos del conjunto de datos vehicles_us.csv, el cual contiene información sobre precios, kilometraje, tipo de vehículo y otras características relevantes del mercado de autos usados.

El objetivo principal de la aplicación es facilitar la exploración de los datos mediante visualizaciones interactivas, permitiendo identificar patrones y relaciones entre variables importantes como el precio y el kilometraje de los vehículos.

## 🛠️ Instalación
1. Clona el repositorio:

    git clone https://github.com/DilanSoR/EDA_vehicle_add_sell.git

2. Creamos un entrono de trabajo:

    conda create -n vehicles_env python=3.9 pandas streamlit plotly jupyter -c conda-forge

3. Activamos el entrono de trabajo:

    conda activate vehicles_env

4. Ejecutamos la aplicación:

    streamlit run.\app.py
