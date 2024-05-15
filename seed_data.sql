-- Sample data for Customer table
INSERT INTO Customer (name, email_address, phone_number, address, credit_score)
VALUES ( 'John Doe', 'john@example.com', '123-456-7890', '123 Main St', 750),
    ( 'Jane Smith', 'jane@example.com', '987-654-3210', '456 Elm St', 800),
	( 'Michael Johnson', 'michael@example.com', '111-222-3333', '789 Oak St', 700),
    ( 'Emily Brown', 'emily@example.com', '444-555-6666', '101 Pine St', 780),
    ( 'David Wilson', 'david@example.com', '777-888-9999', '222 Maple St', 720),
    ( 'Sarah Johnson', 'sarah@example.com', '333-111-2222', '789 Walnut St', 740),
    ( 'Robert Davis', 'robert@example.com', '666-999-1111', '888 Cedar St', 760),
    ( 'Amanda Martinez', 'amanda@example.com', '222-444-6666', '333 Birch St', 780),
    ( 'Daniel Thompson', 'daniel@example.com', '555-777-8888', '555 Pine St', 720),
    ( 'Olivia Garcia', 'olivia@example.com', '888-222-4444', '777 Oak St', 790);


-- Sample data for Loan table
INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status)
VALUES ( 1, 200000.00, 4.5, 120, 'HomeLoan', 'Approved'),
    ( 2, 150000.00, 5.0, 60, 'HomeLoan', 'Pending'),
    ( 3, 100000.00, 6.0, 48, 'HomeLoan', 'Approved'),
    ( 4, 50000.00, 4.0, 72, 'HomeLoan', 'Pending'),
    ( 5, 30000.00, 6.5, 36, 'HomeLoan', 'Approved'),
    ( 6, 100000.00, 4.0, 60, 'CarLoan', 'Pending'),
    ( 7, 80000.00, 5.0, 48, 'CarLoan', 'Approved'),
    ( 8, 60000.00, 4.5, 36, 'CarLoan', 'Pending'),
    ( 9, 40000.00, 6.0, 60, 'CarLoan', 'Approved'),
    ( 10, 20000.00, 3.5, 48, 'CarLoan', 'Pending');

-- Sample data for HomeLoan table
INSERT INTO HomeLoan (loan_id, propertyaddress, propertyvalue)
VALUES 
    (1, '456 Elm St', 300000),
    (2, '888 Cedar St', 250000),
    (4, '101 Pine St', 200000),
    (5, '222 Maple St', 150000),
    (7, '789 Walnut St', 400000),
    (8, '333 Birch St', 350000);

-- Sample data for CarLoan table
INSERT INTO CarLoan (loan_id, CarModel, CarValue)
VALUES 
    (6, 'Toyota Camry', 25000),
    (9, 'Honda Accord', 20000),
    (10, 'Ford Mustang', 35000);
