
import vosk
import wave
import os
import json
import pickle
from config import ACTION_PROB_THRESHOLD

current_path = os.path.dirname(os.path.abspath(__file__))
model_folder = os.path.join(current_path, 'vosk_small')
# speech_files_folder = os.path.join(current_path, 'speech_files')
phrases_model_file = os.path.join(current_path, 'models', 'phrases_model.pkl')


def load_asr_model():
    return vosk.Model(model_folder)


def load_phrase_model():
    with open(phrases_model_file, 'rb') as handle:
        vectorizer, clf = pickle.load(handle)
    return vectorizer, clf


def recognize(data, vectorizer, clf, ACTION_PROB_THRESHOLD_CONST=ACTION_PROB_THRESHOLD):
    text_vector = vectorizer.transform([data]).toarray()[0]
    probs = clf.predict_proba([text_vector])
    max_prob = max(probs[0])

    if max_prob >= ACTION_PROB_THRESHOLD_CONST:
        answer = clf.classes_[probs[0].argmax()]
        return answer.split(' ', 1)

    return None, None


def transcribe(filename, asr_model, speech_files_folder_const=""):
    wf = wave.open(os.path.join(speech_files_folder_const, filename), "rb")
    rec = vosk.KaldiRecognizer(asr_model, wf.getframerate())
    data = wf.readframes(wf.getnframes())
    rec.AcceptWaveform(data)
    return json.loads(rec.Result())["text"]

def transcribe_chunked(filename, asr_model, chunk_size=4000):
    """Обработка аудиофайла с помощью Vosk по частям (чанками)"""
    wf = wave.open(os.path.join("speech_files_folder", filename), "rb")
    
    if not wf.getnchannels() == 1:
        raise ValueError("Аудиофайл должен быть монофоническим.")
    
    rec = vosk.KaldiRecognizer(asr_model, wf.getframerate())
    rec.SetWords(True)  # Опционально, чтобы включить распознавание слов
    transcript = []
    
    while True:
        data = wf.readframes(chunk_size)
        if len(data) == 0:
            break
        # Передаём текущий чанк в модель
        if rec.AcceptWaveform(data):
            # Если модель распознала полное предложение
            result = json.loads(rec.Result())
            transcript.append(result["text"])
        else:
            # Промежуточные результаты (частичные)
            partial_result = json.loads(rec.PartialResult())
            if "partial" in partial_result and partial_result["partial"]:
                print(f"Промежуточный результат: {partial_result['partial']}")
    
    # Финальный результат после обработки всех чанков
    final_result = json.loads(rec.FinalResult())
    transcript.append(final_result["text"])

    return " ".join(transcript)

def transcribe_old(filename):
    model = vosk.Model(model_folder)

    wf = wave.open(os.path.join("speech_files_folder", filename), "rb")

    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    data = wf.readframes(wf.getnframes())
    rec.AcceptWaveform(data)

    return json.loads(rec.Result())["text"]
    

def recognize_old(data):
    vectorizer, clf = load_phrase_model()

    text_vector = vectorizer.transform([data]).toarray()[0]

    probs = clf.predict_proba([text_vector])
    max_prob = max(probs[0])

    if max_prob >= ACTION_PROB_THRESHOLD:
        answer = clf.classes_[probs[0].argmax()]

        return answer.split(' ', 1)

    return None, None
