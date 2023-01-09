# [Afisha from Artem "Artem Poster"](https://aslepaugo.pythonanywhere.com)

It's an interactive map to track and find events, interesting places and some zones for relax.

Demo of this site is available [here](https://aslepaugo.pythonanywhere.com). to get access to admin panel for content creation go to [aslepaugo.pythonanywhere.com/admin/](https://aslepaugo.pythonanywhere.com/admin/).

## How to add new location

1. Enter into the admin panel with provided lgin and password.

![image](https://user-images.githubusercontent.com/17562496/211249520-b2ca280b-0a75-4d40-b5ef-d4df8bb3f72d.png)

2. Go to Panel *PLACES* and then click Add.

![image](https://user-images.githubusercontent.com/17562496/211249577-746d6244-a268-4b63-ab0c-5b163a72907a.png)

3. Fill all info required as in the example below.

![image](https://user-images.githubusercontent.com/17562496/211249678-3e2efe71-e710-4d71-997e-2fad19aa558f.png)
![image](https://user-images.githubusercontent.com/17562496/211249700-14ffcaca-a6f8-4aa1-a8e0-4e095afc4d97.png)


## How to edit location

Open location from the list. And edit as you wish

![image](https://user-images.githubusercontent.com/17562496/211249764-5d887d35-5c33-4690-a308-43e0ad52c392.png)


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
