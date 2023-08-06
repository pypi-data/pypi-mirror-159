# stf_decomposition
stf_decomposition: Seasonal-Trend decomposition using the Fast Fourier transform

# Installation
Installing stf_deocmposition can be done with pip installation syntax
```
pip install stf-decomposition
```
The package is tested on Python 3.7, 3.8 and 3.9.

# Getting Started
In order to use stf_decomposition you will need a time series dataset of type pandas DataFrame or pandas Series. You will also need to specify the following input variables:
- window: A string indicating the name of a window function for use during the Fast Fourier transform process to reduce spectral leakage. 
The possible window inputs can be found in the [get_window](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html) scipy documentation. 
- period: An integer indicating the period of the time series input data. 
The period must be specified by the user if the input data does not have a frequency.

Optional input variable:
- seasonal: An integer indicating the seasonal window of the time series input data. 
If no input is given than an optimization function will be run to find the seasonal window that produces the smallest correlation between the seasonal and trend decomposed components. 
The code below shows reading in a Carbon Emissions time series dataset as a pandas DataFrame and
creating an `STF` object from the DataFrame with a "blackman" window. 
The CO2 input data has a frequency so a user specified period is not needed. 

```
co2 = pd.read_csv('data/co2.csv', index_col='date', parse_dates=True, squeeze=True)

stf = STF(co2, "blackman")
```

# Example
This demonstration will walkthrough the complete process of reading in data,
creating an `STF` object, fitting the object, 
and plotting the decomposed components.

1. Read in time series data as a pandas DataFrame or Series
```
from stf_decomposition import STF

data = pd.read_csv('data/AirPassengers.csv', index_col = "Month", parse_dates=True, squeeze=True)
```

2. Create an `STF` object and indicate a window, period (if needed), and seasonal window (if desired).
```
stf = STF(data, window = "hanning")
```

3. Fit the object. 
After fitting the decomposition you can access the trend, seasonal, and residual components.
```
res = stf.fit()

# View decomposed components
print(res.trend.head())
print(res.seasonal.head())
print(res.residual.head())
```
4. Plot the trend, seasonal, and residual components 
```
fig = res.plot()
```

# Testing
The package include a test suite that can be run in the main directory using the pystest library
```
pytest
```
