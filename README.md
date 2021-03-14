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
![check1](https://user-images.githubusercontent.com/44212979/111077278-02f02780-8516-11eb-838b-ace63bd4b818.png)!

### 127.0.0.1:8000/api/login/ ###
POST request: Login an existing user to get token
![check1](https://user-images.githubusercontent.com/44212979/111077436-c1ac4780-8516-11eb-8562-ebe463ea3881.png)

### 127.0.0.1:8000/api/content/ ###

#### Protected Route, need to provide token in Authorization HTTP header before using : ####

GET request: View All contents created by user
![check1](https://user-images.githubusercontent.com/44212979/111077526-2d8eb000-8517-11eb-9625-633fda4e93c8.png)

POST request: Add a new content
![check1](https://user-images.githubusercontent.com/44212979/111077579-6fb7f180-8517-11eb-842a-ee29ad286f43.png)

### 127.0.0.1:8000/api/content/content_id/ ###
#### Protected Route, need to provide token in Authorization HTTP header before using ####
GET request : Get the content by id
![check1](https://user-images.githubusercontent.com/44212979/111077846-ad694a00-8518-11eb-88b3-8c3c75edd688.png)

DELETE request: Delete particular content by id
![check1](https://user-images.githubusercontent.com/44212979/111077979-5dd74e00-8519-11eb-84af-7c1ac7d3ee01.png)

UPDATE request: Update particular content by id
![check1](https://user-images.githubusercontent.com/44212979/111077925-105ae100-8519-11eb-97f7-2bbf5e4ca07f.png)


## Searching and Filtering ##
Search fields by specifying fields in route followed by suffix '__icontains' followed by your desired query.
Example: 127.0.0.1:8000/api/content/?title__icontains=MyPostj&body__icontains=body&summary__icontains=dummary
![check1](https://user-images.githubusercontent.com/44212979/111078156-3634b580-851a-11eb-961b-743dc4525f52.png)



## Creating Admin via seeding ##
To create an Admin user via seeding, run the following command:
```
python manage.py createsuperuser
```


![check1](https://user-images.githubusercontent.com/44212979/111077125-4f873300-8515-11eb-86c7-f90d38355ef0.png)
