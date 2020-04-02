"""The idea is to put any math utility routines that we need to write in this module"""
import numpy as np
import scipy.integrate as integrate
import  math

def integral(f, xmin, xmax, nsteps, logspace = True):
    """
    Name: 
        integrate
    
    Purpose:
        Integrate 1D functions using specified gridpoints, and optionally running until convergence to within a percentage, eBounds
    
    Explanation: 
        Integrate using a basic right-handed Riemann sum. 
    
    Calling Seuqence:
        integrator, f, xmin, xmax, nsteps, F
        
    Input/Output:
        f - The function to be integrated. Must return a float.
        xmin - Lower bound of integration
        xmax - Upper bound of integration
        nsteps - The number of points to use for computing the integral, as a starting point
    
    Limitations: If any gridpoints fall on a singularity, the routine will fail. 
    If there is a divergence not directly evaluated, the integral will fail to converge
    and we will get a nonsense answer. 
        
        
    
    """
    if logspace == True:
        xgrid = np.logspace(np.log10(xmin), np.log10(xmax), nsteps+1)
    else:
        xgrid = np.linspace(xmin, xmax, nsteps + 1)
    
    ygrid = f(xgrid)
    integral = integrate.simps(ygrid, xgrid)
    return integral

def e_n(n, x, nsteps = 1e4, xmax = 1e2):
    """
    Name: 
        e_n
    
    Purpose:
        Calculate the exponential integral functions, E_n(x)
    
    Explanation: 
        The functions are 
        .. math:: E_n = \\int_1^\infty e^{-x t}/t^n dt
    
    Calling Seuqence:
        e_n, x, n, nsteps, xmax
        
    Input/Output:
        x - the point at which to evaluate E_n
        n - the order of the function
        nsteps - The number of points to use for computing the integral
        xmax - the maximum xvalue to integrate to integrate out to 
    
    Limitations: If any gridpoints fall on a singularity, the routine will fail. 
    If there is a divergence not directly evaluated, the integral will fail to converge
    and we will get a nonsense answer. 
        
        
    
    """
    integral = np.zeros(len(x))
    j = 0
    for point in x:
        xgrid = np.logspace(0, np.log10(xmax), nsteps)
        ygrid = np.exp(-point*xgrid) / (xgrid**n)
        integral[j] = (integrate.simps(ygrid, xgrid))
        j += 1
    return integral
    

        