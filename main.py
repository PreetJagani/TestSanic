from sanic import Sanic
from sanic.response import json

app = Sanic("TestApp")


@app.get("/ping")
async def test(request):
    try:
        return json({"status": 200, "res": "Hi from sanic"})
    except ValueError:
        return json({"status": 400, "error": "invalid request"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
