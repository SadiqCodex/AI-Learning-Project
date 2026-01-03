# Loan Data Preprocessing Pipeline

A comprehensive machine learning project focused on preprocessing loan dataset for predictive modeling. This project demonstrates essential data cleaning, feature engineering, and transformation techniques using Python's data science stack.

## 🚀 Features

- **Data Loading & Exploration**: Efficient loading and initial analysis of loan dataset
- **Missing Value Handling**: Multiple imputation strategies for categorical and numerical data
- **Categorical Encoding**: One-hot encoding, label encoding, and ordinal encoding implementations
- **Outlier Detection & Removal**: IQR method, Z-score analysis, and statistical outlier handling
- **Feature Scaling**: Standardization and Min-Max scaling for numerical features
- **Data Transformation**: Log transformations for skewed distributions
- **Duplicate Removal**: Automated detection and removal of duplicate records
- **Visualization**: Comprehensive data distribution plots and correlation heatmaps

## 📋 Prerequisites

- Python 3.8+
- Jupyter Notebook
- Required packages listed in `requirements.txt`

## 🛠 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd loan-data-preprocessing
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## 📊 Usage

### Running the Preprocessing Pipeline

1. **Data Exploration** (`notebooks/main.ipynb`):
   - Load and examine the loan dataset
   - Analyze missing values and data distributions
   - Perform initial data cleaning

2. **Feature Engineering** (`notebooks/app.ipynb`):
   - Apply feature scaling techniques
   - Handle categorical variables
   - Remove outliers and duplicates

### Example Usage

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv('data/loan_data.csv')

# Handle missing values
data.fillna(data.mean(), inplace=True)

# Scale features
scaler = StandardScaler()
data['scaled_income'] = scaler.fit_transform(data[['Annual_Income']])
```

## 📁 Data Description

The project uses a loan dataset (`data/loan_data.csv`) containing the following key features:

- **Customer_Age**: Age of the loan applicant
- **Gender**: Applicant's gender
- **Marital_Status**: Marital status
- **Dependents**: Number of dependents
- **Annual_Income**: Annual income of the applicant
- **Credit_Score**: Credit score
- **Loan_Amount**: Requested loan amount
- **Loan_Term_Months**: Loan term in months
- **Interest_Rate**: Interest rate on the loan
- **Property_Area**: Location of property
- **Account_Balance**: Account balance

## 📚 Notebooks Overview

### `notebooks/main.ipynb`
- Comprehensive data preprocessing workflow
- Missing value imputation using mode/mean strategies
- Categorical variable encoding
- Outlier detection using IQR and Z-score methods
- Data visualization with seaborn and matplotlib

### `notebooks/app.ipynb`
- Advanced feature scaling techniques
- Standardization and normalization
- Log transformations for skewed data
- Duplicate record handling
- Feature engineering pipelines

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Sadik Mohammad**

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

*Built with ❤️ using Python, pandas, scikit-learn, matplotlib, and seaborn*
