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

 <h1 align='center'>Primer Proyecto Individual (<b>Machine learning Operations</b>)</h1>


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


Debido a su tamaño considerable, estos archivos no están incluidos en **Github**, pero en la carpeta 
[Raw Data](https://drive.google.com/drive/folders/14hpIxPrYuxjBHCg91e-9WJZfnMz0J04e?usp=drive_link), ubicada en el
_Drive_ del autor del presente proyecto se encuentran disponibles.


<br><br>


## 1. Proceso de _ETL_ para los datos de insumo 

Primeramente, se realizó un proceso de extracción, transformación y carga (_ETL_) de los tres archivos en formato ***JSON***, para su posterior trabajo en los procesos siguientes del proyecto. Los detalles del proceso aparecen en el notebook de IPython [01_ETL](https://github.com/MMoscoteAlarcon/Proyecto-Individual_01/blob/master/01_ETL.ipynb), el cual contiene el código para la _limpieza_ de los tres archivos utilizados en el presente proyecto.
Problemas relacionados con la capacidad de cómputo y disponibilidad de los archivos de insumo originales, sugieren que se revise el Notebook de Ipython [01 ETL](https://drive.google.com/file/d/1pcNf187xG1L-ETgNbnZ6rcfQOEcTLe3Y/view?usp=drive_link), el cual se encuentra en ***Google Drive,** y en el cual se presenta de forma detallada todo el proceso de _ETL_ para los tres conjuntos de datos.

 Cabe mencionar que una primera obsevación del conjunto de datos mostró que los archivos presentaban columnas anidadas, es decir, que tienen un diccionario o una lista como valores en cada fila; además para realizar  consultas de valor para la _API_ debían eliminarse columnas que no resultaban de utilidad, eliminación de valores nulos, cambio en el formato de ciertas variables



<br><br><br><br>

















