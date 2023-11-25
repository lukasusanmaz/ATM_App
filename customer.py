import database as db


class Customer:
    def __init__(self, name, sur_name, identity_number, card_number, password, balance):
        self.name = name
        self.surName = sur_name
        self.identityNumber = identity_number
        self.cardNumber = card_number
        self.balance = balance
        self.password = password