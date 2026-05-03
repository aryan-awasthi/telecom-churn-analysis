-- Churn by Internet Type

SELECT 
internet_type,
COUNT(*) AS total_customers,
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
) AS churn_rate
FROM bronze_telecom
GROUP BY internet_type;

-- Churn by Contract

SELECT 
contract,
COUNT(*) AS total,
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) AS churned,
ROUND(
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
) AS churn_rate
FROM bronze_telecom
GROUP BY contract;

-- Churn by Payment Method

SELECT 
payment_method,
COUNT(*) AS total,
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) AS churned,
ROUND(
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
) AS churn_rate
FROM bronze_telecom
GROUP BY payment_method;

-- High vs Low Monthly Charges

SELECT 
CASE 
    WHEN monthly_charge < 50 THEN 'Low'
    WHEN monthly_charge BETWEEN 50 AND 100 THEN 'Medium'
    ELSE 'High'
END AS charge_group,

COUNT(*) AS total,
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) AS churned,
ROUND(
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
) AS churn_rate

FROM bronze_telecom
GROUP BY charge_group;