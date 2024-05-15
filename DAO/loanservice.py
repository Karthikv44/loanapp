from abc import ABC, abstractmethod
from Util.dbconn import DBConnection
from Exception.loanexception import InvalidLoanException

class ILoanRepository(ABC):
    @abstractmethod
    def apply_loan(self,customer_id, principal_amount, interest_rate, loan_term_months, loan_type): 
        pass
    
    @abstractmethod
    def calculate_interest(self,loan_id):
        pass

    @abstractmethod
    def loan_status(self,loan_id):
        pass
        
    @abstractmethod
    def calculate_emi(self,loan_id):
        pass    

    @abstractmethod
    def loan_repayment(self,loan_id, amount):
        pass

    @abstractmethod
    def get_all_loan(self):
        pass
    @abstractmethod
    def get_loan_by_id(self,loan_id):
        pass


class ILoanRepositoryImpl(DBConnection ):

    def apply_loan(self,customer_id, principal_amount, loan_term_months, loan_type): 
        
        try:
            if loan_type == 1:
                interest_rate = 5.0

                self.cursor.execute(
                "INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status) VALUES (?, ?, ?, ?, ?, ?)",
                (customer_id, principal_amount, interest_rate, loan_term_months, "HomeLoan", "Pending"),
                )
                self.conn.commit()
            elif loan_type == 2:
                interest_rate = 5.0

                self.cursor.execute(
                "INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status) VALUES (?, ?, ?, ?, ?, ?)",
                (customer_id, principal_amount, interest_rate, loan_term_months, "CarLoan", "Pending"),
                )
                self.conn.commit()
                
        except Exception as e:
            print(e)

    def get_all_loan(self):

        try:
            self.cursor.execute(
                "Select * from loan",
                )
            rows = self.cursor.fetchall()  # Get all data
            for row in rows:
                print(row)
        except Exception as e:
            print(e)  

    def calculate_interest(self,loan_id):
        try:

            self.cursor.execute(
                "select principal_amount, interest_rate, loan_term_months from loan where loan_id = (?)",
                (loan_id)
                )
            
            row = self.cursor.fetchone()
            if type(row) == 'NoneType':
                raise InvalidLoanException(loan_id)
            else:
                principal_amount = row[0]  
                interest_rate = row[1]     
                loan_term_months = row[2]
                interest = (principal_amount * interest_rate * loan_term_months) / 12
            print(interest)
        except Exception as e:
            print(e) 

    def get_loan_by_id(self,loan_id):
        try:
            self.cursor.execute(
                "select * from loan where loan_id = (?)",
                (loan_id)
                )
            row = self.cursor.fetchone()
            print(row)
        except Exception as e:
            print(e)    

    def loan_status(self,loan_id):
        try:         
            self.cursor.execute(
                "select credit_score from Customer join loan on Customer.customer_id = Loan.customer_id where loan_id = (?)",
                (loan_id)
                )
            row = self.cursor.fetchone()
            if len(row[0]) == 0:
                raise InvalidLoanException(loan_id)
            else:    
                if(row[0] > 650):
                    print("Your loan has been approved")
                else:
                     print("Your loan has been rejected")
        except Exception as e:
                print(e) 
    def loan_repayment(self,loan_id, amount):
         pass
    def calculate_emi(self,loan_id):
         pass   