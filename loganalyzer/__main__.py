import psycopg2
from . import queries

ARTICLE_REPORT_DESC = '1. What are the most popular three articles of all time?'
ARTICLE_REPORT_FMT = '"{text}" — {amount} views'
AUTHOR_REPORT_DESC = '2. Who are the most popular article authors of all time?'
AUTHOR_REPORT_FMT = '"{text}" — {amount} views'
ERRORS_REPORT_DESC = (
    '3. On which days did more than 1% of requests lead to errors?'
)
ERRORS_REPORT_FMT = '"{text}" — {amount:.1%} errors'

class Report:

    def __init__(self):

        self.db = psycopg2.connect('dbname=news')
        self.cur = self.db.cursor()
        self.create_view_for_article_views()
        self.report_from_query(
            query=queries.popular_articles,
            desc=ARTICLE_REPORT_DESC,
            fmt=ARTICLE_REPORT_FMT
        )
        self.report_from_query(
            query=queries.author_views,
            desc=AUTHOR_REPORT_DESC,
            fmt=AUTHOR_REPORT_FMT
        )
        self.report_from_query(
            query=queries.errors_by_day,
            desc=ERRORS_REPORT_DESC,
            fmt=AUTHOR_REPORT_FMT
        )

    def create_view_for_article_views(self):

        self.cur.execute(queries.article_views)
        self.db.commit()

    def report_from_query(self, query, desc, fmt):

        print(desc)
        self.cur.execute(query)
        for text, amount in self.cur.fetchall():
            report_line = fmt.format(text=text, amount=amount)
            print(report_line)

    @classmethod
    def generate_report(cls):
        cls()

if __name__ == '__main__':

    Report.generate_report()
