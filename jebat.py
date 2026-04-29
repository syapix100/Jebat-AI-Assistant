import speech_recognition as sr
import pyttsx3
import ollama
engine = pyttsx3.init('sapi5')
def speak(text):
    print(f"JEBAT: {text}")
    engine.say(text)
    engine.runAndWait()
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengar...") # Listening
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-US')
        print(f"Tuan: {query}")
        return query.lower()
    except:
        return ""            
if __name__ == "__main__":
    speak("Sistem Jebat sedia berkhidmat.")

    while True:
        print("\n--- Jebat Sedia Berkhidmat ---")
        print("Sila bercakap atau tekan 'Enter' untuk menaip...")

        command = ""


        try:
            command = listen()
        except Exception as e:

            pass


        if not command:
            command = input("Tuan, sila taip di sini: ").lower()


        if "keluar" in command:
            speak("Hamba pergi dulu, tuan")
            break

        if command:
            respon = ollama.chat(
                model='llama3.1',
                messages=[
                    {'role': 'system', 'content': 'You are Jebat, a brave and loyal Malay warrior assistant.'},
                    {'role': 'user', 'content': command},
                ]
            )

            hasil = respon['message']['content']
            print(f"Jebat: {hasil}")
            speak(hasil)



    