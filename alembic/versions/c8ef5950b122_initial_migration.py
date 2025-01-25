"""Initial migration

Revision ID: c8ef5950b122
Revises: 544664d773dc
Create Date: 2025-01-25 09:17:57.000953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8ef5950b122'
down_revision: Union[str, None] = '544664d773dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
