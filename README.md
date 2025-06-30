# Bati Bank Credit Scoring Model

## 1. Credit Scoring Business Understanding

### Objective

To develop a credit scoring model that estimates the default risk of users based on their transaction behavior in an eCommerce environment. This model will support buy-now-pay-later (BNPL) partnerships.

### Regulatory Context: Basel II and Model Interpretability

Under Basel II, financial institutions are required to:

- Ensure models used for credit risk are interpretable, auditable, and well-documented.
- Quantify model risk and ensure stable performance over time.
- Use conservative assumptions if uncertainty exists in model predictions.

As a result, **model transparency and interpretability** are essential, especially when decisions affect lending, capital reserves, or customer approval.

### Why a Proxy Target is Needed

The dataset provided does not contain actual loan defaults or payment history.
To address this, we create a **proxy label** using:

- **Recency** of activity
- **Frequency** of transactions
- **Monetary value** of transactions (RFM analysis)

By clustering customers using these dimensions, we assume that users who are inactive (high recency), low-frequency, and low monetary value are **higher risk**.

This is not perfect — some mislabeling is expected — but it’s a **practical solution** for bootstrapping credit modeling in the absence of labeled outcomes.

### Trade-offs: Simple vs Complex Models

| Factor           | Simple (Logistic, WOE) | Complex (XGBoost, RF)               |
| ---------------- | ---------------------- | ----------------------------------- |
| Interpretability | ✅ High                | ❌ Low                              |
| Regulatory Fit   | ✅ Basel-friendly      | ⚠️ Requires explanation (e.g. SHAP) |
| Accuracy         | ⚠️ Moderate            | ✅ High                             |
| Deployment       | ✅ Lightweight         | ⚠️ Heavier infra requirement        |
| Maintenance      | ✅ Easier              | ⚠️ Risk of overfitting              |

In early-stage fintech or new credit products like BNPL, **starting with simpler interpretable models** is preferred. Complex models may be used later with added explainability techniques.

---

## 2. Project Tasks

- ✅ Task 1: Business Understanding
- ⏳ Task 2: Exploratory Data Analysis (EDA)
- ⏳ Task 3: Feature Engineering
- ⏳ Task 4: Target Variable via Clustering
- ⏳ Task 5: Model Training & MLflow Tracking
- ⏳ Task 6: API + Docker + CI/CD
