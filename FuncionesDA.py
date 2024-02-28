#------------------------------------------------------------------------------------------------------------
# 27.02.2024
#------------------------------------------------------------------------------------------------------------

# Paquete de Funciones para Analisis de datos (DA) en Python usados en
# Proyecto Individual. El DA incluye el proceso de Limpieza de datos de un dataframe 

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

import pandas as pd
from textblob import TextBlob
import re
import regex

#------------------------------------------------------------------------------------------------------------
 
def Data_Type(DF):
    '''
    Esta función toma un DataFrame como insumo y devuelve un Dataframe de resumen con información 
    sobre los tipos de datos de cada variable presentes en el Dataframe (columnas), la cantidad 
    tanto de registros nulos como no nulos por variable y el valor porcentual de 
    registros tanto nulos como no nulos. 

    Parámetros que utiliza:
        DF --> Objeto tipo pandas.DataFrame. 
               Corresponde al Dataframe a ser utilizado

    Objetos de retorno de la función:
        DF_Res --> Objeto tipo pandas.DataFrame
                  El Dataframe que retorna la función Data_Type() posee los siguientes campos:
                  - 'Variable':   Nombre correspondiente al campo de cada columna.
                  - 'Type':  Tipos de datos únicos presentes en cada campo.
                  - 'NaN':        Cantidad de valores nulos en cada campo.
                  - 'No_NaN':     Número de valores no nulos presentes en cada campo.
                  - 'NaN_(%)':    Porcentaje de valores nulos por campo en el Dataframe.
                  - 'No_NaN_(%)': Porcentaje de valores no nulos en cada variable.
             
    '''

    Dict = {"Variable": [], "Type": [], "NaN": [], "No_NaN": [], "NaN_(%)": [], "No_NaN_(%)": []}

    for Column in DF.columns:
        No_NaN_Perc = ((DF[Column].count() / len(DF)) * 100)
        Dict["Variable"].append(Column)
        Dict["Type"].append(DF[Column].apply(type).unique())
        Dict["NaN"].append(DF[Column].isnull().sum())
        Dict["No_NaN"].append(DF[Column].count().sum())
        Dict["NaN_(%)"].append(round(100 - No_NaN_Perc, 3))
        Dict["No_NaN_(%)"].append(round(No_NaN_Perc, 3))
        

    DF_Res = pd.DataFrame(Dict)
        
    return DF_Res


#------------------------------------------------------------------------------------------------------------

def Duplicates(DF, Campo):
    '''
    Esta función toma objeto de insumo un DataFrame y el nombre de un campo (columna) en particular.
    Muestra las filas duplicadas dependiendo del campo especificado y luego identifica las filas 
    duplicadas basadas en el contenido de ese campo o variable, las filtra y las ordena.

    Parámetros que utiliza:
        DF --> Objeto tipo pandas.DataFrame 
               Corresponde al DataFrame en el que se realizará  la busqueda de filas duplicadas.
        Campo --> Objeto tipo str
               Es el nombre asignado del campo (variable o columna) en la cual se 
               realizará la verificación  de los registros duplicados.

    Objetos de retorno de la función::
        pandas.DataFrame or str: Un DataFrame que contiene las filas duplicadas filtradas y ordenadas,
        listas para su inspección y comparación, o el mensaje "No hay duplicados" si no se encuentran duplicados.
    '''
    
    duplicated_rows = DF[DF.duplicated(subset=Campo, keep=False)]
         # Filtrado de las filas duplicadas

    if duplicated_rows.empty:
        return "No existen valores duplicados"
    
    
    duplicated_rows_sorted = duplicated_rows.sort_values(by=Campo)
         # Ordenado de las filas duplicadas para realizar la comparación entre ellas


    return duplicated_rows_sorted


#------------------------------------------------------------------------------------------------------------


def Year_release(Date):
    '''
    Esta función toma como entrada una fecha en formato 'yyyy-mm-dd', extrae y devuelve el año de la fecha
    si el formato del dato es válido. Si la fecha es nula o inconsistente, devuelve 'Dato no disponible'.

    Parámetros de entrada:
        Date --> Objeto en formato str, float, None 
        Corresponde a la fecha en formato 'yyyy-mm-dd'.

    Objetos de retorno de la función:
        El año de la fecha si viene en formato válido, 'Dato no disponible' si es el dato viene en
        formato None o el formato no es el correcto.
    '''

    if pd.notna(Date):
        if re.match(r'^\d{4}-\d{2}-\d{2}$', Date):
            return Date.split('-')[0]
    return 'Dato no disponible'


#------------------------------------------------------------------------------------------------------------

