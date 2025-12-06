🤖 **Model Building & Evaluation**

I experimented with three machine learning algorithms to identify the best model for heart disease prediction:

🔹 Models Tried

1. Logistic Regression

2. K-Nearest Neighbors (KNN)

3. Random Forest Classifier
------------
📈 **Baseline Model Accuracies**

Model	Accuracy

Logistic Regression	88.5%

K-Nearest Neighbors	68.8%

Random Forest	83.6%

* Logistic Regression performed the best even before tuning.

------------

🎛 **Hyperparameter Tuning**

✔ 1. KNeighborsClassifier tuning

Tuned n_neighbors, weights, distance metrics manually

Best accuracy obtained: 75.4%

KNN could not outperform Logistic Regression

------------

✔ 2. RandomizedSearchCV (cv = 5) for Random Forest

Performed hyperparameter search on:

n_estimators, max_depth, min_samples_split, min_samples_leaf

Best accuracy: 86.8%

Although accuracy improved slightly, it was still lower than Logistic Regression

------------

✔ 3. RandomizedSearchCV & GridSearchCV for Logistic Regression

Tested multiple solvers, C-values

Both searches produced same best accuracy: 88.5%

Logistic Regression consistently remained the strongest model

------------

🏆 Final Model Chosen: **Logistic Regression**

Reasons:

Highest accuracy (88.5%)

More stable performance across different validation sets

Interpretable coefficients

Lower variance compared to Random Forest

Lower computational cost

------------

🧪 **Evaluation Metrics Performed on Logistic Regression**

To ensure the model performance was reliable, I evaluated using:

✔ Confusion Matrix

Shows True Positive, True Negative, False Positive, False Negative values.

✔ Classification Report

Includes:

Precision

Recall

F1-score

✔ ROC Curve & AUC Score

AUC score indicates strong separability

Logistic Regression achieved high AUC, confirming strong performance

✔ Feature Importance (Coefficients)

Identified which variables most strongly impact heart disease prediction

Helpful for medical interpretability

------------
📊 **Model Comparison Plot**

<p align="center">
  <img src = "https://github.com/user-attachments/assets/5ded4cc1-8ce5-4aba-ac72-d525145b3a9e" width="500">
</p>
