# Forest-Fires-Regression
This regression project uses the forest fires dataset from UCI Machine Learning Repository. This project is aimed to analyse the dataset and create regression models based on the best R2 scores.

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

## Link to the Dataset
[UCI ML Repository, Forest Fires Data Set](https://archive.ics.uci.edu/ml/datasets/forest+fires)

## References
1. [Cortez, Paulo & Morais, A.. (2007). A Data Mining Approach to Predict Forest Fires using Meteorological Data.](https://www.researchgate.net/publication/238767143_A_Data_Mining_Approach_to_Predict_Forest_Fires_using_Meteorological_Data)
2. [Model Building with Forest Fire Data: Data Mining, Exploratory Analysis and Subset Selection](http://fisher.stats.uwo.ca/faculty/aim/2018/4850G/projects/FIREProjectFinalReport.pdf)
3. [Predict The Burned Area Of Forest Fires](https://www.kaggle.com/code/elikplim/predict-the-burned-area-of-forest-fires/notebook)
4. [Basic regression: Predict fuel efficiency](https://github.com/tensorflow/docs/blob/a3fbfca0af5773cec68c17c1b1ea6cb21d35f791/site/en/tutorials/keras/regression.ipynb)
