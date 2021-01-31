# Car Acceptibility Evaluator

There are various characteristics of a car which affect its acceptibility among its users. Some of these characteristics are: cost of buying and maintaining the car, the safety features, the luggage and boot space and the number of passengers it can carry. When these features are combined and compared, some cars have a better acceptance over others. This project involves training a Machine Learning model which takes different characteristics of a car and predicts it acceptance with the users. Once the model is trained, its hosted as a web-service for consumption.

## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
The screencast of the project can be accessed using the link: https://youtu.be/SD7OUOWWGHA
<br>It covers the following points:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
One of the standout suggestions was to enable logging in the deployed model. This was achieved by simply adding the following line of code:
```
service.update(enable_app_insights=True)
```
![app-insights](./screenshots/app-insights.PNG)
