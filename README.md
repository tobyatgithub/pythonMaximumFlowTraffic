# python Maximum Flow Traffic

## Introduction

> Introduction = what we want to do

Driving is such a meaningful and pleasant event. However, driving in cities is usually a nightmare. A bad traffic situation could cause many unfortunate problems. For example, it overall brings down the happiness of the residents, causing more anxieties and depressions; it undermines potential economic development due to unrealized mobility; it worsens pollution and wastes precious energy.

It doesn't have to be that way. We must be able to do better.

This project attempts to solve/improve traffic jams by using a network algorithm (Ford-Fulkerson). In short, we model the city road infrastructure as a graph and use Ford-Fulkerson to find the bottleneck of the current traffic design. This bottleneck information can guide people on how to improve the traffic. And lastly, we could use the same algorithm to evaluate a given improvement plan.

More specifically, our methodology here is to model traffic optimization as a "network flow" problem and solve it using an algorithm called the Ford-Fulkerson Algorithm[1]. By "solve it" we mean providing a deterministic solution for problems such that "given a fixed amount of resource, which design of roads will maximize the total amount of traffic per unit time."

Group members:

## Table of Contents

- [Introduction](#introduction)
- [Approach](#approach)
- [Application and Scope](#Application-and-scope)
- [Reference and Resources](#reference-and-resources)

## Approach

> approach = how we gonna create the solution

![add image](https://github.com/tobyatgithub/pythonMaximumFlowTraffic/blob/main/img/whiteBoard11272021.jpg?raw=true)
figure 1 - white board from 1st brain-storm.

**This project will unfold in three phases:**

1 - We start simple and use Ford-Fulkerson to solve the single-source single-sink max flow problem (with an augmenting path algorithm).

2 - Then, we generalize the single-source and single-sink scenario to the multi-source multi-shink scenario. We will see that even with this additional complexity, we can easily reduce it to our first single-single scenario. To do so, we could introduce a dummy source node that is connected to all the source nodes with infinite capacity links. And similarly introducing a dummy sink node that connects with the original sink nodes with infinite capacity links [2]).

3 - We assign this multi-source multi-sink scenario with a context. For example, we can frame it as a morning-rush-hour traffic optimization with the following assumptions:

- We will have **multiple sources** in the morning rush hour, such as population-dense communities.
- We will have **multiple sinks** in the morning rush hour, such as campus, malls, and office buildings.
- Our target is car-traffic optimization. Thus our model will be based on cars and are only interested in highways, roads, bridges. We won't consider the effect of public transportations such as subways, sky trains, and rapid buses in our current model.
- We will model the maximum capacity of each edge using a function based on "length of the road", "number of lines", and a "traffic-light-coefficient". See more in part TODOTODO.
- We will assume each source has an unlimited supply to simulate the worst-case and explore the bottleneck of the graph. And we will make the same assumption for each sink.
- We later can see there exists an easy way to regulate the unlimited supply from sources and demand from sinks.
- The overall goal of this traffic optimization is to provide tooling for comparing different graph designs (which stands for different road/bridge designs for traffic.)

## Application and Scope

> Application and Scope = how to apply our solution

## Reference and Resources

> Reference = something we find useful

[1] [Textbook about Flow Problems](https://www-sop.inria.fr/members/Frederic.Havet/Cours/flow.pdf)

[2] [Lecture 20, Max Flow and Augment Path Algorithm](http://www.ifp.illinois.edu/~angelia/ge330fall09_maxflowl20.pdf)
