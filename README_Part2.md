# Part 2 – Feature Engineering, Regression, and Classification

## Dataset Used
This part of the project uses the cleaned dataset generated in Part 1: `cleaned_data.csv`.

The dataset contains stock-market related features such as opening price, high price, low price, trading volume, engineered date features, and categorical variables such as day name and volume category.

---

# 1. Label Definitions

## Regression Label
The continuous regression target was defined as:

- **`y_reg = close`**

This means the regression model is trained to predict the stock’s **closing price**.

## Classification Label
A binary classification target was created from the regression label by binarizing the closing price at its median:

- **`y_clf = (close > close.median()).astype(int)`**

Interpretation:
- **1** → closing price is above the median closing price
- **0** → closing price is at or below the median closing price

This converts the continuous price prediction problem into a binary classification problem.

---

# 2. Feature Matrix Definition

The feature matrix **X** was created from all columns except the target and columns with clear leakage risk.

The following columns were **excluded**:
- **`close`** → used as the regression target
- **`adj_close`** → dropped to reduce leakage risk because it is extremely close to the closing price
- **`date`** → dropped in raw string form because it is not directly usable without further time-series feature engineering

The remaining columns were used as input features for both regression and classification.

---

# 3. Encoding of Categorical Variables

## 3.1 Ordinal Encoding
The column **`volume_category`** was encoded using label/ordinal encoding because it has a **natural order**:

- **Low → 0**
- **Medium → 1**
- **High → 2**

### Justification
This ordering preserves the real meaning of the categories:  
**Low < Medium < High** in terms of trading volume level.

---

## 3.2 One-Hot Encoding
The columns **`ticker`** and **`day_name`** were treated as **nominal categorical variables** and encoded using **one-hot encoding** with `drop_first=True`.

### Why one-hot encoding was used
These categories do **not** have a natural numerical order. For example:
- `Monday`, `Tuesday`, and `Wednesday` are labels, not ranked quantities
- ticker names are identifiers, not ordered values

If label encoding were used for such columns, it would incorrectly imply a false ordinal relationship such as:
- Monday < Tuesday < Wednesday
- one ticker being “larger” than another ticker

One-hot encoding avoids this false-ordinal problem by creating separate binary indicator columns for each category.

---

# 4. Train-Test Split and Leak-Free Scaling

The data was split into training and test sets using:

```python
train_test_split(X, y, test_size=0.2, random_state=42)
```

A **StandardScaler** was then applied as follows:

1. Fit the scaler **only on the training set**
2. Transform the training set using the fitted scaler
3. Transform the test set using the same scaler

## Why fitting the scaler on the full dataset would be data leakage
If the scaler were fit on the **entire dataset**, the mean and standard deviation of the **test set** would influence the scaling transformation. That would leak information from the test data into training, making evaluation unrealistically optimistic. To avoid this, the scaler was fit **only on `X_train`**.

---

# 5. Regression Task – Linear Regression

A **Linear Regression** model from `sklearn.linear_model` was trained on the scaled training features to predict the closing price.

## Evaluation Metrics
The regression model was evaluated on the test set using:

- **Mean Squared Error (MSE)**
- **R² score**

### Linear Regression Results
- **MSE:** `<fill from outputs/part2_summary_metrics.csv>`
- **R²:** `<fill from outputs/part2_summary_metrics.csv>`

---

# 6. Linear Regression Coefficients and Interpretation

The model coefficients were printed alongside their corresponding feature names.

## Interpretation of coefficients
Because the features were standardized, each coefficient represents the expected change in the predicted closing price for a **one standard deviation increase** in that feature, holding the other features constant.

- A **large positive coefficient** means that as the scaled feature increases by one unit, the predicted closing price **increases** by the coefficient value.
- A **large negative coefficient** means that as the scaled feature increases by one unit, the predicted closing price **decreases** by the coefficient value.

## Top 3 features with the largest absolute coefficient values
The three most influential features were identified by sorting the coefficients based on their absolute values. These can be read from:

- `outputs/linear_regression_coefficients.csv`

---

# 7. Ridge Regression

A **Ridge Regression** model with `alpha=1.0` was trained using the same training and test split and the same scaled features.

## Ridge vs Linear Regression Comparison

| Model | MSE | R² |
|---|---:|---:|
| Linear Regression | `<fill from outputs/regression_comparison.csv>` | `<fill from outputs/regression_comparison.csv>` |
| Ridge Regression (alpha=1.0) | `<fill from outputs/regression_comparison.csv>` | `<fill from outputs/regression_comparison.csv>` |

