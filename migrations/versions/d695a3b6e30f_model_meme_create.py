"""model Meme create.

Revision ID: d695a3b6e30f
Revises: dcec07724b8f
Create Date: 2022-07-01 19:46:09.854914

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d695a3b6e30f"
down_revision = "dcec07724b8f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "meme",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("url", sa.String(length=300), nullable=True),
        sa.Column("title", sa.String(length=300), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("url"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("meme")
    # ### end Alembic commands ###
