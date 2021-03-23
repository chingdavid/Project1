from botbuilder.core import TurnContext

# when type hi, the response will also return hi
class bot:
    async def turn_on(self, turn_context:TurnContext):
        await turn_context.send_activity(turn_context.activity.text)
