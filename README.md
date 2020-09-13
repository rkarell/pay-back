# PayBack
A web application to optimize the transactions when paying back debts, like WeShare.

Consider a case where a group of people has purchased multiple things. Different people buy different things and the amount of participants of each purchase vary. When the time comes to even out the debts, how should the transactions be done to minimize them?

## Algorithms
The used algorithms are presented in the picture below.
![Algorithms](media/algorithms.png)

## Framework
Django

## Additional notes
The user interface was created with minimum effort. The original purpose was just to see if the designed algorithms work.

Time complexity of the algorithms is poor in terms of the number of participants. However, in the context of this kind of software it should not be a problem.

The data related to debts is basically a directed graph. A library for graphs could have been used to implement it.