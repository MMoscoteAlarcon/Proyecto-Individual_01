![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)
<br>

<p align='center'>
<img src ="scr\HenryLogo.jpg">
<p>

 <h1 align='center'>Primer Proyecto Individual (_Machine learning Operations_)</h1>


 <h2 style="text-align: center; border: none;">
 Mauricio Moscote Alarcón  
</h2>

<br><br>


<h1> Introducción</h1> 



 El presente proyecto propone la simulación del trabajo de un <b>MLOps Engineer</b>, es decir, la combinación de un _Ingeniero de datos_ y _Científico de datos_, para la plataforma multinacional de videojuegos _Steam_. Para su desarrollo, me entregan como insumo un conjunto datos y se me solicita la entrega de un _Producto Mínimo Viable_ por medio de una _API_ ***(Interfaz de Programación de Aplicaciones)***, la cual está desplegada en un servicio en la nube que contenga la aplicación de dos modelos de ***Machine Learning*** por un lado; y por otro, un análisis de sentimientos sobre los comentarios de los usuarios de los juegos, además de la recomendación de juegos de la plataforma a partir del ingreso del nombre de un juego y/o partiendo de los gustos particulares de un usuario.
  

<br><br>


<h1>Contexto</h1>


_Steam_ es una plataforma de distribución digital de videojuegos desarrollada por Valve Corporation. Fue lanzada en septiembre de 2003 como una forma para de proveer actualizaciones automáticas a sus juegos, pero finalmente se amplió para incluir juegos de terceros. Actualmente ofrece servicios en la nube y servicios online para los usuarios inscritos que les permite la compra, descarga y servicios propios de la comunidad de videojuegos. A fecha de 2017 contaba con más de 142 millones de cuentas de usuario activas.

<br><br>

<h1>Especificación de los Datos</h1>

Para el presente proyecto se tienen como insumos los siguientes tres archivos en formato ***JSON***:

* **australian_user_reviews.** Este conjunto de datos contiene los comentarios de usuarios acerca de los juegos que consumen, además de información adicional como entre otras, la recomendación o no del juego a otros usuarios y estadísticas acerca de la utilidad de los comentarios o sugerencias para otros usuarios. También presenta el número de identificación (_ID_) del usuario que realiza un comentario de un juego en particular, junto con la _url_ del perfil del usuario y el _ID_ del juego que el usuario comenta.

* **australian_users_items.** Es un dataset que contiene información sobre los juegos consumidos por todos los usuarios registrados, así como el tiempo acumulado que cada usuario jugó a un juego determinado en la plataforma.

* **output_steam_games.** Contiene información relacionada de los mismos juegos ofrecidos por la plataforma _Steam_, tales como el título, el desarrollador, precio, características técnicas, etiquetas, entre otros.


Para la posibilidad de la descarga los archivos originales, que debido a su tamaño no están incluidos en el presente proyecto, se encuentran disponibles en el enlace siguiente:

[Raw Data](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)




<br><br>


