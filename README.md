# CompetenciApp
WebApp para la gestión y consulta de competencias informáticas personales y grupales.  
<br>
![](header.png)

## Objetivo
CompetenciApp se encarga de almacenar diferentes competencias en una **base de datos vectorial**. Las relaciones entre competencias son calculadas mediante un modelo de **inteligencia artificial**, con el fin de ofrecer al usuario relacionar o buscar competencias que podrían ser similares a las suyas. También incluye un **sistema de usuarios**, que facilita conocer las aptitudes de potenciales compañeros/as de proyectos, como también poder añadir competencias que el usuario haya aprendido.

## Stack
- **Front-end:** **Python** ([Django](https://www.djangoproject.com/))
- **Back-end:** Base de datos [PostgreSQL](https://www.postgresql.org/), conectada con el **ORM** de Django. **Sistema vectorial** soportado mediante [pgvector-python](https://github.com/pgvector/pgvector-python)
- **Modelo de IA:** [mxbai-embed-large v1](https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1) para la vectorización de tokens y [Llama 3.2](https://www.llama.com/) para el chatbot, ambos ejecutados mediante el Framework [Ollama](https://ollama.com/).

## Funcionalidades
- Sistema de registro de usuarios
- Consultar las competencias de cualquier usuario
- Añadir a tu usuario nuevas competencias que hayas aprendido 
- Inserción y vectorización de competencias nuevas en la base de datos
- Ver qué usuarios comparten la competencia buscada

## Comportamiento de la base de datos
La base de datos soporta dos competencias diferentes: **Lenguajes de programación** (más general) y **Librerías** (más específica); sin embargo, ambas están relacionadas ya que a cada librería se le asocia un lenguaje. A cada usuario se le asocian una serie de lenguajes y/o librerías, y calculando las **distancias** de los vectores de otras competencias, se puede obtener el nivel de similitud que tienen entre ellas. Cuanto más corta sea la distancia entre dos vectores, más similares serán las competencias.

## Prototipo de datos
Mendiante ficheros .csv, se pueden inicializar unos **datos de prueba**. Estos datos son **vectorizados** por la IA y añadidos a la base de datos. Los ficheros .csv contienen datos de lenguajes, librerías, usuarios y de la relación que tienen entre ellos, y ofrecen una forma de ver cómo la aplicación podría funcionar con varios usuarios y competencias diferentes. Los ficheros .csv se encuentran en `resources/`

## Build
### Docker 
En la raíz del repositorio, ejecuta el siguiente comando:
`docker build -t Sprinter05/competenciapp:v1 .`

Este comando genera la **imagen de Docker** del proyecto. Antes de ejecutarla, se deben definir las siguientes **variables de entorno** en un fichero llamado `.env` en la raíz del proyecto:

```
OLLAMA_HOST = <ip>
POSTGRES_IP = <ip>
POSTGRES_PORT = <puerto>
POSTGRES_DB = <nombre_db>
POSTGRES_USER = <usuario_db>
POSTGRES_PASSWORD = <contraseña_db>
```

Una vez hayas definido las variables de entorno y hayas obtenido la imagen, ésta se puede ejecutar desde **Docker CLI**. La WebApp se ejecutará en el puerto `8000` y estará lista para ser utilizada.

### Ejecución en local
- Si lo necesitas, crea un **entorno virtual** de Python
- Instala los requerimientos con `pip install -r requirements.txt`
- Crea las migraciones de la base de datos con `python manage.py makemigrations core` y aplícalas con `python manage.py migrate`
- Antes de ejecutar, asegúrate que las variables de entorno necesarias (mostradas arriba) están definidas en el fichero de variables de entorno `.env`
- Finalmente, inicia el servidor con `python manage.py runserver`

## Dependencias y requerimientos
Consulta `requirements.txt` para obtener informacíon sobre los requerimientos del programa.

## Codeowners
Este proyecto fue realizado durante el evento [HackUDC 2025](https://hackudc.gpul.org/), en la [Universidade da Coruña](https://www.udc.es/), por el siguiente grupo de desarrolladores:

- [dza205 (Daniel Deza Prieto)](https://github.com/dza205)
- [markelmencia (Markel Mencía)](https://github.com/markelmencia)
- [sprinter05 (Sprinter)](https://github.com/Sprinter05)
- [yagueto](https://github.com/yagueto)

Más información sobre contribuciones individuales en `CONTRIBUTORS.md`

## Licencia
Este repositorio sigue la GNU General Public License (GPLv3). Se permite la copia y distribución de copias literales de esta licencia, pero no se permite su modificación. Para más información, consulta `LICENSE`

## Links externos de interés
- [Repositorio de pgvector (original, no Python support)](https://github.com/pgvector/pgvector)
- [Setup de mxbai-embed-large con Ollama](https://ollama.com/library/mxbai-embed-large)
- [Explicación de bases de datos vectoriales](https://www.cloudflare.com/learning/ai/what-is-vector-database/)
