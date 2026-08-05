-- stg_events.sql: clean, typed, deduped events (Silver)
WITH source AS (
  SELECT
    event_id,
    user_id,
    session_id,
    TIMESTAMP(timestamp) AS event_timestamp,
    page,
    product,
    action,
    value,
    hour,
    date
  FROM {{ source('cymbal_warehouse', 'clickstream_raw') }}
  WHERE event_id IS NOT NULL
),
deduped AS (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY event_id ORDER BY event_timestamp) AS rn
  FROM source
)
SELECT * EXCEPT (rn)
FROM deduped
WHERE rn = 1
