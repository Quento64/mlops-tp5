import joblib

model = joblib.load("regression.joblib")
data_test = [[150, 2, 1]]

prediction = model.predict(data_test)
print(f"Predicted price from model: {prediction[0]}")

def generate_c_linear_regression(model, output_file="linear_regression.c"):
    bias = model.intercept_
    thetas = model.coef_
    code = f"""#include <stdio.h>
    
double prediction(double *features, int n_feature) {{
    double sum = {bias};
    double thetas[] = {{{', '.join(f"{t}" for t in thetas)}}};
    for (int i = 0; i < n_feature; i++) {{
        sum += features[i] * thetas[i];
    }}
            
    return sum;
}}

int main() {{
    int n_feature = 3;
    double data_test[3] = {{150, 2, 1}};

    double y_pred = prediction(data_test, n_feature);
    printf("Predicted price from c file: %f\\n", y_pred);
    return 0;
}}
"""
    
    with open(output_file, "w") as f:
        f.write(code)

def generate_c_logistic_regression(model, output_file="logistic_regression.c"):
    bias = model.intercept_
    thetas = model.coef_
    code = f"""import <stdio.h>
    
double exp_approx(double x, int n_term) {{
    double sum = 1;
    double pow_count = 1;
    double fact_count = 1;
        
    for (int i = 1; i <= n_term; i++) {{
        pow_count *= x;
        fact_count *= i;
        sum += pow_count / fact_count;
    }}
            
    return sum;
}}

double sigmoid(double x) {{
    return 1 / (1 + exp_approx(-x, 10));
}}

double prediction(double *features, int n_feature) {{
    double sum = {bias};
    double thetas[] = {{{', '.join(f"{t:.8f}" for t in thetas)}}};
    for (int i = 0; i < n_feature; i++) {{
        sum += features[i] * thetas[i];
    }}
            
    return sigmoid(sum);
}}

int main() {{
    int n_feature = 3;
    double data_test[3] = {{150, 2, 1}};

    double y_pred = prediction(data_test, n_feature);
    printf("Predicted price from c file: %f\n", y_pred);
    return 0;
}}
"""
    
    with open(output_file, "w") as f:
        f.write(code)

def generate_c_decision_tree(model, output_file="decision_tree.c"):
    bias = model.intercept_
    thetas = model.coef_
    code = f"""#include <stdio.h>
    
double prediction(double *features, int n_feature) {{
    double sum = {bias};
    double thetas[] = {{{', '.join(f"{t}" for t in thetas)}}};
    for (int i = 0; i < n_feature; i++) {{
        sum += features[i] * thetas[i];
    }}
            
    return sum;
}}

int main() {{
    int n_feature = 3;
    double data_test[3] = {{150, 2, 1}};

    double y_pred = prediction(data_test, n_feature);
    printf("Predicted price from c file: %f\\n", y_pred);
    return 0;
}}
"""

    with open(output_file, "w") as f:
        f.write(code)

generate_c_linear_regression(model)
