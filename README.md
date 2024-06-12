# 🎵 Soundom 🎵

## Description

Soundom is a Python-based utility designed to process `.wav` audio files. It segments the audio into specified durations, converts frequencies to MIDI notes, and calculates average decibels. Additionally, the tool generates random numbers based on the frequency analysis of the audio segments.

## Features

- 🎶 **Select Random Audio File**: Choose a random `.wav` file from a specified directory.
- 📊 **Audio Analysis**: Analyze the audio file by segmenting it into specified durations, converting frequencies to MIDI notes, and calculating decibel levels.
- 🎲 **Random Number Generation**: Generate a random number based on the frequency analysis of the audio segments.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/FlenderrAX/Soundom.git
    cd Soundom
    ```

2. **Create a Virtual Environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Place Your Audio Files**:
   Place your `.wav` files in the `records` directory.

2. **Run the Script**:
    ```sh
    python main.py
    ```

3. **Example Output**:
    ```
    Selected File: ../records\sound.wav
    [+] Loading file...
    [+] Successfully loaded the audio file
    [+] Converted segment duration
    [+] Arrays initialized
    [+] Successfully calculated the number of segments
    [+] Converting frequencies to MIDI notes and storing it :
    33.33%...
    66.67%...
    100.00%...
    [+] Done!
    Final Random Number : 1910
    ```

## Code Explanation

### `select_random_wav_file(directory_path)`

This function scans the specified directory for `.wav` files and selects one at random. It returns the full path to the selected file.

### `analyze_audio(file_path, segment_duration_ms)`

This function loads the selected audio file, segments it based on the specified duration, and performs a Short-Time Fourier Transform (STFT) on each segment. It converts frequencies to MIDI notes and calculates the mean decibels for each segment.

### `randomInt(frequencies)`

This function generates a random number based on the frequency analysis. It selects random MIDI notes from the analyzed frequencies and computes a unique number from them.

## Contributing

Contributions are welcome! Please fork this repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to open an issue.