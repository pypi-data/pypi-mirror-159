# tv-slr
Implementation of time-varying SLR using OLS estimates

## Idea
One of the basic assumptions of the general linear model is that the parameters are constant over time. It has been often suggested that this may not be the valid assumption to make. In cross section studies there can be heterogeneity in the parameters across different units, where as in time series studies there can be variation over time in the parameters...
[paper link](https://www.researchgate.net/publication/348422809_TIME_VARYING_ESTIMATION_OF_REGRESSION_MODEL_USING_OLS_ESTIMATES)

## Installation
    pip install tvslr

## Usage
### In python
```python
    from tvslr.tvslr import TVSLR
    """
        X:= numpy array containing the independent feature vectors
        y:= numpy array containing dependent variable
        n:= subset size (must be greater than number of independent features including intercept variable)
    """

    reg = TVSLR(X, y, n)
    betas = reg.run()
    print(betas)
    print("R-squared:", reg.cod)
    print("Adj. R-squared:", reg.adj_cod)
```

### In command prompt
```bat
    python -m tvslr <excel filename> <sheetname> <subset size>
```
