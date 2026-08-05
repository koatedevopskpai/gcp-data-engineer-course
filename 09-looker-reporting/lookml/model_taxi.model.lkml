# LookML reference: model_taxi

# Explores expose views to end users. Explores are the exam-relevant concept.

connection: bigquery_demo
include: "/views/*.view.lkml"

explore: taxi_trips {
  label: "Taxi Trips"

  view_name: taxi_trips

  # Allow users to explore by date and vendor
  always_filter: {
    filters: [taxi_trips.pickup_date: "past 30 days"]
  }

  # Joins (example: to a vendor dimension)
  join: vendor {
    sql_on: ${taxi_trips.vendor_id} = ${vendor.vendor_id} ;;
    relationship: many_to_one
    type: left_outer
  }
}

view: vendor {
  sql_table_name: `gcp-data-engineering-course.cymbal_warehouse.vendor_dim` ;;

  dimension: vendor_id { type: string; sql: ${TABLE}.vendor_id ;; }
  dimension: vendor_name { type: string; sql: ${TABLE}.vendor_name ;; }
}
