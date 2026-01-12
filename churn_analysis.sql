USE churn_analysis;

SELECT 
  COUNT(*) AS total_customers,
  SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
  ROUND(
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
    2
  ) AS churn_rate
FROM cleaned_churn_dataset;

SELECT 
    Contract,
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM cleaned_churn_dataset
GROUP BY Contract
ORDER BY churn_rate DESC;


SELECT 
    tenure_group,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM cleaned_churn_dataset
GROUP BY tenure_group
ORDER BY churn_rate DESC;

SELECT 
    PaymentMethod,
    COUNT(*) AS total_customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS churn_rate
FROM cleaned_churn_dataset
GROUP BY PaymentMethod
ORDER BY churn_rate DESC;

SELECT 
    Contract,
    tenure_group,
    charge_bucket,
    COUNT(*) AS churned_customers
FROM cleaned_churn_dataset
WHERE Churn = 'Yes'
GROUP BY Contract, tenure_group, charge_bucket
ORDER BY churned_customers DESC;

