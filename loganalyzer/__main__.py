#!/bin/env python2.7
"""Report log analysis to standard out"""
import psycopg2
from . import queries

# Reporting text
_ARTICLE_REPORT_DESC = '1. What are the most popular three articles of all time?'
_ARTICLE_REPORT_FMT = '"{text}" — {amount} views'
_AUTHOR_REPORT_DESC = '2. Who are the most popular article authors of all time?'
_AUTHOR_REPORT_FMT = '"{text}" — {amount} views'
_ERRORS_REPORT_DESC = (
    '3. On which days did more than 1% of requests lead to errors?'
)
_ERRORS_REPORT_FMT = '"{text}" — {amount:.1%} errors'

class Report:
    """Log analysis report object, manages view creation and report execution

    Report runs at instantiation time. It establishes db connection, creates
    reporting views from .sql files in `queries` submodule, and executes
    the three quired reports.
    """

    def __init__(self):
        # Create db connection
        self.db = psycopg2.connect('dbname=news')
        # Get cursor object
        self.cur = self.db.cursor()
        # Add view to db with view counts by slug
        self.create_view_for_article_views()
        # Run report modules
        self.run_reports()

    def run_reports(self):
        """Run all three report modules"""
        # Popular articles
        self.report_from_query(
            query=queries.popular_articles,
            desc=_ARTICLE_REPORT_DESC,
            fmt=_ARTICLE_REPORT_FMT
        )
        # Popular article authors
        self.report_from_query(
            query=queries.author_views,
            desc=_AUTHOR_REPORT_DESC,
            fmt=_AUTHOR_REPORT_FMT
        )
        # High error-rate days
        self.report_from_query(
            query=queries.errors_by_day,
            desc=_ERRORS_REPORT_DESC,
            fmt=_ERRORS_REPORT_FMT
        )

    def create_view_for_article_views(self):
        """Create view-count-by-slug view from .sql file"""
        # Run view creation statements
        self.cur.execute(queries.article_views)
        self.db.commit()

    def report_from_query(self, query, desc, fmt):
        """Execute individual report module 

        Print report description, execution report sql, and
        print report output.

        Arguments:
            query (str): SQL query to generate reporting results
            desc (str): Report description / header
            fmt (str): Report output template to be populated 
                with query results
        """
        # Print report descrition / header to screen
        print(desc)
        # Execute analysis query to generate reporting results
        self.cur.execute(query)
        # Iterate over query results to populate report output
        for text, amount in self.cur.fetchall():
            report_line = fmt.format(text=text, amount=amount)
            # Print report output to screen
            print(report_line)


if __name__ == '__main__':
    # Generate report
    Report()
