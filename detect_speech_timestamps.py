import json
import os
from pydub import AudioSegment, silence

# -------------------------
# CONFIG
# -------------------------
input_audio = "output/extracted_audio.wav"
output_json = "segments.json"
min_silence_len = 500   # 1 sec silence
silence_thresh_offset = 14
# -------------------------

print("🔍 Detecting speech timestamps...")

# Load audio
audio = AudioSegment.from_file(input_audio, format="wav")

# Calculate silence threshold
silence_thresh = audio.dBFS - silence_thresh_offset

# Detect non-silent ranges
nonsilent_ranges = silence.detect_nonsilent(
    audio,
    min_silence_len=min_silence_len,
    silence_thresh=silence_thresh,
    seek_step=1
)

# Save to JSON
segments = [{"start": start / 1000, "end": end / 1000} for start, end in nonsilent_ranges]
with open(output_json, "w") as f:
    json.dump(segments, f, indent=2)

print(f"✅ Saved timestamps to {output_json}")
