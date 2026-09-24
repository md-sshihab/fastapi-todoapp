"""phone num column adding

Revision ID: febe54dfebe1
Revises: 
Create Date: 2026-09-24 10:38:53.471942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'febe54dfebe1'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #op.add_column('users',sa.Column('phone',sa.String(),nullable=True))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
