-- fct_daily_sales.sql: daily product sales metrics (Gold)
SELECT
  date,
  product,
  COUNT(*)                                            AS total_views,
  COUNTIF(action = 'add_to_cart')                     AS add_to_carts,
  COUNTIF(action = 'purchase')                        AS purchases,
  SUM(CASE WHEN action = 'purchase' THEN value ELSE 0 END) AS revenue
FROM {{ ref('stg_events') }}
GROUP BY date, product
