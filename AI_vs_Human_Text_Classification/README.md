# AI vs. Human Text Binary Classification

This project is a text classification model designed to distinguish between **AI-generated** and **human-written** text. It leverages a Kaggle API dataset for training and evaluation.

<h2 id="project-overview">Project Overview</h2>
---
The core of this project is a **binary classification** task. The primary goal is to accurately categorize text as either "AI" or "Human." I explored two models for this task:

-   **Base Model: Logistic Regression** 
    -   This model achieved a prediction accuracy of **95%** on the training data.
-   **Production Model: Naive Bayes** 
    -   Selected for its efficiency and strong performance, this model achieved a prediction accuracy of **97%** on the training data, making it the more reliable choice for live predictions.

<h2 id="Model-Selection">Model-Selection</h2>
---
- **Why Logistic Regression?**
  - Simple and effective for binary classification problems.
  - Easy to interpret and understand.
  - Performs well with linearly separable data.
  - Provides a good baseline to compare with more advanced models.

- **Why Naive Bayes?**
  - Performs good for smaller dataset.
  - Performs better than Logistic Regression in this case, likely due to the way it handles word frequency and text features.

<h2 id="performance-and-limitations">Performance and Limitations</h2>
---
While both models show high accuracy on the trained data, their performance on **unseen data** is limited. This is primarily due to the **small size** and scope of the initial dataset. 

<h2 id="future-improvements">Future Improvements</h2>
---
To overcome the current limitations, the following improvements are planned:

-   **Data Acquisition**: Collect a larger and more diverse dataset from a variety of sources to improve the model's ability to generalize.
-   **Continuous Training**: Implement a system for continuous training and model updates as more data becomes available.
