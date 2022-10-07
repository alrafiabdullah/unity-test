# Unity

##

## Requirements

- Create and activate a virtual environment
- Run `pip install -r requirements.txt` to install dependencies
- Create a `.env` file and add the following data:

```
DJANGO_SECRET_KEY=
PG_NAME=
PG_USER=
PG_PASSWORD=
PG_HOST=
PG_PORT=
PG_TEST_NAME=
```

- Run `python manage.py migrate` to create the database
- Run `python manage.py runserver` to start the server
- The server will start in [http://127.0.0.1:8000](http://127.0.0.1:8000)

##

Creating an email list with consent to target with promotional emails is a cost effective way to increase sales. Infact, studies have shown that email
marketing has ~42000% ROI. Unity is a simple seller tool that helps an online store maintain an email list. It consists of a widget installed an online store and a Django application which will provide the ability to manage these new customers.

##

![Seller Tool](cac-widget.png)

##

Here is the brief functionality of the seller tool

- A widget pops up on the online store and prompts the store visitor to signup using email address
- The signup data will be sent to an API provided by the Django app (Unity backend)
- The app stores the data in its own model
- The app exposes a view which
  1.  lists down the emails in the reverse chronological order of their timestamp
  2.  Shows the number of new emails in the current calendar month
- The app sends an email to the seller every Monday and Wednesday including the statistics around the email list

##

## Task

Build a Django application with following functionalities

1. Exposes an API to store the emails. Feel free to use Django REST Framework
2. A view to list down the emails in the reverse chronological order and show the number of new emails added this calendar month
3. Integrate the api with the email collection widget present in this project.
4. Bonus - setup a celery task that runs every Monday and Wednesday and prints the number of new emails added in the current calendar month to the console.

##

## Steps

1. Download the attached zip file which is a git repo. The repo already contains the following
   - `widgets` - a Javascript project for creating the widget. This includes the webpack based toolchain to generate the widget's JS file. If you are not comfortable with all these, don't worry about it.
   - `static/js/e-widgets.v1.min.js` - The widget's javascript file to be included in the seller's online store. You need to configure your Django project to serve this static file to any online store.
   - `widgets/test/store.html` - A test HTML file which includes the widget.
2. Create a Django project inside the repo.
3. Create Django app with name - unity.
4. Create a data model to store the emails.
5. Expose an REST API to be used by the widget to submit the email data.
6. Create a Django view for listing the emails. As shown in the figma file for reference : https://www.figma.com/file/CYhfwmtEK4Xm7ZsNM6Swej/Unity?node-id=0%3A1
7. Bonus - Create a celery periodic task that does what is specified above

##

## Submission

Push it to your own git repo and share a link. This way you have a useful, working project against your profile!

##

```

```