## Why Ridge can produce different coefficients than OLS Linear Regression
Ordinary Least Squares (OLS) Linear Regression chooses coefficients that minimize the residual sum of squares. Ridge Regression adds an **L2 penalty** on the magnitude of the coefficients. This penalty shrinks coefficients toward zero, which can reduce overfitting and improve stability when predictors are correlated. The parameter **alpha** controls the strength of this penalty:
- **larger alpha** → stronger shrinkage
- **smaller alpha** → weaker shrinkage and behavior closer to ordinary linear regression

---

# 8. Classification Task – Logistic Regression

A logistic regression model was trained to predict whether the closing price is above the median.

## Class imbalance handling
The class distribution in `y_clf_train` was checked using:

```python
y_clf_train.value_counts()
```

If one class had fewer than 35% of the samples, imbalance handling was applied using:

- **`class_weight='balanced'`**

### Why this method was chosen
`class_weight='balanced'` increases the importance of the minority class during training without generating synthetic samples. It is simple, effective, and prevents the model from becoming biased toward the majority class.

The before/after class distribution should be reported in the notebook output.

---

# 9. Classification Metrics

The baseline logistic regression model (`C=1.0`) was evaluated using:

- confusion matrix
- accuracy
- precision
- recall
- F1-score
- ROC curve
- AUC

## Confusion Matrix
The confusion matrix is generated in the notebook and also saved in:

- `outputs/classification_report_baseline.txt`

## Baseline Logistic Regression Results
- **Accuracy:** `<fill from outputs/part2_summary_metrics.csv>`
- **Precision:** `<fill from outputs/part2_summary_metrics.csv>`
- **Recall:** `<fill from outputs/part2_summary_metrics.csv>`
- **F1-score:** `<fill from outputs/part2_summary_metrics.csv>`
- **AUC:** `<fill from outputs/part2_summary_metrics.csv>`

---

# 10. Precision and Recall Formulas

Let:
- **TP** = True Positives
- **FP** = False Positives
- **FN** = False Negatives

Then:

## Precision
\[
Precision = \frac{TP}{TP + FP}
\]

Precision answers: **Of all samples predicted as positive, how many were actually positive?**

## Recall
\[
Recall = \frac{TP}{TP + FN}
\]

Recall answers: **Of all actual positive samples, how many did the model successfully detect?**

---

# 11. Which Metric Matters More for This Task?

In this project, the classification task predicts whether the closing price is above the dataset median.

A reasonable interpretation is:

- If the goal is to **avoid missing high-price days**, then **Recall** is more important because false negatives are costly.
- If the goal is to **avoid incorrectly flagging too many days as high-price days**, then **Precision** is more important because false positives are costly.

For this stock-price-above-median task, **Recall is usually the more important metric** if the use case is to identify potentially strong price days and avoid missing them. However, if predictions are used for automated actions where false alarms are expensive, precision may become more important.

---

# 12. ROC Curve and AUC

The ROC curve was plotted using the predicted probabilities from `predict_proba()`.

Saved file:
- `outputs/roc_curve_baseline.png`

## AUC Interpretation
The AUC (Area Under the ROC Curve) measures the model’s ability to rank positive cases higher than negative cases across all classification thresholds.

- **AUC = 1.0** → perfect separation
- **AUC = 0.5** → random guessing
- **Higher AUC** means better class separation

The baseline logistic regression AUC was:

- **AUC = `<fill from outputs/part2_summary_metrics.csv>`**

This means the model has that level of ability to distinguish between:
- days where closing price is above the median, and
- days where it is at or below the median.

---

# 13. Decision Threshold Sensitivity Analysis

The logistic regression model produces probabilities using:

```python
model.predict_proba(X_test_scaled)[:, 1]
```

Predicted probabilities were converted into class labels at thresholds:

- **0.30**
- **0.40**
- **0.50**
- **0.60**
- **0.70**

At each threshold, the following metrics were computed:
- Precision
- Recall
- F1-score

The results are saved in:

- `outputs/threshold_sensitivity.csv`

---

# 14. Threshold Analysis Interpretation

## Threshold that maximised F1-score
The threshold that produced the highest F1-score was:

- **Best threshold = `<fill from outputs/part2_summary_metrics.csv>`**

## Which metric is more important?
For this task, if missing above-median closing-price cases is more costly, then **Recall** is more important. If falsely predicting too many above-median days is more costly, then **Precision** is more important.

