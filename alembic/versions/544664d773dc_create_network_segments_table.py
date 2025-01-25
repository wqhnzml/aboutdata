from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'network_segments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('segment', sa.String(length=255), nullable=False),
        sa.Column('sensitive_info_enabled', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('network_segments')