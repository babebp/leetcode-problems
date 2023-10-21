select email
from person
group by email
having count(id) >= 2;

-- LINK : https://leetcode.com/problems/duplicate-emails/