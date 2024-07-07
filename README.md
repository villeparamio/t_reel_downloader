# Instagram Reel Downloader Bot

Este bot de Telegram descarga Reels de Instagram utilizando la librería `instaloader`. Solo necesitas enviar el enlace del Reel y el bot lo descargará y enviará de vuelta.

## Características

- Descarga Reels de Instagram.
- Proporciona información del usuario que envía el enlace.
- Registra todas las actividades en un archivo de log.

## Instalación

1. Clona este repositorio:

```sh
   git clone https://github.com/tu_usuario/instagram-reel-downloader-bot.git
   cd instagram-reel-downloader-bot
```

2. Crea y activa un entorno virtual:

```sh
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```
3. Instala las dependencias:

```sh
pip install -r requirements.txt
```

4. Reemplaza `YOUR_TOKEN_HERE` en el código con el token de tu bot de Telegram.


## Uso

Ejecuta el bot:

```sh
python bot.py
```
## Comandos Disponibles

- /start: Da la bienvenida al usuario.
- /help: Proporciona información de ayuda.
- /chatid: Proporciona el ID del chat del usuario.

## Envío de Reels

Para descargar un Reel, simplemente envía el enlace del Reel de Instagram al bot. Asegúrate de que el enlace tiene el formato correcto:

```ruby
https://www.instagram.com/reel/C5UiWfWtvEI/?igsh=eXdxZ2JjMXp3OHk3
```

## Dependencias

- instaloader
- pyTelegramBotAPI
- logging
- os
- re

## Contribución

Si deseas contribuir, por favor haz un fork del repositorio y crea un pull request con tus cambios.
Licencia

Este proyecto está bajo la Licencia Apache 2.0.

## Donaciones

Si encuentras este proyecto útil y te gustaría apoyar su desarrollo y mantenimiento, considera hacer una donación. Tu apoyo será muy apreciado.

### PayPal
Puedes realizar tu donación a través de PayPal haciendo clic en el siguiente botón:

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?business=95M7L3UZENS6Q&no_recurring=0&currency_code=EUR)



Gracias por tu apoyo.
