-- get number of each transaction made for a specific date
SELECT t.type, COUNT(t.type) 'number of transactions', DATE(t.date) 'date'
 FROM cash.transaction t
 WHERE DATE(t.date) = CURDATE()
 GROUP BY t.type;