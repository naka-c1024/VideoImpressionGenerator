# AI感想レポート作成ツール

このツールは、動画の内容から自動的に感想レポートを生成するプログラムです。

## Feature

動画を入力からffmpegで音声を抜き出し、whisperで音声からテキストに変換した後、その内容をGPTモデルに与えて感想文を生成します。

## Requirement

- openai  0.27.7
- ffmpeg-python  0.2.0
- pyyaml  6.0
- python-dotenv  1.0.0

## Usage

### 1. Git clone

```
git clone https://github.com/naka-c1024/VideoImpressionGenerator.git
```

### 2. APIキーの設定

`.env` ファイルを作成し、OpenAIのAPIキーを設定します。

```
echo "OPENAI_API_KEY='XXX'" > .env
```

### 3. Yamlファイルの設定

```yaml
MOV_FILE_PATH: /path/to/your/video
AUDIO_FILE_PATH: /path/to/audio/file
PROMPT_BASE: <Write a GPT prompt>
GPT_MODEL: gpt-3.5-turbo
OUTPUT_FILE_PATH: /path/to/output/file
```

### 4. 環境設定

#### Dockerを使用する場合

```bash
docker build -t video_impression_generator .
docker run -v $(pwd):/app -p 8080:8080 -it video_impression_generator bash
```

#### Dockerを使用せずローカル環境で実行したい場合

```
sudo apt install ffmpeg
pip install -r requirements.txt
```

### 5. ツールの実行

```bash
python main.py
```

## Note

遊びで作ったものなので参考程度に留めておき、本物のレポートはAIではなく自分で考えてください!
