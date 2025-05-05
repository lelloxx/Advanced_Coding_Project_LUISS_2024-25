# Advanced Coding Project – LUISS 2024–2025

Authors: [Michele Turco](https://www.linkedin.com/in/michele-turco-11b249268), [Lorenzo Laterza](), [Mattia Cervelli]()

This repository contains the code and documentation for the **Advanced Coding Project** for the LUISS 2024–25 academic year.

## 📊 Dataset Overview

The dataset includes detailed information about various system users, with historical records reflecting changes in financial behavior and credit scores. Each row corresponds to one user and contains the following fields:

Dataset structure:

| **Column Name**           | **Description**                                                                 | **Data Type** | **Example**              |
|----------------------------|---------------------------------------------------------------------------------|---------------|--------------------------|
| Customer_ID               | Unique identification of a person                                               | String        | C12345                   |
| Month                     | Month of the record                                                             | String        | January                  |
| Name                      | Full name of the person                                                         | String        | John Doe                 |
| Age                       | Age of the person                                                               | Integer       | 35                       |
| SSN                       | Social Security Number                                                          | String        | 123-45-6789              |
| Occupation                | Current occupation                                                              | String        | Software Engineer        |
| Annual_Income             | Yearly income (in USD)                                                          | Float         | 75000.00                 |
| Monthly_Inhand_Salary     | Monthly base salary                                                             | Float         | 6250.00                  |
| Num_Bank_Accounts         | Number of bank accounts                                                         | Integer       | 3                        |
| Num_Credit_Card           | Number of credit cards held                                                     | Integer       | 2                        |
| Interest_Rate             | Interest rate on credit cards                                                   | Float         | 15.5                     |
| Num_of_Loan               | Number of loans taken                                                           | Integer       | 1                        |
| Type_of_Loan              | Types of loans taken                                                            | String        | Personal Loan            |
| Delay_from_due_date       | Avg. days delayed beyond due date                                               | Integer       | 5                        |
| Num_of_Delayed_Payment    | Avg. number of delayed payments                                                 | Integer       | 2                        |
| Changed_Credit_Limit      | Percent change in credit card limit                                             | Float         | 10.0                     |
| Num_Credit_Inquiries      | Number of credit card inquiries                                                 | Integer       | 4                        |
| Credit_Mix                | Classification of credit types                                                  | String        | Good                     |
| Outstanding_Debt          | Remaining debt to be paid (in USD)                                              | Float         | 15000.00                 |
| Credit_Utilization_Ratio  | Utilization ratio of available credit                                           | Float         | 0.35                     |
| Credit_History_Age        | Age of credit history                                                           | String        | 5 Years 3 Months         |
| Payment_of_Min_Amount     | Whether only the minimum payment was made                                       | String        | Yes                      |
| Amount_invested_monthly   | Monthly investment amount (in USD)                                              | Float         | 500.00                   |
| City                      | City of residence                                                               | String        | Lonton                   |
| Street                    | Street address                                                                  | String        | 123 Main St              |
| Credit Score              | Target variable representing the user's credit score                            | String        | Good                     |

---

## 📁 Project Structure

### 1. **Exploratory Data Analysis (EDA)**

The first step in the project involved performing Exploratory Data Analysis (EDA) to assess the dataset's structure and quality. Several key issues were identified:

- **Missing Values**: Roughly 10% of the rows were nearly empty, with missing entries in most columns. Surprisingly, the only column consistently filled was the target variable, **Credit Score**.
- **Anomalous Values**: The dataset contained clearly unrealistic entries, such as negative ages and incomes. These values were flagged for removal or correction.
- **Skewed Distributions**: Many numerical variables were highly skewed due to outliers—often the same unrealistic values mentioned above—which distorted the true distribution.
- **Categorical Variables**: Several categorical variables were poorly structured, with an excessive number of unique categories or ambiguous labeling, making them difficult to interpret or use in modeling.

---

### 2. **Data Imputation**

Due to the high volume of missing data, our first priority was to perform imputation. This step was essential both for visualizing variable distributions and for preparing the data for modeling. 
Fortunately, the dataset had a **recursive, time-series-like structure**, recording information for each customer from **January through August**. This structure allowed us to impute missing values with a high degree of confidence by leveraging past data from the same customer. 
For example, if a customer's March record was missing certain values, we could look at January and February for valid entries. This month-to-month continuity enabled deterministic or highly plausible imputations across most variables.

#### Example: Customer Time Series Imputation

| **Customer_ID** | **Month**  | **Name**        | **Variable_1** | **Variable_2** |
|------------------|------------|------------------|----------------|----------------|
| CUS_0xd40        | January    | Aaron Maashoh    | 1              | 2              |
| CUS_0xd40        | February   | Aaron Maashoh    | 1              | 2              |
| CUS_0xd40        | March      | Aaron Maashoh    | 1              | 2              |
| CUS_0xd40        | April      | Aaron Maashoh    | 1              | 2              |
| CUS_0xd40        | May        | Aaron Maashoh    | 1              | 2              |
| CUS_0xd40        | June       | Aaron Maashoh    | 1              | 2              |
| CUS_0xd40        | July       | Aaron Maashoh    | 1              | 2              |
| CUS_0xd40        | August     | Aaron Maashoh    | 1              | 2              |

By propagating reliable values across months for the same customer, we could fill in gaps with high fidelity, laying a clean foundation for downstream processing.

---

### 3. **Removal of Anomalous Values - Outlier Removal**

This step was carried out almost in parallel with the imputation process. As previously mentioned, the dataset contained numerous anomalous values that were easy to identify and did not require advanced imputation methods. Most of these anomalies were clearly unrealistic—such as negative values for age or income, or abnormally high figures that deviated significantly from a customer's typical monthly data.
Given the structure of the dataset, where each customer had multiple monthly entries, we could reasonably apply assumptions based on common sense and customer-specific trends. For instance, it is highly unlikely for a person’s income in a single month to spike to 10 times their average without explanation. Based on such logic, rows containing extreme or logically invalid values were removed to ensure data integrity and prevent distortion during modeling.

