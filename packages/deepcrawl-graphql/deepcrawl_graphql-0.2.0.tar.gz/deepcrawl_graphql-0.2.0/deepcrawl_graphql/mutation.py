"""
Base Mutation
=============
"""

from deepcrawl_graphql.api import DeepCrawlConnection
from deepcrawl_graphql.projects.fields import ProjectFields
from deepcrawl_graphql.reports.fields import ReportDownloadFields


class Mutation:
    """Mutation class"""

    def __init__(self, conn: DeepCrawlConnection) -> None:
        self.conn = conn
        self.ds = conn.ds
        self.mutation = self.ds.Mutation

    def create_project(self, project_input, fields=None):
        """Creates a Project

        :param project_input: Project input.
        :type project_input: dict
        :param fields: Select specific fields.
        :type fields: List(DSLField)
        """
        mutation = self.mutation.createProject.args(input=project_input).select(
            self.ds.CreateProjectPayload.project.select(*fields or ProjectFields.fields(self.ds))
        )
        return self.conn.run_mutation(mutation)

    def create_report_download(self, report_download_input, fields=None):
        """Creates a report download.

        :param report_download_input: Report Download input.
        :type report_download_input: dict
        :param fields: Select specific fields.
        :type fields: List(DSLField)
        """
        mutation = self.mutation.createReportDownload.args(input=report_download_input).select(
            self.ds.CreateReportDownloadPayload.reportDownload.select(*fields or ReportDownloadFields.fields(self.ds))
        )
        return self.conn.run_mutation(mutation)
