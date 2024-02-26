SELECT DISTINCT SUBSTRING(email from POSITION('@' in email) + 1) as email_domain, COUNT(*)
FROM Emails
WHERE RIGHT(email, 4) = '.com'
GROUP BY email_domain
ORDER BY email_domain, COUNT(*) desc
