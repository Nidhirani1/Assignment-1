# Q1. What is Flask Framework? What are the advantages of Flask Framework?
# Flask Framework:
# Flask is a lightweight, open-source web framework written in Python. It is classified as a microframework, meaning it doesn't require particular tools or libraries, making it easy to extend with third-party plugins. Flask provides the essentials for building web applications, such as URL routing, template rendering, and request handling, but leaves developers the flexibility to add other components as needed. It is based on WSGI (Web Server Gateway Interface) and Jinja2 templating engine.

# Advantages of Flask:

# Lightweight and Minimalistic: Flask is simple to set up and does not impose any restrictions on the structure of the application, allowing developers to create custom solutions.
# Flexibility: Flask gives developers more control over how to build their applications and which libraries or tools to use.
# Extensibility: Flask supports extensions to add functionalities like authentication, database integration, form validation, and more.
# Easy to Learn: Flask's minimalism makes it a great choice for beginners, and its well-documented and intuitive structure helps developers get up to speed quickly.
# Built-in Development Server: Flask comes with a built-in development server, making it easy to test applications locally without the need for a full-scale web server.
# RESTful Request Dispatching: Flask is well-suited for creating RESTful APIs, with tools to easily handle HTTP requests and responses.
# Jinja2 Templating: Flask uses the Jinja2 templating engine, which allows dynamic rendering of HTML templates and includes features like template inheritance and control structures.












# Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.
# Here’s a basic Flask application to display "Hello World!!":

# python

# from flask import Flask

# # Create a Flask application instance
# app = Flask(__name__)

# # Define a route for the root URL
# @app.route('/')
# def hello_world():
#     return 'Hello World!!'

# # Run the application
# if __name__ == "__main__":
#     app.run(debug=True)
# To run this code, make sure Flask is installed by running pip install Flask. Once you run the code, open your browser and visit http://127.0.0.1:5000/ to see the "Hello World!!" message.

# In Jupyter Notebook, you can run this cell and follow the instructions to take a screenshot of the output when it's displayed in your browser.







# Q3. What is App routing in Flask? Why do we use app routes?
# App Routing in Flask:
# App routing refers to the mechanism that maps a URL to a specific function in a Flask application. Routes are created using the @app.route() decorator, which binds a URL to a Python function. When a user visits a specific URL, the corresponding function is executed, and the response is returned to the browser.

# Why We Use App Routes:

# Defining URL Endpoints: Routes are used to define how different URLs (or paths) in your application are handled and what content is returned for each URL.
# Separation of Concerns: Routing allows for clean and organized code by separating the logic for each URL.
# Flexibility: Different routes can have different HTTP methods (GET, POST, etc.), making it easy to handle various types of requests.
# Dynamic URLs: Routes can include dynamic components like parameters (e.g., @app.route('/user/<username>')), enabling flexible URL patterns.











# Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/” route to show the following details:
# Company Name: ABC Corporation
# Location: India
# Contact Detail: 999-999-9999
# Here’s the code to create the required routes:

# python# Copy
# from flask import Flask

# # Create a Flask application instance
# app = Flask(__name__)

# # Route to display welcome message
# @app.route('/welcome')
# def welcome():
#     return 'Welcome to ABC Corporation'

# # Route to display company details
# @app.route('/')
# def company_info():
#     return '''
#     Company Name: ABC Corporation<br>
#     Location: India<br>
#     Contact Detail: 999-999-9999
#     '''

# # Run the application
# if __name__ == "__main__":
#     app.run(debug=True)
# The /welcome route will show the message "Welcome to ABC Corporation".
# The / route will display company details.
# Once you run the application, navigate to http://127.0.0.1:5000/ and http://127.0.0.1:5000/welcome in your browser to see the respective outputs.

# Attach a screenshot in Jupyter Notebook by running this cell and displaying the results in the browser.











# Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.
# url_for():
# In Flask, the url_for() function is used to build a URL for a specific endpoint (a route function). It dynamically generates URLs based on the name of the function associated with the route, which is useful in templates or when you need to create URLs programmatically. It can also handle URL parameters for dynamic routes.

# Here’s a Python code to demonstrate the working of url_for():

# python

# from flask import Flask, url_for

# # Create a Flask application instance
# app = Flask(__name__)

# # Route to display homepage
# @app.route('/')
# def home():
#     return 'Home Page'

# # Route to display about page
# @app.route('/about')
# def about():
#     return 'About Page'

# # Route to demonstrate url_for usage
# @app.route('/show-url')
# def show_url():
#     # Build URL for the "about" page using url_for
#     about_url = url_for('about')
#     return f'The URL for the About page is: {about_url}'

# # Run the application
# if __name__ == "__main__":
#     app.run(debug=True)