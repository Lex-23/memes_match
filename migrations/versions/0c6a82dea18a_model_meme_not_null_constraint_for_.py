"""model Meme not null constraint for fields.

Revision ID: 0c6a82dea18a
Revises: 744630df6b2d
Create Date: 2022-07-01 19:57:25.050705

"""
import sqlalchemy as sa  # noqa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "0c6a82dea18a"
down_revision = "744630df6b2d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "meme", "url", existing_type=mysql.VARCHAR(length=300), nullable=False
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "meme", "url", existing_type=mysql.VARCHAR(length=300), nullable=True
    )
    # ### end Alembic commands ###
