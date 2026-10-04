"""initial
RevisionID : 001"""
from alembic import op
import sqlalchemy as sa
revision="0001"
down_revision =None
branch_labels=None
depends_on=None

def  upgrade():
    op.create_table(

        "users",
        sa.Column("id",sa.Integer,primary_key=True),

        sa.Column("email",sa.String(255),nullable=False),
        sa.Column("hashed_password",sa.String(255),nullable=False),
        sa.Column("created_at",sa.DateTime,nullable=True),
    )
    op.create_index("ix_users_email","users",["email"],unique=True)

    op.create_table(
        "notifications",

        sa.Column("id",sa.Integer, primary_key=True),
        sa.Column("user_id",sa.Integer,sa.ForeignKey("users.id"), nullable=False),
        sa.Column("title",sa.String(255),nullable=False),
        sa.Column("body",sa.Text,nullable=False),
        sa.Column("fcm_message_id",sa.String(255),nullable=True),
        sa.Column(
            "status",
            sa.Enum("SENT","FAILED",name ="notificationsstatus"),
            nullable=True,
        ),
        sa.Column("created_at",sa.DateTime,nullable=True),
    )

def downgrade():
    op.drop_table("notifications")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")