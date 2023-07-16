Successfully created a flask restful API using OOPs 

1.Create a new Python virtual environment
2.Activate the virtual environment
3.Install Flask and PyMongo libraries in virtual environment
4.Create a database user in mongoDB database and create a collection users in this database
5.Run the .py file
6.Open Postman create new HTTP request
7. Copy the http link from terminal in request

To create new user :
  1. create a POST request to add new user and provide raw JSON containing the details of user
  2. http://127.0.0.1:5000/item
  3. Send the request
  4. New user got created in database

To get all users from database :
  1. Create GET request for getting all users
  2. http://127.0.0.1:5000/item
  3. You will get all users in database collection

To get a user with specific ID :
  1. HTTP request with GET method with specific ID
  2. http://127.0.0.1:5000/item/<id>
  3. You will get a user with specific id

To update a user with specific ID :
  1. HTTP request with PUT method with specific ID and provide a raw JSON containing the parameters which you want to update 
  2. http://127.0.0.1:5000/item/<id>
  3. User with given id will get updated

To delete a specific user :
  1. HTTP request with DELETE method with specific ID 
  2. http://127.0.0.1:5000/item/<id>
  3. User with given id will get deleted





  
