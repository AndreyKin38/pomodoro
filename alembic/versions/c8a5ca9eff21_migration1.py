"""migration1

Revision ID: c8a5ca9eff21
Revises: e1d5ba1605c9
Create Date: 2025-05-09 19:20:09.518382

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8a5ca9eff21'
down_revision: Union[str, None] = 'e1d5ba1605c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Categories', sa.Column('category', sa.String(), nullable=False))
    op.alter_column('Categories', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Categories', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('Categories', 'category')
    # ### end Alembic commands ###
