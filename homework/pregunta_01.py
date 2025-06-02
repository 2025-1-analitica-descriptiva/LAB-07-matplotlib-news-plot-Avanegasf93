"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import os
import pandas as pd
import matplotlib.pyplot as plt

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    # Leer el archivo CSV con los datos
    df = pd.read_csv("files/input/news.csv")

    # Crear el directorio de salida si no existe
    output_path = "files/plots"
    os.makedirs(output_path, exist_ok=True)

    # Agrupar por categoría (por ejemplo) y contar ocurrencias si no hay conteo explícito
    if 'category' in df.columns:
        data = df['category'].value_counts().sort_values(ascending=True)
        title = "Distribución de noticias por categoría"
        xlabel = "Cantidad de noticias"
        ylabel = "Categoría"
    else:
        # Caso alternativo si el CSV no tiene columnas claras
        data = df.iloc[:, 0].value_counts().sort_values(ascending=True)
        title = "Distribución de datos (primera columna)"
        xlabel = "Cantidad"
        ylabel = "Valores"

    # Configurar el estilo del gráfico
    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(10, 6))

    # Crear gráfico de barras horizontales
    data.plot(kind="barh", color="#1f77b4", ax=ax)

    # Agregar títulos y etiquetas
    ax.set_title(title, fontsize=14)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    # Ajustar diseño para que no se recorte el contenido
    plt.tight_layout()

    # Guardar el gráfico como imagen PNG
    output_file = os.path.join(output_path, "news.png")
    plt.savefig(output_file)

    # Cerrar la figura para liberar memoria
    plt.close()