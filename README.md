# Mushroom Classification API 🍄

**Project Overview:**  
This project predicts whether a mushroom is edible or poisonous based on its physical characteristics. It uses the [Mushroom Classification dataset](https://www.kaggle.com/datasets/uciml/mushroom-classification) and exposes the predictions through a simple API.

## Tools & Technologies

-   Python – main programming language
-   pandas – data manipulation and preprocessing
-   scikit-learn – machine learning (Decision Tree and Random Forest)
-   FastAPI – serving predictions via API
-   Docker – containerizing the API for deployment
-   pickle / joblib – saving trained models and input features

## How It Works

1. **Data processing and exploration**

    - The dataset is loaded and explored to understand the features.
    - Categorical variables are one-hot encoded to prepare them for modeling.

2. **Modeling**

    - A decision tree is trained first to identify which features matter most.
    - A random forest is trained for better accuracy and validated using 5-fold cross-validation.
    - K-Nearest Neighbors (KNN) experiments: KNN was also tested as a baseline classifier. Categorical features were label-encoded, and various values of `k` were evaluated using both train/test splits and cross-validation. While KNN achieved high accuracy, it was generally outperformed by the random forest model in terms of robustness and overall performance.

3. **Deployment**
    - The trained model and feature list are saved with pickle and joblib.
    - A FastAPI endpoint allows users to submit mushroom features and get a prediction.
    - The API is containerized with Docker for easy deployment.

## Features

-   Real-time mushroom classification via an API
-   Ensemble modeling with random forest for robust predictions
-   Containerized deployment for portability

## Summary

This project shows a complete workflow from data exploration and modeling to deployment, resulting in a practical system for automatically classifying mushrooms.
