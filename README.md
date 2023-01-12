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

- `SECRET_KEY` = 'secret_key'

    A secret key for a particular Django installation is used to provide cryptographic signing. [More details](https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-SECRET_KEY).

- `DATABASE_URL` = sqlite:////home/user/project/db.sqlite3

    SCHEMA and PATH to Database based on [type-casting methods of environ.Env](https://django-environ.readthedocs.io/en/latest/types.html#environ-env-db-url)

___Variables with predefined default values___

- `DEBUG` = False

    A boolean that turns on/off debug mode.

- `ALLOWED_HOSTS` = 'localhost', '127.0.0.1'

    A list of strings representing the host/domain names that this Django site can serve.

- `STATIC_URL` = '/static/'

    URL to use when referring to static files located in STATIC_ROOT.

- `STATIC_ROOT` = 'static/'

    The absolute path to the directory where collectstatic will collect static files for deployment.

- `MEDIA_URL` = '/media/'

    URL that handles the media served from MEDIA_ROOT, used for managing stored files. It must end in a slash if set to a non-empty value.

- `MEDIA_ROOT` = 'media/'

    Absolute filesystem path to the directory that will hold user-uploaded files.

- `LANGUAGE_CODE` = 'en-us'

    A string representing the language code for this installation. This should be in standard language ID format.

- `USE_I18N` = True

    A boolean that specifies whether Django’s translation system should be enabled. 

- `USE_TZ` = True

    A boolean that specifies if datetimes will be timezone-aware by default or not. If this is set to True, Django will use timezone-aware datetimes internally.

- `TIME_ZONE` = 'UTC'

    A string representing the time zone for this installation. See the [list of time zones.](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)

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

## Add location using command

There is an additional utility `load_place` to help in uploading json data into database.

To upload data use manage utility load_place with json path as a parameter:

```bash
python manage.py load_place https://your.json.url
```

JSON schema for location:

```bash
{
    "title": "Title of the location",
    "imgs": [
        "https://link.to.image.1",
        "https://link.to.image.2"
    ],
    "description_short": "Summary for the location or event",
    "description_long": "Full description",
    "coordinates": {
        "lng": longitude_value,
        "lat": latitude_value
    }
}
```
