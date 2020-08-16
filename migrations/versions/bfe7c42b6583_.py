"""empty message

Revision ID: bfe7c42b6583
Revises: 
Create Date: 2020-08-17 00:56:27.621761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfe7c42b6583'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.Column('song_name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('song_id'),
    sa.UniqueConstraint('song_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('songs')
    # ### end Alembic commands ###
