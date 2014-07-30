---
layout: post
title: "Playing with Photogrammetry 1"
description: "how I relearned how to measure things off photographs"
category: 
tags: [photogrammetry, python, opencv, numpy, matplotlib, geomatics]
---
{% include JB/setup %}

## Photogrammetry 101

[Photogrammetry](http://en.wikipedia.org/wiki/Photogrammetry) is the art and
science of making measurements of things in the real world, from photographs.

{% highlight python %}
def find_rad_targets(ellipses):
    '''
    Given a list of ellipses, return a list of rad-targets, specified by their
    inner ellipse and outer ellipse i.e.

    [
        [small_ellipse, big_ellipse]
        .
        .
        .
    ]
    '''
    rad_targets = []

    # photomodeler rad targets have as specific small/large circle ratio
    # for each ellipse, find the closest in position which is smaller in both
    # axes and has a similar angle

    ellipse_pairs = itertools.combinations(ellipses, 2)

    for ellipse1, ellipse2 in ellipse_pairs:
        # now check if they are in fact 'concentric'
        if ellipse1.isCloseTo(ellipse2):
            if ellipse1.isSmallerThan(ellipse2):
                if 3.5 < (ellipse2.Ma / ellipse1.Ma) < 5:
                    rad_targets.append((ellipse1, ellipse2))
            else:
                if 3.5 < (ellipse1.Ma / ellipse2.Ma) < 5:
                    rad_targets.append((ellipse2, ellipse1))
    return rad_targets
{% endhighlight %}

This below here should be a maths block.

$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$
