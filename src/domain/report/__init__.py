from .commands import LoadReportCommand
from .loader import ReportLoader
from .repository import ReportRepository

SERVICES = (
    ReportRepository,
    ReportLoader,
    LoadReportCommand,
)
