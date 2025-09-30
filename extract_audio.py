import subprocess
import os

# -------------------------
# CONFIG
# -------------------------
input_file = "input/test-audio.wav"       # your video file
output_audio = "output/extracted_audio.wav"  # where audio will be saved
# -------------------------

# Ensure input folder exists
os.makedirs("input", exist_ok=True)

# Extract audio using ffmpeg
print("🎥 Extracting audio from video...")
cmd = [
    "ffmpeg",
    "-i", input_file,
    "-vn",                # no video
    "-acodec", "pcm_s16le",
    "-ar", "16000",       # sample rate
    "-ac", "1",           # mono
    output_audio,
    "-y"
]
subprocess.run(cmd, check=True)

print(f"✅ Audio saved to {output_audio}")
