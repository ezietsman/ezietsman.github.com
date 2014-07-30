---
layout: post
title: "Playing with Photogrammetry 2"
description: ""
category: Science
tags: []
---
{% include JB/setup %}

As discussed in the [previous
post](/photogrammetry/science/2014/07/29/playing-with-photogrammetry-1/), our
first task is to figure out a way to find RAD targets on our images. Let's have
a look at these things then.

Here is a typical photo we will deal with.
![RAD targets on a radio dish]({{site.url}}/assets/images/photogrammetry/dish-1.jpg)

And here is a closeup of one of the RAD targets:
![Close view of a RAD and normal target]({{site.url}}/assets/images/photogrammetry/rad-closeup-1.jpg)

As you can see, there is an outer ring, with a single 'notch' and an inner
circle. Between these there is another ring, with at least one segment filled
in. These targets come in sets and the inner segments denote the encoding.
There are 12 segments in the inner ring and 11 of them can be filled or blank.
One is always filled and lines up with the notch in the outer ring. _This is
important, we'll use this later_.

You'll also note that we don't necessarily look at them perpendicularly so on
an image they appear as *rotated ellipses*. So we need to figure out a way to 
distinguish the RAD target from the normal ones. You can see the uncoded
target in the close-up image.

**WIP**
