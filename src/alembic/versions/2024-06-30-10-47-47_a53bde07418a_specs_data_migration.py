"""specs data migration

Revision ID: a53bde07418a
Revises: 24d5df3b62df
Create Date: 2024-06-30 10:47:47.169360

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "a53bde07418a"
down_revision: Union[str, None] = "24d5df3b62df"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
spec_table = sa.table("spec", sa.column("name"), sa.column("role"))


def upgrade() -> None:
    op.bulk_insert(
        spec_table,
        [
            {
                "name": "Tank",
                "role": "tank",
            },
            {
                "name": "Healer",
                "role": "healer",
            },
            {
                "name": "StaminaDPS",
                "role": "dps",
            },
            {
                "name": "MagickaDPS",
                "role": "dps",
            },
        ],
    )


def downgrade() -> None:
    op.execute("DELETE FROM spec WHERE role in ('dps', 'healer', 'tank')")
