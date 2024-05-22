import sqlalchemy as db
from sqlalchemy import text
import pandas as pd

def connect_world_cup():
    engine = db.create_engine("mysql://root:root@172.16.5.4:3310/world_cup")
    conn = engine.connect()

    return conn

def connect_dw_world_cup():
    engine = db.create_engine("mysql://root:root@172.16.5.4:3310/dw_world_cup")
    conn = engine.connect()

    return conn