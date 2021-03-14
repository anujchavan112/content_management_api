# content managment api usning django-rest-framework #
 ### Problem Statement : https://docs.google.com/document/d/1F90KvSqxxPzIRyeX7kD3wULrT0xNJMLdIgGVHq4KMxk/edit ###

 # Installation #  
### Download this repository and change into directory of project. Then use pip to install all required pacakages : 
```
pip install -r requirements.txt
```
###

## Files and Directory Structure ##
```
content_management_api:This is the root folder of this project.
|__contentapi:This is main api folder.
|__contentmanager:This folder contains essential settings and configuration files of project.
```
## Launching the API ## 
cd into the root folder of the project and run the following command:
```
python manage.py runserver
```
## Routes ##
### 127.0.0.1:8000/api/register/  ###
POST request: Register a new user to get back user details and token
### 127.0.0.1:8000/api/login/ ###
POST request: Login an existing user to get token

### 127.0.0.1:8000/api/content/ ###
Protected Route, need to provide token in Authorization HTTP header before using
GET request: View All contents created by user
POST request: Add a new content
### 127.0.0.1:8000/api/content/content_id/ ###
Protected Route, need to provide token in Authorization HTTP header before using
DELETE request: Delete particular content by id
UPDATE request: Update particular content by id

## Searching and Filtering ##
Search fields by specifying fields in route followed by suffix '__icontains' followed by your desired query.
Example: 127.0.0.1:8000/api/content/?title__icontains=MyPostj&body__icontains=Post&summary__icontains=Summary&categories__icontains=Sports

## Creating Admin via seeding ##
To create an Admin user via seeding, run the following command:
```
python manage.py createsuperuser
```
