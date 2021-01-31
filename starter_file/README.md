# Car Acceptibility Evaluator

There are various characteristics of a car which affect its acceptibility among its users. Some of these characteristics are: cost of buying and maintaining the car, the safety features, the luggage and boot space and the number of passengers it can carry. When these features are combined and compared, some cars have a better acceptance over others. This project involves training a Machine Learning model which takes different characteristics of a car and predicts it acceptance with the users. Once the model is trained, its hosted as a web-service for consumption.

## Dataset

### Overview

The Car Evaluation dataset has been taken from the UCI Machine Learning Repository. This dataset contains various structural and technical details about cars on the basis of which they are classified into different categories. Some of those details are:
  1. Cost of buying the car (low, med, high, vhigh)
  2. Maintenance of the car (low, med, high, vhigh)
  3. Number of doors present in the car (2,3,4,5more)
  4. Number of passengers the car can accomodate (2, 4, more)
  5. Luggage space in the car (small, med)
  6. Safety of the car (low, med, high)
  7. Acceptibility (unacc, acc, good, vgood)

### Task

The task involves classifying the cars into different acceptibility categories and hence this is a Classification problem. Out of the 7 features of the dataset mentioned above, we use the first 6 features (cost of buying, cost of maintaining, number of doors, number of passengers, luggage space, safety) for training the model while the 7th feature (acceptibility) is used as the target column.

### Access
We access the data directly from the UCI ML Repository using the ```TabularDatasetFactory.from_delimited_files()``` method. The screenshot below demonstrates how this method was used.
![dataset](./screenshots/dataset-access.PNG)

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
