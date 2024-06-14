# Cervical Cancer Prediction Project

## Meet The E.R. Staff

- Vanessa Jimenez

- Luis Millet

- Rayner Morla

- Rad Joe



## Project Overview

This project aims to leverage Machine Learning (ML) to predict the likelihood of cervical cancer based on patient's historical data. Early detection of cervical cancer can significantly improve treatment outcomes and reduce mortality rates. By analyzing a dataset containing medical history we aim to build a predictive model that assists in early diagnosis.


## The Critical Question

How accurately can we predict the likelihood of a patient developing cervical cancer using medical history?


## Data Sources:

- Dataset: Cervical Cancer Risk Factors dataset from the UCI Machine Learning Repository.
  - Link: [UCI Cervical Cancer Risk Factors Dataset](https://archive.ics.uci.edu/dataset/383/cervical+cancer+risk+factors)


## Data Wrangling, Cleaning & Manipulation

Data Cleaning and Wrangling:

   - Dropped columns with majority missing values and filled NaN values based on mean and median
   - Corrected data types
   - Removed outliers
   - Encoded, scaled and oversampled the data for the model

## Findings
Through the use of Randomized Search we found that LogisticRegression with parameters max_iter=1000, penalty='l1', solver='saga' to provide the best performing model compared to the original, basic model we first created.


## Presentation

Link - https://www.canva.com/design/DAGHw-5U4jg/D4Zp5sPMn3U5NrrIl9gpcQ/edit
