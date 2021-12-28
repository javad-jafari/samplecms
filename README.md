# samplecms

This project is a simple store that includes:
- the login page
- the registration page
- first page
- the list of products
- details of the product
- the shopping cart
- its management panel uses the Django admin panel.
This project is dockerized , just need migrate and create user.


# how to  run this project
```
git clone https://github.com/javad-jafari/samplecms.git  
```

```
cd samplecms
```
```
touch .env.dev .envdb
```
paste in .env.dev django env variables and in .devdb postgres env 
for docker
then run :
```
docker-compose run web python manage.py makemigrations
```
```
docker-compose run web python manage.py migrate
```
for superuser
```
docker-compose run web python manage.py createsuperuser --user admin --email admin@info.com --password admin -y --noinput
```
finally:
```
docker-compose up
```




