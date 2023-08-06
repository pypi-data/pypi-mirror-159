struct Metadata {
  1: required string client_id,
  2: required string purpose,
  3: optional string tracking_id,
}

struct GetRemainingCapacityRequest {
  1: required Metadata meta,
  2: required string limit_id,
}

struct SetLimitRequest {
  1: required Metadata meta,

  # Will be null when setting a limit for the first time.
  2: optional string limit_id,

  # max size of bucket
  3: optional i32 throttling_burst_limit,

  # requests per second
  4: optional i32 throttling_rate_limit,
}
