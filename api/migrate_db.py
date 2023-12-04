from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from api.models.task import Base
from api.models.file import Base
from api.models.appering import Base
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 環境変数を .env から読み込む。
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

#(Rf): https://docs.sqlalchemy.org/en/14/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.asyncpg
#URL: "mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/demo?charset=utf8"
#HOST 名はサーバーのアドレス (Rf): https://www.nishi2002.com/4123.html#:~:text=%E3%83%9B%E3%82%B9%E3%83%88%E5%90%8D%E3%81%A8%E3%81%AF%E3%80%81%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9,%E3%81%AE%E3%81%8C%E4%B8%80%E8%88%AC%E7%9A%84%E3%81%A7%E3%81%99%E3%80%82
DB_USER = os.environ.get("DB_USER", "root")
DB_PASS = os.environ.get("DB_PASS", "")
DB_URL = (
f"postgresql://{DB_USER}:{DB_PASS}@localhost:5432/test_api_db"
)
engine = create_engine(DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_database()
