select
    time::date as log_date,
    100.0 * sum(
        case when status >= '400' then 1
        else 0 end
        ) / count(*) as error_rate
from log
where method = 'GET'
group by log_date
having 
    100.0 * sum(
        case when status >= '400' then 1
        else 0 end
        ) / count(*) > 1
;
