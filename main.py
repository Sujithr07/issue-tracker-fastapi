from fastapi import FastAPI

app= FastAPI()

items= [
    {"id":1, "name":"item one"}
    {"id":2, "name":"item two"}
    {"id":3, "name":"item three"}
]


@app.get ( "/items" )
def get_items():
    return items



@app.get("/health")
def health_check():
    return {"status":"ok"}