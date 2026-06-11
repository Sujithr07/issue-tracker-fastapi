from fastapi import FastAPI  
from app.routes.issues import router as issues_router

app= FastAPI()

app.include_router(issues_router)



# items= [
#     {"id":1, "name":"item one"},
#     {"id":2, "name":"item two"},
#     {"id":3, "name":"item three"}
# ]

# @app.get("/health")
# def health_check():
#     return {"status":"ok"}

# @app.get ( "/items" )
# def get_items():
#     return items

# @app.get("/items/{item_id}")
# def get_item(item_id:int):
#     for item in items:
#         if item["id"]== item_id:
#             return item
#     return {"error":"item not found"}

# @app.post("/items")
# def add_item(item:dict):
#     items.append(item)
#     return item

