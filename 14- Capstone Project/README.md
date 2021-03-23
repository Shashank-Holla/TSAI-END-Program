# Capstone Project

The objective of this project is to prepare a transformer-based model (with self-attention, multi-head, and scaled-dot product attention) to write python code from English based statements.


## Data Preprocessing

### 1. Dataset division into English statements and Python codes

The dataset contains English statements and corresponding Python code for it. The English statements were corrected as much as possible to include 'Python function' in English statement for Python function code and 'Python program' for Python statements so as to enable the model to learn the code directions.

Comments with keywords 'write', 'python', 'program', 'function', 'class' were picked as English statements and the following code as its Python code. Code for dataset division is present in the notebook.

### 2. Anomalies in the datset

Missing/incorrect indentations for the Python codes were checked using check_indentation.py script and corrected. English statements were corrected to include keywords and provide clear instructions for the Python code.

### 3. Maximum length of Python code for model

## Model Architecture

### Model hyperparameters

* Encoder/Decoder hidden layer dimension= 512
* Encoder layers= 3
* Encoder Head= 8
* Encoder PF dimension= 1024
* Decoder layers= 3
* Decoder Head= 8
* Decoder PF dimension= 1024

The following iterations were carried out to conclude the best fit model hyperparameters.

### Loss Function


## Results

### Generated Python code examples

### Attention for Actual-Generated Python Code

### Train/Validation Loss curve




