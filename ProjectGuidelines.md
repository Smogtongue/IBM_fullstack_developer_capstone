# IBM Fullstack Developer Capstone Project
# Car Dealership Review Site

## Project Sceneario:
  A national car dealership with local branches spread across the United States recently conducted a market survey. One of the suggestions that emerged from the survey was that customers would find it beneficial if they could access a central database of dealership reviews across the country.
  
  You are a new hire at the company. You are assigned the task of building a website that allows new and existing customers to look up different branches by state and look at customer reviews of the various branches. Customers should be able to create an account and add their review for any of the branches. The management hopes this will bring transparency to the system and also increase the trust customers have in the dealership.
  
  After thorough research and brainstorming, the team developed use cases for anonymous, authorized, and admin users.

###  Use cases for anonymous users:

    - View the **Contact Us** page.
    - View the **About Us** page.
    - View the list of dealerships.
    - Filter the list of dealerships by state:
        - Select **Show all** or a specific state from the State dropdown on the dealership page.
        - View all states if nothing is selected in the dropdown.
        - View a table of dealerships for the selected state when the form is submitted.
    - Click on a dealership to view the reviews for that dealership on the details page with each review displayed on a bootstrap card.
    Log in using their credentials.

### Use cases for authorized users:

In addition to the above, authorized users should be able to write a review for any dealership on the dealership's page. In order to enable authorized users to write their reviews:

  1. A Review button should be provided against each dealer listed in the dealership table.
  2. Clicking on the Review button should take the user to the review page.
  3. Filling the form on the review page and submitting it should add the review.
  
          {
              "user_id": 1, => from Django
              "name": "Berkly Shepley", => from Django
              "dealership": 15, => from the form
              "review": "Total grid-enabled service-desk", => form textbox
              "time": "", => current time
              "purchase": true, => form checkbox
              "purchase_date": "07/11/2020", => form calendar (bootstrap)
              "car_make": "Audi", => from django dropdown
              "car_model": "A6", => from django dropdown
              "car_year": 2010 => form django dropdown
          }

  4. On submission, the user should be taken back to the dealership detail page with the submitted review featured at the top of the reviews list, sorted on time.

### Use cases for admin users:

     1. Log in to the admin site with a predefined username and password.
     2. Add new make, model, and other attributes.

Your organization has assigned you as the Lead Full-Stack Software Developer on this project. Your job is to develop this portal as part of your Capstone project by following best practices for Full-Stack software development.


## Architecture Overview:
  The final project for this course has several steps that you must complete. The high-level step list given below will help you with an overview of the complete project. The project is divided into smaller labs with detailed instructions for each step. You must complete all labs to complete the project successfully.

### Project breakdown

**Fork the GitHub repo containing the project template. The main web application is a predefined Django application. You will need to add some new features, and then build and run your project implementation.**
  
    1. Fork the repository in your account.
    2. Clone the repository in the Cloud IDE environment.
    3. Create static pages to finish the user stories.
    4. Run the application locally.

Add user management to the Django application.

    Implement user management using the Django user authentication system and create a REACT frontend.

Implement backend services.

    Create Node.js server to manage dealers and reviews using MongoDB and dockerize it.
    Deploy sentiment analyzer on Code Engine.
    Create Django models and views to manage car model and car make.
    Create Django proxy services and views to integrate dealers and reviews together.

Add dynamic pages with Django templates.

    Create a page that displays all the dealers.
    Create a page that displays reviews for a selected dealer.
    Create a page that lets the end user add a review for a selected dealer.

Implement CI/CD, and then run and test your application

    1. Set up continuous integration and delivery for code linting.
    2. Run your application on Cloud IDE.
    3. Test the updated application locally.
    4. Deploy the application on Kubernetes.

  ## Solution architecture

The solution will consist of multiple technologies

   1. The user interacts with the "Dealerships Website", a Django website, through a web browser.

   2. The Django application provides the following microservices for the end user:

     - get_cars/ - To get the list of cars from
     - get_dealers/ - To get the list of dealers
     - get_dealers/:state - To get dealers by state
     - dealer/:id - To get dealer by id
     - review/dealer/:id - To get reviews specific to a dealer
     - add_review/ - To post review about a dealer

   3. The Django application uses SQLite database to store the `Car Make` and the `Car Model` data.

   4. The "Dealerships and Reviews Service" is an Express Mongo service running in a Docker container. It provides the following services::

    - /fetchDealers - To fetch the dealers
    - /fetchDealer/:id - To fetch the dealer by id
    - fetchReviews - To fetch all the reviews
    - fetchReview/dealer/:id - To fetch reviews for a dealer by id
    - /insertReview - To insert a review

   5. "Dealerships Website" interacts with the "Dealership and Reviews Service" through the "Django Proxy Service" contained within the Django Application.

   6. The "Sentiment Analyzer Service" is deployed on IBM Cloud Code Engine, it provides the following service:

     - /analyze/:text - To analyze the sentiment of the text passed. It returns positive, negative or neutral.

  7. The "Dealerships Website" consumes the "Sentiment Analyzer Service" to analyze the sentiments of the reviews through the Django Proxy contained within the Django application.

<img src= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-CD0321EN-Coursera/labs/v2/m1/images/v2.capstone-dealership-architecture.png" >



## User Management Overview

Now, you have the initial Django application built and deployed. In the next step, the admins of the dealership will review the app to identify users and manage their accesses based on roles (such as anonymous users or registered users). To accomplish this, you need to add authentication and authorization, that is, user management, to the app. In this lesson, you need to perform the following tasks to add the user management feature: 

    Create a superuser for your app.

    Build the Client side and configure it.

    Check the Client configuration.

    Add a Login view to handle login requests.

    Add a Logout view to handle logout requests.

    Add a Registration view to handle Sign-up requests.

Follow the instructional lab to complete the above tasks step by step.

## Node.js Mongo DB dockerized server Overview

The Django application you created in the last module needs to communicate with the database. In this module, you will create a containerized Node.js application that uses MongoDB as the backend to serve API endpoints.

You will write these back-end services in an Express app and containerize it with Docker.

You will view and test the following endpoints:
  
     - /fetchReviews/dealer/29
  
     - /fetchDealers 
  
     - /fetchDealer/3
  
     - /fetchDealers/Kansas

Follow the instructional lab to complete the above tasks step by step.
