# Lab 04.1 — Nested and Repeated Fields (STRUCT / ARRAY)

## Objectives
- Query nested/repeated data from the GA4 e-commerce dataset.
- Flatten arrays with `UNNEST`.
- Build and query nested structures.

## 1. Flatten `event_params` (ARRAY of STRUCTs)
```sql
SELECT
  event_name,
  params.key               AS param_key,
  params.value.string_value AS string_value,
  params.value.int_value    AS int_value
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_20210131`,
UNNEST(event_params) AS params
WHERE event_name = 'purchase'
LIMIT 100;
```

## 2. `items` array for purchase analysis
```sql
SELECT
  items.item_name,
  COUNT(*) AS purchase_count,
  SUM(items.price) AS total_revenue
FROM `bigquery-public-data.ga4_obfuscated_sample_ecommerce.events_20210131`,
UNNEST(items) AS items
WHERE event_name = 'purchase'
GROUP BY items.item_name
ORDER BY total_revenue DESC
LIMIT 10;
```

## 3. Build a nested orders table
```sql
CREATE OR REPLACE TABLE cymbal_warehouse.orders_nested AS
SELECT
  order_id,
  customer_id,
  ARRAY_AGG(
    STRUCT(product_id, product_name, quantity, price)
  ) AS items,
  SUM(price) AS total_amount
FROM cymbal_warehouse.raw_orders
GROUP BY order_id, customer_id;
```

```sql
-- Query it back, flattening the array
SELECT order_id, item.product_name, item.price
FROM cymbal_warehouse.orders_nested,
UNNEST(items) AS item
WHERE item.price > 100;
```

## Exam notes
- `UNNEST` turns an ARRAY into rows; use `LEFT JOIN UNNEST(...)` to keep rows
  with empty arrays.
- Nested repeated columns avoid joins and are the schema used by GA4 exports.
