"""empty message

Revision ID: 248abfe93fef
Revises: fcffd250d566
Create Date: 2023-01-05 16:55:35.723163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '248abfe93fef'
down_revision = 'fcffd250d566'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_url', sa.String(length=250), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('user_url')

    # ### end Alembic commands ###
