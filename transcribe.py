import whisper

input = "input.mp3"
model = whisper.load_model("large")
result = model.transcribe(input, verbose=True, language="ja")
f = open(input + ".txt", "w")
f.write(result)
f.close()
