# Advanced Coding Project – LUISS 2024–25

This repository contains the code and documentation for the **Advanced Coding Project** for the LUISS 2024–25 academic year.

## 📊 Dataset Overview

The dataset includes detailed information about various system users, with historical records reflecting changes in financial behavior and credit scores. Each row corresponds to one user and contains the following fields:

- **Customer_ID**: Unique identification of a person  
- **Month**: Month of the record  
- **Name**: Full name of the person  
- **Age**: Age of the person  
- **SSN**: Social Security Number  
- **Occupation**: Current occupation  
- **Annual_Income**: Yearly income (in USD)  
- **Monthly_Inhand_Salary**: Monthly base salary  
- **Num_Bank_Accounts**: Number of bank accounts  
- **Num_Credit_Card**: Number of credit cards held  
- **Interest_Rate**: Interest rate on credit cards  
- **Num_of_Loan**: Number of loans taken  
- **Type_of_Loan**: Types of loans taken  
- **Delay_from_due_date**: Avg. days delayed beyond due date  
- **Num_of_Delayed_Payment**: Avg. number of delayed payments  
- **Changed_Credit_Limit**: Percent change in credit card limit  
- **Num_Credit_Inquiries**: Number of credit card inquiries  
- **Credit_Mix**: Classification of credit types  
- **Outstanding_Debt**: Remaining debt to be paid (in USD)  
- **Credit_Utilization_Ratio**: Utilization ratio of available credit  
- **Credit_History_Age**: Age of credit history  
- **Payment_of_Min_Amount**: Whether only the minimum payment was made  
- **Amount_invested_monthly**: Monthly investment amount (in USD)  
- **City**: City of residence  
- **Street**: Street address  
- **Credit Score**: Target variable representing the user's credit score  

---

## ⚠️ Problems to Solve

- The dataset contains **missing values**, which is typical in real-world scenarios.
- The dataset contains **numericla values** that are not in the correct format. In particular:
1) 
- There are **incorrect or illogical values** that must be cleaned.Clear examples:
1) Age distribution, that has both negative and very high values (e.g., 200 years old).
- The dataset may contain **biases**, especially in financial and demographic features. These must be analyzed and mitigated, as historical data should not always drive future decisions in sensitive applications.
- **Class imbalance** may be present in the target variable (Credit Score), and appropriate handling is required during model training and evaluation.

---

## 📁 Project Structure (Example)
