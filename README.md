# Twitter-bot
Bot de automatización para X (Twitter) desarrollado en Python con fines académicos .
Una herramienta de automatización para X (Twitter) escrita en Python, diseñada como proyecto académico para la carrera de Ingeniería en Sistemas.
Tabla de Contenidos
Descripción
Requisitos
Instalación
Autenticación
Uso Básico
Seguridad y Buenas Prácticas
Descripción
Este proyecto permite interactuar con la plataforma X (Twitter) mediante scripts de Python utilizando cookies de sesión para omitir los bloqueos tradicionales de credenciales. Permite realizar publicaciones automatizadas y gestionar tareas dentro de la plataforma con fines educativos y de prueba.
Requisitos
Python 3.10 o superior
Librería twitter-api-client
Una cuenta activa de X (Twitter)
Instalación
Clona este repositorio o descarga los archivos en tu equipo local e instala la librería requerida:
pip install twitter-api-client
Autenticación
Debido a las restricciones actuales de inicio de sesión de X por usuario y contraseña, este cliente utiliza cookies de sesión (auth_token y ct0).
Obtener las cookies desde el navegador:
Abre tu navegador e inicia sesión en x.com.
Abre las Herramientas de Desarrollador presionado F12 o Clic Derecho > Inspeccionar.
Dirígete a la pestaña Aplicación (o Almacenamiento) > Cookies > https://x.com.
Copia los valores de las llaves auth_token y ct0.
Uso Básico
Crea un archivo de ejecución (por ejemplo bot.py) y utiliza la siguiente estructura:
from twitter.account import Account

# Reemplaza con tus llaves correspondientes
cookies = {
    "auth_token": "TU_AUTH_TOKEN_AQUI",
    "ct0": "TU_CT0_AQUI"
}

# Inicializar cuenta
account = Account(cookies=cookies)

# Publicar un tweet
account.tweet("¡Hola mundo desde mi bot de Twitter!")

print("Tweet publicado con éxito.")


Seguridad y Buenas Prácticas
IMPORTANTE: Nunca subas tus cookies reales (auth_token o ct0) a tu repositorio de GitHub ni a ningún repositorio público. Las cookies de sesión otorgan acceso completo a tu cuenta.
