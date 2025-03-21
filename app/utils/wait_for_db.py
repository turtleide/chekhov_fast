# app/utils/wait_for_db.py
import asyncio
import asyncpg
import os

async def wait_for_db():
    print("⏳ wait_for_db.py 실행됨: DB 연결을 기다리는 중...")
    dsn = os.getenv("DATABASE_URL", "")
    dsn = dsn.replace("postgresql+asyncpg://", "postgresql://")
    while True:
        try:
            conn = await asyncpg.connect(dsn=dsn)
            await conn.execute("SELECT 1")
            await conn.close()
            print("✅ DB 연결 성공! 쿼리 테스트 완료")
            break
        except Exception as e:
            print(f"DB가 아직 준비되지 않았습니다: {e}. 1초 후 재시도...")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(wait_for_db())