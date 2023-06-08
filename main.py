import openai
import ffmpeg
from dotenv import load_dotenv
import os
import yaml

load_dotenv()

# APIキーが設定されていることを確認
if not os.environ["OPENAI_API_KEY"]:
    raise RuntimeError("APIキーが設定されていません")

openai.api_key = os.environ["OPENAI_API_KEY"]

# configs.yamlファイルを読み込む
with open("configs.yaml", "r") as f:
    configs = yaml.safe_load(f)

MOV_FILE_PATH = configs["MOV_FILE_PATH"]
AUDIO_FILE_PATH = configs["AUDIO_FILE_PATH"]
PROMPT_BASE = configs["PROMPT_BASE"]
GPT_MODEL = configs["GPT_MODEL"]
OUTPUT_FILE_PATH = configs["OUTPUT_FILE_PATH"]

# === ffmpegで動画ファイルから音声を抽出 ===
#抽出する動画ファイル
stream = ffmpeg.input(MOV_FILE_PATH)

#出力する音声ファイル
stream = ffmpeg.output(stream, AUDIO_FILE_PATH)

#抽出実行
ffmpeg.run(stream)


# === Whisperで文字列データに変換 ===
#動画、オーディオファイルを開く
audio_file = open(AUDIO_FILE_PATH, "rb")

#Whisperで音声から文字お越し
transcript  = openai.Audio.transcribe("whisper-1", audio_file)

# === ChatGPTで要約を作成 ===
#ChatGPTプロンプトを作成
prompt = PROMPT_BASE + transcript.text

#推論を実行
response = openai.ChatCompletion.create(
    model=GPT_MODEL,
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# ファイルに書き込む
with open(OUTPUT_FILE_PATH, "w") as f:
    f.write(response["choices"][0]["message"]["content"])
