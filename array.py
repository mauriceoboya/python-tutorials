import pandas as pd
import numpy as np
import os
 
def printOutTheCoefficients(params,coeffecients,intercept):
    tParams = params[np.newaxis].T
    tCoeffs = coeffecients.T
    total = np.concatenate([tParams,tCoeffs],axis=1)
    totalDF = pd.DataFrame(data=total)
    totalDF.to_csv('/home/fibonacci/modelOutput.csv')
    print(totalDF)
    
