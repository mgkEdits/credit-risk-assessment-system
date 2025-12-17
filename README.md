# 🏦 Credit Risk Assessment System

### A Machine Learning Approach to Loan Default Prediction using Real-World Data

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Prototype-orange)
![Domain](https://img.shields.io/badge/Domain-FinTech-green)

## 📖 Overview
This project is a **Credit Risk Modeling** proof-of-concept designed to predict the **Probability of Default (PD)** for single-family loans.

Unlike standard "toy" projects that use synthetic data, this system is engineered using the **Freddie Mac Single-Family Loan-Level Dataset**, utilizing a sample from over **3 million real historical records** (2018-2019 origination). The goal is to demonstrate how backend-engineering principles and statistical modeling can be applied to solve the high-stakes problem of financial risk exposure.

## 🎯 Real-World Problem
Financial institutions face a critical challenge: distinguishing between "Good Risk" (profitable lending) and "Bad Risk" (potential default).
* **False Negatives (Approving a Defaulter):** Result in direct capital loss ($\text{LGD} \times \text{EAD}$).
* **False Positives (Denying a Good Applicant):** Result in opportunity cost and lost interest revenue.

This project aims to optimize this trade-off by building a classifier that prioritizes **financial precision** over raw accuracy.

## 📂 Dataset
* **Source:** Freddie Mac Single-Family Loan-Level Dataset.
* **Scope:** Historical performance data of loans originated in 2018-2019.
* **Volume:** Processed ~3M+ records; used a statistically valid random sampling strategy ("Randomness by Choice") to create a representative training set.
* **Key Features:** Debt-to-Income (DTI), Credit Score (FICO), Loan-to-Value (LTV), Unpaid Principal Balance (UPB).

## 🛠️ Methodology & Architecture
1.  **Data Engineering:** Cleaning massive raw text files, handling missing values in financial columns, and downcasting data types for memory optimization.
2.  **Exploratory Data Analysis (EDA):** Visualizing the distribution of interest rates, credit scores, and their correlation with default status.
3.  **Preprocessing:** Handling Class Imbalance (Defaults are rare events < 1%) using robust sampling techniques.
4.  **Modeling:**
    * **Logistic Regression:** For baseline performance and high interpretability.
    * **Random Forest Classifier:** For capturing non-linear relationships between borrower behaviors.
5.  **Evaluation:** Moving beyond Accuracy. We focus on **Recall**, **Precision**, and **ROC-AUC** to measure the model's ability to catch actual defaults.

## 🚀 Future Roadmap (Adoption & Compliance)
* **Explainable AI (XAI):** Integrating **SHAP (SHapley Additive exPlanations)** to provide reason codes for loan rejection, ensuring compliance with regulations like the **Kenyan Data Protection Act** and **ECOA**.
* **API Deployment:** Wrapping the model in a Flask/FastAPI backend to serve real-time predictions.
* **Full Expected Loss Framework:** Extending the model to estimate LGD (Loss Given Default) and EAD (Exposure at Default).

## 🔗 Links
* **Kaggle Notebook (Code & Analysis):** [Link to your Kaggle Notebook](https://www.kaggle.com/code/elijahnyasiando/creditriskmodel-masterdataset).
* **Dataset Source:** [Freddie Mac Data Page](http://www.freddiemac.com/research/datasets/sf_loanlevel_dataset.page)

---
*Author: [Your Name]*
*A student of the arts of Computing, Machine Learning, and Edge Systems.*
