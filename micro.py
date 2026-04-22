import asyncio
import edge_tts
import os

async def generate_audio() -> None:
    os.makedirs("output",exit_ok=True)

    text= "hello boss, jarvis at your service what can i do you ya"

    #communication= edge.tts.communicate(text=text,voice="en-US-AriaNeural")
    communication = edge_tts.communicate(text=text,voice="hi-IN-SwaraNeural")
    await communication.save("output/output_hi.mp3")

    print("Audio generated sucessfully!Boss")


asyncio.run(generate_audio())

    