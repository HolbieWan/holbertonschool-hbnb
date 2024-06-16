# HBnB Evolution: Part 1 (Model + API)
<br>

## Part 1 - BackEnd of the application

Welcome and thank you for your visit on this repo ! <br>
This is a collaborative student project for the Holberton School Thonon-les-Bains.<br>
The first part is mainly focused on creating a backend for an upcoming full stack project: an 'AirBnB' like application. We call it HBnB.
This part is mainly developped with Python and Flask.

<br>
<br>

<h2><em>-- GOAL OF THE PROJECT --</em></h2>
<br>

The main purpose of developing this backend is to establish a solid foundation for implementing our future online application. Thus, we have defined various Python classes and routes so that the application can be as dynamic as possible in the future. The application also features an 'image' system, allowing it to function on any type of operating system.

<br>

<h2><em>-- UML --</em><h2>

![alt text](<./pictures/UML_class.jpeg>)

<br>

<h2><em>-- REQUIREMENTS, INSTALLATION AND APPLICATION RUNNING --</em></h2>
<br>

- Use a **Linux** distribution *(Ubuntu 20 is highly recommended)*

- Clone our repository in the folder of your choice by following the next steps : 
<br>

```bash 
sudo apt-get install git  // (if git is not installed)
cd /$FolderOfYourChoice$/
git clone https://github.com/HolbieWan/holbertonschool-hbnb.git
```
<br>

- Run the server first with the following command : ```python app.py``` <br>

- Use "Postman" software to allow models and routes interact with *CRUD* methods (you also can use *curl* command instead when app is running if you are more familiar with)

<br>

<h2><em>-- COMPOSITION, FILES, OPTIONS AND EXAMPLES OF USE --</em></h2>

The main folder to focus on is : **app** <br>
<br> Inside this folder you will find :<br>
<br><em>**I - MODELS**</em><br>
<br>
&emsp;=> All the classes necessary to make the application work : 

* *USER*: User model that represents a user with an email, first name,
        and last name.
* *REVIEW*: Review model that represents a review for a place by a user.
* *PLACE*: Place model representing a rental property.
* *COUNTRY*: A class representing a country.
* *CITY*: A class representing a city.
* *AMENITY*: A class representing an amenity.
* *BASEMODEL* : A base class representing a model with common attributes and methods.<br>
&emsp; => <em>This one is vital to every classes above </em> 
<br>

<br><em>**II - API (routes)**</em><br>
<br>
**PLEASE REACH THE FOLLOWING ADRESS TO GET FULL DOCUMENTATION ABOUT HOW USING OUR API IN DETAILS (*when app is running*): ```http://127.0.0.1:5000/api/docs```**
<br>

&emsp;=> All the routes necessary that use classes and make the application work : 

* *USERS ROUTES*: Create User Route, Get all Users Route, Get User by ID Route, Update User Route, Delete User Route
* *REVIEW ROUTES*: Create Review Route, Get Reviews by User Route, Get Reviews by Place Route, Get Review by ID Route, Update Review Route, Delete Review Route, Get All Reviews Route
* *PLACE ROUTES*: Create Place Route, Get Places Route, Get Place by ID Route, Update Place Route, Add Amenity to Place Route, Remove Amenity from Place Route, Delete Place Route 
* *COUNTRY ROUTES*: Create Country Route, Get All Countries Route, Get Country by Code Route, Update Country Route, Delete Country Route
* *CITY ROUTES*: Create City Route, Get All Cities Route, Get City by ID Route, Update City Route, Delete City Route
* *AMENITY ROUTES*: Create Amenity Route, Get All Amenities Route, Get Amenity by ID Route, Update Amenity Route, Delete Amenity Route


<br>
<br>

*FEW EXAMPLES OF USE (NON EXHAUSTIVE LIST)* 

<br>
 
&emsp;**\_CREATE A USER\_**

&emsp;*Route*: /users <br>
&emsp;*Method*: POST <br>
&emsp;*Purpose*: Creates a new user with provided details. <br>
&emsp;*Request* BODY (POSTMAN, or CURL) <br><br>

```bash
{
  "email": "john.doe@example.com",
  "first_name": "John",
  "last_name": "Doe"
}
```
<br>

&emsp;**\_GET ALL USERS\_**

&emsp;*Route*: /users <br>
&emsp;*Method*: GET <br>
&emsp;*Purpose*: Retrieves a list of all users. <br><br>
```bash
GET /users
Response: 
[
  {
    "email": "john.doe@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "created_at": "2024-06-16T12:00:00Z",
    "updated_at": "2024-06-16T12:00:00Z"
  },
  {
    "email": "jane.smith@example.com",
    "first_name": "Jane",
    "last_name": "Smith",
    "created_at": "2024-06-15T10:00:00Z",
    "updated_at": "2024-06-15T10:00:00Z"
  }
]
```
<br>

&emsp;**\_UPDATE AMENITY ROUTE\_**

&emsp;*Route*: /amenities/<amenity_id> <br>
&emsp;*Method*: PUT <br>
&emsp;*Purpose*: Updates details of a specific amenity. <br>
<br>
&emsp; => *REQUEST BODY*
```bash
{
  "name": "Heated Swimming Pool"
}
```
&emsp; => *RESPONSE*
```bash
Response:
{
  "id": "1",
  "name": "Heated Swimming Pool",
  "created_at": "2024-03-12T12:00:00Z",
  "updated_at": "2024-06-16T20:13:00Z"
}
```
<br>

&emsp;**\_DELETE CITY ROUTE\_**

&emsp;*Route*: /cities/<city_id> <br>
&emsp;*Method*: DELETE <br>
&emsp;*Purpose*: Deletes a specific city by its ID. <br>
```bash
DELETE /cities/1
Response: No content (204)
```

<br>

<br><em>**III - DOCKER (MAKE AN IMAGE OF THE APP)**</em><br>
<br>

The application includes a ```Dockerfile``` alongside the app folder. This *Dockerfile* allows users to create a Docker image of the app, enabling the application to run on any operating system that supports Docker.
<br>

*BUT...*
<br>
### How it works :question: 

<br>

1/ **Install Docker**: <br> 

First, you need to install Docker on your operating system. You can find comprehensive installation guides on the [Docker website](https://www.docker.com) <br>

2/ **Build the Docker Image**: <br>

Open a terminal and navigate to the directory containing your Dockerfile. Then, build the Docker image using the following command: <br>
```bash
docker build -t <your_image_name> .
```  
**Note**: Ensure you include the space and the dot . after your image name. <br>
<br>

3/ **Run the Docker Container**: <br>

After successfully building the image, run a container using the image with the following command: <br>
```bash
docker run -p 8000:8000 <your_image_name>
```
This command maps port 8000 of your local machine to port 8000 of the container.
 <br><br>

4/ **Access the Application**: <br>

The application is now running inside a Docker container. You can access it by navigating to http://localhost:8000 in your web browser.
<br>
<br>

Now, your application is containerized and can run consistently across different environments. 

<br>

<h2><em>-- AUTHORS --</em></h2>
<br>

[Cédric Tobie](https://github.com/HolbieWan/) <br>
[Douglas Dachicourt](https://github.com/Douglas-Dachicourt) <br>

<br>

*#C23* cohort from *Thonon-les-Bains* :fr: