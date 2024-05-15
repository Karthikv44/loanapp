CREATE DATABASE Loanapp;

Use Loanapp;



-- Customer table
CREATE TABLE Customer (
    customer_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255) ,
    email_address VARCHAR(255),
    phone_number VARCHAR(20),
    address VARCHAR(255),
    credit_score INT
);

-- Loan table
CREATE TABLE Loan (
    loan_id INT PRIMARY KEY IDENTITY(1,1),
    customer_id INT FOREIGN KEY REFERENCES Customer(customer_id),
    principal_amount DECIMAL(18, 2) ,
    interest_rate DECIMAL(5, 2) ,
    loan_term_months INT ,
    loan_type VARCHAR(50) ,
    loan_status VARCHAR(50) 
);

-- HomeLoan table 
CREATE TABLE HomeLoan (
    loan_id INT PRIMARY KEY,
    propertyaddress VARCHAR(255),
    propertyvalue INT,
    FOREIGN KEY (loan_id) REFERENCES Loan(loan_id)
);

-- CarLoan table 
CREATE TABLE CarLoan (
    loan_id INT PRIMARY KEY,
    carmodel VARCHAR(255),
    carvalue INT,
    FOREIGN KEY (loan_id) REFERENCES Loan(loan_id)
);