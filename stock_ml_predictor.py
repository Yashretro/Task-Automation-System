# My First Machine Learning Project
# Stock Price Predictor - Learning ML by building!

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import yfinance as yf

print("🚀 Welcome to your first ML project!")
print("We're going to predict stock prices using machine learning!")