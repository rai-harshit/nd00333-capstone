from sklearn.ensemble import RandomForestClassifier
import argparse
import os
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

ds = TabularDatasetFactory.from_delimited_files(path="https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data",header=False)

def clean_data(raw_df):
    raw_df = raw_df.to_pandas_dataframe().dropna()
    raw_df.columns = ["buying","maint","doors","persons","lug_boot","safety","decision"]
    raw_x = raw_df[raw_df.columns[:-1]]
    raw_y = raw_df[raw_df.columns[-1]]
    labels_dict = {"unacc": 0, "acc":1, "good":2, "vgood":4}
    x = pd.get_dummies(raw_x)
    y = raw_y.replace(labels_dict)
    return x,y
   
def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_estimators', type=int, default=100, help="The number of trees in the forest")
    parser.add_argument('--max_depth', type=int, default=10, help="Maximum depth of the tree")
    parser.add_argument('--criterion', type=str, default="gini", help="Function to measure the quality of the split")
    parser.add_argument('--max_features', type=int, default=5, help="Number of features to consider when looking for the best split")

    args = parser.parse_args()
    
    x, y = clean_data(ds)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    model = RandomForestClassifier(n_estimators=args.n_estimators,max_depth=args.max_depth,criterion=args.criterion,max_features=args.max_features).fit(x_train, y_train)
    
    run = Run.get_context()
    run.log("Number of Estimators", np.int(args.n_estimators))
    run.log("Maximum Depth", np.int(args.max_depth))
    run.log("Criterion", args.criterion)
    run.log("Maximum Features", np.int(args.max_features))

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    
    joblib.dump(model, "outputs/capstone-hyperdrive-model.joblib")

if __name__ == '__main__':
    main()