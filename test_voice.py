import asyncio
import edge_tts

async def speak(text):
    communicate = edge_tts.Communicate(
        text,
        "en-US-JennyNeural"
    )

    await communicate.save("voice.mp3")

asyncio.run(speak("Hello Sanjeev"))