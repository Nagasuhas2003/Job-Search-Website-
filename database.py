from sqlalchemy import create_engine, text # type: ignore
import os
from dotenv import load_dotenv
load_dotenv()
db_connection_string=os.getenv('connection_string')
engine = create_engine(db_connection_string)