_**ETL**_:
Para conocer más sobre el desarrollo del proceso ETL, existe el siguiente enlace
[Notebook ETL](https://github.com/NPontisLedda/PI01_MLOPs_Henry/blob/main/PI_MLOPs_ETL_EDA.ipynb)



_**Desanidado**_:
1. Algunas columnas están anidadas, es decir, tienen un diccionario o una lista como valores en cada fila, las desanidamos para poder realizar algunas de las consultas API.

_**Eliminar columnas no utilizadas**_:

2. Se eliminan las columnan que no se utilizarán:
   - De output_steam_games: publisher, url, tags, price, specs, early_access.
   - De australian_user_reviews: user_url, funny, last_edited, helpful.
   - De australian_users_items: user_url, playtime_2weeks, steam_id, items_count.

_**Control de valores nulos**_:

3. Se eliminan valores nulos:
   - De output_steam_games: genres, release_date.
   - De australian_user_reviews: item_id.
   - De australian_user_items: user_id

_**Cambio del tipo de datos**_:

4. Las fechas se cambian a datetime para luego extraer el año:
   - De australian_user_reviews: la columna posted .
   - De output_steam_games: la columna release_date.

_**Se quitan datos sin valor**_:

5. Los datos que no tienen ningún valor:
   - De australian_user_items: la columna playtime_forever.

_**Fusión de conjuntos de datos**_:

6. Combiné los datasets para las funciones 1 y 2 en un archivo .csv [Archivo para funciones 1 y 2](https://github.com/NPontisLedda/PI01_MLOPs_Henry/blob/main/df_f1_2.csv), y para las funciones 3, 4 y 5 en otro archivo .csv [Archivo para funciones 3,4 y 5](https://github.com/NPontisLedda/PI01_MLOPs_Henry/blob/main/df_f3_4_5.csv).

_**Análisis de sentimiento**_:

7. En el conjunto de datos australian_user_reviews, hay reseñas de juegos realizadas por diferentes usuarios. Creación de la columna 'sentiment_analysis' aplicando análisis de sentimiento de PNL con la siguiente escala: toma el valor '0' si es negativo, '1' si es neutral y '2' si es positivo. Esta nueva columna reemplaza la columna australian_user_reviews.review para facilitar el trabajo de los modelos de aprendizaje automático y el análisis de datos. Si este análisis no es posible por falta de una reseña escrita, toma el valor de 1.


# _Funciones_
- _**Para obtener más información sobre el desarrollo de las diferentes funciones y una explicación más detallada de cada una, haga clic en el siguiente enlace**_
[Notebook de funciones](https://github.com/NPontisLedda/PI01_MLOPs_Henry/blob/main/FastAPI/fastapi-env/main.py)

Desarrollo API: Se propone disponibilizar los datos de la empresa usando el framework FastAPI . Las consultas que proponemos son las siguientes:

Cada aplicación tiene un decorador (@app.get('/')) con el nombre de la aplicación para poder reconocer su función.

Las consultas son las siguientes:

1. **PlayTimeGenre(género:str)**:
Debe devolver año con más horas jugadas para dicho género.
Ejemplo de retorno: {"Año de lanzamiento con más horas jugadas para Género X" : 2013}

2. **UserForGenre(género:str)**:
Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año.
Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf, "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas : 23}]}

3. **UsersRecommend(año:int)**:
Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos/neutrales)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

4. **def UsersWorstDeveloper(año:int)**:
Devuelve el top 3 de desarrolladores con juegos MENOS recomendados por usuarios para el año dado. (reviews.recommend = False y comentarios negativos)
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

5. **sentiment_analysis(empresa desarrolladora:str)**:
Según la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
Ejemplo de retorno: {'Valve' : [Negative = 182, Neutral = 120, Positive = 278]}

# _**EDA (Análisis exploratorio de datos)**_
Los conjuntos de datos tenían algunos aspectos que corregir relacionados con variables numéricas. La columna playtime_forever tenía algunos valores atípicos con cantidades irreales de horas jugadas para algunos usuarios; las cantidades se corrigieron.

# _**Aprendizaje automático(Machine Learning)**_

El modelo establece una relación artículo-artículo. Esto significa que dado un item_id, en función de qué tan similar sea al resto, se recomendarán artículos similares. Aquí, la entrada es un juego y la salida es una lista de juegos recomendados.

El método de aprendizaje automático utilizado es K-Neighbours. No es el mejor método para abordar los conjuntos de datos y parte de este proyecto se centra en eso. Debido a que el proyecto debe implementarse en Render, la memoria RAM disponible es limitada y lo importante aquí era comprender la diferencia entre los diferentes modelos de Machine Learning. Anteriormente, probé árboles de decisión y procesamiento de lenguaje natural utilizando similitud de coseno.

El sistema de recomendación item-item se planteó originalmente así:

6. **get_recommendations(item_id)**: 
Ingresando el id de producto(item_id), deberíamos recibir una lista con 5 juegos recomendados similares al ingresado.



# _**Implementación de API**_
La implementación de nuestra FastAPI se realiza utilizando Render un entorno virtual.

Haga clic para acceder a mi aplicación FastAPI: [API Deployment](https://proyecto1-gkkk.onrender.com/docs#/)

Para consumir la API, utilice los 6 endpoints diferentes para obtener información y realizar consultas sobre estadísticas de juegos.