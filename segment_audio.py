import json
import os
from pydub import AudioSegment, silence
import shutil

# Example: delete a folder and recreate it
output_folder = "output/segments"
if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
os.makedirs(output_folder, exist_ok=True)


input_audio = "output/extracted_audio.wav"
segments_file = "segments.json"
output_folder = "output/segments"

# Silence trimming configuration
SILENCE_THRESH = -40  
MIN_SILENCE_LEN = 100 
# -------------------------


def trim_silence(audio_segment, silence_thresh=SILENCE_THRESH, min_silence_len=MIN_SILENCE_LEN):
    # Detect nonsilent parts of audio_segment
    nonsilent_ranges = silence.detect_nonsilent(audio_segment,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh)

    if not nonsilent_ranges:
        return audio_segment  

    start_trim = nonsilent_ranges[0][0]
    end_trim = nonsilent_ranges[-1][1]

    return audio_segment[start_trim:end_trim]


def split_audio(input_audio_path, segments_path, output_dir):
    print("✂️ Splitting audio into segments...")

    os.makedirs(output_dir, exist_ok=True)

    audio = AudioSegment.from_file(input_audio_path, format="wav")

    with open(segments_path, "r") as f:
        segments = json.load(f)

    for i, seg in enumerate(segments, 1):
        # More precise start/end in ms with rounding
        start_ms = round(seg["start"] * 1000)
        end_ms = round(seg["end"] * 1000)

        segment_audio = audio[start_ms:end_ms]

        # Optional: trim silence for more precise clipping
        segment_audio = trim_silence(segment_audio)

        segment_filename = os.path.join(output_dir, f"segment_{i:02d}.wav")
        segment_audio.export(segment_filename, format="wav")
        print(f"Exported {segment_filename}")

    print("✅ Segmentation complete.")


if __name__ == "__main__":
    split_audio(input_audio, segments_file, output_folder)
