class Debts(object):
    def __init__(self):
        self.all = []

    def addTransactions(self, transactions):
        for transaction in transactions.all:
            for participant in transaction.participants:
                self.addDebt(participant, transaction.buyer, transaction.share)

    def addDebt(self, debtFrom, debtTo, amount):
        newDebt = Debt(debtFrom, debtTo, amount)
        debt = self.getDebt(debtFrom, debtTo)
        if debt is None:
            self.all.append(newDebt)
        else:
            debt.merge(newDebt)
            if debt.amount == 0:
                self.all.remove(debt)

    def getDebt(self, debtFrom, debtTo):
        for debt in self.all:
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
                self.all.remove(debt)
            else:
                debt.debtFrom = debtFrom
                debt.debtTo = debtTo
                debt.amount = amount

    def getDebtsFromParticipant(self, participant):
        debts = []
        for debt in self.all:
            if debt.debtFrom == participant:
                debts.append(debt)
        return debts

    def reduce(self):
        reduced = True
        while reduced == True:
            reduced = False
            for debt in self.all:
                sequentialDebts = self.getDebtsFromParticipant(debt.debtTo)
                if len(sequentialDebts) > 0:
                    debt2 = sequentialDebts[0]
                    difference = abs(debt.amount - debt2.amount)
                    if debt.amount < debt2.amount:
                        self.addDebt(debt.debtFrom, debt2.debtTo, debt.amount)
                        self.setDebt(debt2.debtFrom, debt2.debtTo, difference)
                        self.all.remove(debt)
                    else:
                        self.addDebt(debt.debtFrom, debt2.debtTo, debt2.amount)
                        self.setDebt(debt.debtFrom, debt.debtTo, difference)
                        self.all.remove(debt2)
                    reduced = True
                    break

    def __str__(self):
        return '\n'.join(map(str, self.all))

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

