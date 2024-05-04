# In your Django app, create a new Python file called "populate_projects.py" inside a "management/commands" directory.

# myapp/management/commands/populate_projects.py

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from portfolio.models import Project

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        help = 'Populates the database with initial projects'

        # Define the list of projects
        projects = []

        # Extract information from the HTML blocks and populate the projects list
        projects_html = """
        <div id="to-do-div" class="proj">
            <h2><a href="https://to-do-list-manager-nu.vercel.app/" target="_blank">TO DO MANAGER</a></h2>
            <div id="todo-flex" class="proj-flex">
                <img src="../static/images/Task Manager.png" alt="screenshot of a website" class="screenshots">
                <div class="description">
                    <p>To-Do List Manager is the ultimate task management solution designed for users seeking 
                        simplicity and efficiency. Say goodbye to the complexities of task organization and
                        hello to a streamlined, hassle-free experience. With its intuitive interface and 
                        robust features, managing your to-do lists has never been easier</p>
                    <span class="hidden-content description" id="to-do-manager">
                        <h3>Key features include:</h3>
                        <p><strong>Effortless Task Management: </strong> Seamlessly add, edit, and delete tasks with a user-friendly interface that puts productivity at your fingertips.</p>
                        <p><strong>Clear Progress Tracking: </strong>Mark tasks as completed or pending to gain a clear overview of your progress and priorities.</p>
                        <p><strong>Intuitive Prioritization: </strong> Utilize drag-and-drop functionality to easily rearrange tasks and adapt to changing needs.</p>
                        <p><strong>Secure Data Storage: </strong>Your to-do lists are stored securely using localStorage, ensuring privacy without the need for complex authentication methods.</p>
                        <h3>Technology Used:</h3>
                        <p><strong>React: </strong>Built with React, To-Do List Manager offers a modern and responsive user interface for an optimal task management experience.</p>
                        <p><strong>JavaScript: </strong>Leveraging the power of JavaScript, To-Do List Manager delivers dynamic functionality and seamless interactions.</p>
                        <p><strong>HTML/CSS: </strong>The application's layout and styling are crafted with HTML and CSS to provide a visually appealing and intuitive interface.</p>
                        <p><strong>localStorage: </strong>Securely store user data directly on the device, eliminating the need for external servers and authentication processes.</p>
                    </span>
                    <button class="read-more btn" onclick="toggleDescription('to-do-manager')">Read more</button>
                </div>
            </div>
        </div>

        <div id="note_capture" class="proj">
            <h2><a href="https://note-capture.onrender.com/api-docs/#/" target="_blank">NOTE CAPTURE</a></h2>
            <div class="proj-flex">
                <img src="../static/images/notes_api_ss.png" alt="screenshot of a website" class="screenshots">
                <div class="description">
                    <p>Crafted a robust and secure personal note-taking API, offering seamless CRUD operations
                        for users. Leveraging MongoDB for data storage, Swagger for intuitive documentation and UI,
                        and Supertest for thorough unit testing, the application ensures user privacy with strict 
                        authentication and authorization controls. Elevate your note-taking experience with this 
                        efficient and user-friendly solution.</p>
                    <span class="hidden-content description" id="note-capture-details">
                        <h3>Key features include:</h3>
                        <p><strong>Data Security: </strong> Utilizing MongoDB as the backend data storage solution, the Note Capture Project ensures the utmost security for your notes. Your data is stored in a robust and reliable database, safeguarding it from unauthorized access.</p>
                        <p><strong>Intuitive Documentation and UI: </strong> Swagger is seamlessly integrated into the project, providing an intuitive and interactive documentation interface. Users can effortlessly explore and understand the API's functionalities, making the integration process smooth and developer-friendly.</p>
                        <p><strong>Thorough Unit Testing with Supertest: </strong> Prioritizing the reliability of the API, Supertest is employed for thorough unit testing. This ensures that each component of the application functions as intended, contributing to a stable and error-free user experience.</p>
                        <p><strong>Strict Authentication and Authorization Controls: </strong> User privacy is a top priority in the Note Capture Project. The application implements strict authentication and authorization controls, guaranteeing that only authorized users can access and manipulate their personal notes.</p>
                        <p><strong>Elevated User Experience: </strong> The project is designed to elevate your note-taking experience. With a focus on efficiency and user-friendliness, users can perform CRUD operations seamlessly, enhancing their productivity and overall satisfaction.</p>
                    </span>
                    <button class="read-more btn" onclick="toggleDescription('note-capture-details')">Read more</button>
                </div>
            </div>
        </div>
        """

        # Extract information from each project HTML block
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(projects_html, 'html.parser')

        # Loop through each project and extract title and description
        for project_div in soup.find_all('div', class_='proj'):
            title = project_div.find('h2').text.strip()
            description = project_div.find('div', class_='description').text.strip()
            projects.append({'title': title, 'description': description})

        # Print the populated projects list
        
        for project in projects:
            print(project)


        # def handle(self, *args, **kwargs):
        #     # Create project instances
        #     projects = [
        #         {'title': 'Project 1', 'description': 'Description 1'},
        #         {'title': 'Project 2', 'description': 'Description 2'},
        #         # Add more projects as needed
        #     ]

            for project_data in projects:
                project_instance = Project(**project_data)  # Create an instance of Project
                project_instance.save()  # Save the instance to the database


            
