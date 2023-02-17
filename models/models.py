from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, VARCHAR
from models.database import Base
from datetime import datetime

#userテーブル
class user(Base):
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

# from models.database import db_session
# from models.models import user
# c1 = user("sosuke","R34","111")
# c2 = user("kinu","301","222")
# c3 = user("sen","305","333")
# db_session.add(c1)
# db_session.add(c2)
# db_session.add(c3)
# db_session.commit()


#productテーブル
class product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id  = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(Text, nullable=False)
    body  = Column(Text, nullable=False)
    picture_path  = Column(Text, nullable=False)
    date = Column(DateTime, default=datetime.now(), nullable=False)

    #初期化する
    def __init__(self, user_id=None,title=None,body=None,picture_path=None,date=None):
        self.user_id = user_id
        self.title = title
        self.body =  body
        self.picture_path =  picture_path
        self.date =  date


# from models.database import db_session
# from models.models import product
# c1 = product("1","フライパン","このフライパンは1年利用しました。テフロン加工は現在も機能しており、焦げ付くことなく利用できます","aaa")
# c2 = product("2","パンツ","このパンツはLサイズで男性用です。気になる方がいましたらご連絡下さい","bbb")
# c3 = product("3","sen","少しギシギシ言うので、壊れやすいかと思います。しかし、汚れなどは一切ございません。捨てることになるので、ぜひ使って頂きたいです。","ccc")
# db_session.add(c1)
# db_session.add(c2)
# db_session.add(c3)
# db_session.commit()
