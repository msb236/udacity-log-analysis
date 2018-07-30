create or replace view article_views as 
select
    substring(path from 10) as slug, 
    count(*) as views
from log
where path like '/article/%'
group by slug 
order by views desc
;
