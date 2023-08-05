# Django Admin Gift Card Crawler
**Django Gift Card Crawler** allows you to Crawl card and serial number from the share links &amp; extract (download) csv file of all data.

<br />

## Why Django Gift Card Crawler?

- Get many links from file (txt, csv, xls) in django admin panel
- Crawl all links and extract card &amp; serial numbers from all links
- Run Crawling process in different process so don't worry about system slow down. 
- Download the result of the content as csv file
- Simple interface
- Easy integration

> Currently, this system uses limited providers like `egift activationspot` & `claim egifterrewards`. If you know other providers, please introduce them to me so that I can add them to this package.

<br>

## How to use it

<br />

* Download and install latest version of Django Gift Card Crawler:

```bash
$ pip install django-gift-card-crawler
# or
$ easy_install django-gift-card-crawler
```

<br />

* Add `gift_card_crawler` application to the `INSTALLED_APPS` setting of your Django project `settings.py` file:

```python
INSTALLED_APPS = (
# ...
"gift_card_crawler.apps.GiftCardCrawlerConfig",
)
```

<br />

* Collect static if you are in production environment:
```bash
$ python manage.py collectstatic
```

* Clear your browser cache

<br />

## Start the app

```bash
# Set up the database
$ python manage.py makemigrations
$ python manage.py migrate

# Create the superuser
$ python manage.py createsuperuser

# Start the application (development mode)
$ python manage.py runserver # default port 8000
```

* Access the `admin` section in the browser: `http://127.0.0.1:8000/`

