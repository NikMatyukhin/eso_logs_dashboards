"""regions data migration

Revision ID: 24d5df3b62df
Revises: 4ea088a28854
Create Date: 2024-06-30 10:47:40.033056

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "24d5df3b62df"
down_revision: Union[str, None] = "4ea088a28854"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
region_table = sa.table("region", sa.column("id"), sa.column("name"), sa.column("slug"))


def upgrade() -> None:
    op.bulk_insert(
        region_table,
        [
            {
                "id": 1,
                "name": "North America",
                "slug": "NA",
            },
            {
                "id": 2,
                "name": "Europe",
                "slug": "EU",
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM region WHERE id in (1, 2)")
