from transpile_library import transpile_linear_regression, transpile_logistic_regression, transpile_decision_tree
import joblib

if __name__ == "__main__":
    # Our model is a linear regression, load it
    model = joblib.load("regression.joblib")

    # Test some data on it to compare it to the transpiled model
    data_test = [[150, 2, 1]]
    prediction = model.predict(data_test)
    print(f"Predicted price from model: {prediction[0]}")

    # Transpile the model
    transpile_linear_regression(model)
