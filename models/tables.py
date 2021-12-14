from datetime import date, time
from enum import unique
from sqlalchemy import Table, Column, engine, Sequence
from sqlalchemy import Table, Column, ForeignKey, text, true
from sqlalchemy.sql.expression import table
from sqlalchemy.sql.sqltypes import TEXT, Date, Integer, String, DateTime, Text, Time
from config.db import meta, engine

USER_ID_SEQ = Sequence('user_id_seq')
users = Table("users", meta, 
                Column("user_id", Integer, USER_ID_SEQ, primary_key=true, server_default=USER_ID_SEQ.next_value(), unique=true),
                Column("username", String(50), primary_key=true, unique=true),
                Column("sex", String(50)),
                Column("age", Integer),
                Column("description", Text),
                Column("instagram", String(255)),
                Column("facebook", String(255)),
                Column("twitter", String(255)),
                Column("linkedin", String(255)))

user_acc = Table("usrconf", meta,
                Column("email", String(255), primary_key=true, unique=true),
                Column("password", String(255)),
                Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=true))

events = Table("events", meta, 
                Column("event_id", Integer, USER_ID_SEQ, primary_key=true, server_default=USER_ID_SEQ.next_value(), unique=true),
                Column("title", String(50), primary_key=true, unique=true),
                Column("date", Date, nullable=False),
                Column("hour", Time, nullable=False),
                Column("description", Text, nullable=False),
                Column("location", String(255), nullable=False),
                Column("host", Integer, nullable=False))
            
assistance = Table("assistance", meta,
                Column("user_id", Integer, ForeignKey("users.user_id"), primary_key=true),
                Column("event_id", Integer, ForeignKey("events.event_id"), primary_key=true),
                Column("status", Integer))


meta.create_all(engine)