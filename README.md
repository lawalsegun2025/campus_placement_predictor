# WhatsApp Text Analyzer

## Table of Content
*  [Demo](#demo)
* [Overview](#overview)
* [Motivation](#motivation)
* [Problem Solving Steps](#problem-solving-steps)
* [Source of Dataset](#source-of-dataset)
* [Data Cleaning Techniques](#data-cleaning-techniques)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Model Building](#model-building)
* [Model Performance](#model-performance)
* [Deployment](#deployment)
* [Future scope of project](#future-scope-of-project)

## Demo




https://github.com/lawalsegun2025/jop_placement_predictor/assets/94943377/a75d0994-a1b1-4374-a5dd-7c220836764a




## Overview

This project builds a model that predicts whether a student can get job placement opportunity after graduating based on his/her academic performance, work experiences, projects etc. 
</br></br>

<div align="center">
  <img src="img/students.jpeg">
</div>

## Motivation

The Placement of students is one of the most important objective of an educational institution. Reputation and yearly admissions of an institution invariably depend on the placements it provides it students with. That is why all the institutions, arduously, strive to strengthen their placement department so as to improve their institution on a whole. Any assistance in this particular area will have a positive impact on an institution’s ability to place its students. This will always be helpful to both the students, as well as the institution. 

## Problem Solving Steps
1. Load the data into a dataframe
2. Perform Data Preprocessing like handling missing values, feature creation etc.
3. Perform Eploratory Data Analysis and get valuable insights from the data
4. Perform feature selection and select the best algorithm which fits the data
5. Save the model in a pickle file and integrate the model with the UI which is made using flask.
6. Deploy the model web app on a cloud platform

## Source of Dataset

This data set consists of Placement data of students in a XYZ campus. It includes secondary and higher secondary school percentage and specialization. It also includes degree specialization, type and Work experience and salary offers to the placed students.

I would like to thank Dr. Dhimant Ganatara, Professor Jain University for helping the students by providing this data.

Data set can be found [here](https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement)

## Data Cleaning Techniques

The `salary` column was the only column with missing values which were filled with the mean salary. This because visualizing the comparison between mean salary, mode salary and median salary, mean salary had a better representation of the salary distribution.

## Exploratory Data Analysis

Extensive Data Analysis was carried out during this project to help understand the data and answer importand questions such as;
- Top 5 earns from each degree coure
- Maximum and Minimum Salary
- Maximun number of students placed from each department
- Which Departnment get the most placement
- Percentage of Male and Female Placement

## Model Building
Feature Selection was carried out using `ExtraTreesClassifier` feature importance and `mutual_infor_classif`. This is to get the features that contributes the most to predicting the target.

4 Models were built, these include
- RandomForestClassifier
- Logistic Regression
- DecisionTreeClassifie and
- SVM 


## Model Performance

RandomForestClassifier was the best performing model with an accuracy of over 88%

## Deployment

The model was deployed on Render cloud platform

## Future scope of project

Get more data to improve theaccuracy and performance of the model



