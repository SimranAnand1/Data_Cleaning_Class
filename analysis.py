# Basic EDA

import pandas as pd
import numpy as np

data = pd.read_csv('D:\Adda247\Data_Cleaning_Class\StudentsPerformance.csv')

print(data.info())
print(data.describe())      

# graphs for visualization
import matplotlib.pyplot as plt             
import seaborn as sns
sns.histplot(data['math score'])
plt.show()