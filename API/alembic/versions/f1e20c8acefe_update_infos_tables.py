"""Update infos tables

Revision ID: f1e20c8acefe
Revises: 925254e8968e
Create Date: 2024-12-18 11:34:28.590286

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1e20c8acefe'
down_revision: Union[str, None] = '925254e8968e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_associates_email', table_name='associates')
    op.create_index(op.f('ix_associates_email'), 'associates', ['email'], unique=False)
    op.drop_index('ix_orphanages_name', table_name='orphanages')
    op.create_index(op.f('ix_orphanages_name'), 'orphanages', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orphanages_name'), table_name='orphanages')
    op.create_index('ix_orphanages_name', 'orphanages', ['name'], unique=True)
    op.drop_index(op.f('ix_associates_email'), table_name='associates')
    op.create_index('ix_associates_email', 'associates', ['email'], unique=True)
    # ### end Alembic commands ###
