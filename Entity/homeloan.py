from Entity import Loan

class HomeLoan(Loan):
    def __init__(self, loan_id, property_address, property_value):
        self.loan_id = loan_id
        self.property_address = property_address
        self.property_value = property_value