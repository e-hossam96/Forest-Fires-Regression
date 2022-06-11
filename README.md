# Forest Fires Regression
## Introduction
<img align="right" width="100" height="100" src="https://user-images.githubusercontent.com/72099185/161308460-ff41ee80-09c5-4c92-9cd6-37df955598c7.jpg">

Forest fires have somewhat of a major impact on the environment. That's why having a model that predicts the burned area of a forest in advance will help prevents such terrible impacts. These predictions shall trigger the appropriate level of precautions to maintain or even prevent them from happening.

This regression project uses the forest fires dataset from UCI Machine Learning Repository. This project is aimed to analyse the dataset and create regression models based on the best R2 scores. Throughout the three notebooks of the project, we will implement data cleansing, transformation, and modeling as appoved in the literature. See `References` at the end of this README file to find out more.

## Dataset Description
### Attributes
#### Features

*Spatial Attributes (S)*
* X     : x-axis coordinate (from 1 to 9)
* Y     : y-axis coordinate (from 1 to 9)

*Temporal Attributes (T)*
* month : Month of the year (January to December)
* day   : Day of the week (Monday to Sunday)

*Fire Weather Index Attributes (FWI)*
* FFMC  : Fine Fuel Moisture Code
* DMC   : Duff Moisture Code
* DC    : Drought Code
* ISI   : Initial Spread Index

*Weather/Meteorological Attributes (M)*
* temp  : Outside temperature (in Celsius)
* RH    : Outside relative humidity (in percentage)
* wind  : Outside wind speed (in kilometer per hour)
* rain  : Outside rain (in millimeter per square meter)

#### Target Variable
* area  : Total burned area (in ha)

### Link to the Dataset
[UCI ML Repository, Forest Fires Data Set](https://archive.ics.uci.edu/ml/datasets/forest+fires)

## Notebook 01 Summary
* In this notebook we have explored different regression models trying to come up with good R2 scores but the data distributions and coorelations among features themselves and with the target vaiable are not satisfying the linear regression models.<br>
* Also, as suggested from literature, we have tried using different subsets of the full data and tried to regress on only the nonzero observations but still no good results show up.<br>
* For the sake of finding different interactions among data features, we tried different techniques including adding polynomial and spline features. Yet, nothing produced good results but the spline transform proved to have good significance on the R2 score. For that reason, we only included the spline transformations and obmitted the polynomial transformations.<br>
* In addition, we defined a function to print out the maximum R2 score when selecting subset features of the full data attributes [scoringfn](https://github.com/E-Hossam96/Forest-Fires-Regression/blob/0b0817c6a0ba4c53bebb360351d8f0711d0f47df/scoringfn.py). we used two techniques: the first was using different combinations using the `combinations` class from the `itertools` library, and the second was using automatic feature selection from `feature_selection` module. When using automatic feature selection, we used only the `RFE` (recursive feature elemination) class for having the best selection process.<br>
* Lastly, we reied different transormation techniques on the features including `boxcox` transformation, but it gave errors. So, we kept only the `np.sin` and `np.log1p`.

## Notebook 02 Summary
In this notebook we used tree based regression models to fit the data. Of course, after somewhat overfitting the data, we managed to produce better R2 scores. The best three models came out to be `DecisionTreeRegressor`, `ExtraTreeRegressor`, and `ExtraTreesRegressor`. The R2 scores were respectively as follows: 0.996112, 0.996112, 0.996112. For the sake of producing these results without repeating any steps, we produced a `python` `class` to fit and print the scores on the training and testing datasets [Evaluate_Model](https://github.com/E-Hossam96/Forest-Fires-Regression/blob/0b0817c6a0ba4c53bebb360351d8f0711d0f47df/Evaluate_Model.py).

## Notebook 03 Summary
In this notebook we used the deep learning approach to predict the burned area. We have applied different `Sequential` models that have different `layers` from the `tensorflow` software using `keras` library. The results weren't that much perfect but `loss` and `val_loss` values converged to their minimum. We also defined some [utility_functions](https://github.com/E-Hossam96/Forest-Fires-Regression/blob/0b0817c6a0ba4c53bebb360351d8f0711d0f47df/utility_functions.py) to produce the results and plot the propagation of `loss` and `val_loss` values.

## References
1. [Cortez, Paulo & Morais, A.. (2007). A Data Mining Approach to Predict Forest Fires using Meteorological Data.](https://www.researchgate.net/publication/238767143_A_Data_Mining_Approach_to_Predict_Forest_Fires_using_Meteorological_Data)
2. [Model Building with Forest Fire Data: Data Mining, Exploratory Analysis and Subset Selection](http://fisher.stats.uwo.ca/faculty/aim/2018/4850G/projects/FIREProjectFinalReport.pdf)
3. [Predict The Burned Area Of Forest Fires](https://www.kaggle.com/code/elikplim/predict-the-burned-area-of-forest-fires/notebook)
4. [Basic regression: Predict fuel efficiency](https://github.com/tensorflow/docs/blob/a3fbfca0af5773cec68c17c1b1ea6cb21d35f791/site/en/tutorials/keras/regression.ipynb)
