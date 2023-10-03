# __PROYECTO FINAL__ - Matias Christello - _Comision 47665_

-----------------------
## _**Descripción**_

"_**PROYECTO POKEMON**_" es una aplicación desarrollada con Django que permite gestionar información relacionada con el mundo Pokémon. La aplicación ofrece las siguientes funcionalidades:

    * Gestionar Pokemones: Los usuarios pueden agregar Pokemones a la base de datos utilizando un formulario que recopila información como el nombre, el tipo y el ataque del Pokémon, defensa y health, y una imagen. Automáticamente se genera la fecha y hora en que fue creado.

    * Gestión de Entrenadores Pokémon: Los usuarios pueden crear perfiles de Entrenadores Pokémon, proporcionando detalles como el nombre, el apellido y su tipo de Pokémon favorito, además de seleccionar todos los pokemones que son parte de su colección.

    * Gestión de Gimnasios Pokémon: La aplicación permite crear gimnasios Pokémon, con información como el nombre, el tipo y el líder del gimnasio, mostrando los entrenadores disponibles que han sido creados con anterioridad.

    * Búsqueda de Pokémon: Los usuarios pueden buscar Pokémon por nombre y ver sus detalles.

    * Listado de Clases: La aplicación muestra un listado completo de todos los elementos en las tres clases: Pokémon, Entrenadores Pokémon y Gimnasios Pokémon.

    * Gestión de Usuario: Cada usuario puede crear una cuenta, loguearse y editar tanto su información de perfil, como su avatar.

## __Servidor__

La aplicación sigue la arquitectura MVT (Model-View-Template) de Django y se ejecuta en el servidor local utilizando el comando:

    > $ py manage.py runserver

## __Rutas Principales__

> Las siguientes son las rutas disponibles del proyecto, con sus respectivas funcionalidades.

    - Panel de Administración: http://localhost:8000/admin - Accede al panel de administración de Django para gestionar los datos de la aplicación:
        - SuperUser: Username: admin || Password: admin

    - Página de Inicio: http://localhost:8000/ - Página de inicio de la aplicación.

    - Endpoints:
        - Gestión de Pokemones: 
            - /pokemons/pokemonList - Listado de todos los Pokemons.
            - /pokemons/pokemonCreate - Formulario para crean nuevo pokemon.
            - /pokemons/pokemonDetail/<id> - Detalle del Pokemon solicitado mediante ID.
            - /pokemons/pokemonUpdate/<id> - Formulario para actualizar los datos de un Pokemon.
            - /pokemons/pokemonDelete/<id> - Borrar un Pokemon especificado mediante ID.

        - Gestión de Entrenadores: 
            - /trainers/trainerList - Listado de todos los entrandores Pokemon.
            - /trainers/trainerCreate - Formulario para crean nuevo Trainer.
            - /trainers/trainerDetail/<id> - Detalle del Trainer solicitado mediante ID.
            - /trainers/trainerUpdate/<id> - Formulario para actualizar los datos de un Trainer
            - /trainers/trainerDelete/<id> - Borrar un Trainer especificado mediante ID.

        - Gestión de Gimnasios:
            - /gyms/gymList - Listado de todos los Gimnasios Pokemon.
            - /gyms/gymCreate - Formulario para crean nuevo Gym.
            - /gyms/gymDetail/<id> - Detalle del gym solicitado mediante ID.
            - /gyms/gymUpdate/<id> - Formulario para actualizar los datos de un gym
            - /gyms/gymDelete/<id> - Borrar un Gym especificado mediante ID.

        - Gestión de Ususario:
            - /users/resgister - Formulario para crear una cuenta de usuario.
            - /users/login - Formulario para iniciar sesión.
            - /users/editProfile - Formulario para editar la información del usuario
            - /users/agregarAvatar - Formulario para agregar o cambiar el avatar del ususario.
            - /users/logout - Pagina de cierre de sesión.

        - Búsqueda de Pokémon:
            - /result/?query=''&element_type='' - Realiza busqueda por nombre de cualquier modelo de la base de datos: Trainers, Pokemons y Gyms.

        - About Me:
            - /aboutMe - Pequeña página con información acerca de mí, y links de interés.

## __Imagenes__
This site was built using [GitHub Pages](https://pages.github.com/).