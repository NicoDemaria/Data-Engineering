WITH raw_hosts AS (
    SELECT
        *
    FROM AIRBNB.RAW.RAW_HOSTS
        
)
SELECT
    id AS host_id,
    name AS host_name,
    IS_SUPERHOST,
    CREATED_AT,
    UPDATED_AT
    
FROM
    raw_hosts