def reemplaza_a_flotante(value):
    '''
    Reemplaza valores no numéricos y nulos en una columna con 0.0.

    Esta función toma un valor como entrada y trata de convertirlo a un número float.
    Si la conversión es exitosa, el valor numérico se mantiene. Si la conversión falla o
    el valor es nulo, se devuelve 0.0 en su lugar.

    Parameters:
        value: El valor que se va a intentar convertir a un número float o nulo.

    Returns:
        float: El valor numérico si la conversión es exitosa o nulo, o 0.0 si la conversión falla.
    '''
    if pd.isna(value):
        return 0.0
    try:
        float_value = float(value)
        return float_value
    except:
        return 0.0
    
def convertir_fecha(cadena_fecha):
    '''
    Convierte una cadena de fecha en un formato específico a otro formato de fecha.
    
    Args:
    cadena_fecha (str): Cadena de fecha en el formato "Month Day, Year" (por ejemplo, "September 1, 2023").
    
    Returns:
    str: Cadena de fecha en el formato "YYYY-MM-DD" o un mensaje de error si la cadena no cumple el formato esperado.
    '''
    match = re.search(r'(\w+\s\d{1,2},\s\d{4})', cadena_fecha)
    if match:
        fecha_str = match.group(1)
        try:
            fecha_dt = pd.to_datetime(fecha_str)
            return fecha_dt.strftime('%Y-%m-%d')
        except:
            return 'Fecha inválida'
    else:
        return 'Formato inválido'

def resumen_cant_porcentaje(df, columna):
    '''
    Cuanta la cantidad de True/False luego calcula el porcentaje.

    Parameters:
    - df (DataFrame): El DataFrame que contiene los datos.
    - columna (str): El nombre de la columna en el DataFrame para la cual se desea generar el resumen.

    Returns:
    DataFrame: Un DataFrame que resume la cantidad y el porcentaje de True/False en la columna especificada.
    '''
    # Cuanta la cantidad de True/False luego calcula el porcentaje
    counts = df[columna].value_counts()
    percentages = round(100 * counts / len(df),2)
    # Crea un dataframe con el resumen
    df_results = pd.DataFrame({
        "Cantidad": counts,
        "Porcentaje": percentages
    })
    return df_results

def bigote_max(columna):
    '''
    Calcula el valor del bigote superior y la cantidad de valores atípicos en una columna.

    Parameters:
    - columna (pandas.Series): La columna de datos para la cual se desea calcular el bigote superior y encontrar valores atípicos.

    Returns:
    None
    '''
    # Cuartiles
    q1 = columna.describe()[4]
    q3 = columna.describe()[6]

    # Valor del vigote
    bigote_max = round(q3 + 1.5*(q3 - q1), 2)
    print(f'El bigote superior de la variable {columna.name} se ubica en:', bigote_max)

    # Cantidad de atípicos
    print(f'Hay {(columna > bigote_max).sum()} valores atípicos en la variable {columna.name}')


 


#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------





'''
def analisis_sentimiento(review):
    
    Realiza un análisis de sentimiento en un texto dado y devuelve un valor numérico que representa el sentimiento.

    Esta función utiliza la librería TextBlob para analizar el sentimiento en un texto dado y
    asigna un valor numérico de acuerdo a la polaridad del sentimiento.

    Parameters:
        review (str): El texto que se va a analizar para determinar su sentimiento.

    Returns:
        int: Un valor numérico que representa el sentimiento del texto:
             - 0 para sentimiento negativo.
             - 1 para sentimiento neutral o no clasificable.
             - 2 para sentimiento positivo.
    
    if review is None:
        return 1
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    if polarity < -0.2:
        return 0  
    elif polarity > 0.2: 
        return 2 
    else:
        return 1 
    
def ejemplos_review_por_sentimiento(reviews, sentiments):
    
    Imprime ejemplos de reviews para cada categoría de análisis de sentimiento.

    Esta función recibe dos listas paralelas, `reviews` que contiene los textos de las reviews
    y `sentiments` que contiene los valores de sentimiento correspondientes a cada review.
    
    Parameters:
        reviews (list): Una lista de strings que representan los textos de las reviews.
        sentiments (list): Una lista de enteros que representan los valores de sentimiento
                          asociados a cada review (0, 1, o 2).

    Returns:
        None: La función imprime los ejemplos de reviews para cada categoría de sentimiento.
    
    for sentiment_value in range(3):
        print(f"Para la categoría de análisis de sentimiento {sentiment_value} se tienen estos ejemplos de reviews:")
        sentiment_reviews = [review for review, sentiment in zip(reviews, sentiments) if sentiment == sentiment_value]
        
        for i, review in enumerate(sentiment_reviews[:3], start=1):
            print(f"Review {i}: {review}")
        
        print('\n')

'''
   