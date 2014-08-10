---
layout: post
title: "Finding targets"
description: "I explain an algorithm I developed to find two types of Photomodeler targets on images of a radio telescope's dish."
category: photogrammetry
tags: [photogrammetry, target detection, numpy, scipy, kdtree]
---
{% include JB/setup %}
* TOC
{:toc}


## The story so far...

In the previous post I discussed how it is possible to find areas of interest
on images like I got from my friend. I showed how one can use an **adaptive
threshold** technique to transform your image into one that only has image
values of 0 or 255. Here's our before and after images:

![/assets/images/photogrammetry/original-threshold.png](/assets/images/photogrammetry/original-threshold.png)

Let's see a closeup of a target on the threshold image again (from the last post):

![/assets/images/photogrammetry/threshold.png](/assets/images/photogrammetry/thresh.png)

The next thing I needed to do was to find the regions where the targets are
located. The threshold image is perfect for this because it only has regions
that is one of two values.

## Contours!

The reason the threshold image is great is because if I calculate contours of
the image values, the contours will fall exactly on the boundaries between the
light and dark parts of the targets. This way I get to leverage a powerful
algorithm that will give me a much smaller amount of data to work with as well
as polygons which are situated near the regions I'm interested in.

From wikipedia:

>   "More generally, a contour line for a function of two variables is a curve
>   connecting points where the function has the same particular value."

`opencv` has a function that can calculate the contours for me. I used it in
the following way:

{% highlight python %}
def get_contours(self):
    ''' Get contours in given image'''
    threshold = copy.deepcopy(self.threshold)
    contours, hierarchy = \
        cv2.findContours(threshold,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE)
    # filter out short ones
    contours = [cnt for cnt in contours if len(cnt) > 10]
    return contours
{% endhighlight %}

The line containing `copy.deepcopy` is to avoid my threshold image being
destroyed by the contouring function. That line makes a completely separate copy
of the threshold, which I don't mind being mangled by another function.

The last bit is a python list comprehension that filters out contours that is
shorter than 10 vertices.

Plotting the contours over the original image gives us something like this:

<figure>
<img src="/assets/images/photogrammetry/contours.png" alt="Contours plotted over
the original image">
<figcaption>The contours (red)  plotted over the original image.</figcaption>
</figure>


The contour function returns a list of contours and these in turn are basically
lists of the coordinates of the contours' vertices. So I know I wanted the
positions of the targets (this is what I'm trying to do, afterall), so there is
a few ways I can do this:

* calculate the centre of mass of the contour vertices
* fit an ellipse to the contour coordinates and use its centre

I rejected the first option immediately because many of the contours are asymmetric. 
I really want the centre of ellipses and the contours are just rough
estimations of where I may find an elliptical target.

The second option *works* but it is not ideal. For the contours that are
located on the outer edge of a RAD target, there is a concave part where the
notch is. If I blindly fit an ellipse to these contours, that concave part will
skew the ellipse's centre along a line from the notch through the centre. The
ellipse's values will also be affected. In the image below I illustrate this problem.

<figure>
  <img src="/assets/images/photogrammetry/ellipse-fits.png" alt="Image showing data along two ellipses and the best fitting ellipse fitted to each.">
  <figcaption>Red: Ellipse fitted to convex data points. Green: ellipse fitted to data points with concave 'notch'.</figcaption>
</figure>

In the plot[^ellipse-fitting-script], the red markers show data points where
the edge of an ellipse falls. In the case of the red markers, all the points
fall on the edge of some ellipse (I know this because I made up the numbers).
In the case of the green points, I changed two of them to fall on the edge of a
smaller ellipse that is otherwise the same as the one we have here. This
simulates the *zero-notch* we get on the outer edge of the RAD targets.

I calculated the best-fitting ellipse for each dataset and I plotted those
ellipses over the data points. The ellipse fitted to the convex points (no
 notch) is a solid (red) line and the ellipse fitted to the points
containing the notch is a dashed (green) line. I also plotted the centres of
both ellipses. As you can clearly see, the two ellipses are not the same and
the two centres are also slightly offset.

The way I got around this was to find a way to 'get rid' of the notch. What I
needed was a polygon that would fit around the contour (notch and all) but 
*bridge* that gap where the notch is. Sound familiar? Again, luckily, this 
is a solved problem. Enter the [convex hull](http://en.wikipedia.org/wiki/Convex_hull).

From Wikipedia

>In mathematics, the convex hull or convex envelope of a set X of points in the Euclidean plane or Euclidean space is the smallest convex set that contains X.  For instance, when X is a bounded subset of the plane, the convex hull may be visualized as the shape formed by a rubber band stretched around X.

A rubber band stretched around X eh?  Now the cool thing is, the convex hull
calculation will not *add* any new data points to my ellipse contours. It will
give me straight lines between points that are already on my ellipses, should
it encounter a *notch* or concave segment. This way, if I fit an ellipse to the
convex hull points, the notchy parts do not affect my fits so much and hence I
get very good coordinates for the centers of the ellipses.

So, armed with this knowledge, I set out to calculate, for each contour I got
from the threshold, the convex hull and it is to this that I fitted ellipses.


## Ellipses: I have too many


[^ellipse-fitting-script]: [Python script for ellipse plot](/assets/scripts/ellipse-fitting-demo.py)

