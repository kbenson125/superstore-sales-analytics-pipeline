-- Clean orders table
CREATE TABLE clean_orders AS
SELECT
    order_id,
    order_date,
    ship_date,
    region,
    state,
    city,
    category,
    sub_category,
    product_name,
    sales,
    profit,
    quantity,
    discount,
    customer_id,
    segment
FROM raw_orders
WHERE sales IS NOT NULL
AND quantity > 0;

-- Sales summary table
CREATE TABLE sales_summary AS
SELECT
    region,
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT customer_id) AS customers
FROM clean_orders
GROUP BY region, category;

-- Monthly sales table
CREATE TABLE monthly_sales AS
SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(sales) AS monthly_sales,
    SUM(profit) AS monthly_profit
FROM clean_orders
GROUP BY month;
