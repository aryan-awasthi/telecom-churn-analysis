-- KPI Analysis: Churn Rate

SELECT 
COUNT(*) AS total_customers,
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) AS churned_customers,
ROUND(
SUM(CASE WHEN customer_status = 'Churned' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2
) AS churn_rate
FROM bronze_telecom;
