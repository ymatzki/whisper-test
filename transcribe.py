import whisper

input = "input.mp3"
model = whisper.load_model("large")
result = model.transcribe(input, verbose=True, language="ja")

with open(input + ".txt", "w", encoding="utf-8") as f:
    for segment in result["segments"]:
        f.write(segment["text"] + "\n")
