from sqlalchemy import Column, Integer, String
from app.database import Base

# 예제 모델
class BoardPost(Base):
    __tablename__ = "board_post"

    id = Column(Integer, primary_key=True, index=True, autoincrement = "auto")
    boardId = Column('board_id', Integer, nullable=False)
    title = Column(String(255), nullable=False)
    contents = Column(String, nullable=True)
    writer = Column(String, nullable=False)
    registDate = Column('regist_date', String, nullable=False)
    passwd = Column(String, nullable=True)