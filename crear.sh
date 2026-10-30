#!/usr/bin/env bash
# Uso: ./crear.sh <id>   (necesita guiones/<id>.json y audio/<id>.mp3)
set -euo pipefail
cd "$(dirname "$0")"
id="$1"; w="work/$id"
mkdir -p "$w" videos
cp "guiones/$id.json" "$w/script.json"
python3 engine/tts_andrew.py "$w" "audio/$id.mp3"
TPL=slp.html node engine/render.js "$w" >/dev/null
python3 engine/mix.py "$w" >/dev/null
cp "$w/final.mp4" "videos/$id.mp4"
node engine/cover.js "guiones/$id.json" "videos/$id.jpg"
ffmpeg -v error -y -i "videos/$id.mp4" -vf "fps=1/3,scale=180:-1,tile=6x2" -frames:v 1 "$w/check.png"
echo "ok videos/$id.mp4 ($(ffprobe -v error -show_entries format=duration -of csv=p=0 videos/$id.mp4)s) — revisa $w/check.png"
