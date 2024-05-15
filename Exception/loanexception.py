class InvalidLoanException(Exception):
    def __init__(self,loan_id):
        super().__init__(f"Loan with {loan_id} id not found")