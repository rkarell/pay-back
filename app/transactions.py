class Transactions(object):

    def __init__(self):
        self.all = []

    def load(self, input):
        lines = input.strip().splitlines()
        for line in lines:
            parts = line.split(";", 3)
            if len(parts) < 3:
                return "There is an syntax error on line: " + line
            elif not parts[0] or not parts[1] or not parts[2]:
                return "A part missing on line: " + line
            parts[1] = parts[1].replace(",", ".")
            try:
                parts[1] = float(parts[1])
            except:
                return "Amount is not a number on line: " + line
            participants = parts[2].split(",")
            self.all.append(Transaction(parts[0], parts[1], participants))

class Transaction(object):
    
    def __init__(self, buyer, amount, participants):
        self.buyer = buyer;
        self.amount = amount;
        self.participants = participants;
        self.share = self.amount / (len(self.participants) + 1)