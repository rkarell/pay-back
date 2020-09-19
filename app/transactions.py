class Transactions(object):

    def __init__(self):
        self.transactions = []

    def load(self, input):
        lines = input.strip().splitlines()
        for line in lines:
            if not line:        #skip empty lines
                continue
            transactionArray, errorText = self.validateTransaction(line)
            if errorText:
                return errorText
            else:
                self.transactions.append(Transaction(transactionArray[0], transactionArray[1], transactionArray[2]))

    def validateTransaction(self, line):
        parts = line.split(";")
        if len(parts) != 3:
            return None, "There is a syntax error on line: " + line
        elif not parts[0] or not parts[1] or not parts[2]:
            return None, "A part missing on line: " + line
        parts[0] = parts[0].strip()
        parts[1] = parts[1].replace(",", ".")
        try:
            parts[1] = float(parts[1])
        except:
            return None, "Amount is not a number on line: " + line
        participants = parts[2].split(",")
        for i in range(len(participants)):
            participants[i] = participants[i].strip()
        if parts[0] in participants:
            return None, "Buyer can't be one of the participants: " + line
        if "" in participants or not parts[0]:
            return None, "Buyer/participant can't be empty: " + line
        return [parts[0], parts[1], participants], None

class Transaction(object):
    
    def __init__(self, buyer, amount, participants):
        self.buyer = buyer;
        self.amount = amount;
        self.participants = participants;
        self.share = self.amount / (len(self.participants) + 1)