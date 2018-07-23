create or replace view article_views as 
select
    trim(leading '/article/' from path) as slug, 
    count(*) as views
from log
where path like '/article/%'
group by slug 
order by views desc
;
