from Entity import Loan

class CarLoan(Loan):
    def __init__(self, loan_id, car_model, car_value):
        self.loan_id = loan_id
        self.car_model = car_model
        self.car_value = car_value