# ClassifyML
First ML project based on classification

## Components
* Front end HTML/JS/CSS UI where users upload image to be identified
* Backend server which connects to ML model that identifies image and returns to webpage

## Overview of steps (3/6 COMPLETE)
* Download dataset - DONE
* Find out how to get image data and encode to numeric data - DONE
* Generate model
* Create API
* Design frontend (css and html) - DONE
* Connect frontend to backend (Flask and js)

## Current Task
* Integrate model into server file - model uses LinearSVC model with the following properties: {'penalty': 'l2', 'dual'=False 'tol': 0.001} (Already ran grid search for best params) also use .env to capture filepath of csv


## To Do
* Link classify function to model to get answer produced
* Edit index.js to read answer (in body of response) and if resp.ok, go to result page with answer as the query param


## Completed
* Download dataset (ignored by git)
* Play with image encoding in jupyter
* Compile numeric data in csv
* Create and test model - linear regression etc.
* Create file structure for Flask
* Create .env file
* Add routes
* Create and test model - linear regression etc.

