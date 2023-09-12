# Goals

These are the goals for the regression project:

* Create a readme file, containing goals, project description, project planning, questions, data dictionary, instructions and findings.
* Acquire data from CodeUp database to complete the regression project.
* Prepare data for exploration.
* Explore and analyse data to find what features have a correlation or relationship with the house prices.
* Prepare the rest of the data for modeling.
* Create some models to predict house prices, including a baseline model.
* Create a conclusion, recommendations, and state key findings and next steps.


# Project Description

This is a project about regression models. For this project, I will be using the zillow dataset from CodeUp's database. I am going to retrieve the data, explore it, analyse it, clean it up, and use models to try to predict house prices. There will be a MVP that consists of using only 3 features, and if time allows it then I will try using many more features. After creating my models, I will test my best one and create my conclusion for the project and reflect on what can be done better next time.


# Project plan

0. Do an inital first pass of the project to create a MVP consiting of just 3 features.
0. Acquire the data using a SQL query, and save it locally so it is faster to access.
0. Prepare data so it is ready for exploration.
0. Explore the data to see what features are most relevant to house prices.
0. Prepare data for modeling.
0. Create models, including a baseline, and test the best performing model ONCE!
0. Analyse results, and come up with my key findings and conclusions.


# Questions:

* How does the number of bedrooms affect the price of a house?

* How does the number of bathrooms affect the price of a house?

* How does the square footage of a house affect price?

* What features seem to have the most effect on price?


# Data Dictionary

MVP:

| Feature    |              Description                  |
| --------   |               -------                     |
| price      |   The price of the house                  |
| bedrooms   |   The number of bedrooms in the house     |
| bathrooms  |   The number of bathrooms in the house    |
| sq_ft      |   The square footage of the house         |
| pools      |   The number of pools in the house        |
| fireplaces |   The number of fireplaces in the house   |
| garages    |   The square garages of the house         |
| fips       |   The name of the county the house is in  |
| year       |   The year the house was built in         |
| lot_sq_ft  |   The square footage of the lot           |

# Instructions

1. You will need access to CodeUp's database of information since the information for this project is all pulled from the database.

2. Download and install Anaconda, and install Python through Anaconda so that you have all of the necessary data science libraries and tools that you will need for pyhton.

2. Query zillow data from the Codeup database using SQL and then locally save a .csv copy of it so it is faster to load up.

3. Once you have Python, all of the necessary libraries, and access to CodeUp's database or the .csv file containing the zillow data,  you are all set to go.


# Key Findings

Houses become more expensive with an increase number of amenities. More rooms, such as bathrooms and bedrooms, had a positive relationship with prices. House and lot size (sq ft) also had a positive correlation with house prices.

Models had little variation in scores. Some were better than others but not by huge margins. Adjusting hyperparameters had little effect. It seems that the best way to improve scores would be to input better data into the models. I created an MVP using just sq ft, bedrooms, and bathrooms and it did much worse. The extra data really helped the model perform better.