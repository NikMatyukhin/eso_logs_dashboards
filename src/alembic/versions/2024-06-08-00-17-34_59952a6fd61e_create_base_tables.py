"""create base tables

Revision ID: 59952a6fd61e
Revises:
Create Date: 2024-06-08 00:17:34.972553

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "59952a6fd61e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ability",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("icon", sa.String(), nullable=False),
        sa.Column("flags", sa.Integer(), nullable=False),
        sa.Column("_type", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_ability")),
    )
    op.create_table(
        "damage_source",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("icon", sa.String(), nullable=False),
        sa.Column("_type", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_damage_source")),
    )
    op.create_table(
        "difficulty",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_difficulty")),
    )
    op.create_table(
        "gear",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("slot", sa.Integer(), nullable=False),
        sa.Column("icon", sa.String(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("set_id", sa.Integer(), nullable=False),
        sa.Column("set_name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_gear")),
    )
    op.create_table(
        "partition",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("compact_name", sa.String(), nullable=False),
        sa.Column("default", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_partition")),
    )
    op.create_table(
        "region",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("slug", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_region")),
    )
    op.create_table(
        "spec",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("role", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_spec")),
    )
    op.create_table(
        "zone",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_zone")),
    )
    op.create_table(
        "encounter",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("zone_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["zone_id"], ["zone.id"], name=op.f("fk_encounter_zone_id_zone")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_encounter")),
    )
    op.create_table(
        "report",
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("start_time", sa.Date(), nullable=False),
        sa.Column("end_time", sa.Date(), nullable=False),
        sa.Column("trial_score", sa.Integer(), nullable=True),
        sa.Column("trial_time", sa.Time(), nullable=True),
        sa.Column("region_id", sa.Integer(), nullable=False),
        sa.Column("zone_id", sa.Integer(), nullable=False),
        sa.CheckConstraint(
            "start_time <= end_time", name=op.f("ck_report_start_less_than_end")
        ),
        sa.ForeignKeyConstraint(
            ["region_id"], ["region.id"], name=op.f("fk_report_region_id_region")
        ),
        sa.ForeignKeyConstraint(
            ["zone_id"], ["zone.id"], name=op.f("fk_report_zone_id_zone")
        ),
        sa.PrimaryKeyConstraint("code", name=op.f("pk_report")),
    )
    op.create_table(
        "actor",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("display_name", sa.String(), nullable=False),
        sa.Column("damage_done", sa.Integer(), nullable=False),
        sa.Column("healing_done", sa.Integer(), nullable=False),
        sa.Column("_type", sa.String(), nullable=False),
        sa.Column("sub_type", sa.String(), nullable=False),
        sa.Column("report_code", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["report_code"], ["report.code"], name=op.f("fk_actor_report_code_report")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_actor")),
    )
    op.create_table(
        "fight",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("start_time", sa.Date(), nullable=False),
        sa.Column("end_time", sa.Date(), nullable=False),
        sa.Column("average_item_level", sa.Float(), nullable=False),
        sa.Column("boss_percentage", sa.Float(), nullable=True),
        sa.Column("report_code", sa.String(), nullable=False),
        sa.Column("encounter_id", sa.Integer(), nullable=True),
        sa.Column("difficulty_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["difficulty_id"],
            ["difficulty.id"],
            name=op.f("fk_fight_difficulty_id_difficulty"),
        ),
        sa.ForeignKeyConstraint(
            ["encounter_id"],
            ["encounter.id"],
            name=op.f("fk_fight_encounter_id_encounter"),
        ),
        sa.ForeignKeyConstraint(
            ["report_code"], ["report.code"], name=op.f("fk_fight_report_code_report")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_fight")),
    )
    op.create_table(
        "report_damage_sources",
        sa.Column("total", sa.Integer(), nullable=False),
        sa.Column("report_code", sa.String(), nullable=False),
        sa.Column("damage_source_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["damage_source_id"],
            ["damage_source.id"],
            name=op.f("fk_report_damage_sources_damage_source_id_damage_source"),
        ),
        sa.ForeignKeyConstraint(
            ["report_code"],
            ["report.code"],
            name=op.f("fk_report_damage_sources_report_code_report"),
        ),
        sa.PrimaryKeyConstraint(
            "report_code", "damage_source_id", name=op.f("pk_report_damage_sources")
        ),
    )
    op.create_table(
        "actor_abilities",
        sa.Column("actor_id", sa.Uuid(), nullable=False),
        sa.Column("ability_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["ability_id"],
            ["ability.id"],
            name=op.f("fk_actor_abilities_ability_id_ability"),
        ),
        sa.ForeignKeyConstraint(
            ["actor_id"], ["actor.id"], name=op.f("fk_actor_abilities_actor_id_actor")
        ),
        sa.PrimaryKeyConstraint(
            "actor_id", "ability_id", name=op.f("pk_actor_abilities")
        ),
    )
    op.create_table(
        "actor_gear_sets",
        sa.Column("trait", sa.Integer(), nullable=False),
        sa.Column("enchant", sa.Integer(), nullable=False),
        sa.Column("actor_id", sa.Uuid(), nullable=False),
        sa.Column("gear_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["actor_id"], ["actor.id"], name=op.f("fk_actor_gear_sets_actor_id_actor")
        ),
        sa.ForeignKeyConstraint(
            ["gear_id"], ["gear.id"], name=op.f("fk_actor_gear_sets_gear_id_gear")
        ),
        sa.PrimaryKeyConstraint("actor_id", "gear_id", name=op.f("pk_actor_gear_sets")),
    )
    op.create_table(
        "actor_specs",
        sa.Column("actor_id", sa.Uuid(), nullable=False),
        sa.Column("spec_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["actor_id"], ["actor.id"], name=op.f("fk_actor_specs_actor_id_actor")
        ),
        sa.ForeignKeyConstraint(
            ["spec_id"], ["spec.id"], name=op.f("fk_actor_specs_spec_id_spec")
        ),
        sa.PrimaryKeyConstraint("actor_id", "spec_id", name=op.f("pk_actor_specs")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("actor_specs")
    op.drop_table("actor_gear_sets")
    op.drop_table("actor_abilities")
    op.drop_table("report_damage_sources")
    op.drop_table("fight")
    op.drop_table("actor")
    op.drop_table("report")
    op.drop_table("encounter")
    op.drop_table("zone")
    op.drop_table("spec")
    op.drop_table("region")
    op.drop_table("partition")
    op.drop_table("gear")
    op.drop_table("difficulty")
    op.drop_table("damage_source")
    op.drop_table("ability")
    # ### end Alembic commands ###
