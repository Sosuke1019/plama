from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, VARCHAR
from models.database import Base
from datetime import datetime
from flask_login import UserMixin

#userテーブル
class user(UserMixin, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Text, unique=True, nullable=False)
    room_number = Column(Text, nullable=False)
    hash = Column(VARCHAR, nullable=False)

    #初期化する
    def __init__(self, name=None,room_number=None,hash=None):
        self.name = name
        self.room_number = room_number
        self.hash = hash

#productテーブル
class product(UserMixin, Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id  = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(Text, nullable=False)
    body  = Column(Text, nullable=False)
    picture_path  = Column(Text, nullable=False)
    date = Column(Text, default=datetime.now(), nullable=False)

    #初期化する
    def __init__(self, user_id=None,title=None,body=None,picture_path=None,date=None):
        self.user_id = user_id
        self.title = title
        self.body =  body
        self.picture_path =  picture_path
        self.date =  date
