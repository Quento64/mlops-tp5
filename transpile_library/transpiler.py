from sklearn.linear_model import LinearRegression, LogisticRegression

def transpile_linear_regression(model: LinearRegression, output_file="linear_regression.c"):
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
    printf("Predicted price from c file: %.10f\\n", y_pred);
    return 0;
}}
"""
    
    with open(output_file, "w") as f:
        f.write(code)

    print(f"To compile, run gcc {output_file}, then execute a.out")

def transpile_logistic_regression(model: LogisticRegression, output_file="logistic_regression.c"):
    bias = model.intercept_
    thetas = model.coef_
    code = f"""#include <stdio.h>
    
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
    double thetas[] = {{{', '.join(f"{t}" for t in thetas)}}};
    for (int i = 0; i < n_feature; i++) {{
        sum += features[i] * thetas[i];
    }}
            
    return sigmoid(sum);
}}

int main() {{
    int n_feature = 3;
    double data_test[3] = {{150, 2, 1}};

    double y_pred = prediction(data_test, n_feature);
    printf("Predicted price from c file: %.10f\\n", y_pred);
    return 0;
}}
"""
    
    with open(output_file, "w") as f:
        f.write(code)

    print(f"To compile, run gcc {output_file}, then execute a.out")

def transpile_decision_tree(output_file="decision_tree.c"):
    code = f"""#include <stdio.h>
    
int prediction(double* features, int n_features) {{
    int sum = 0;
    for (int i = 0; i < n_features; i++) {{
        sum += features[i] > 0;
    }}
    return sum == 0;
}}

int main() {{
    int n_feature = 3;
    double data_test[3] = {{-1, 0.5, 1}};

    int y_pred = prediction(data_test, n_feature);
    printf("Prediction from decision tree: %d\\n", y_pred);
    return 0;
}}
"""

    with open(output_file, "w") as f:
        f.write(code)

    print(f"To compile, run gcc {output_file}, then execute a.out")
