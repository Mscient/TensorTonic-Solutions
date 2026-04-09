import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    MSE=0;
    y_pred=np.array(y_pred)
    y_true=np.array(y_true)
    if(y_true.shape!=y_pred.shape):
        return None
    mse=np.mean((y_pred-y_true)**2)
    return float(mse)
   
