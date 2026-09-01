# Twitter-bot

Bot de automatización para X (Twitter) desarrollado en Python con fines académicos.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Diagrama de Flujo](#diagrama-de-flujo)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Autenticación](#autenticación)
- [Uso Básico](#uso-básic  o)
- [Seguridad](#seguridad)

---

## Descripción
Este proyecto permite interactuar con la plataforma X (Twitter) mediante scripts de Python utilizando cookies de sesión para omitir los bloqueos tradicionales de credenciales. Permite realizar publicaciones automatizadas y gestionar tareas dentro de la plataforma con fines educativos y de prueba.

---

## Diagrama de Flujo

<!-- Si exportaste tu diagrama de draw.io como imagen y la guardaste en una carpeta 'img', usa esta línea: -->
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
