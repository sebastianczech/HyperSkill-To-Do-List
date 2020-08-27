class PiggyBank:

    def __init__(self, deposit_dollars, deposit_cents):
        self.dollars = deposit_dollars + int(deposit_cents / 100)
        self.cents = deposit_cents % 100

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        self.dollars += int(self.cents / 100)
        self.cents = self.cents % 100
