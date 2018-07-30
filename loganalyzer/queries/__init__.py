import pkg_resources
import glob
import os

author_views = pkg_resources.resource_string(
    __name__, 
    "author_views.sql"
).decode('utf-8')
article_views = pkg_resources.resource_string(
    __name__, 
    "article_views.sql"
).decode('utf-8')
errors_by_day = pkg_resources.resource_string(
    __name__, 
    "errors_by_day.sql"
).decode('utf-8')
popular_articles = pkg_resources.resource_string(
    __name__, 
    "popular_articles.sql"
).decode('utf-8')
