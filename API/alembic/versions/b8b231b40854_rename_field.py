"""Rename field

Revision ID: b8b231b40854
Revises: f5aa74eae413
Create Date: 2024-12-18 18:39:35.226624

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8b231b40854'
down_revision: Union[str, None] = 'f5aa74eae413'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orphanages', sa.Column('city', sa.String(), nullable=False))
    op.drop_column('orphanages', 'neighborhood')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orphanages', sa.Column('neighborhood', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('orphanages', 'city')
    # ### end Alembic commands ###
