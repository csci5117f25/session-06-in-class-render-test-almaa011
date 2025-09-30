
# from contextlib import contextmanager
# import os

# import psycopg2  # For SQL DB
# from psycopg2.pool import ThreadedConnectionPool
# from psycopg2.extras import DictCursor, RealDictCursor

# pool = None  


# def setup():

#     global pool
#     if pool is not None:
#         return  #initialized

#     DATABASE_URL = os.environ.get("DATABASE_URL")#get DATABASE_URL from .env
#     if not DATABASE_URL:
#         raise RuntimeError("U don't have DB URL not set")

    
#     sslmode = os.environ.get("DB_SSLMODE", "prefer")  #get sslmode from .env

#     pool = ThreadedConnectionPool(1, 20, dsn=DATABASE_URL, sslmode=sslmode)


#     """ database is a library, to talk to library you need access card which is connection.
#         can't generate cards all the time so use connection pool

#         connection pool is: a box of ready-to-use connections

#         1, 20 → means:

#             Keep at least 1 card in the box.

#             Don’t let more than 20 cards exist at once.

#     """

#     _ensure_schema()
#     # this does: CREATE TABLE IF NOT EXISTS
#     # Prevents  error, ex: if you deploy to a fresh DB where the table  x hasn’t been created yet.


# @contextmanager
# def get_db_connection():
    

#     if pool is None:
#         raise RuntimeError("DB pool not initializ")
#     conn = pool.getconn()
#     try:
#         yield conn
#     finally:
#         pool.putconn(conn)


# @contextmanager
# def get_db_cursor(commit: bool = False):

#     with get_db_connection() as conn:
#         cur = conn.cursor(cursor_factory=DictCursor)
#         try:
#             yield cur
#             if commit:
#                 conn.commit()
#         finally:
#             cur.close()


# @contextmanager
# def get_db_cursor_realdict(commit: bool = False):
#     """Yield a RealDictCursor; commit if requested"""
#     with get_db_connection() as conn:
#         cur = conn.cursor(cursor_factory=RealDictCursor)
#         try:
#             yield cur
#             if commit:
#                 conn.commit()
#         finally:
#             cur.close()


# def _ensure_schema():
#     """Create the submission table if not created"""
#     with get_db_cursor(commit=True) as cur:
#         cur.execute(
#             """
#             CREATE TABLE IF NOT EXISTS submissions (
#                 id BIGSERIAL PRIMARY KEY,
#                 name TEXT NOT NULL DEFAULT '',
#                 email TEXT NOT NULL DEFAULT '',
#                 feedback TEXT NOT NULL DEFAULT '',
#                 created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
#             );
#             """
#         )


# # used by server.py bellow

# def insert_submission(name: str, email: str, feedback: str) -> int:
#     """Insert submission ---- returns id."""
#     setup()  
#     with get_db_cursor(commit=True) as cur:
#         cur.execute(
#             "INSERT INTO submissions(name, email, feedback) VALUES (%s, %s, %s) RETURNING id",
#             (name, email, feedback),
#         )
#         return cur.fetchone()[0]


