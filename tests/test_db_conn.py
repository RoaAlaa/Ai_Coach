print("1. Script started")

from sqlalchemy import text
print("2. SQLAlchemy imported")

from app.core.database import engine
print("3. Engine imported")

with engine.connect() as connection:
    print("4. Connected to database")
    result = connection.execute(text("SELECT 1"))
    print("5. Query result:", result.scalar_one())

print("6. Test finished")