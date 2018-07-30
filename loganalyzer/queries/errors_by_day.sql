select
    concat(
        trim(to_char(time, 'Month')), 
        ' ', 
        to_char(time, 'DD, YYYY')) as log_date,
    1. * sum(
        case when status >= '400' then 1
            else 0 end
        ) / count(*) as error_rate
from log
where method = 'GET'
group by log_date
having 
    1. * sum(
        case when status >= '400' then 1
        else 0 end
        ) / count(*) > .01
;
