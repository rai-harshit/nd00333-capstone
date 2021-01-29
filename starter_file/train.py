from sklearn.ensemble import RandomForestClassifier
import argparse
import os
from sklearn.metrics import accuracy
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

ds = TabularDatasetFactory.from_delimited_files("https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv")

def clean_data(raw_df):
    raw_x = raw_df[raw_df.columns[:-1]]
    raw_y = raw_df[raw_df.columns[-1]]
    labels_dict = {"unacc": 0, "acc":1, "good":2, "vgood":4}
    x = pd.get_dummies(raw_x)
    y = raw_y.replace(labels_dict)
    return x,y
   
def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--n_estimators', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()
    
    x, y = clean_data(ds)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    model = RandomForestClassifier(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    
    run = Run.get_context()
    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    
    joblib.dump(model, "outputs/capstone-hyperdrive-model.joblib")

if __name__ == '__main__':
    main()
