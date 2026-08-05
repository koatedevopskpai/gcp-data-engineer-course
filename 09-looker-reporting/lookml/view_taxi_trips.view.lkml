# LookML reference: view_taxi_trips

# Exam-only: the exam tests Looker/LookML concepts. Looker Studio does NOT
# use LookML; these files model the same data for Looker.

connection: bigquery_demo
include: "/views/*.view.lkml"

view: taxi_trips {
  sql_table_name: `gcp-data-engineering-course.cymbal_warehouse.taxi_trips` ;;

  dimension: trip_id {
    type: string
    sql: ${TABLE}.trip_id ;;
    primary_key: yes
  }

  dimension: vendor_id {
    type: string
    sql: ${TABLE}.vendor_id ;;
  }

  dimension_group: pickup {
    type: time
    timeframes: [date, week, month, year]
    sql: ${TABLE}.pickup_datetime ;;
  }

  dimension: payment_type {
    type: string
    sql: ${TABLE}.payment_type ;;
  }

  measure: total_fare {
    type: sum
    sql: ${TABLE}.fare_amount ;;
  }

  measure: avg_fare {
    type: average
    sql: ${TABLE}.fare_amount ;;
  }

  measure: trip_count {
    type: count
    sql: ${TABLE}.trip_id ;;
  }
}
