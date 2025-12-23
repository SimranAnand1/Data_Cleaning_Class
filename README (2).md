# Property Price Data — Data Cleaning & EDA

This repository contains an exploratory notebook (property_price_data.ipynb) that performs data loading, cleaning and initial exploratory data analysis (EDA) on a property / housing price dataset.

Notebook: [property_price_data.ipynb](https://github.com/SimranAnand1/Data_Cleaning_Class/blob/main/property_price_data.ipynb)

---

## Summary

The notebook walks through:

- Loading the dataset (`property_price_data.csv`).
- Inspecting shape and data types.
- Counting missing values and showing missing-value percentages.
- Categorizing columns with missing values (numerical vs categorical).
- Imputing missing values:
  - Numerical columns: median imputation.
  - Categorical columns: mode imputation.
- Verifying no missing values remain and checking duplicates.
- Basic EDA: descriptive statistics and plotting distributions for numerical features using matplotlib / seaborn.

The notebook is written for interactive execution (originally run in Google Colab).

---

## Files

- `property_price_data.ipynb` — main notebook performing cleaning and EDA.
- `property_price_data.csv` — dataset used by the notebook (not included here in the README — ensure it sits in the same folder as the notebook when running locally).

---

## Requirements

Recommended Python packages (install with pip):

```bash
pip install pandas numpy matplotlib seaborn jupyterlab notebook
```

---

## How to run

1. Open in Google Colab:
   - Use the Colab URL:  
     `https://colab.research.google.com/github/SimranAnand1/Data_Cleaning_Class/blob/main/property_price_data.ipynb`
   - Upload `property_price_data.csv` to Colab (or modify the notebook to point to a dataset hosted online).

2. Run locally:
   - Clone the repo or download the notebook and CSV to the same folder.
   - Create and activate a virtual environment (optional):
     ```bash
     python -m venv venv
     source venv/bin/activate  # Linux / macOS
     venv\Scripts\activate     # Windows
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
     or
     ```bash
     pip install pandas numpy matplotlib seaborn jupyterlab
     ```
   - Start Jupyter and open the notebook:
     ```bash
     jupyter lab
     # or
     jupyter notebook
     ```

---

## Notebook overview (detailed)

- Load libraries: pandas, numpy, matplotlib, seaborn.
- `data.info()` and `data.shape()` to inspect dataset size and types.
- Count missing values and compute missing-value percentages.
- Identify columns with missing values and split them into numerical and categorical groups.
- Imputation strategy used in the notebook:
  - Numerical columns with missing values: filled with median.
  - Categorical columns with missing values: filled with mode (most frequent value).
- Confirmed `data.isnull().sum().sum()` is zero after imputation.
- Checked duplicate rows with `data.duplicated().sum()`.
- Performed EDA:
  - `data.describe()` for numeric summary.
  - Histogram plots (Seaborn) for numerical variables.

---

## Notes, caveats & suggestions (recommended improvements)

- Imputing categorical features with the mode is simple but may be inappropriate for features where NaN means "not present" (e.g., `PoolQC`, `MiscFeature`, `Alley`, `Fence`). Consider encoding these with a meaningful category like `None` or `NoFeature` instead of the statistical mode.
- The dataset contains columns with a very high percentage of missing values (e.g., `PoolQC`, `MiscFeature`, `Alley`, `Fence`) — dropping or specially encoding those may be preferable.
- For `LotFrontage`, `GarageYrBlt`, and other numeric features, median imputation is reasonable but consider:
  - Group-wise imputation (e.g., by `Neighborhood` or property type).
  - Predictive imputation (e.g., simple regressors to predict missing values).
- Consider feature engineering:
  - Combine related features (e.g., total bathroom count, total porch area).
  - Create age of house (YrSold - YearBuilt) or time-since-remodel (YrSold - YearRemodAdd).
- Check and treat outliers (e.g., extremely large `LotArea`, `SalePrice`) — consider log-transforming `SalePrice` when modeling.
- After cleaning and feature engineering, split data into train/test and apply baseline regression models (Linear Regression, Random Forest, Gradient Boosting) and evaluate with appropriate metrics (RMSE, MAE).
- Encode categorical variables using one-hot encoding or target encoding depending on model choice.
- Add a reproducible pipeline (scikit-learn pipelines) to maintain consistent preprocessing for modeling.

---

## Next steps (recommended)

1. Revisit imputation strategy for features with domain-specific meaning.
2. Create a versioned preprocessing script (or sklearn Pipeline) so the same steps can be applied to train and test sets.
3. Perform feature selection / dimensionality reduction if using models sensitive to many dummy variables.
4. Try baseline models and produce a README section describing model results and comparison.
5. Add unit tests for preprocessing functions (if turning steps into Python scripts).

---
