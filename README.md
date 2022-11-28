# SOL Math Data Dashboard
Dashboard for displaying a limitless bank of 4th grade math Standards of Learning (SOL) questions by standard.

## Project Description
All data come from the Virginia Standards of Learning (SOL) 2014 4th grade math practice test. We converted the raw questions into formatted string templates in Python that allow the numbers in and context of the questions to be randomized each time the question is accessed, creating a limitless bank of practice test questions. The majority (42) of the randomizable questions are multiple choice, while a few (3) are fill in the blank. After creating the questions, we used the Pandas package to create a DataFrame of multiple-choice answers. Next, we turned each question into a Python class so that it could be easily displayed along with its answer choices. We also added class attributes that allow the questions to be searchable by grade level and SOL standard.

We then displayed the randomized templates in a Dash dashboard for use by teachers and students. Teachers and students can search for questions they would like to practice based upon SOL standard, grade level, and number of questions they wish to encounter. They can then view and answer the questions directly in their web browser and receive immediate feedback for every answer. Researchers can use the provided code and templates to construct similar dashboards for other grade levels, subject areas, and states. Researchers could also use these data to conduct experiments such as measuring the impact of providing this limitless bank of test questions.

The next steps will be to continue to build out the dashboard for other grade levels and subject areas as well as refine the GPT-2 model discussed below. 

## Getting Started and Launching the Docker Container
- First, open a terminal and change directory (CD) to the folder containing this repository
- Next, build the docker image using the command, "docker build . -t solmathdashboard", in your terminal
- Then use the command, "Docker compose up", to launch the Docker container
- Next, copy and paste the Jupyter Lab URL from the output of the Docker compose command into your web browser
- Change the port to 8889 and hit enter
- You are now ready to run any of the files in this repository in a Jupyter Lab development environment!

## Guide to Using this Repository
The /app/templates folder contains all the code needed to build and launch the dashboard. All you need to do to launch the dashboard is open and run the app.ipynb file. If you wish to add additional question templates, you can add them to the templates.py file. If you wish to test your new question templates, you can do so in the testing_templates.ipynb file. 

The other main element in this folder is the /app/GPT-2 Model folder, which contains code needed to retrain a GPT-2 model based on sample test questions generated from the dashboard (thank you to [madisonmay](https://github.com/madisonmay), [Margaret Mitchell et al](https://arxiv.org/abs/1810.03993), and [webproduktion01](https://github.com/webproduktion01) who developed this code). This article (https://medium.com/ai-innovation/beginners-guide-to-retrain-gpt-2-117m-to-generate-custom-text-content-8bb5363d8b7f) describes how to retrain and run this model. If you wish to add additional sample question data into this model, you may do so using the /app/Templates/initialize_mongo.ipynb file. However, the GPT-2 model is still very much in development and we do not recommend using it at this time. 

