-- get total number of accounts created today
SELECT a.date_created date, COUNT(*) accounts_created
 FROM cash.account a
 WHERE a.date_created = CURDATE();