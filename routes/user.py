from fastapi import APIRouter, HTTPException
from py2neo.data import Node
from sqlalchemy.sql.expression import delete, join, select
from sqlalchemy import exc
from config.db import conn, meta
from models.tables import users, user_acc, events
from schemas.datatypes import CreateUser, Login, Response, UserID
# Los codigos de retorno que se necesiten especificar
from starlette.status import HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
# Pare neo4j:
from config.neo_db import graph
from py2neo import Node, Relationship



user = APIRouter()

@user.get("/users", tags=["Usuarios"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users/notfollowing/{my_id}", tags=["Usuarios"])
def get_users_not_followed_by(my_id: int):
    res = conn.execute(users.select()).fetchall()
    tx = graph.begin()
    u1 = graph.nodes.match("User", user_id=my_id).first()
    ans=[]
    if(u1 != None):
        for idx,r in enumerate(res):
            a = graph.evaluate("MATCH (n {user_id:"+str(my_id)+"})-[r:following]->(c {user_id:"+str(r.user_id)+"}) RETURN n")
            if(a == None and my_id!=r.user_id):
                ans.append(r)
    tx.commit()
    return ans

@user.get("/users/followedBy/{my_id}", tags=["Usuarios"])
def get_users_followed_by(my_id: int):
    res = conn.execute(users.select()).fetchall()
    tx = graph.begin()
    u1 = graph.nodes.match("User", user_id=my_id).first()
    ans = []
    if(u1 != None):
        for idx,r in enumerate(res):
            a = graph.evaluate("MATCH (n {user_id:"+str(my_id)+"})-[r:following]->(c {user_id:"+str(r.user_id)+"}) RETURN c")
            print(a)
            if(a != None):
                ans.append(r)
    tx.commit()
    return ans

@user.post("/createuser", response_model=Response, tags=["Usuarios"])
def post_user(user: CreateUser):
    new_user = {
        "username": user.username,
        "sex": user.sex,
        "age": user.age,
        "description": user.description,
        "instagram": user.instagram,
        "facebook": user.facebook,
        "twitter": user.twitter,
        "linkedin": user.linkedin
    }
    # Insertamos el user en la tabla user.
    try : 
        conn.execute(users.insert().values(new_user))
    except exc.IntegrityError:
        return {"status":-1, "detail":{"error":"El usuario ya existe"}}
    # Pedimos el user_id creado.
    select_st = select([users.c.user_id]).select_from(users).where(users.c.username == user.username)
    res = conn.execute(select_st).fetchone()
    # Insertamos la configuracion del usuario
    new_config = {
        "email" : user.email,
        "password" : user.password,
        "user_id" : res.user_id
    }
    try: 
        conn.execute(user_acc.insert().values(new_config))
    except exc.IntegrityError:
        # En este punto el usuario ya fue creado, como hubo un error al insertar
        # hacemos un rollback de la base de datos borrando el usuario.
        conn.execute(delete(users).where(users.c.user_id==res.user_id))
        return {"status":-1, "detail":{"error":"El email ya esta en uso"}}
    # Creamos el nodo del usuario en Neo4J, como el user es unico entonces en neo tambien
    # va a ser unico...
    tx = graph.begin()
    UsrToAdd = Node("User", username=user.username, user_id=res.user_id)
    tx.create(UsrToAdd)
    tx.commit()
    return {"status":1, "detail":new_config}

@user.post("/login", response_model=Response, tags=["Usuarios"])
def post_login(user: Login):
    
    select_st = select([user_acc.c.user_id,user_acc.c.password]).select_from(user_acc).where(user_acc.c.email == user.email)
    res = conn.execute(select_st).fetchone()
    print(res)
    if res == None:
        return {"status":-1, "detail":{}}
    usr = {
        "email" : user.email,
        "password" : user.password,
        "user_id" : res.user_id
    }
    if res.password == user.password:
        return {"status":1, "detail":usr}
    else:
        return {"status":-1, "detail":{}} #invalid credentials
        
@user.get("/getuserid/{username}", response_model=UserID, tags=["Usuarios"])
def get_userid(username: str):
    select_st = select([users.c.user_id]).select_from(users).where(users.c.username == username)
    res = conn.execute(select_st).fetchone()
    return res

@user.get("/user/{my_id}/follow/{to_follow_id}", tags=["Usuarios"])
def follow(my_id: int, to_follow_id: int):
    tx = graph.begin()
    u1 = graph.nodes.match("User", user_id=my_id).first()
    if(u1 != None):
        u2 = graph.nodes.match("User", user_id=to_follow_id).first()
        if(u2 != None):
            rel = Relationship(u1, "following", u2)
            tx.create(rel)
            tx.commit()
            return 1
    return HTTPException(status_code=404, detail="User ID not found.")

@user.get("/user/{my_id}/unfollow/{to_follow_id}", tags=["Usuarios"])
def follow(my_id: int, to_follow_id: int):
    tx = graph.begin()
    u1 = graph.nodes.match("User", user_id=my_id).first()
    u2 = graph.nodes.match("User", user_id=to_follow_id).first()
    if(u1 == None or u2 == None):
        return HTTPException(status_code=404, detail="User ID not found.")
    else:
        r = graph.evaluate("MATCH (n {user_id:"+str(my_id)+"})-[r:following]->(c {user_id:"+str(to_follow_id)+"}) RETURN r")
        if(r != None):
            tx.separate(r)
            tx.commit()
            return 1
        else:
            return HTTPException(status_code=404, detail="There was no relationship.")

@user.get("/user/{my_id}/followedBy/{to_follow_id}", response_model=Response, tags=["Usuarios"])
def followed_by (my_id: int, to_follow_id: int):
    tx = graph.begin()
    u1 = graph.nodes.match("User", user_id=my_id).first()
    if(u1 == None):
        return {"status":-1, "detail":{}}
    else:
        r = graph.evaluate("MATCH (n {user_id:"+str(to_follow_id)+"})-[r:following]->(c {user_id:"+str(my_id)+"}) RETURN n")
        print("Te muestro r:")
        print(r)
        tx.commit()
        if(r == None):
            return {"status":-1, "detail":{}}
        return {"status":1, "detail":{}}

@user.get("/countFollowers/{user_id}", response_model=Response, tags=["Usuarios"])
def get_count_followers (user_id: int):
    r = graph.evaluate("MATCH (n)-[:following]->(x {user_id:"+str(user_id)+"}) RETURN count(n)")
    print(r)
    return {"status":1, "detail":{"qty": r}}

@user.get("/countFollowing/{user_id}", response_model=Response, tags=["Usuarios"])
def get_count_following (user_id: int):
    r = graph.evaluate("MATCH (n {user_id:"+str(user_id)+"})-[:following]->(x) RETURN count(x)")
    print(r)
    return {"status":1, "detail":{"qty": r}}

@user.get("/user/{user_id}/events", response_model=Response, tags=["Usuarios"])
def get_to_attend_events (user_id: int):
    assist=meta.tables['assistance']
    join_res = events.join(assist, assist.c.event_id == events.c.event_id)
    select_st=select([events.c.event_id,events.c.title,events.c.date,events.c.hour,events.c.description,events.c.location,events.c.host]).select_from(join_res).where(assist.c.user_id == user_id)
    res =conn.execute(select_st).fetchall()
    return {"status":1, "detail":{"res":res}}

@user.get("/user/{my_id}/friendsOfFriends/{user_id}", response_model=Response, tags=["Usuarios"])
def friends_of_friends(my_id: int, user_id: int):
    tx = graph.begin()
    res = graph.run("match (a { user_id:"+str(my_id)+"})-[r1:following]->(e) match (e)-[r2:following]->(b { user_id:"+str(user_id)+"}) return e.user_id as user_id, e.username as username").data()
    tx.commit()
    return {"status":1, "detail":{"res":res}}


# Create node:
# TheMatrix = Node("Movie", title='The Matrix', released=1999, tagline='Welcome to the Real World')
# LillyW = Node("Person", name='Lilly Wachowski', born=1967)

# Create relationships:
# LillyWTheMatrix = Relationship(LillyW, "DIRECTED", TheMatrix)

# Commitear cambios:
# tx = graph.begin()
# tx.create(TheMatrix)
# tx.create(LillyW)
# tx.create(LillyWTheMatrix)
# tx.commit()