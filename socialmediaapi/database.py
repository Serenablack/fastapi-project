import databases
import sqlalchemy
from config import config

metadata = sqlalchemy.metadata()  # is used to defined the table in the database

post_table = sqlalchemy.Table(
    "posts",  # name of table
    metadata,  # sqlalchemy uses to store the information about the table and also to validate the multiple relationships
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("body", sqlalchemy.String),
)

comment_table = sqlalchemy.Table(
    "comments",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("comment", sqlalchemy.String),
    sqlalchemy.Column("post_id", sqlalchemy.ForeignKey("posts.id"), nullable=False),
)
# is used to allow sqlalchemy to connect to the database
engine = sqlalchemy.create_engine(
    config.DATABASE_URL,
    # needed only for sqlite as it is single threaded
    connect_args={"check_same_thread": False},
)

metadata.create_all(engine)

database = databases.Database(
    config.DATABASE_URL, force_rollback=config.DB_FORCE_ROLL_BACK
)
