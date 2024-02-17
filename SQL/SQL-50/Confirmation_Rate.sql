select s.user_id, 
CASE
    WHEN c.time_stamp is null THEN 0.0
    ELSE round(avg(c.action = "confirmed"), 2)
END as confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id;
