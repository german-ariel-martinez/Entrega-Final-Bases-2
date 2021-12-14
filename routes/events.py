from sys import prefix
from fastapi import APIRouter
from sqlalchemy import exc
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.functions import user
from config.db import conn, meta
from models.tables import events,assistance,users
from schemas.datatypes import Assists, CreateEvent, Event, Response
# Los codigos de retorno que se necesiten especificar
from starlette.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED



event = APIRouter()

@event.get("/events/{my_id}", response_model=Response, tags=["Eventos"])
def get_events(my_id:int):
    select_st = select([events.c.event_id,events.c.title,events.c.date,events.c.hour,events.c.description,events.c.location,events.c.host]).select_from(events).where(events.c.event_id.notin_(select([events.c.event_id]).select_from(events).where(events.c.host==my_id)))
    res = conn.execute(select_st).fetchall()
    return {"status":1, "detail":{"res":res}}

@event.get("/myevents/{my_id}", response_model=list[Event], tags=["Eventos"])
def get_my_events(my_id:int):
    return conn.execute(events.select().where(events.c.host==my_id)).fetchall()

@event.post("/createvent", response_model=Response, tags=["Eventos"])
def post_user(event: CreateEvent):
    new_event = {
        "title": event.title,
        "date": event.date,
        "hour": event.hour,
        "description": event.description,
        "location": event.location,
        "host": event.host
    }
    # Insertamos el user en la tabla user.
    try:
        conn.execute(events.insert().values(new_event))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El evento ya existe"}}
    print(new_event["title"])
    select_st = select([events.c.event_id]).select_from(events).where(events.c.title == new_event["title"])
    res = conn.execute(select_st).fetchone()
    print(res)
    new_event["event_id"]=res
    return {"status":1, "detail":new_event}

@event.post("/event/{event_id}/user/{user_id}/attend", response_model=Assists, tags=["Eventos"])
def post_ass_a(ass: Assists):
    new_ass = {
        "user_id": ass.user_id,
        "event_id": ass.event_id,
        "status": ass.status
    }
    # Insertamos el user en la tabla user.
    conn.execute(assistance.insert().values(new_ass))
    return new_ass

@event.get("/event/{event_id}/user/{user_id}/decline", response_model=Response, tags=["Eventos"])
def post_ass_d(event_id: int, user_id:int):
    select_st =  assistance.delete().where(assistance.c.event_id==event_id and assistance.c.user_id==user_id)
    conn.execute(select_st)
    return {"status":1,"detail":{}}

@event.delete("/event/{event_id}/user/{user_id}/delete",response_model=Response, tags=["Eventos"])
def delete_event(event_id: int, user_id: int):
    conn.execute(assistance.delete().where(assistance.c.event_id==event_id))
    conn.execute(events.delete().where(events.c.event_id==event_id and events.c.host==user_id))
    return {"status":1, "detail":{}}

@event.get("/event/{event_id}/user/{my_id}/participants", response_model=Response, tags=["Eventos"])
def get_participants(event_id: int, my_id: int):
    assist=meta.tables['assistance']
    join_res = users.join(assist, assist.c.user_id == users.c.user_id)
    select_st=select([users.c.user_id,users.c.username,users.c.description,users.c.age,users.c.sex, users.c.instagram,users.c.facebook,users.c.twitter,users.c.linkedin]).select_from(join_res).where(assist.c.event_id == event_id, users.c.user_id != my_id)
    res =conn.execute(select_st).fetchall()
    return {"status":1, "detail":{"res":res}}






    