from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql+psycopg2://postgres:my_secret_password@localhost:5432/bases2")

meta = MetaData()

conn = engine.connect()
