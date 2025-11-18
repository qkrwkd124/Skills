from sqlalchemy import create_engine

url = "mysql+pymysql://root:1234@localhost:3306/test"
engine = create_engine(url, echo=True)