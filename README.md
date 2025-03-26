# Audio/Video Processor

This project processes audio and video files to extract audio, preprocess it, and transcribe it into text. It leverages FastAPI for a web interface.

## Features

- Extracts audio from video files.
- Resamples audio to 16000 Hz.
- Trims or pads audio to 30 seconds.
- Boosts the audio volume if necessary.
- Transcribes audio to text and saves it in a text file.
- Provides a RESTful API for easy access and integration.

## Requirements

- Python 3.7 or later
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jayahariv/audio.git
   cd audio
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv   # Create a virtual environment
   source venv/bin/activate  # Activate the virtual environment (Linux/Mac)
   # or
   venv\Scripts\activate  # Activate the virtual environment (Windows)
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**:
   Start the FastAPI application using:
   ```bash
   # usage sample
   python main.py

   // copy the audio/video files in the root directory of the project. 
   mkdir sample
   cd sample 
   cp path/to/mp4 sample/

   python main.py -f sample/filename.mp4 -s artpark -o path/to/transcript.txt
   ```

2. **API Endpoints**:
   Once the server is running, you can access the API documentation at `http://127.0.0.1:8000/docs`.

3. **Process Audio/Video Files**:
   To process an audio or video file, send a POST request to the `/process` endpoint with the file as multipart/form-data.

   **Example using `curl`:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/process" -F "file=@/path/to/your/audio_or_video_file"
   ```

   **Response:**
   The server will respond with a JSON object containing the paths to the processed audio files and the transcription text.

## Directory Structure

```
audio_video_processor/
├── audio_processor.py   # Handles audio preprocessing tasks
├── video_processor.py   # Handles video processing tasks
├── processors           # These are different processors we can use, like Whisper, Google Speech etc.
├── main.py              # Main entry point of the application
├── requirements.txt     # List of dependencies
├── LICENSE              # License
├── .gitignore           # Ignore specific files
├── sample/              # Directory for sample files (create and add files)
└── README.md            # Project documentation
```

## Dependencies

The project uses the following libraries:

- **FastAPI**: For building the web application.
- **Librosa**: For audio processing.
- **MoviePy**: For video processing and audio extraction.
- **SpeechRecognition**: For transcribing audio files.
- **NumPy**: For numerical operations.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature`
3. Make your changes and commit them: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin my-feature`
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the contributors and the open-source community for their valuable libraries and tools.