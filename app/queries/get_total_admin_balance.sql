-- the total number of fees taken from users to the admin account
SELECT u.username, a.current_balance AS total_balance
 FROM cash.user AS u
 JOIN cash.account AS a
 ON a.user = u.username
 WHERE u.role = "admin"
 ;