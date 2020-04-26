# Trady

This project is a machine learning example for forex prediction using RandomForestClassifier. 

Disclaimer : 50% of the time it works every time. 

## How to make prediction ? 

1) Download the currency pair you want to predict 
2) Generate features using generator.py. You may add more features this way : 

```python
...
data['cci'] = trend.cci(data['bidhigh'], data['bidlow'], data['bidclose'])
...
```

3) Generate the model using the results.csv file 
4) Dowload last market data using test.py script 
5) Become bald 
6) Become bankrupt 
7) Get a proper job 
