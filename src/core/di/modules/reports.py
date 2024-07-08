from domain.report.commands import LoadReportCommand
from domain.report.loader import ReportLoader
from domain.report.repository import ReportRepository

PROVIDERS = [
    (ReportLoader, lambda: ReportLoader()),
    (ReportRepository, lambda: ReportRepository()),
    (LoadReportCommand, lambda: LoadReportCommand()),
]
