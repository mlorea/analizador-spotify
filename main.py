from utils import cargar_csv, generar_informe_txt
from analisis import (
    analizar_artistas_frecuentes,
    analizar_frecuencia_agregado,
    canciones_menos_populares,
    clasificar_por_duracion
)
from tabulate import tabulate

def main():
    # 1. Cargar datos
    print("Cargando datos...")
    datos = cargar_csv('datos/mi_playlist.csv')
    
    if datos is None:
        print("No se pudo cargar el archivo. Terminando programa.")
        return
    
    # 2. Análisis de artistas
    print("\nAnalizando artistas...")
    top_artistas = analizar_artistas_frecuentes(datos)
    print(tabulate(top_artistas.reset_index(), 
                 headers=['Artista', 'Canciones'], 
                 tablefmt='grid'))
    
    # 3. Análisis por fecha
    print("\nAnalizando fechas...")
    por_dia, por_mes = analizar_frecuencia_agregado(datos)
    
    print("\nPor día:")
    print(tabulate(por_dia.reset_index(), 
                  headers=['Día', 'Canciones'], 
                  tablefmt='grid'))
    
    print("\nPor mes:")
    print(tabulate(por_mes.reset_index(), 
                  headers=['Mes', 'Canciones'], 
                  tablefmt='grid'))
    
    # 4. Canciones menos populares
    print("\nBuscando canciones menos populares...")
    menos_pop = canciones_menos_populares(datos)
    print(tabulate(menos_pop, 
                  headers=['Canción', 'Artista', 'Popularidad'], 
                  tablefmt='grid'))
    
    # 5. Análisis por duración
    print("\nClasificando por duración...")
    duracion = clasificar_por_duracion(datos)
    print(tabulate(duracion.reset_index(), 
                  headers=['Duración', 'Canciones'], 
                  tablefmt='grid'))
    
    # 6. Generar informe
    print("\nGenerando informe...")
    generar_informe_txt(
        artistas=top_artistas,
        dias=por_dia,
        meses=por_mes,
        menos_populares=menos_pop,
        duracion=duracion
    )
    print("Informe guardado en: informes/informe.txt")

if __name__ == "__main__":
    main()