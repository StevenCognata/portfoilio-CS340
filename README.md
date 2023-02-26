# portfoilio-CS340 
README - SNHU CS-340 Dashboard

1. Use these guidelines to create programs that are easy to maintain, readable, and adaptable: Use version control, write clear, legible code, test it, 
document it, use meaningful names and comments, keep it simple, and be open to criticism.

2. As a computer scientist, problem-solving entails dissecting issues into smaller, more manageable components, coming up with a strategy, 
carrying it out, and testing the outcome.I comprehended the client's needs for the Grazioso Salvare project, devised a plan, and used the right technologies to construct the database. This assignment demanded greater practical problem-solving abilities compared to prior courses. 
To assure quality and dependability in the future, I would solicit client input, conduct in-depth testing, and adhere to best practices for software development.

3.Computer scientists create software, hardware, algorithms, and creative fixes for a range of issues. My work on the database project might, in the instance of Grazioso Salvare, aid them in operating more successfully, making wiser judgments, and succeeding more in their commercial operations. 
The project can enhance the dependability and correctness of corporate information, promote teamwork, and offer insights and analytics.






Steven Cognata
Southern New Hampshire University
CS-340-T3339
Professor Paruchuri
February 19, 2023


This project is an online dashboard for investigating and displaying data from animal shelters. The Dash framework, which offers a quick and flexible approach to build web apps using Python, is used to build the dashboard. Using a unique AnimalShelter class, the dashboard gets data from a MongoDB database and shows it in a datatable. The user may choose columns in the datatable for additional analysis and filter the data by animal kind using a radio button. The dashboard also contains a graph and a map for displaying the data.

Required Functionality
The dashboard should provide the following functionality:

Display a datatable of animal shelter data from a MongoDB database
Filter the data by animal type using a radio button
Select columns in the datatable for further analysis
Visualize the data using a graph and a map
Screenshots of the dashboard are available in the screenshots directory.

Tools Used
The following tools were used to develop this project:

Python 3.9
Dash 2.0
Plotly 5.4
Dash Leaflet 0.2
MongoDB 5.0
PyMongo 3.12
Python was selected as the primary programming language due of its widespread use and simplicity. Because of their strong data visualization capabilities and simple Python interaction, Dash and Plotly were selected. The map component was created with Dash Leaflet. MongoDB was selected as the development's model component because to its adaptability and scalability, as well as its simplicity in integrating with Python via PyMongo.

MongoDB
A NoSQL database called MongoDB is made for swiftly and effectively storing and retrieving huge amounts of data. It offers a flexible schema that makes it simple to alter data structures without the use of intricate migration scripts. Moreover, MongoDB offers a powerful query language that enables in-depth data retrieval and analysis.

Data on animal shelters was stored and retrieved in this project using MongoDB. Using PyMongo, the AnimalShelter class was utilized to communicate with the MongoDB database. The class offers ways to add, read, update, and remove data from the database. MongoDB's adaptability and scalability make it the perfect solution for this project because the database's capacity may be simply increased or decreased.

Dash Framework
Python module called the Dash framework offers a quick and adaptable solution to build web apps. It adheres to the Model-View-Controller (MVC) design pattern, where the controller controls user input and oversees the interaction between the model and the view, while the model represents the data and the view the user interface.

Dash was utilized in this project to design the user interface and control how the user interacted with the data. The dashboard in a Jupyter notebook was operated using the JupyterDash class. The user interface elements, such as the datatable, radio button, graph, and map, were made using the html and dcc modules. The callback functions that update the state were made using the Input, Output, and State decorators.

Resources
The following resources and software applications were used in this project:

Python: https://www.python.org/
Dash: https://dash.plotly.com/
Plotly: https://plotly.com/
Dash Leaflet: https://dash-leaflet.herokuapp.com/
MongoDB: https://www.mongodb.com/
PyMongo: https://pymongo.readthedocs.io/en/stable/
Jupyter Notebook: https://jupyter.org/


