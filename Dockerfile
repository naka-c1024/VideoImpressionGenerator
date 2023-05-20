# Use the official Python image.
FROM python:3.9

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# aliasとtailwindcssのためのnpm設定
RUN apt update \
    && apt install -y ffmpeg \
    && echo 'alias pm="python main.py"' >> ~/.bashrc
