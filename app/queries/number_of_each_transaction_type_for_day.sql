-- get number of each transaction made for a specific date

 SELECT type, COUNT(type) 'number of transactions', DATE(date) 'date'
 FROM cash.transaction
 WHERE DATE(date) = CURDATE()
 GROUP BY type;