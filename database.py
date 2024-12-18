from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

DATABASE_URL = "mysql+asyncmy://root:Q!w2e3r4@127.0.0.1/clicknapi"

# SQLAlchemy 비동기 엔진 생성
engine = create_async_engine(DATABASE_URL, echo=True)

# 세션 생성
async_session = sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Base 클래스 생성
Base: DeclarativeMeta = declarative_base()

# 세션을 가져오는 함수
async def get_db():
    async with async_session() as session:
        yield session