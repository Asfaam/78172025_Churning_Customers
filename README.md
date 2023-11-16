-- Customer Churn Predictor --

## Overview
This project is a Customer Churn Predictor that utilizes machine learning to predict whether a customer is likely to churn. The model is built using a combination of exploratory data analysis (EDA), data pre-processing, feature selection, and a neural network (multi-layer perceptron using functional API) for classification. The deployment is done through a Streamlit web app, allowing users to input customer details and receive predictions on potential churn.

## Project Structure
The project is organized into two main parts:

Model Development: This section includes the Jupyter Notebook (78172025_Churning_Customers.ipynb) where the machine learning model is developed. It covers data analysis, preprocessing, feature selection, model training, and evaluation. Key libraries used include pandas, numpy, scikit-learn, TensorFlow, and Keras.

- **Data Analysis:** Exploratory Data Analysis is performed to understand the dataset, visualize key insights, and identify patterns.

- **Data Pre-processing:** Data cleaning, handling missing values, and converting categorical variables into numerical form are performed for effective model training.

- **Feature Selection:** A Random Forest classifier is used to identify the most relevant features for predicting customer churn.

- **Model Training:** A neural network is constructed using TensorFlow and Keras, and the model is trained on the selected features.

- **Model Evaluation:** The model's performance is assessed using various metrics, such as accuracy, precision, recall, and AUC score.

- **Deployment:** The deployment is done using Streamlit, and the relevant files are included in the deployment folder. The main deployment script is app.py, and the trained model is loaded from the saved file (churn_model.h5). User interface and interaction are handled through the Streamlit web app.

## Video Demonstration
For a detailed demonstration, watch this video [https://youtu.be/ntVdzrMcm-E]


## Future Improvements

- For a better prediction, we can consider incorporating additional features or experimenting with different machine learning models to enhance prediction accuracy.

- We can explore ways to optimize the neural network architecture for better performance.

- We can gather more diverse data to improve the model's ability to generalize to different customer demographics.


## Author
- Asmawu Ibrahim

---
