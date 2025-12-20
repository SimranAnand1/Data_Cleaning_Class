Project Summary: Students Performance Analysis This project focuses on data cleaning, exploratory data analysis (EDA) and machine learning modeling using the Students Performance dataset. The objective is to understand how different factors affect student performance and to build a Linear Regression model to predict academic score.

This updated .ipynb(Students Performance Analysis) contains following steps: 

a. Importing Required Libraries: 
NumPy, Pandas → data handling 
Matplotlib, Seaborn → visualization 
Scikit-learn → model building & evaluation

b. Loading the Dataset:
Loaded the students performance dataset using Pandas.

c. Data Cleaning:
Checked for missing values and handled them. 
Converted categorical variables into numerical form using encoding.

d. Exploratory Data Analysis (EDA):
Visualized score distributions using histograms. 
Checked outlier by plotting boxplots.

e. Feature Selection:
Selected relevant independent variables. 
Defined the target variable (student score).

f. Train-Test Split:
Splitted the dataset into training and testing sets using train_test_split.

g. Model Building (Linear Regression):
Implemented Linear Regression using Scikit-learn. 
Trained the model on the training dataset.

h. Model Prediction:
Generated predictions on the test data Compared predicted values with actual values.

i. Model Evaluation:
Calculated evaluation metrics such as: 
Mean Absolute Error (MAE) 
Mean Squared Error (MSE) 
R² Score
