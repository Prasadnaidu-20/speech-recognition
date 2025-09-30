# Speech Recognition Project

A Python-based audio processing toolkit for extracting audio from videos, detecting speech timestamps, and segmenting audio files.

## Features

- **Audio Extraction**: Extract audio from video files (MP4, AVI, etc.)
- **Speech Detection**: Detect speech timestamps in audio files
- **Audio Segmentation**: Split audio into segments based on detected speech timestamps
- **Silence Trimming**: Remove silence from audio segments for cleaner output

## Project Structure

```
speech_recognition/
├── input/                  # Input files (videos, audio)
│   ├── sample-10s.mp4
│   ├── sample-30s.mp4
│   ├── video-test.mp4
│   └── test-audio.wav
├── output/                 # Output files
│   ├── extracted_audio.wav # Extracted audio from video
│   └── segments/          # Audio segments
│       ├── segment_01.wav
│       ├── segment_02.wav
│       └── ...
├── main.py                # Main entry point
├── extract_audio.py       # Audio extraction from video
├── detect_speech_timestamps.py # Speech detection
├── segment_audio.py       # Audio segmentation
├── segments.json          # Speech timestamps data
└── requirements.txt       # Python dependencies
```

## Installation

1. **Clone or download the project**
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment**:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

- **pydub**: Audio processing and manipulation
- **moviepy**: Video processing and audio extraction
- **numpy**: Numerical operations
- **Pillow**: Image processing (required by moviepy)
- **tqdm**: Progress bars
- **python-dotenv**: Environment variable management

## Usage

### 1. Extract Audio from Video

```bash
python extract_audio.py
```

This will extract audio from video files in the `input/` folder and save as `output/extracted_audio.wav`.

### 2. Detect Speech Timestamps

```bash
python detect_speech_timestamps.py
```

This analyzes the extracted audio and creates `segments.json` with speech timestamps.

### 3. Segment Audio

```bash
python segment_audio.py
```

This splits the audio into segments based on the detected timestamps and saves them in `output/segments/`.


Runs the complete workflow: extract → detect → segment.

## Configuration

### Audio Extraction (`extract_audio.py`)
- Input video files are processed from the `input/` directory
- Output audio is saved as `output/extracted_audio.wav`

### Speech Detection (`detect_speech_timestamps.py`)
- Uses silence detection to identify speech segments
- Configurable silence threshold and minimum segment length
- Outputs timestamps in `segments.json`

### Audio Segmentation (`segment_audio.py`)
- Splits audio based on detected timestamps
- Automatically trims silence from segments
- Configurable silence detection parameters:
  - `SILENCE_THRESH`: Silence threshold in dBFS (default: -40)
  - `MIN_SILENCE_LEN`: Minimum silence length in ms (default: 100)

## File Formats

- **Input**: MP4, AVI, MOV, WAV, MP3, etc.
- **Output**: WAV format for best quality
- **Timestamps**: JSON format with start/end times in seconds

## Example Output

### segments.json
```json
[
  {"start": 0.5, "end": 3.2},
  {"start": 4.1, "end": 7.8},
  {"start": 9.0, "end": 12.5}
]
```

### Generated Segments
- `segment_01.wav` (0.5s - 3.2s)
- `segment_02.wav` (4.1s - 7.8s)
- `segment_03.wav` (9.0s - 12.5s)

## Troubleshooting

### Common Issues

1. **FFmpeg not found**: Install FFmpeg and add to PATH
2. **Audio codec issues**: Ensure input files are in supported formats
3. **Memory issues**: For large files, consider processing in chunks
4. **Silence detection**: Adjust `SILENCE_THRESH` and `MIN_SILENCE_LEN` parameters

### Performance Tips

- Use WAV format for processing (no compression)
- For large files, consider splitting into smaller chunks
- Adjust silence detection parameters based on your audio quality

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Feel free to use and modify as needed.

## Support

For issues or questions, please check the troubleshooting section or create an issue in the repository.
