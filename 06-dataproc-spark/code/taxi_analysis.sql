CREATE TEMPORARY VIEW taxi_trips
USING org.apache.spark.sql.parquet
OPTIONS (path "gs://cymbal-raw-<PROJECT>/taxi/*.parquet");

CREATE TEMPORARY VIEW vendor_stats AS
SELECT
  vendor_id,
  COUNT(*)          AS trip_count,
  AVG(fare_amount)  AS avg_fare,
  SUM(fare_amount)  AS total_revenue,
  AVG(trip_distance) AS avg_distance
FROM taxi_trips
WHERE fare_amount > 0
GROUP BY vendor_id;

SELECT * FROM vendor_stats ORDER BY total_revenue DESC;
