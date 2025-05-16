"""add_submissions_table

Revision ID: 4a987f6143a3
Revises: 4d9e48b38f40
Create Date: 2025-05-15 20:09:10.432555

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4a987f6143a3"
down_revision: Union[str, None] = "4d9e48b38f40"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    #     ID: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    # user_id: uuid.UUID = Field(foreign_key="user.ID")
    # language: str
    # source_code: str
    # status: SubmissionStatus = Field(default=SubmissionStatus.PENDING)
    # result: SubmissionResult | None
    # execution_time: int | None
    # memory_usage: int | None

    op.create_table(
        "submissions",
        sa.Column("ID", sa.UUID, primary_key=True),
        sa.Column("user_id", sa.UUID, sa.ForeignKey("users.ID")),
        sa.Column("problem_id", sa.UUID, nullable=False),
        sa.Column("language", sa.String, nullable=False),
        sa.Column("source_code", sa.String, nullable=False),
        sa.Column("status", sa.String, nullable=False),
        sa.Column("result", sa.String, nullable=True),
        sa.Column("execution_time", sa.Integer, nullable=True),
        sa.Column("memory_usage", sa.Integer, nullable=True),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("submissions")
