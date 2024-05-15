from DAO import ILoanRepositoryImpl
from Entity import CarLoan, Customer, HomeLoan, Loan

def main():
    menu = ILoanRepositoryImpl()

    while True:
        print(
            """
                1.Apply Loan
                2.Display all loan
                3.calculate interest
                4.Get loan details
                5.Get loan status
                6.Exit
              """
        )
        choice = int(input("Enter the choice: "))
        if choice == 1:
            customer_id = int(input("Enter customer id: "))
            principal_amount = int(input("Enter principal_amount "))
            loan_term_months = int(input("Enter loan_term_months "))
            loan_type = int(
                input("Enter loan_type(1 for home loan / 2 for car loan): ")
            )
            menu.apply_loan(customer_id, principal_amount, loan_term_months, loan_type)
        elif choice == 2:
            menu.get_all_loan()
        elif choice == 3:
            loan_id = int(input("Enter the loan id: "))
            menu.calculate_interest(loan_id)
        elif choice == 4:
            loan_id = int(input("Enter the loan id: "))
            menu.get_loan_by_id(loan_id)
        elif choice == 5:
            loan_id = int(input("Enter the loan id: "))
            menu.loan_status(loan_id )
        elif choice == 6:
            menu.close()
            break


if __name__ == "__main__":

    print("Welcome to the loan app")
    main()

    