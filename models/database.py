from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#plama.dbという名前で、database.pyのある場所（os.path.dirname(__file__)）に、絶対パス（os.path.abspath）で、plama.dbを保存する
databese_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'plama.db')

#sqliteを使って(engin)、database_fileに保存されているplama.dbを使う、またechoで実行の際にsqliteを出す（echo=True)
engine = create_engine('sqlite:///' + databese_file,echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

#DBの初期化をする関数
def init_db():
    #modelsディレクトリのmodelsをインポート
    import models.models
    Base.metadata.create_all(bind=engine)