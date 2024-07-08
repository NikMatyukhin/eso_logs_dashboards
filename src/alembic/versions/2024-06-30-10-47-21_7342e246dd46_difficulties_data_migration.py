"""difficulties data migration

Revision ID: 7342e246dd46
Revises: fee6db95beea
Create Date: 2024-06-30 10:47:21.427190

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "7342e246dd46"
down_revision: Union[str, None] = "fee6db95beea"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
difficulty_table = sa.table("difficulty", sa.column("id"), sa.column("name"))


def upgrade() -> None:
    op.bulk_insert(
        difficulty_table,
        [
            {
                "id": 120,
                "name": "Normal",
            },
            {
                "id": 121,
                "name": "Veteran",
            },
            {
                "id": 122,
                "name": "Veteran Hard Mode",
            },
            {
                "id": 123,
                "name": "Veteran +1",
            },
            {
                "id": 124,
                "name": "Veteran +2",
            },
            {
                "id": 125,
                "name": "Veteran +3",
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM difficulty WHERE id IN (120, 121, 122, 123, 124, 125)")
