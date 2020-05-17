"""pending table

Revision ID: 522d0de4ef57
Revises: d3c9b10f4599
Create Date: 2020-04-13 22:22:52.506040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '522d0de4ef57'
down_revision = 'd3c9b10f4599'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pending',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pending_email'), 'pending', ['email'], unique=True)
    op.create_index(op.f('ix_pending_username'), 'pending', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pending_username'), table_name='pending')
    op.drop_index(op.f('ix_pending_email'), table_name='pending')
    op.drop_table('pending')
    # ### end Alembic commands ###
