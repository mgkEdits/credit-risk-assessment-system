# 📄 Model Card: Credit Risk Assessment System (v1.0)

## 1. Model Details
* **Developer:** Elijah Nyasiando
* **Model Type:** Random Forest Classifier (Ensemble Learning)
* **Dataset:** Freddie Mac Single-Family Loan-Level Dataset (2018-2019 Originations).
* **Target Variable:** `DEFAULT_LABEL` (Binary: 1 if 90+ days delinquent or foreclosure, 0 otherwise).

## 2. Intended Use
* **Primary Use:** Proof-of-Concept (POC) for automated credit scoring in a mortgage lending context.
* **Intended Users:** Risk Officers and Credit Analysts at financial institutions (Banks/SACCOs).
* **Out-of-Scope:** This model is for research/demonstration and is not intended for live lending decisions without further hyperparameter tuning and local market recalibration.

## 3. Technical Rationale: Why Random Forest?
In selecting an algorithm, I benchmarked **Logistic Regression** against **Random Forest**. While Logistic Regression is the industry legacy standard, I chose Random Forest for the following reasons:

* **Handling Non-Linearity:** Credit risk factors rarely have a linear relationship with default. For example, a high Debt-to-Income (DTI) ratio doesn't just increase risk; at a certain "tipping point," risk spikes exponentially. Random Forest captures these "threshold" effects natively through its tree-based structure.
* **Feature Interaction:** Financial variables are highly interdependent. High Loan-to-Value (LTV) combined with low FICO scores creates a risk profile greater than the sum of its parts. Random Forest excels at identifying these complex interactions.
* **Robustness to Outliers:** Financial data is "noisy." Random Forest is an ensemble method that aggregates multiple decision trees, making it less sensitive to outliers and variance in the 3M+ record dataset.


## 4. Metrics & Evaluation
Because of the significant **Class Imbalance** (Defaults < 2%), **Accuracy** was discarded as a primary metric. Instead, the model was optimized for:

* **F1-Score:** To balance the trade-off between Precision and Recall.
* **Precision-Recall AUC:** To ensure the model remains performant across different decision thresholds.
* **Cost-Weighted Evaluation:** Prioritizing the reduction of **False Negatives** (undetected defaults), which carry the highest financial cost (Principal Loss).

The financial impact is measured via the **Expected Loss (EL)** formula:
$$\text{Expected Loss} = \text{PD} \times \text{LGD} \times \text{EAD}$$

## 5. Ethical & Regulatory Considerations
* **Transparency:** Integrated with **SHAP (Explainable AI)** to ensure compliance with the **Kenya Data Protection Act (2019)** regarding the "Right to Explanation" for automated decisions.
* **Fairness:** Features were restricted to financial and collateral metrics (FICO, DTI, LTV). Personal demographic data was excluded to prevent algorithmic bias.
