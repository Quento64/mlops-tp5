#include <stdio.h>
    
double prediction(double *features, int n_feature) {
    double sum = -8152.937710156519;
    double thetas[] = {717.2583697096838, 36824.1959742563, 101571.84002157034};
    for (int i = 0; i < n_feature; i++) {
        sum += features[i] * thetas[i];
    }
            
    return sum;
}

int main() {
    int n_feature = 3;
    double data_test[3] = {150, 2, 1};

    double y_pred = prediction(data_test, n_feature);
    printf("Predicted price from c file: %f\n", y_pred);
    return 0;
}
