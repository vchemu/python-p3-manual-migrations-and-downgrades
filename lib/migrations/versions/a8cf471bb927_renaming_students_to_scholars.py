"""Renaming students to scholars

Revision ID: a8cf471bb927
Revises: 791279dd0760
Create Date: 2023-11-03 01:00:55.670793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8cf471bb927'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
