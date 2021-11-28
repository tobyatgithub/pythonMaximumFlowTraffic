# pythonMaximumFlowTraffic

An attempt to solve/improve traffic jam by using network algorithm (Ford-Fulkerson).

## Table of Contents

## Introduction

In thie repo, we try to model traffic optimization as a "network flow" problem, and solve it using an algorithm called the Ford-Fulkerson Algorithm[1].

## Approach

![add image](https://github.com/tobyatgithub/pythonMaximumFlowTraffic/blob/main/img/whiteBoard11272021.jpg?raw=true)
figure 1 - white board from 1st brain-storm.

**This project will unfold in three phases:**

1 - We start simple and use Ford-Fulkerson to solve the single-source single-sink max flow problem (with augment path algorithm).

2 - Then we genealize the single-source and single-sink scenario to the multi-source multi-shink scenario. We will see that even with this additional complexity, we can easily reduce it to our first single-single scenario (by introducing a dummy source node that is connected to the original source nodes with inifinite capacity links; and similiary introducing a dummy sink node that is connected with the original sink nodes with infinite capacity links [2]).

3 - we assign this multi-source multi-sink scenario with a context. For example, we can frame as a morning rush hour traffic optimization wtih following assumptions:

- We will have **multiple sources** in the morning rush hour such as population dense communities.
- We will have **multiple sinks** in the morning rush hour such as campus, malls, and office buildings.
- Our main target is car-traffic optimization, thus our model will be based on cars, and are only interested in highways, roads, bridges. We won't consider subways, skytrains, rapid buses in our model.
- We will model the capacity of each edge using a function based on "length of the road", "number of lines", and a "traffic-light-coefficient". See more in part TODOTODO.
- We will assume each source has unlimited supply (we later can see there is an easy way to regulate that) to simulate the worst case and explore the bottleneck of the graph. And we will make the same assumption for each sink.
- The overall goal of this traffic optimization is to provide a tooling for comparing different graph designs (which stands for different road/bridge design for traffic.)

## Reference and Resources

[1] [Textbook about Flow Problems](https://www-sop.inria.fr/members/Frederic.Havet/Cours/flow.pdf)

[2] [Lecture 20, Max Flow and Augment Path Algorithm](http://www.ifp.illinois.edu/~angelia/ge330fall09_maxflowl20.pdf)
