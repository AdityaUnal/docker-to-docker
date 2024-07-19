from sanic import Sanic
from sanic.exceptions import Unauthorized
from sanic.response import json
import datetime

app = Sanic("time_container")

API_TOKEN = "Bearer X-Sanic-token"


@app.middleware('request')
async def authorization_middleware(request):
    if request.path == '/time':
        token = request.headers.get("Authorization")
        if not token or token != API_TOKEN:
            raise Unauthorized("Invalid token")


@app.route("/time")
async def time(request):
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S")
    return json({"current_time": formatted_time})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
# docker run -d -p 8080:8080 --name know_time know_time
