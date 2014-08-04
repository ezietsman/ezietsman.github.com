---
layout: post
title: "Playing with Photogrammetry 1"
description: "A plan for a new photogrammetry coding project"
category: Science
tags: [photogrammetry, python, opencv, numpy, matplotlib, geomatics]
---
{% include JB/setup %}

* TOC
{:toc}

## Photogrammetry in a nutshell

A couple of weeks ago I met up with a friend I haven't seen in a while, and he
was telling me what he got up to during and shortly after his PhD studies.  One
of the things he did was using photographs of a radio telescope dish to measure
it's shape. With a background in Geomatics, this interested me a great deal. It
turns out he went to Ghana and carefully stuck encoded and standard
[Photomodeler](http://www.photomodeler.com) targets on the dish and used a
consumer-grade digital SLR camera to get his results, using the Photomodeler
software. The method used to perform these measurements is called
[Photogrammetry](http://en.wikipedia.org/wiki/Photogrammetry).

<!--more-->

From the Wikipedia article:

  >Photogrammetry is the science of making measurements from photographs,
  >especially for recovering the exact positions of surface points.

So basically one can take photos of an object and then later go and calculate,
from the x-y coordinates on the images, the real world 3D coordinates of
points. Sweet!!

I was trying to recall how this method and I could just remember the basics,
something about a 'Bundle adjustment'. So in order not to forget what I had
learned all those years go (10+ now O_o), I decided to do what any good
Geomatician-turned-Astronomer-turned-Coder would do. I am going to reproduce
what photomodeler does (maybe in a very simplistic way), and document the
process.

## The plan

In those days I only knew, barely, three programming languages. Turbo Pascal,
Java (1.2?) and Visual Basic 6.0. Today, many 10k lines of code later and I
don't know those three anymore. In that time I went through a few more: C, C++,
Fortan 77/90/95, javascript, coffeescript and (thank the stars!), Python. I've
been using Python for EVERYTHING for years now so any weekend coding projects
will be done in that.

So here's the steps I'm going to try and follow (actually, I've done some of
them already). Write code to:

1.  Find the encoded RAD (Ringed Automatically Detected) targets on an image.
2.  Decode the RAD targets that have been found.
3.  Find all the uncoded targets.
4.  Using the results from 1. and 2. find the camera positions and rotations.
5.  Calculate rough 3D coordinates for all targets using orientations obtained 
    from encoded targets.
6.  Find final values and error estimates for all target coordinates, camera
    positions and rotations, scale, lens distortion etc.


Sounds easy? Maybe...

We'll tackle point number one in the next post.

