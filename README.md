# A computational introduction to stochastic differential equations

<img src="./assets/fpk.gif" alt="SDE density evolution in time" width="400"/>
<img src="./assets/filtering-smoothing.gif" alt="Stochasti filtering and smoothing" width="400"/>

This course aims to develop a computational view of stochastic differential equations (SDEs) for students that have an applied or engineering background, e.g., machine learning, signal processing, electrical engineering, control, and statistics.

# Prerequisites

1. Linear algebras
2. Real analysis (not essential)
3. Probability theory
4. Ordinary differential equations

# How to register

The registration is now closed. If you still would like to enroll the course, please send an email to the course responsible.

# Lecture notes

The lectures are given on chalkboard (numerical experiments are given in Jupyter Notebook). Hence it is recommended that the students take the note during the class, although the course responsible will upload the lecture note (possibly hand-written) to this repository.

# Essential lectures (6 credits)

1. **Introduction to the course**. <br>
    17 Oct, 2022. Room 4005 Ångström. (Swedish) 13:15 - 15:00.

2. **Stochastic differential/integral equations**. <br>
    21 Oct, 2022. Room 101132 Ångström. (Swedish) 13:15 - 15:00.

3. **Numerical solution to stochastic differential equation**. <br>
    24 Oct, 2022. Room 101127 Ångström. (Swedish) 13:15 - 15:00.

4. **Statistical properties of SDE solutions**. <br>
    28 Oct, 2022. Room 101142 Ångström. (Swedish) 13:15 - 15:00.

5. **Linear SDEs and Gaussian processes**. <br>
    31 Oct, 2022. Room 101146 Ångström. (Swedish) 13:15 - 15:00.

-  **Exercise 1**. <br>
    2 Nov, 2022. Room 101127 Ångström. (Swedish) 13:15 - 15:00. <br>
    In this exercise session, the students should deliver answers to the assignments that are associated with Lectures 2 - 3.

6. **Filtering and smoothing problems I (i.e., regression with SDE prior)**. <br>
    4 Nov, 2022. Room 101127 Ångström. (Swedish) 13:15 - 15:00.

7. **Filtering and smoothing problems II (i.e., regression with SDE prior)**. <br>
    7 Nov, 2022. Room 101150 Ångström. (Swedish) 13:15 - 15:00.

-  **Exercise 2**. <br>
    9 Nov, 2022. Room 101150 Ångström. (Swedish) 13:15 - 15:00. <br>
    In this exercise session, the students should deliver answers to the assignments that are associated with Lectures 4 - 5.

