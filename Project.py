from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from ProjectBot import bot
import asyncio
import cdqa

app = Flask(__name__)
loop = asyncio.get_event_loop()

botadaptersettings = BotFrameworkAdapterSettings("", "")
botadapter = BotFrameworkAdapter(botadaptersettings)

# calling the class created above (create bot instance)
ebot = bot()

@app.route("/api/messages", methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
        jsonmessage = request.json
    else:
        return Response(status=415)

    activity = Activity().deserialize(jsonmessage)

    async def turn_call(turn_context):
        await ebot.turn_on(turn_context)

    task = loop.create_task(botadapter.process_activity(activity, "", turn_call))
    loop.run_until_complete(task)

if __name__ == '__main__':
    app.run('localhost', 3978)