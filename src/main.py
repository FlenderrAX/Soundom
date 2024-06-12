import librosa
import numpy as np
import random
import os

def select_random_wav_file(directory_path):
    files = os.listdir(directory_path)
    wav_files = [file for file in files if file.endswith('.wav')]
    
    if not wav_files:
        raise ValueError("Aucun fichier '.wav' trouvé dans le dossier spécifié.")
    
    selected_file = random.choice(wav_files)
    file_path = os.path.join(directory_path, selected_file)
    
    return file_path

def analyze_audio(file_path, segment_duration_ms):
    print("[+] Loading file...")
    y, sr = librosa.load(file_path, sr=None)
    print("[+] Successfully loaded the audio file")
    
    segment_duration_s = segment_duration_ms / 1000.0
    segment_size = int(sr * segment_duration_s)
    print("[+] Converted segment duration")
    
    frequencies = []
    decibels = []
    print("[+] Arrays initialized")
    
    num_segments = int(np.ceil(len(y) / segment_size))
    print("[+] Successfully calculated the number of segments")
    
    print("[+] Converting frequencies to MIDI notes and storing it :")
    for i in range(1, num_segments + 1):
        start = (i - 1) * segment_size
        end = min(i * segment_size, len(y))
        segment = y[start:end]

        stft_result = librosa.stft(segment)
        magnitude = np.abs(stft_result)
        db = librosa.amplitude_to_db(magnitude)

        fft_frequencies = librosa.fft_frequencies(sr=sr)
        fft_frequencies[fft_frequencies == 0] = np.finfo(float).eps

        midi_notes = [librosa.hz_to_midi(freq) for freq in fft_frequencies]

        frequencies.append(midi_notes)
        decibels.append(db.mean(axis=1))

        percentage = (i / num_segments) * 100
        print(f"{percentage:.2f}%...")
    print("[+] Done!")
    
    return frequencies, decibels

def randomInt(frequences):
    final_freq = [j[random.randint(0, len(j) - 1)] for j in frequences]
    random_freq = final_freq[random.randint(0, len(final_freq) - 1)]
    finalNb = int(str(random_freq**2).split('.')[1][:4]) if '.' in str(random_freq**2) else 0

    return finalNb

directory_path = '../records'

try:
    file_path = select_random_wav_file(directory_path)
    print(f"Selected File: {file_path}")

except ValueError as e:
    print(e)

segment_duration_ms = 1000
frequencies, decibels = analyze_audio(file_path, segment_duration_ms)

print(f"Final Random Number : {randomInt(frequencies)}")