class Debts(object):
    def __init__(self):
        self.debts = []
        self.participants = []

    def addTransactions(self, transactions):
        for transaction in transactions.all:
            self.addParticipant(transaction.buyer)
            for participant in transaction.participants:
                self.addParticipant(participant)
                self.addDebt(participant, transaction.buyer, transaction.share)

    def addDebt(self, debtFrom, debtTo, amount):
        newDebt = Debt(debtFrom, debtTo, amount)
        debt = self.getDebt(debtFrom, debtTo)
        if debt is None:
            self.debts.append(newDebt)
        else:
            debt.merge(newDebt)
            if debt.amount == 0:
                self.debts.remove(debt)

    def getDebt(self, debtFrom, debtTo):
        for debt in self.debts:
            if ((debt.debtFrom == debtFrom) and (debt.debtTo == debtTo)) or ((debt.debtFrom == debtTo) and (debt.debtTo == debtFrom)):
                return debt
        return None

    def setDebt(self, debtFrom, debtTo, amount):
        debt = self.getDebt(debtFrom, debtTo)
        if debt is None:
            if amount > 0:
                self.addDebt(debtFrom, debtTo, amount)
        else:
            if amount == 0:
                self.debts.remove(debt)
            else:
                debt.debtFrom = debtFrom
                debt.debtTo = debtTo
                debt.amount = amount

    def getDebtsFromParticipant(self, participant):
        debts = []
        for debt in self.debts:
            if debt.debtFrom == participant:
                debts.append(debt)
        return debts

    def addParticipant(self, participant):
        if not participant in self.participants:
            self.participants.append(participant)

    def optimizeAlgorithm1(self):
        reduced = True
        while reduced:
            reduced = False
            for debt in self.debts:
                sequentialDebts = self.getDebtsFromParticipant(debt.debtTo)
                if len(sequentialDebts) > 0:
                    debt2 = sequentialDebts[0]
                    difference = abs(debt.amount - debt2.amount)
                    if debt.amount < debt2.amount:
                        self.addDebt(debt.debtFrom, debt2.debtTo, debt.amount)
                        self.setDebt(debt2.debtFrom, debt2.debtTo, difference)
                        self.debts.remove(debt)
                    else:
                        self.addDebt(debt.debtFrom, debt2.debtTo, debt2.amount)
                        self.setDebt(debt.debtFrom, debt.debtTo, difference)
                        self.debts.remove(debt2)
                    reduced = True
                    break

    def optimizeAlgorithm2(self):
        reduced = True
        while reduced:
            reduced = False
            debtorPairs = self.getPairs(self.participants)
            for debtorPair in debtorPairs:
                debts1 = self.getDebtsFromParticipant(debtorPair[0])
                debts2 = self.getDebtsFromParticipant(debtorPair[1])
                creditorPair = self.getMatchingCreditorPair(debts1, debts2)
                if creditorPair:
                    debts = []
                    for debtor in debtorPair:
                        for creditor in creditorPair:
                            debts.append(self.getDebt(debtor, creditor))
                    smallestDebt = sorted(debts, key=lambda x: x.amount)[0]
                    d1 = smallestDebt.debtFrom                  #d1, d2, c1, c2 are the same as in planning image
                    d2 = debtorPair[not debtorPair.index(d1)]   #'not' here gives the other index (0->1 or 1->0)
                    c1 = smallestDebt.debtTo
                    c2 = creditorPair[not creditorPair.index(c1)]
                    self.addDebt(d1, c2, smallestDebt.amount)
                    self.addDebt(d2, c1, smallestDebt.amount)
                    self.addDebt(d2, c2, -smallestDebt.amount)
                    self.debts.remove(smallestDebt)
                    reduced = True
                    break

    def getMatchingCreditorPair(self, debts1, debts2):
        creditorPairs1 = self.getPairs(self.getCreditors(debts1))
        creditorPairs2 = self.getPairs(self.getCreditors(debts2))
        for cp in creditorPairs1:
            if cp in creditorPairs2:
                return(cp)
        return(None)

    def getCreditors(self, debts):
        creditors = []
        for debt in debts:
            creditors.append(debt.debtTo)
        return(creditors)

    def getPairs(self, list):
        pairs = []
        if len(list) < 2:
            return []

        for i in range(len(list)-1):
            for j in range(i+1,len(list)):
                pairs.append([list[i],list[j]])

        return(pairs)

    def __str__(self):
        return '\n'.join(map(str, self.debts))

class Debt():
    def __init__(self, debtFrom, debtTo, amount):
        self.debtFrom = debtFrom
        self.debtTo = debtTo
        self.amount = amount

    def __str__(self):
        return "From " + self.debtFrom + " to " + self.debtTo + ": " + str(round(self.amount,2))

    def merge(self, otherDebt):
        if (self.debtFrom == otherDebt.debtFrom) and (self.debtTo == otherDebt.debtTo):     # Merge is always called with the same two people but the direction of the debt is solved here
            self.amount += otherDebt.amount
        else:
            self.amount -= otherDebt.amount
            if self.amount < 0:
                self.swap()

    def swap(self):
        temp = self.debtFrom
        self.debtFrom = self.debtTo
        self.debtTo = temp
        self.amount *= -1

