CREATE TABLE claims (
    claim_id INT PRIMARY KEY,
    member_id INT,
    provider_id INT,
    claim_date DATE,
    amount DECIMAL(10,2),
    updated_at DATETIME
);
