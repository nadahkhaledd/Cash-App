-- get total fees added to admin on chosen date
SELECT SUM(t.fees) as total_fees, DATE(t.date) date
 FROM transaction t
 WHERE DATE(t.date) = CURDATE()
 ;