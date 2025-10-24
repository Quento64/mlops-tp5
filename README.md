# MLOPS TP5

This repository is the submission of the TP5 of the mlops course.

It consists of a Python library to transpile simple models from Python to C.

---

## How to use

1. Create environment and install depedencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a model in Python

There is already a script for the linear regression: **create_model.py**.
It stores the model as **regression.joblib**.

3. Transpile the model into C

In the **transpile_simple_model.py** file, you have a example for the linear regression.

```bash
python3 transpile_simple_model.py
```

4. Compile the C file and check the results

The commands to use are printed by the previous function, but here are the steps for the linear regression.

```bash
gcc linear_regression.c -o linear_regression
./linear_regression
```

You can now check the results between the Python and C models.

