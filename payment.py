class Payment:
    def __init__(self, payment_id, amount, payer):
        self.payment_id = payment_id
        self.amount = amount
        self.payer = payer

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "amount": self.amount,
            "payer": self.payer
        }
