import os
import whisper


def transcribe(file):
    model = whisper.load_model("large")
    return model.transcribe(file, verbose=True, language="ja", fp16=False)


def write_file(file, segments):
    with open(file, "w", encoding="utf-8") as f:
        for segment in segments:
            f.write(segment["text"] + "\n")


if __name__ == '__main__':
    input_dir = 'input'
    output_dir = 'output'

    files = os.listdir(path=input_dir)

    for file in files:
        if not file.endswith('.mp3'):
            continue
        result = transcribe(input_dir + "/" + file)
        write_file(output_dir + "/" + file + ".txt", result["segments"])