8. **SDE system identification**. <br>
    11 Nov, 2022. Room 101142 Ångström. (Swedish) 13:15 - 15:00. <br>
    This lecture presents estimation methods for SDEs. These are typically based on discrete-time measurements, and therefore the tranformation of the original model into a discrete-time model is important. The focus is on the linear time-invariant case. We will breifly discuss sampling of continuous-time models, the main challenges of estimating continuous-time models, and discribe some of the available basic estimation approaches. The approaches can be divided into direct approaches and indirect approaches. Among the direct approaches is the maximum likelihood method, which is based on exact discretization of the model and a discrete-time Kalman filter.<br>
    Lecturer: [Mohamed Abdalmoaty](https://user.it.uu.se/~mohab408/)

-  **Exercise 3**. <br>
    18 Nov, 2022. Room 101127 Ångström. (Swedish) 13:15 - 15:00. <br>
    In this exercise session, the students should deliver answers to the assignments that are associated with Lectures 6 - 8.

-  **Student project work presentation**. <br>
    16 Dec, 2022. Room 101142 Ångström.

Time is (Swedish) 13:15 - 15:00 for all the lectures (45 mins + 45 mins + 10 mins break).

# Seminar lectures (9 credits)

By attending (not necessarily all) the seminar courses and complete their writing assigments/exericses, you get upgrade to 9 credits.

1. **Continuous-time filtering**. <br>
    This lecture is concerned with continuous-time filtering, for example, Zakai equation, Kushner equation, and projection filtering. <br>
    Date: 13:15 - ?, 17 Nov, 2022. Zoom <br>
    Lecturer: [Muhammad Fuady Emzir](https://scholar.google.com/citations?user=nfBRAHAAAAAJ&hl=en) (KFUPM)

2. **SDEs and Markov chain Monte Carlo**. <br>
    In this lecture, we present a general recipe for constructing Markov chain Monte Carlo (MCMC) samplers, including stochastic gradient (SG) versions, from stochastic continuous dynamics (SDEs). We also explore the connections between SG-MCMC and stochastic optimization methods via simple annealing techniques. Recommended readings: 1) A Complete Recipe for Stochastic Gradient MCMC. 2) Bridging the gap between stochastic gradient MCMC and stochastic optimization. <br>
    Date: 09:15 - 11:00, 22 Nov, 2022. Room 4101 Ångström <br>
    Lecturer: [Cagatay Yildiz](https://cagatayyildiz.github.io/) (University of Tübingen)

3. **Probabilistic numerics for ordinary differential equations**. <br>
    Probabilistic numerical methods aim to explicitly represent the numerical uncertainty that results from limited computational resources. In this lecture, we present a class of probabilistic numerical solvers for ODEs which pose the numerical solution of an ODE as a Gauss--Markov regression problem. The resulting methods, called "ODE filters", efficiently compute posterior distributions over ODE solutions with methods from Bayesian filtering and smoothing. <br>
    Date: 13:15 - 15:00, 22 Nov, 2022. Room 2001 Ångström <br>
    Lecturer: [Nathanael Bosch](https://nathanaelbosch.github.io/) (University of Tübingen)

4. **Applications of SDEs in statistical signal processing**. <br>
    In this lecture we present a few applications that use SDEs to solve signal processing problems. These include, for example, using SDEs to construct non-stationary processes to model complicated signals, and using SDEs to estiamte the spectrogram of signals with uncertainty. <br>
    Date: 28 Nov, 2022. Room 101127 Ångström (subject to change)

5. **Topic TBD**. <br>
    2 Dec, 2022. Room 101127 Ångström. <br>
    Lecturer: [Roland Hostettler](http://hostettler.co/) (Uppsala University)

6. **Constructions of Wiener processes and stochastic integrals**. <br>
    This lecture explains the constructions of Brownian motion and Ito integrals. <br>
    Date: 5 Dec, 2022. Room 101127 Ångström

Note that the dates for the seminar courses are not fixed. They are subject to change depending on the schedule of the lecturers.

# Reserved timeslots

We have also reserved 09.12.2022 and 12.12.2022 at Room 101127 Ångström, 13:15 - 15:00 (Swedish) as backup.

# Course arrangement

The course consists of lectures, exercises, and project work. Specifically, in each week, there would be one/two lectures (45 + 45 mins) and an exercise session (60 mins). The students shall present and discuss their exercise solutions during the exercise session. 

Total credit is 6 or 9.

In order to get 6 credits, you need to 

- actively participate all the essential lectures,
- pass the three exercise assignments,
- present the project work. Depending on the number of students, you may do the project work in group.

If you would like to get 9 credits, you need to fullfill the requirements for the 6 credits as stated above, and in addition, 

- actively participate all the seminar lectures,
- Select five from all the seminar lectures, then pass the exercises of the selected, or do a writing assignment if the lecture has no exercise. (We will define the writing assignment later).

The course grade is based on pass/fail.

# Project work

To be added.

# Reading materials

This course is mainly based on the following textbooks.

- Hui-Hsiung Kuo. Introduction to stochastic integration. Universitext. Springer, 2006.
- Simo Särkkä and Arno Solin. Applied stochastic differential equations. Cambridge University Press, 2019.
- Ioannis Karatzas and Steve E. Shreve. Brownian motion and stochastic calculus. Springer, 2nd edition, 1991.

# Course history

- Oct - Dec, 2022, Uppsala Universitet, FTN0332 TN22H006.

# Contact

Zheng Zhao, Uppsala University. 

firstname.lastname@it.uu.se

https://zz.zabemon.com
