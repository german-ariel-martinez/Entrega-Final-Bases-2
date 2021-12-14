# Trabajo Practico Especial - Base de Datos 2

## Contenido
1. Idea Principal.
2. Estructura del trabajo.
3. Instructivo de instalación.
4. Integrantes del trabajo.

## 1 - Idea principal:
Para este trabajo se nos pidio solucionar un problema (a elección) en el cual la solucion al mismo sea utilizando 2 bases de datos distintas. El problema que seleccionamos consiste en crear una red social que permita asistir y auspiciar eventos publicos. Tambien se espera que por medio de esta aplicacion los usuarios puedan conocer a otras personas para luego mantenerce en contacto. La solucion que se propuso se basa en la idea de utilizar PostgreSQL y Neo4J para persistir datos y relaciones de los usuarios.

## 2 - Estructura del trabajo:
El proyecto en general esta formado por 2 partes, el backend y el frontend. Cada uno fue desarrollado de la siguiente manera:
- Backend: el mismo fue desarrollado en Python utilizando la libreria de FastAPI para el desarrollo de la API, en conjunto con Psycopg2 para la conexion a Postgres y Py2neo para la conexion con la base de datos en Neo4J.
- Fronend: este fue desarrollado utilizando Vue CLI, un framework de desarrollo web que utiliza la tecnologia de Vue JS de fondo. Para la parte visual se utilizo un plugin de Vue CLI conocido como Vuetify (https://vuetifyjs.com/en/), al mismo tiempo para conectarse con la API se utilizo otro plugin conocido como Axios el cual realiza las consultas a la misma (https://axios-http.com/docs/intro). Por ultimo se incluyo otro plugin conocido como MDI Icons que añade una gran cantidad de iconos los cuales siguen las normativas de Material Design impuesta por Google, esto es de gran utilidad ya que Vuetify tambien busca cumplir con las mismas.

## 3 - Instructivo de instalación:
Si usted esta corriendo en Windows recomendamos tener las siguientes aplicaciones instaladas:
- Para correr el proyecto en Python en un entorno seguro recomendamos tener instalado Anaconda (https://www.anaconda.com/products/individual).
- Para instalar y configurar ambas base de datos usted puede tenerlas corriendo de forma local en su computadora pero recomendamos tener funcionando sus imagenes en Docker Desktop ya que esto es mas simple, ademas de que ofrece un mayor potencial a la hora de administrar las imagnes que usted tenga instaladas en su computadora (https://www.docker.com/products/docker-desktop).
- Por ultimo para navegar por medio de su terminal de una forma mas comoda y en un estilo similar al que se logra utilizando una terminal de Linux, recomendamos descargar la siguiente terminal (https://cmder.net/).
- Debe tener instalado Node JS (https://nodejs.org/es/download/)

Si usted esta trabajando en un sistema operativo de Linux lo unico que recomendamos instalar es Anaconda y tener previamente instalado Node JS.

¡Una vez llegado este punto estamos listos para comenzar!

Primero es necesario instalar ambas bases de datos via docker, para esto ejecutamos los siguientes comandos:

### PostgreSQL:
docker run --name "nombre de la imagen en docker" -e POSTGRES_PASSWORD=<mysecretpassword> -p 5432:5432 -d postgres
### Neo4J:
docker run --name "nombre de la imagen en docker" -p 7474:7474 -p 7687:7687 --env=NEO4J_AUTH=none -d neo4j

Luego de tener ambas bases de datos corriendo deberia verse algo de este estilo en Docker Desktop:
  
![image](https://user-images.githubusercontent.com/18686695/146066637-35f1b745-ad4e-45ad-969a-2ec3d6b32493.png)

Una vez logrado lo anterior crear en Postgres una base de datos llamada "bases2" y en Neo4J una llamada "neo4j" (ya viene con una que utiliza dicho nombre). No hay que preocuparse para crear las tablas en las bases de datos ya que la API se encarga de esto automaticamente.
  
Luego de hacer todo lo anterior lo que queda es correr la aplicacion, para hacer esto:
1. Clonar el repositorio de github en su computadora.
2. Desde la terminal de Anaconda correr el comando "conda activate tp-bases", luego ejecute "code ." para abrir Visual Studio Code en la carpeta del proyecto (en la primer imagen notar como cambia el entorno de trabajo, remarcado en rojo). Puede que tenga que cambiar el interprete de VS Code al de la version de Python que esta corriendo en el entorno creado por anaconda, para esto ir a la parte inferior de VS Code y cambiarlo, deberia ver algo como lo que se muestra en la segunda imagen:
  
  ![image](https://user-images.githubusercontent.com/18686695/146067629-7f23da7f-5104-4942-a34b-6fff7e97c95a.png)
  
  ![image](https://user-images.githubusercontent.com/18686695/146067949-17488dca-07c0-448d-ab4d-06b29209035a.png)

3. Dentro del proyecto en Python correr "uvicorn app:app --reload" para correr la API. La API corre en el puerto 8000 de su computadora, para acceder a los endpoints puede hacer "localhost:8000/docs", sabra que esta corriendo si ve algo como esto:
  
  ![image](https://user-images.githubusercontent.com/18686695/146068459-993ae6d4-ec98-4518-aea0-6462cae560df.png)

4. Ahora queda correr la web-app, para esto vaya a la terminal de Cmder (o la que usted elija) y vaya a la carpeta "bases-front" dentro del proyecto, una vez dentro ejecute el comando "npm run serve", debera ver algo como esto cuando la pagina este corriendo:
  
  ![image](https://user-images.githubusercontent.com/18686695/146068764-02583472-798e-4073-81a3-94393411873d.png)

¡Listo! Ya puede acceder a la pagina utilizando la direccion que se muestra en la imagen anterior.
  
## 4 - Integrantes del trabajo:
  - Joaquin Garcia del Rio (59051).
  - German Ariel Martinez (58574).
  - Santiago Preusche (59233).

