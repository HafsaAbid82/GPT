from openai import OpenAI

client = OpenAI()
with open("Sample_Pashto.mp3", "rb") as f:
    result = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",
        file=f
    )
language_result = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "Detect the language of the following text and return the ISO 639-1 code."},
        {"role": "user", "content": result.text}
    ]
)

detected_language = language_result.choices[0].message.content
print("Detected language:", detected_language)





