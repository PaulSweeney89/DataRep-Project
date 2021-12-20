# DataRep-Project


**Data Representation Project 2021**

*Develop a program that demonstrates the use of creating & consuming RESTful APIs*

- - - -

## Introduction

This project forms part of theData Representation module for 2021, please refer to the [project.pdf](https://github.com/PaulSweeney89/DataRep-Project/blob/main/Project%20Description.pdf) document included in this repository for the full project outline & instructions.

The main objectives of the project include:

1. Create a basic Flask server that has a REST API, (to perform CRUD operations).
2. Create one database table and accompanying web interface. 
3. Use AJAX calls, to perform the CRUD operations.

## Repository Files & Folders
List of files & folders contained within the Github Repository:

- *data folder*
    - **embodiedCarbonDB.sql** -  backup or restore file of the MySQL database.
    - **iceDB.csv** - a cleaned csv file version of The Inventory of Carbon and Energy (ICE) Database V3.0, available free on the [Circular Ecology website](https://circularecology.com/embodied-carbon-footprint-database.html).
    - **iceDB.xlsx** - original downloaded xlsx file version of the ICE Database V3.0.
- *staticpages folder*
    - **index.html** - main html page displaying the Embodied Carbon Database
    - **references.html** - html page with link to source database & additional useful links.
- **.gitignore file** - specifies files to be untracked by git.
- **DBconfigTemplate.py** - MYSQL database configuration template file.
- **IceDB.ipynb** - Jupyter Notebook used for reviewing & cleaning the original downloaded xlsx ICE database.
- **Project Description.pdf** -  - full description of the Machine Learning & Statistics assessment & objectives.
- **carbonDao.py** - python script to connect to & perform operations (CRUD) on the MYSQL *embodiedCarbon DB* database.
- **createDB.py** - python script use to create the MYSQL *embodiedCarbonDB* Database.
- **createTable.py** - python script to create the *iceData* table in the *embodiedCarbonDB* MYSQL Database from the *iceData.csv* file.
- **README.md** - This README markdown file.
- **requirements.txt** - list of all Python dependencies used within the web application.
- **server.py** - Python Flask Web Application

## Instructions on running the Web Application

1. Download this repository to your selected folder using the git clone command within the terminal command line:

    ```$ git clone git@github.com:PaulSweeney89/DataRep-Project.git```

2. Create the MYSQL embodiedCarbonDB database:

    2.1 Update the user specific MYSQL Database configuration properties in the *DBconfigTemplate.py* file.
    ```
    mysql = {
	"host":[host], 
	"user":[username],
	"password":[MYSQL database password],
	"database":"embodiedCarbonDB"
    }
    ```
    Save & rename file to DBconfig.py. 

    2.2 Run the createDB.py script to create the *embodiedCarbonDB* Database:

    ```$ python createDB.py```

    2.3 Run the createTable.py script to create & populate the *iceData* within the *embodiedCarbonDB*.

    ```$ python createTable.py```

    Alternatively to steps 2.2 & 2.3, the embodiedCarbonDB.sql file can be directly loaded into MYSQL using:

    ```mysql embodiedCarbonDB < data/embodiedCarbonDB.sql``` - Linux/Mac

    ```mysql -p -u [user] embodiedCarbonDB < data/embodiedCarbonDB.sql``` - Windows

2. Set-up a virtual environment within the terminal command line:

    ```$ python -m venv venv```

    Activate the virtual environment:

    ```$ source venv/bin/activate``` - Linux / Mac

    ```.\venv\Scripts\activate.bat``` - Windows

3. Install the required python libraries from the requirements.txt file:

    ```$ pip install -r requirements.txt ```

4. Run the Flask server server.py:

    ```$ python server.py```

5. Load the web application, visit http://127.0.0.1:5000/index.html

6. To deactivate the virtual environment, use the command:

    ```$ deativate```

## References

**Embodied Carbon - The ICE Database**

The Inventory of Carbon and Energy (ICE) was developed by Dr Craig Jones, formerly of the University of Bath & Professor Geoff Hammond of the Sustainable Energy Research Team (SERT).
The latest version of the ICE Database can be downloaded from the following [link](https://circularecology.com/embodied-carbon-footprint-database.html)