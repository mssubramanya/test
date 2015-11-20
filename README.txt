INTRODUCTION
------------

The test project module demonstrates the use of pyramid framework to develop a simple web site
that pre-populates a mongo database with two builtin users Try1 and Try2 with passwords 123 and 456
for adding more users open users.py and having the following arguments :
Username, password, city, Country

ex:
  ,User('Subbu','789','Bangalore','India')
will add a user by name Subbu with password 789.

REQUIREMENTS
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
This sample web site requires the following modules:

Python 3.5.0:
=============
Python is one of the most often used Object oriented programming language and is used 
from rapid prototyping to building full scale enterprise systems that cater to a wide 
variety of uses.

Depending on your OS and bitness of your Operating System download Python Version 3.5.0 from:
*    https://www.python.org/downloads/release/python-350/

Mongo Database:
===============
MongoDB is an open-source, document database designed for ease of development and scaling.
It is one of the foremost no-sql databases in the market that allows storage and 
retreival of data based on key:value pairs and helps in rapid prototyping.

Depending on your OS and bitness of your Operating System download Mongo Database 3.0.7 from:
*	https://www.mongodb.org/downloads#production

Pyramid:
========
Pyramid is a simple and easy to use web framework that allows rapid prototyping and scaling of 
web sites. Pyramid is a good goldilocks solution, in that the learning curve is little
and developers become productive very soon. Pyramid is a add-on package to python and can be 
installed via pip utility in python

INSTALLATION
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
Download and install Python 3.5.0 and Mongo database 3.0.7 from the above urls.
Download the five files to a seperate directory and then execute setup.bat file.

To Execute the web site run the command with administrator privileges:
				C:\test python MainFile.py

 *    There are six files that are packaged with this test web site.
 		* setup.bat:
			This file sets up the environment required to run this web site. It creates 
			python virtual environment that is used to host the other files.
			This file also copies the rest of the source files. It installs pyramid and 
			python wrapper over mongo databaseby itself.
		* MainFile.py:
			The core of the web site lies in this file and this is the file to be executed to run the 
			web site.
		* mongo_layer.py:
			This file defines the user class and also provides a database abstraction layer that 
			allows the rest of the python source follow business logic easily rather than get 
			tied up with database access logic.
		* strings.py:
			This file contains string literals that are used to render the web pages.
		* users.py:
			This file contains the sample users that get inserted into mongo db and are then available 
			for using this web site. 
			Login to the web site using these users.
FUTURE EXTENSIONS:
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
Pagination: 
Pagination will be added in a future version of this web site. In the method 
deserialize_all_users() in the class we can split the results of the method 
			results = list(self.dicts.find())
to 
			results = list(self.dicts.find()).split([prevCount:currentCount])
which will give a sub set of results in the list and we would then display the same in the UI.
Here prevCOunt would hold the previous number of users that were displayed, and  currentCount 
would be a constant that would be displayed in the UI.

Versioning:
Versioning will be based on the directory where the source files are placed. 
For Example:
	Version 1 would be placed in C:\test\Ver1
where Ver1 stands for version 1.
for Version 2 this would be:
	C:\test\Ver2

DEVELOPER
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------
Current Developer:
		Subramanya Mysore Srinivasa (ms.mssubramanya@gmail.com)
