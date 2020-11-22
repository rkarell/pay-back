# PayBack
A web application to optimize the transactions when paying back debts.

## Background
When using applications that help you share bills, I started to wonder the algorithms used to optimize the problem. I thought it would be a nice brain-teaser to figure it out and so I took my shot at the case.

Originally, I created an app to just test the designed algorithms but ended up turning it into a web application for demonstration purposes. It lacks a proper user interface, which reflects my current interests: back end.

## Algorithms
The algorithms used to optimize the debts are presented in the picture below.
![Algorithms](media/algorithms.png)

## Relevant data structures
##### Transaction
Represents one transaction containing attributes for the buyer, the participants, the total amount and the share for each participant (buyer automatically participates in the purchase and the share is always the same for each participant)

##### Transactions
A list of **transaction** objects containing methods for reading and validating input

##### Debt
Represents a debt between two participants, containing attributes for the two participants and the amount of debt.

##### Debts
A list of **debt** objects containing the algorithms for optimizing the actual problem and a number of helper functions for working with **debt** objects.

Participants are stored as simple strings in the attributes of **debt** and **transaction** objects

## Program operation principle
The UI is simple and used only to input transactions as text on separate rows (sent to the server with POST request). First, the transactions are parsed and validated. Based on the transactions, debts between each two people are calculated. Then above-mentioned algorithms are applied. They reduce the amount of debts in a way that each participant still has to pay the same amount. In the end, the resulting debts are returned to the client.

## Framework
Django

## Additional notes
Time complexity of the algorithms is poor in terms of the number of participants. However, in the context of this kind of software it should not be a problem.

The data related to debts is basically a directed graph. A library for graphs could have been used to implement it.