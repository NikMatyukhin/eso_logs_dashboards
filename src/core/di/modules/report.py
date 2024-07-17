import aioinject

from core.di._types import Providers
from src.domain.report.commands import LoadReportCommand
from src.domain.report.loader import ReportLoader
from src.domain.report.repository import ReportRepository

PROVIDERS: Providers = (
    aioinject.Scoped(ReportRepository),
    aioinject.Scoped(ReportLoader),
    aioinject.Scoped(LoadReportCommand),
)
