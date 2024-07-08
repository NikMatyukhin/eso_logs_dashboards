"""zones data migration

Revision ID: fee6db95beea
Revises: 506f099f978b
Create Date: 2024-06-30 10:47:09.804601

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "fee6db95beea"
down_revision: Union[str, None] = "506f099f978b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
zone_table = sa.table("zone", sa.column("id"), sa.column("name"))


def upgrade() -> None:
    op.bulk_insert(
        zone_table,
        [
            {
                "id": 1,
                "name": "Aetherian Archive",
            },
            {
                "id": 2,
                "name": "Hel Ra Citadel",
            },
            {
                "id": 3,
                "name": "Sanctum Ophidia",
            },
            {
                "id": 5,
                "name": "Maw of Lorkhaj",
            },
            {
                "id": 6,
                "name": "The Halls of Fabrication",
            },
            {
                "id": 7,
                "name": "Asylum Sanctorium",
            },
            {
                "id": 8,
                "name": "Cloudrest",
            },
            {
                "id": 11,
                "name": "Maelstrom Arena",
            },
            {
                "id": 12,
                "name": "Sunspire",
            },
            {
                "id": 14,
                "name": "Kyne's Aegis",
            },
            {
                "id": 15,
                "name": "Rockgrove",
            },
            {
                "id": 16,
                "name": "Dreadsail Reef",
            },
            {
                "id": 17,
                "name": "Sanity's Edge",
            },
            {
                "id": 18,
                "name": "Lucent Citadel",
            },
        ],
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM zone WHERE id IN (1, 2, 3, 5, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18)"
    )
