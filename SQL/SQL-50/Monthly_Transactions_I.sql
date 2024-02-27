-- Problem : https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT TO_CHAR(trans_date, 'YYYY-MM') as month, 
    country, count(*) as trans_count, 
    SUM(
        CASE
            WHEN state = 'approved' THEN 1
            ELSE 0
        END
    ) as approved_count,
    SUM(amount) as trans_total_amount,
    SUM(
        CASE
            WHEN state = 'approved' THEN amount
            ELSE 0
        END
    ) as approved_total_amount
FROM Transactions
GROUP BY month, country;
