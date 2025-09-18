Project Overview

This project is a **Fake News Detector** developed to classify news headlines as either "Fake" or "Real" using machine learning techniques. We focused on building a highly accurate model from scratch in a very short amount of time, demonstrating the efficiency of natural language processing for real-time applications.

Features

  - Accurate Classification:** The model uses two different algorithms to classify headlines.
      - Logistic Regression** model achieved **94% accuracy**.
      - Random Forest** model achieved **92% accuracy**.
  - User-Friendly UI:** A simple and interactive user interface built with **Streamlit** that allows users to input a headline and get an instant result.
  - Pattern Recognition:** The model analyzes patterns and keywords in text to make a decision.
  - Scalable Design:** The current model works on text strings but is designed to be expanded with web scraping capabilities for real-time news analysis in the future.

Technology Stack

  - Python
  - Scikit-learn
  - Pandas
  - Streamlit
  - HTML/CSS (for the UI)

-----

Files in this Repository

  - `model_train.py`: This script contains the code for data preprocessing, model training, and evaluation. It shows how the Logistic Regression and Random Forest models were trained and their accuracies were calculated.
  - `main.py`: This file contains the backend logic and the Streamlit code for the user interface. It loads the trained model and processes user input to provide predictions.
  - `background.png`: A background image used for the Streamlit UI to give it a polished look.

-----
How to Run the Project Locally

Follow these simple steps to get the project up and running on your local machine:

1.  Clone the repository:

    ```bash
    git clone [Your GitHub Repo Link]
    ```

2.  Navigate to the project directory:

    ```bash
    cd Fake-News-Detector
    ```

3.  Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4.  Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

    (Note: You'll need to create a `requirements.txt` file by running `pip freeze > requirements.txt` after installing all dependencies.)

5.  Run the Streamlit app:

    ```bash
    streamlit run main.py
    ```

The app will open in your browser, and you can start testing the fake news detector\!

-----

## Future Enhancements

  - Integrate a web scraper to check the authenticity of a news article's source.
  - Improve the model's accuracy by training it on a larger and more diverse dataset.
  - Develop a full-fledged web application using Flask or Django for deployment.
