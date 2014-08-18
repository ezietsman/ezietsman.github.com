import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'PT Sans'
# need matplotlib >= 1.4
matplotlib.style.use('ggplot')

'''
    Script to demonstrate the encoding calculation
'''

if __name__ == "__main__":
    # make dummy data
    theta = np.linspace(0, 2*np.pi, 144)
    value1 = np.zeros_like(theta) + 255
    value2 = np.zeros_like(theta)

    # create the notches
    value1[60:72] = 0
    value2[60:72] = 255

    # calculate the data so that zero notch is at start
    zero = np.where(value1 == 0)
    notch_theta = theta[zero]
    start_notch = min(notch_theta)
    start_index = np.where(theta == start_notch)[0][0]

    newvalue1 = np.roll(value1, -start_index)
    newvalue2 = np.roll(value2, -start_index)

    # plot
    fig, ax = plt.subplots(1)
    fig.set_size_inches(6, 3)

    plt.plot(theta, value1, label="Outer ellipse")
    plt.plot(theta, value2, label="Inner ellipse")

    plt.xlabel("Angular distance along perimeter", size=16)
    plt.ylabel("Image value", size=16)
    plt.xlim(0, 2*np.pi)
    plt.ylim(-50, 400)
    plt.legend()
    plt.tight_layout()

    plt.savefig('encoding-demo.png', bbox_inches='tight')

    # plot the rotated data
    fig2, ax2 = plt.subplots(1)
    fig2.set_size_inches(6, 3)
    plt.plot(theta, newvalue1, label="Outer ellipse")
    plt.plot(theta, newvalue2, label="Inner ellipse")

    # plot the 12 segments
    segments = np.linspace(0, 2*np.pi, 13)
    plt.vlines(segments, -50, 300, colors='gray')

    plt.xlabel("Angular distance along perimeter", size=16)
    plt.ylabel("Image value", size=16)
    plt.xlim(0, 2*np.pi)
    plt.ylim(-50, 400)
    plt.legend()
    plt.tight_layout()

    plt.savefig('encoding-demo-rotated.png', bbox_inches='tight')
    plt.show()
