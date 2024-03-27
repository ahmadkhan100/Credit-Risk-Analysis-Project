# Credit Risk Analysis Project

## Overview
This project aims to analyze and predict credit risk using financial lending data. By applying machine learning techniques, we intend to identify potential risk factors that influence loan defaults, thereby aiding in making informed lending decisions.

## Project Structure
credit-risk-analysis/
│
├── README.md
├── requirements.txt
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── data_preparation.ipynb
│ ├── exploratory_data_analysis.ipynb
│ └── model_building_and_evaluation.ipynb
│
├── src/
│ ├── data
│ │ ├── make_dataset.py
│ │ └── clean_dataset.py
│ ├── features
│ │ ├── build_features.py
│ │ └── scale_features.py
│ ├── models
│ │ ├── train_model.py
│ │ └── evaluate_model.py
│ └── visualization
│ └── visualize.py
│
└── tests/
└── test_data.py

For a detailed explanation of the project structure, see [GitHub Repository Structure](#github-repository-structure).

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ahmadkhan100/credit-risk-analysis.git
2.  Navigate to the project directory:
     cd credit-risk-analysis

3. Install the required packages:
  pip install -r requirements.txt

## USAGE: 

1. Start with the data preparation notebook:
jupyter notebook notebooks/data_preparation.ipynb

2. Proceed with exploratory data analysis:
jupyter notebook notebooks/exploratory_data_analysis.ipynb

3. Finally, run the model building and evaluation notebook:
jupyter notebook notebooks/model_building_and_evaluation.ipynb


