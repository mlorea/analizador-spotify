import pandas as pd
import matplotlib.pyplot as plt

def analizar_artistas_frecuentes(df, top_n=10):
    """
    Encuentra los artistas con más canciones en la playlist
    y muestra un gráfico de barras.
    
    Args:
        df: DataFrame con los datos de canciones
        top_n: Cuántos artistas mostrar (por defecto 10)
    
    Returns:
        Series con los artistas y sus conteos
    """
    # Contar canciones por artista
    artistas = df['Artist Name(s)'].value_counts().head(top_n)
    
    # Crear gráfico
    plt.figure(figsize=(10, 5))
    artistas.plot(kind='bar', color='green')
    
    plt.title(f'Top {top_n} artistas más frecuentes')
    plt.xlabel('Artista')
    plt.ylabel('Canciones')
    plt.xticks(rotation=45)
    
    # Guardar imagen
    plt.savefig('graficos/artistas_frecuentes.png', bbox_inches='tight')
    plt.close()
    
    return artistas

def analizar_frecuencia_agregado(df):
    """
    Analiza cuándo se agregaron las canciones a la playlist
    por día de semana y por mes.
    
    Args:
        df: DataFrame con los datos de canciones
    
    Returns:
        Dos Series: canciones por día y por mes
    """
    # Convertir fecha y extraer día/mes
    df['Added At'] = pd.to_datetime(df['Added At'])
    df['Dia'] = df['Added At'].dt.day_name()
    df['Mes'] = df['Added At'].dt.month_name()
    
    # Ordenar días de lunes a domingo
    dias = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    por_dia = df['Dia'].value_counts().reindex(dias)
    
    # Conteo por mes
    por_mes = df['Mes'].value_counts()
    
    # Gráfico por día
    plt.figure(figsize=(8, 4))
    por_dia.plot(kind='bar', color='blue')
    plt.title('Canciones agregadas por día')
    plt.savefig('graficos/canciones_por_dia.png')
    plt.close()
    
    # Gráfico por mes
    plt.figure(figsize=(8, 4))
    por_mes.plot(kind='bar', color='orange')
    plt.title('Canciones agregadas por mes')
    plt.savefig('graficos/canciones_por_mes.png')
    plt.close()
    
    return por_dia, por_mes

def canciones_menos_populares(df, top_n=10):
    """
    Encuentra las canciones menos populares según Spotify.
    
    Args:
        df: DataFrame con los datos
        top_n: Cuántas canciones mostrar (por defecto 10)
    
    Returns:
        DataFrame con las canciones menos populares
    """
    # Ordenar por popularidad (menor a mayor)
    menos_populares = df.sort_values('Popularity').head(top_n)
    
    # Gráfico de dispersión
    plt.figure(figsize=(10, 5))
    plt.scatter(df.index, df['Popularity'], alpha=0.5, color='red')
    plt.title('Popularidad de las canciones')
    plt.savefig('graficos/popularidad.png')
    plt.close()
    
    return menos_populares[['Track Name', 'Artist Name(s)', 'Popularity']]

def clasificar_por_duracion(df):
    """
    Clasifica canciones por duración en cortas, medias y largas.
    
    Args:
        df: DataFrame con los datos
    
    Returns:
        Series con el conteo por categoría
    """
    # Convertir a minutos
    df['Minutos'] = df['Duration (ms)'] / 60000
    
    # Crear categorías
    condiciones = [
        (df['Minutos'] < 3),
        (df['Minutos'] <= 4.5),
        (df['Minutos'] > 4.5)
    ]
    categorias = ['Corta (<3min)', 'Media (3-4.5min)', 'Larga (>4.5min)']
    
    df['Categoria'] = pd.cut(df['Minutos'], 
                            bins=[0, 3, 4.5, float('inf')], 
                            labels=categorias)
    
    conteo = df['Categoria'].value_counts()
    
    # Gráfico de pastel
    plt.figure(figsize=(6, 6))
    conteo.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Duración de canciones')
    plt.ylabel('')
    plt.savefig('graficos/duracion_canciones.png')
    plt.close()
    
    return conteo