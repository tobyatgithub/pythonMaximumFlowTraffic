# pythonMaximumFlowTraffic

An attempt to solve/improve traffic jam by using network algorithm (Ford-Fulkerson).

## Table of Contents

## Introduction

In thie repo, we try to model traffic optimization as a "network flow" problem, and solve it using an algorithm called the Ford-Fulkerson Algorithm[1].

## Approach

![add image](https://)

This project will unfold in three phases:

1 - We start simple and use Ford-Fulkerson to solve the single-source single-sink max flow problem (with augment path algorithm).

2 - Then we genealize the single-source and single-sink scenario to the multi-source multi-shink scenario. We will see that even with this additional complexity, we can easily reduce it to our first single-single scenario (by introducing a dummy source node that is connected to the original source nodes with inifinite capacity links; and similiary introducing a dummy sink node that is connected with the original sink nodes with infinite capacity links [2]).

## Reference and Resources

[1] [Textbook about Flow Problems](https://www-sop.inria.fr/members/Frederic.Havet/Cours/flow.pdf)

[2] [Lecture 20, Max Flow and Augment Path Algorithm](http://www.ifp.illinois.edu/~angelia/ge330fall09_maxflowl20.pdf)
