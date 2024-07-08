"""encounters data migration

Revision ID: 4ea088a28854
Revises: 7342e246dd46
Create Date: 2024-06-30 10:47:30.598108

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "4ea088a28854"
down_revision: Union[str, None] = "7342e246dd46"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None
encounter_table = sa.table(
    "encounter",
    sa.column("id"),
    sa.column("zone_id"),
    sa.column("name"),
    sa.column("is_final"),
    sa.column("vhm_difficulty_id"),
)


def upgrade() -> None:
    op.bulk_insert(
        encounter_table,
        [
            {
                "id": 1,
                "zone_id": 1,
                "name": "Lightning Storm Atronach",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 2,
                "zone_id": 1,
                "name": "Foundation Stone Atronach",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3,
                "zone_id": 1,
                "name": "Varlariel",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 4,
                "zone_id": 1,
                "name": "The Mage",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 5,
                "zone_id": 2,
                "name": "Ra Kotu",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 6,
                "zone_id": 2,
                "name": "The Yokedas",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 8,
                "zone_id": 2,
                "name": "The Warrior",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 9,
                "zone_id": 3,
                "name": "Possessed Mantikora",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 10,
                "zone_id": 3,
                "name": "Stonebreaker",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 11,
                "zone_id": 3,
                "name": "Ozara",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 12,
                "zone_id": 3,
                "name": "The Serpent",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 13,
                "zone_id": 5,
                "name": "Zhaj’hassa The Forgotten",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 14,
                "zone_id": 5,
                "name": "The Twins",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 15,
                "zone_id": 5,
                "name": "Rakkhat",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 16,
                "zone_id": 6,
                "name": "The Hunter Killers",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 17,
                "zone_id": 6,
                "name": "Pinnacle Factotum",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 18,
                "zone_id": 6,
                "name": "Archcustodian",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 19,
                "zone_id": 6,
                "name": "The Refabrication Committee",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 20,
                "zone_id": 6,
                "name": "Assembly General",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 21,
                "zone_id": 7,
                "name": "Saint Llothis the Pious",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 22,
                "zone_id": 7,
                "name": "Saint Felms the Bold",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 23,
                "zone_id": 7,
                "name": "Saint Olms the Just",
                "is_final": True,
                "vhm_difficulty_id": 124,
            },
            {
                "id": 24,
                "zone_id": 8,
                "name": "Shade of Galenwe",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 25,
                "zone_id": 8,
                "name": "Shade of Relequen",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 26,
                "zone_id": 8,
                "name": "Shade of Siroria",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 27,
                "zone_id": 8,
                "name": "Z'Maja",
                "is_final": True,
                "vhm_difficulty_id": 125,
            },
            {
                "id": 3000,
                "zone_id": 11,
                "name": "Vale of the Surreal",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3001,
                "zone_id": 11,
                "name": "Seht's Balcony",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3002,
                "zone_id": 11,
                "name": "Drome of Toxic Shock",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3003,
                "zone_id": 11,
                "name": "Seht's Flywheel",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3004,
                "zone_id": 11,
                "name": "Rink of Frozen Blood",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3005,
                "zone_id": 11,
                "name": "Spiral Shadows",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3006,
                "zone_id": 11,
                "name": "Vault of Umbrage",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3007,
                "zone_id": 11,
                "name": "Igneous Cistern",
                "is_final": False,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 3008,
                "zone_id": 11,
                "name": "Theater of Despair",
                "is_final": True,
                "vhm_difficulty_id": 121,
            },
            {
                "id": 43,
                "zone_id": 12,
                "name": "Lokkestiiz",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 44,
                "zone_id": 12,
                "name": "Yolnahkriin",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 45,
                "zone_id": 12,
                "name": "Nahviintaas",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 46,
                "zone_id": 14,
                "name": "Yandir the Butcher",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 47,
                "zone_id": 14,
                "name": "Captain Vrol",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 48,
                "zone_id": 14,
                "name": "Lord Falgravn",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 49,
                "zone_id": 15,
                "name": "Oaxiltso",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 50,
                "zone_id": 15,
                "name": "Flame-Herald Bahsei",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 51,
                "zone_id": 15,
                "name": "Xalvakka",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 52,
                "zone_id": 16,
                "name": "Lylanar and Turlassil",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 53,
                "zone_id": 16,
                "name": "Reef Guardian",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 54,
                "zone_id": 16,
                "name": "Tideborn Taleria",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 55,
                "zone_id": 17,
                "name": "Exarchanic Yaseyla",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 56,
                "zone_id": 17,
                "name": "Archwizard Twelvane and Chimera",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 57,
                "zone_id": 17,
                "name": "Ansuul the Tormentor",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 58,
                "zone_id": 18,
                "name": "Count Ryelaz and Zilyesset",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 59,
                "zone_id": 18,
                "name": "Orphic Shattered Shard",
                "is_final": False,
                "vhm_difficulty_id": 122,
            },
            {
                "id": 60,
                "zone_id": 18,
                "name": "Xoryn",
                "is_final": True,
                "vhm_difficulty_id": 122,
            },
        ],
    )


def downgrade() -> None:
    op.execute(
        "DELETE FROM encounter WHERE zone_id IN (1, 2, 3, 5, 6, 7, 8, 11, 12, 14, 15, 16, 17, 18)"
    )
