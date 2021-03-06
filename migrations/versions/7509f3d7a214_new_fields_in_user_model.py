"""new fields in user model

Revision ID: 7509f3d7a214
Revises: 617f96ccb702
Create Date: 2020-02-07 16:31:14.789354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7509f3d7a214'
down_revision = '617f96ccb702'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
