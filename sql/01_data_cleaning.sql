
ALTER TABLE bronze_telecom
CHANGE `Customer ID`customer_id VARCHAR(50),
CHANGE `Total Revenue` total_revenue FLOAT;
SELECT COUNT(customer_id) FROM bronze_telecom;
ALTER TABLE bronze_telecom
CHANGE `Total Charges`total_charges FLOAT,
CHANGE `Monthly Charge`monthly_charge FLOAT,
CHANGE `Customer Status`customer_status VARCHAR(20),
CHANGE `Churn Category` churn_category VARCHAR(50),
CHANGE `Churn Reason`churn_reason VARCHAR(100);
ALTER TABLE bronze_telecom
CHANGE `Gender`gender VARCHAR(10);

ALTER TABLE bronze_telecom
CHANGE `Age`age VARCHAR(10),
CHANGE `Married`married VARCHAR(10),
CHANGE `Number of Dependents`dependents VARCHAR(50),
CHANGE `Phone Service`phone_service VARCHAR(40),
CHANGE `Internet Service`internet_service VARCHAR(50),
CHANGE `Internet Type`internet_type VARCHAR(50),
CHANGE `Contract`contract VARCHAR(50),
CHANGE `Payment Method`payment_method VARCHAR(50);
ALTER TABLE bronze_telecom
MODIFY age INT,
MODIFY dependents INT;
