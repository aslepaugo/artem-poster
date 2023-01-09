# [Afisha from Artem "Artem Poster"](https://aslepaugo.pythonanywhere.com)

It's an interactive map to track and find events, interesting places and some zones for relax.

Demo of this site is available [here](https://aslepaugo.pythonanywhere.com). to get access to admin panel for content creation go to [aslepaugo.pythonanywhere.com/admin/](https://aslepaugo.pythonanywhere.com/admin/).

## How to add new location

1. Enter into the admin panel with provided lgin and password.

_image_

2. Go to Panel *PLACES* and then click Add.

_image_

3. Fill all info required as in the example below.

_image_

## How to edit location

Open location from the list. And edit as you wish

_image_


## Project setup

You should install Python3.

1. Install required dependencies.

```bash
pip install -r requirements.txt
```

2. Create `.env` file with the following variables:

 ___Mandatory variables___

```bash 
SECRET_KEY = 'secret_key'
DATABASE_URL = sqlite:////home/user/project/db.sqlite3
```

___Variables with predefined default values___

```bash
DEBUG = False
ALLOWED_HOSTS = 'localhost', '127.0.0.1'
STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_TZ = True
TIME_ZONE = 'UTC'
```

3. Apply migrations.

```bash
python3 manage.py migrate
```

4. Create super user (admin).

```bash
python3 manage.py createsuperuser
```

5. Start server locally

```bash
python3 manage.py runserver
```
