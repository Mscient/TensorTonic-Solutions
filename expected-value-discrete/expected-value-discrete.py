import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    
    prob=0;
    total_prob=0;
    
    for i in range(len(x)):
        prob=prob+p[i]*x[i]
        total_prob+=p[i]
    if(total_prob!=1):
        raise ValueError

    return prob
  
    pass
