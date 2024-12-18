from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import get_db
from app.boards.model import BoardPost
from faker import Faker
import hashlib
import time  # 시간 측정을 위한 모듈
import asyncio
router = APIRouter(
    prefix="/boards",
    tags=["boards"],
    responses={404: {"description": "Not found"}},
)
fake = Faker()

@router.get("/{board_id}")
async def read_board_posts(board_id: int, db: AsyncSession = Depends(get_db)):
    start_time = time.time()
    
    query = select(BoardPost).where(BoardPost.boardId == board_id)  # WHERE 조건
    result = await db.execute(query)
    
    items = result.scalars().fetchall()
    
    end_time = time.time()

            # 실행 시간 계산
    execution_time = end_time - start_time
    print(f"Execution Time: {execution_time:.3f} seconds")
    return items

@router.post("/{board_id}")
async def create_board_post(board_id: int,db: AsyncSession = Depends(get_db)):
        # 시작 시간 기록
        start_time = time.time()
        for _ in range(1000):
            passwd = fake.password(length=10)  # 랜덤 비밀번호 생성
            hashed_password = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
            regist_date = fake.date_time()  # 랜덤 날짜 생성 (올해 날짜)
            boardPost = BoardPost(
                boardId=board_id, 
                title=fake.sentence(nb_words=6),  # 가짜 제목 생성
                contents=fake.paragraph(nb_sentences=100),  # 가짜 내용 생성
                writer=fake.name(),
                registDate=regist_date,
                passwd=hashed_password
            )
            db.add(boardPost)
        await db.commit()
            
            # 종료 시간 기록
        
        end_time = time.time()

            # 실행 시간 계산
        execution_time = end_time - start_time
        print(f"Execution Time: {execution_time:.3f} seconds")