## Should the threshold be raised or lowered?
- **Lowering the threshold** usually increases **Recall** but may reduce **Precision**
- **Raising the threshold** usually increases **Precision** but may reduce **Recall**

### Cost of changing the threshold
- Lower threshold → more positives predicted → fewer missed positives, but more false positives
- Higher threshold → fewer false positives, but more actual positives may be missed

Thus, the threshold should be selected based on the business objective.

---

# 15. Logistic Regression Regularization Experiment

A second logistic regression model was trained with:

- **`C = 0.01`**

This applies **stronger regularization** than the baseline model (`C=1.0`).

## Comparison Table

| Model | Precision | Recall | F1 | AUC |
|---|---:|---:|---:|---:|
| Logistic Regression (C=1.0) | `<fill from outputs/logistic_regularization_comparison.csv>` | `<fill from outputs/logistic_regularization_comparison.csv>` | `<fill from outputs/logistic_regularization_comparison.csv>` | `<fill from outputs/logistic_regularization_comparison.csv>` |
| Logistic Regression (C=0.01) | `<fill from outputs/logistic_regularization_comparison.csv>` | `<fill from outputs/logistic_regularization_comparison.csv>` | `<fill from outputs/logistic_regularization_comparison.csv>` | `<fill from outputs/logistic_regularization_comparison.csv>` |

## What does C control in logistic regression?
In logistic regression, **C** is the inverse of regularization strength.

- **Large C** → weaker regularization
- **Small C** → stronger regularization

So:
- `C=1.0` = baseline regularization
- `C=0.01` = much stronger regularization

Stronger regularization shrinks the model coefficients more aggressively, which can reduce overfitting but may also reduce predictive power if the model becomes too constrained.

## Did reducing C improve performance?
After running the experiment, compare the precision, recall, and AUC values in the table above. If the `C=0.01` model has lower metrics, then strong regularization worsened performance. If it has higher metrics, then the extra regularization improved generalization on this dataset.

---

# 16. Bootstrap Confidence Interval for AUC Difference

To assess whether the baseline logistic regression (`C=1.0`) reliably outperformed the strongly regularized model (`C=0.01`), a bootstrap experiment was performed on the **test set**.

## Procedure
- Draw **500 bootstrap samples** from the test set using sampling **with replacement**
- For each sample:
  - compute AUC for the baseline model
  - compute AUC for the strong-regularization model
  - compute the difference:

\[
AUC_{C=1.0} - AUC_{C=0.01}
\]

- After 500 iterations, compute:
  - mean AUC difference
  - 2.5th percentile
  - 97.5th percentile

## Results
- **Mean AUC Difference:** `<fill from outputs/bootstrap_auc_difference_summary.csv>`
- **95% CI Lower Bound:** `<fill from outputs/bootstrap_auc_difference_summary.csv>`
- **95% CI Upper Bound:** `<fill from outputs/bootstrap_auc_difference_summary.csv>`

## Interpretation
- If the **95% confidence interval excludes zero**, then the performance advantage of the `C=1.0` model is likely consistent and reliable across different test samples.
- If the **95% confidence interval includes zero**, then the observed AUC difference may not be reliable and could be due to sampling variation.

---

# 17. Output Files Generated

The following outputs are generated by the Part 2 code:

- `outputs/linear_regression_coefficients.csv`
- `outputs/regression_comparison.csv`
- `outputs/classification_report_baseline.txt`
- `outputs/roc_curve_baseline.png`
- `outputs/threshold_sensitivity.csv`
- `outputs/logistic_regularization_comparison.csv`
- `outputs/bootstrap_auc_difference_summary.csv`
- `outputs/part2_summary_metrics.csv`

---

# 18. Conclusion

In this part of the project:

- A **regression model** was built to predict stock closing price
- A **binary classification model** was built to classify whether the closing price is above the median
- Categorical variables were encoded appropriately using ordinal and one-hot encoding
- Scaling was performed in a **leak-free** manner using only training data statistics
- Regression performance was compared between **Linear Regression** and **Ridge Regression**
- Classification performance was evaluated using **precision, recall, F1, ROC, and AUC**
- Threshold sensitivity analysis showed how changing the decision threshold affects performance
- A stronger regularization logistic model (`C=0.01`) was compared against the baseline model
- Bootstrap resampling was used to estimate the reliability of the AUC difference between the two logistic models

This completes the full Part 2 modeling workflow for the capstone project.
