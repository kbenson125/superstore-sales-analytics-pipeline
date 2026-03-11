-- Null sales check
SELECT COUNT(*) AS null_sales
FROM clean_orders
WHERE sales IS NULL;

-- Negative profit check
SELECT COUNT(*) AS negative_profit
FROM clean_orders
WHERE profit < 0;

-- Row counts
SELECT COUNT(*) FROM raw_orders;
SELECT COUNT(*) FROM clean_orders;

-- High discount check
SELECT *
FROM clean_orders
WHERE discount > 0.5;
