"""empty message

Revision ID: 539388d27e4d
Revises: 89ed6714130c
Create Date: 2020-08-23 17:42:27.851819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '539388d27e4d'
down_revision = '89ed6714130c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('job', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'job')
    # ### end Alembic commands ###
