# contentful-blog-app
Blog app developed with Django, Bulma CSS, Contentful & Heroku. Contentful is used for content infrastructure management for the application. 
The Contentful web app is an easy-to-use editor for authoring content. A non technical user easily create and update content on the application using Contentful.
Content published is automatically deployed to the web app using the content API.

## APIs
Contentful follows an API-first approach, which means that all of its functionality is provided by an API. Blog content (date, title, author etc) are modelled on the Contentful web app.
The Python SDK for Contentful is used to import the content as objects.

## Cloud Hosting
The application is hosted on Heroku. https://hidden-dawn-21749.herokuapp.com/

## Database
The application database is a Heroku Postgres db.

## CD Pipeline
The application uses a Heroku GitHub pipeline for continous development. Changes pushed to the main branch are automatically deployed to production.

## Frontend Development
The application was developed using Bulma CSS Framework template.

## environment variables
For security the application uses environment variables to store secret keys, passwords and other sensitive data.

