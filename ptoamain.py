import pyttsx3
import PyPDF2


# pdfname = input("enter the pdf name")
pdfname = "SyDeInt Guide.pdf"

pdfreader = PyPDF2.PdfReader(open(pdfname, 'rb'))

speaker = pyttsx3.init()

txttosave = ''

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', '')
    txttosave += clean_text
    print(clean_text)

mp3name = pdfname[:-4] if pdfname.lower().endswith(".pdf")else pdfname

speaker.save_to_file(clean_text, mp3name+'.mp3')
speaker.runAndWait()

speaker.stop()
