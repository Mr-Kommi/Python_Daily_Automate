import pyttsx3
import PyPDF2
import re
import threading
import asyncio
# using asyncio to run the code when other parts ie pdf is being read continiously
from playsound import playsound

# pdfname = input("Enter the PDF name: ")
pdfname = "SyDeInt Guide.pdf"

pdfreader = PyPDF2.PdfReader(open(pdfname, 'rb'))

# Initialize the text-to-speech engine
speaker = pyttsx3.init()

# Set properties (optional)
speaker.setProperty('rate', 150)  # Speed of speech

txttosave = ''

# Reading PDF to convert to speech
for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', '')
    txttosave += clean_text
    print(clean_text)

# Replace "." with a pause, except in certain cases (e.g., domain names)
txttosave_with_pause = re.sub(r'\.(?![a-zA-Z])', '...', txttosave)

mp3name = pdfname[:-4] if pdfname.lower().endswith(".pdf") else pdfname

# Save the modified text to an MP3 file synchronously
speaker.save_to_file(txttosave_with_pause, mp3name + '.mp3')

# Asynchronously play the audio file using playsound


async def play_audio():
    await asyncio.sleep(1)  # Give some time for the file to be saved
    playsound(mp3name + '.mp3')

# Start a new thread to run text-to-speech asynchronously
thread = threading.Thread(target=lambda: asyncio.run(play_audio()))
thread.start()

# Wait for the thread to finish (timeout set to 60 seconds)
thread.join(timeout=60)

# Stop the text-to-speech engine
speaker.stop()
