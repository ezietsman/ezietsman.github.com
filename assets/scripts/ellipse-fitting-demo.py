#import prettyplotlib as plt
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'PT Sans'
# need matplotlib >= 1.4
matplotlib.style.use('ggplot')

#font = {'size': 16}
#matplotlib.rc('font', **font)
'''
    Script tot illustrate ellipse fitting problems on contours that have
    concave parts to them
'''


def convex_data(theta):
    # make some data
    Ma = 3.0
    ma = 2.5
    x0 = 5.0
    y0 = 4.0
    x = Ma*np.sin(theta) + x0
    y = ma*np.cos(theta) + y0

    return x, y


def concave_data(theta):
    # make some data
    Ma = 3.0
    ma = 2.5
    x0 = 5.0
    y0 = 4.0
    x = Ma*np.sin(theta) + x0
    y = ma*np.cos(theta) + y0

    # make the concave notch
    dpi = np.pi*2/12.
    notch = theta < dpi
    x[notch] = 0.75*Ma*np.sin(theta[notch]) + x0
    y[notch] = 0.75*ma*np.cos(theta[notch]) + y0

    return x, y


def error_function(params, xi, yi, theta):
    ''' Return residuals given params
    '''
    x0, y0, Ma, ma = params
    x = Ma*np.sin(theta) + x0
    y = ma*np.cos(theta) + y0
    return ((xi - x)**2 + (yi - y)**2)**0.5


def ellipse_func(params, theta):
    x0, y0, Ma, ma = params
    x = Ma*np.sin(theta) + x0
    y = ma*np.cos(theta) + y0
    return x, y


if __name__ == "__main__":

    # initial parameter estimates
    params = [0.0, 0.0, 1.0, 1.0]
    theta = np.linspace(0, 2*np.pi-2.0/21*np.pi, 21)

    x1, y1 = convex_data(theta)
    x2, y2 = concave_data(theta)

    fit1, success = scipy.optimize.leastsq(error_function,
                                           params,
                                           args=(x1, y1, theta))
    fit2, success = scipy.optimize.leastsq(error_function,
                                           params,
                                           args=(x2, y2,
                                                 theta))

    fittheta = np.linspace(0, 2*np.pi, 200)
    x1fit, y1fit = ellipse_func(fit1, fittheta)
    x2fit, y2fit = ellipse_func(fit2, fittheta)

    fig, ax = plt.subplots(1)
    ax.set_aspect('equal')

    # convex data
    plt.scatter(x1, y1, s=25, color='r')
    plt.plot(x1fit, y1fit, 'r', linewidth=1, label="Fit to convex data")
    plt.scatter((fit1[0],), (fit1[1],), color='r', marker='o')

    # concave data
    plt.scatter(x2, y2, s=25, color='g')
    plt.plot(x2fit, y2fit, 'g--', linewidth=1, label="Fit to concave data")
    plt.scatter((fit2[0],), (fit2[1],), color='g', marker='o')

    plt.legend(fontsize=16)
    plt.ylim(1, 8.5)
    plt.xlim(1.5, 8.5)
    ## As you noted.
    plt.savefig('output.png', bbox_inches='tight', pad_inches=0)
    plt.show()
