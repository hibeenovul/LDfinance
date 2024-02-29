# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv
# import os

# load_dotenv()
# PASSWORD = os.getenv("DB_PASSWORD")
# USERNAME = os.getenv("DB_USERNAME")
# HOSTNAME = os.getenv("DB_HOST")
# DATABASE = os.getenv("DB_NAME")

# db_connection_string = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DATABASE}?charset=utf8mb4"

# engine = create_engine(db_connection_string, connect_args={
#     "ssl": {
#         "ssl_ca": "/etc/ssl/cert.pem"
#     }
# })

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))
#     print(result.all())