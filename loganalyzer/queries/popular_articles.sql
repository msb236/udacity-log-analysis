select
    a.title,
    v.views
from articles as a
join article_views as v
    on a.slug = v.slug
order by v.views desc
limit 3;
