from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from alembic import context
import os
import asyncio
from app.models import Base
from app.database import DATABASE_URL
import traceback

from sqlalchemy import event
from sqlalchemy.engine import Engine

#@event.listens_for(Engine, "before_cursor_execute")
#def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
#    print("🚀 Executing SQL:", statement)

config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async def do_migrations():
        try:
            async with connectable.begin() as connection:
                await connection.run_sync(
                    lambda sync_conn: context.configure(
                        connection=sync_conn,
                        target_metadata=target_metadata,
                        render_as_batch=True,
                        compare_type=True,
                        compare_server_default=True,
                    )
                )
                await connection.run_sync(lambda conn: context.run_migrations())
                #await connection.commit()
        except Exception as e:
            print("🔥 EXCEPTION CAUGHT DURING MIGRATION 🔥")
            traceback.print_exc()
        finally:
            await connectable.dispose()

    asyncio.run(do_migrations())

run_migrations_online()
