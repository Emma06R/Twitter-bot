# Twitter-bot

Bot de automatización para X (Twitter) desarrollado en Python con fines académicos.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Diagrama de Flujo](#diagrama-de-flujo)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Autenticación](#autenticación)
- [Uso Básico](#uso-básico)
- [Seguridad](#seguridad)

---

## Descripción
Este proyecto permite interactuar con la plataforma X (Twitter) mediante scripts de Python utilizando cookies de sesión para omitir los bloqueos tradicionales de credenciales. Permite realizar publicaciones automatizadas y gestionar tareas dentro de la plataforma con fines educativos y de prueba.

---

## Diagrama de Flujo

![Diagrama de Flujo del Bot](img/diagrama_bot.png)

*Representación gráfica del flujo del sistema:*

```mermaid
graph TD
    A([Inicio]) --> B[Importar twitter.account]
    B --> C[Definir cookies: auth_token y ct0]
    C --> D[Inicializar Account con cookies]
    D --> E{¿Sesión Válida?}
    E -- Sí --> F[Ejecutar account.tweet]
    F --> G[Imprimir mensaje de éxito]
    G --> H([Fin])
    E -- No --> I[Error de Autenticación / JSON]
    I --> H

Requisitos
Python 3.10 o superior

Librería twitter-api-client

Una cuenta activa de X (Twitter)

Instalación
Instala la librería requerida ejecutando en tu terminal:
pip install twitter-api-client
Autenticación
Debido a las restricciones actuales de inicio de sesión por usuario y contraseña, este bot utiliza cookies de sesión (auth_token y ct0).

Obtener cookies desde el navegador:
Abre tu navegador e inicia sesión en x.com.

Presiona F12 o da clic derecho y selecciona Inspeccionar.

Ve a Aplicación (o Almacenamiento) > Cookies > [https://x.com](https://x.com).

Copia los valores de las llaves auth_token y ct0.

Uso Básico
Crea un archivo llamado bot.py con el siguiente código:
from twitter.account import Account

# Reemplaza con tus cookies correspondientes
cookies = {
    "auth_token": "TU_AUTH_TOKEN_AQUI",
    "ct0": "TU_CT0_AQUI"
}

# Inicializar cuenta
account = Account(cookies=cookies)

# Publicar un tweet
account.tweet("¡Hola mundo desde mi bot de Twitter!")

print("Tweet publicado con éxito.")
