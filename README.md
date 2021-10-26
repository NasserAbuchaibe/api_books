# API Books

## **Description**  

This application consists of a web service with an endpoint that receives a request  
 and returns requested data about the author of books and a webapp to consult the information  
 about the author by entering the name in the application.  

## **Enviroment:**

### **Backend:**
* Python
* Django
* Dajngo-rest-framework
s
### **Frontend:**
* HTML5
* Boostrap

## This project was developed in a virtual environment using virtualenv with python 3.8.5 

### For testing purposes, I suggest using virtualenv and installing the necessary libraries using the requirements.txt file. 

## **To test the web service:**

Once the server is up using postman, you can make a GET request to the endpoint  
with the name of the author to consult using the following format:

### endpoint:  http://127.0.0.1:8000/books/

```
{
   "author": "garcia marquez"
}
   
```

You should receive a JSON with the information of the query or with the status code if the query fails.  


<img src="https://i.imgur.com/Kvevj9b.png">  

## **To test the webApp:**

### In the browser enter the following link :  

```
http://127.0.0.1:8000/qbooks/
```  

### Use the form to consult by entering the name of the author


<img src="https://i.imgur.com/98PSAFF.png">  

### In the webapp a table will be displayed with the author's books or books about the consulted author.

<img src="https://i.imgur.com/WP0H30L.png">  





## **Author:**
* **Nasser Abuchaibe** - [NasserAbuchaibe](https://github.com/NasserAbuchaibe)