# SongsApp

## Despliegue local con Docker

Para desplegar la aplicación es necesario tener docker instalado, y seguir los siguientes pasos:

1. Copiar el repositorio  a tu carpeta local.
2. Para instalar las dependencias, en la raiz del proyecto ejecuta npm install
3. Ejecutar el comando docker compose up -d para levantar el contenedor docker
4. Asegurarse de tener instalado Node.js para ejecutar la API REST
5. Ejecutar el servidor ingresando en terminal
  cd Views, en la raíz del proyecto ejecutar npm run dev

## Descripcion del proyecto

SongsApp es una aplicación web de música que permite a los usuarios explorar canciones organizadas por género, reproducirlas y administrar sus listas de favoritos. La plataforma ofrece funciones de registro, inicio de sesión y personalización del perfil de usuario, brindando una experiencia musical personalizada.

##  Descripción de la base de datos

El proyecto utiliza **MongoDB** como sistema de gestión de bases de datos NoSQL para almacenar y administrar la información 
de los usuarios, las canciones disponibles y las listas de favoritos.

La base de datos está organizada en cinco colecciones principales, cada una encargada de almacenar información específica de la aplicación.

### Colecciones

#### `Usuario`

Almacena la información de los usuarios registrados en la plataforma, incluyendo sus datos personales y de perfil.

**Campos:**
- `id`: Identificador del usuario.
- `nombre`: Nombre completo del usuario.
- `apodo`: Nombre que se muestra en la plataforma.
- `correo`: Correo electrónico del usuario.
- `contraseña`: Contraseña de acceso.
- `genero`: Género indicado por el usuario.
- `foto_perfil`: Imagen de perfil del usuario.

#### `Cancion`

Contiene la información de las canciones disponibles en la plataforma, incluyendo sus datos descriptivos y la ubicación de sus archivos multimedia.

**Campos:**
- `id`: Identificador de la canción.
- `nombre`: Nombre de la canción.
- `autor`: Autor o artista de la canción.
- `portada`: Imagen de portada.
- `archivo_audio`: Ubicación del archivo de audio.
- `genero_id`: Identificador del género musical al que pertenece.

#### `Genero`

Almacena los géneros musicales utilizados para clasificar y organizar las canciones dentro de la plataforma.

**Campos:**
- `id`: Identificador del género.
- `nombre`: Nombre del género musical.

#### `ListaFavoritos`

Representa la lista de canciones favoritas de cada usuario. Permite identificar al propietario de la lista y almacenar su imagen de portada.

**Campos:**
- `id`: Identificador de la lista.
- `usuario_id`: Identificador del usuario propietario.
- `portada`: Imagen de portada de la lista.

#### `Favorito`

Relaciona las canciones con una lista de favoritos y permite conservar el orden en el que aparecen dentro de ella.

**Campos:**
- `id`: Identificador del registro favorito.
- `lista_id`: Identificador de la lista de favoritos.
- `cancion_id`: Identificador de la canción.
- `posicion`: Posición de la canción dentro de la lista.
