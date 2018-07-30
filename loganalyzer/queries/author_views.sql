select
    auth.name as author,
    sum(v.views) as views
from articles as art
join article_views as v
    on art.slug = v.slug
join authors as auth
    on art.author = auth.id
group by auth.name
order by views desc
;
