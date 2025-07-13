import pandas as pd
from datetime import datetime
from tabulate import tabulate
import os

def cargar_csv(ruta_csv):
    """
    Carga un archivo CSV en un DataFrame de pandas.
    
    Args:
        ruta_csv (str): Ruta al archivo CSV
    
    Returns:
        pd.DataFrame: Datos cargados o None si hay error
    """
    try:
        df = pd.read_csv(ruta_csv)
        print("✅ Archivo cargado correctamente")
        return df
    except FileNotFoundError:
        print("❌ Error: Archivo no encontrado")
        return None
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

def crear_directorio_si_no_existe(ruta):
    """Crea el directorio si no existe"""
    directorio = os.path.dirname(ruta)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)

def generar_informe_txt(artistas, dias, meses, duracion=None, menos_populares=None, ruta='informes/informe.txt'):
    """
    Genera un archivo de texto con los resultados del análisis
    
    Args:
        artistas: Top artistas más frecuentes
        dias: Canciones por día de semana
        meses: Canciones por mes
        duracion: Clasificación por duración (opcional)
        menos_populares: Canciones menos populares (opcional)
        ruta: Ruta donde guardar el informe
    """
    # Asegurar que exista el directorio
    crear_directorio_si_no_existe(ruta)
    
    # Obtener fecha actual
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    with open(ruta, 'w', encoding='utf-8') as archivo:
        # Encabezado
        archivo.write(f"Informe de Análisis Musical - {fecha_actual}\n")
        archivo.write("=" * 50 + "\n\n")
        
        # 1. Artistas más frecuentes
        archivo.write("TOP 10 ARTISTAS MÁS FRECUENTES\n")
        tabla = tabulate(artistas.reset_index().values, 
                        headers=["Artista", "Canciones"], 
                        tablefmt="simple")
        archivo.write(tabla + "\n\n")
        
        # 2. Canciones por día
        archivo.write("CANCIONES POR DÍA DE LA SEMANA\n")
        tabla = tabulate(dias.reset_index().values,
                        headers=["Día", "Canciones"],
                        tablefmt="simple")
        archivo.write(tabla + "\n\n")
        
        # 3. Canciones por mes
        archivo.write("CANCIONES POR MES\n")
        tabla = tabulate(meses.reset_index().values,
                        headers=["Mes", "Canciones"],
                        tablefmt="simple")
        archivo.write(tabla + "\n\n")
        
        # 4. Duración (opcional)
        if duracion is not None:
            archivo.write("CLASIFICACIÓN POR DURACIÓN\n")
            tabla = tabulate(duracion.reset_index().values,
                            headers=["Duración", "Canciones"],
                            tablefmt="simple")
            archivo.write(tabla + "\n\n")
        
        # 5. Menos populares (opcional)
        if menos_populares is not None:
            archivo.write("CANCIONES MENOS POPULARES\n")
            tabla = tabulate(menos_populares[['Track Name', 'Artist Name(s)', 'Popularity']].values,
                            headers=["Canción", "Artista", "Popularidad"],
                            tablefmt="simple")
            archivo.write(tabla + "\n\n")
        
        archivo.write("Informe generado correctamente")

# Ejemplo de uso:
# df = cargar_csv("datos/musica.csv")
# if df is not None:
#     artistas = df['Artist'].value_counts().head(10)
#     dias = df['Dia'].value_counts()
#     generar_informe_txt(artistas, dias)