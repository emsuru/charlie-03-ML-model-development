import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from preprocessing.data_preprocessor import DataPreprocessor
from training.model_trainer import ModelTrainer

def train_random_forest():
    df = pd.read_csv('input_data/properties.csv')
    preprocessor = DataPreprocessor(df)
    preprocessor.clean_drop().clean_impute().encode_state_building().encode_epc()
    # preprocessor.save_training_columns('training/training_columns.txt')
    X_train, X_test, y_train, y_test = preprocessor.preprocess_split()
    X_train, X_test = preprocessor.preprocess_encode(X_train, X_test)
    X_train, X_test = preprocessor.preprocess_feat_select(X_train, X_test, y_train)
    X_train, X_test = preprocessor.preprocess_impute(X_train, X_test)

    trainer = ModelTrainer(X_train, X_test, y_train, y_test)
    trainer.train_model(RandomForestRegressor())
    trainer.evaluate_model()
    trainer.save_model("random_forest_model.pkl")

if __name__ == "__main__":
    train_random_forest()
