# importing libraries 

import streamlit as st
from streamlit_option_menu import option_menu
import pyttsx3
import numpy as np
import PyPDF2
import easyocr
import cv2
import speech_recognition as sr
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from streamlit_lottie import st_lottie
import requests
from docx2pdf import convert
import os
from googletrans import Translator
from transformers import BartForConditionalGeneration, BartTokenizer
import io
import os
from docx2pdf import convert
import tempfile


# Setup the pyttsx 

text_to_speech = pyttsx3.init()
text_to_speech.setProperty('rate', 150)

# Seting the page config

st.set_page_config(page_title='TexifyHub', page_icon=':computer:', layout='wide')


# Loading animations
def loader_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Using local css file

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



# Loading assets
front = loader_url('https://lottie.host/d064e392-6d0c-47cb-982b-2e1f04e425d3/WTLJwY86J6.json')
img2text = loader_url('https://lottie.host/d3c41d1f-1bd4-43d6-9f08-4390423ed20d/TpQvMUUs3s.json')
speech2text = loader_url('https://lottie.host/6430f182-0b1f-4d39-81e1-210d067cee99/q0hVJX3YAl.json')
text2speech = loader_url('https://lottie.host/6430f182-0b1f-4d39-81e1-210d067cee99/q0hVJX3YAl.json')
translate = loader_url('https://lottie.host/f7848a35-87e5-4d9e-9e8e-35e7cfe31128/zsnhukFivT.json')
pdf = loader_url('https://lottie.host/72e20e71-19ee-4b06-8fac-401d3dea4ffd/vf4zkfgKTO.json')
conversion = loader_url('https://lottie.host/208d2aa9-7a4b-4d87-bfdb-06b626d8558f/MzY59pQJwg.json')
summarization = loader_url('https://lottie.host/200129df-5e0a-47a5-98e2-fc85c7c20a04/E5TL8nDQC2.json')
contact = loader_url('https://lottie.host/737c309f-89fd-4072-b4ad-d3336083ef83/JeVVdpAQnS.json')


# Home page sidebar

with st.sidebar:
    with st.container():
        l,m,r = st.columns((5,5,5))
        with l:
            st.empty()
        with m:
            st.empty()
        with r:
            st.empty()

    choose = option_menu(
                        "OCR Project", 
                        ["Home","Image to Text", "Speech to text", "Text to speech","Translation", "Pdf extracter", "Document Conversion", "Text Summarization", "Feedback"],
                         icons=[],
                         menu_icon="mortarboard", 
                         default_index=0,
                         orientation =  'vertical',
                         
    )


# Page navigations    

if choose == 'Home':
    
    # Add a beautiful header inside the container
    st.markdown("<h1 style='text-align: center;'>This is TexifyHub</h1>", unsafe_allow_html=True)

    st.write('---')

    # Add comments
    st.markdown("""
                Welcome to TexifyHub - Your All-in-One Operations Hub
        TexifyHub is your one-stop solution for a wide range of daily operations. 
        With an array of powerful features, our platform empowers you to streamline various tasks efficiently and effectively. 
        Explore our versatile tools and discover how TexifyHub can elevate your day-to-day operations.       
                """, unsafe_allow_html=True)

    # Display a lottie animation using st.lottie() inside the container
    st.lottie(front, height=450, key='coding')


# Go to image to text page        

elif choose == "Image to Text":
    
    st.title("Image Text Reader")

    st.write('----')

    st.markdown("""
                
        Utilizing Optical Character Recognition (OCR) technology, 
        we seamlessly transform images into editable text, providing a professional and efficient solution 
        for your data extraction needs.
        """)

    st_lottie(img2text, height=200, key='image2text')

    image_file = st.file_uploader('Upload the image file', type=['jpg', 'png', 'jpeg'])

    if st.button("Extract to text") and image_file is not None:

        if image_file is not None:
            # Convert the uploaded image to a NumPy array
            image = np.array(bytearray(image_file.read()), dtype=np.uint8)
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)

            # Initialize the EasyOCR reader
            reader = easyocr.Reader(['en'])

            # Read text from the image
            results = reader.readtext(image)

            # Extract and display the detected text
            detected_text = ""
            for (box, text, prob) in results:
                detected_text += text + " "
            
            st.write("Detected Text:")
            st.write(detected_text)


# Go to the Speech to text page

elif choose == 'Speech to text':

    st.title("Image Text Reader")

    st.write('---')

    st.markdown("""
        
    Through the utilization of cutting-edge speech recognition technology,
    we facilitate the conversion of audio files into text format, offering a sophisticated and 
    accurate solution for transcribing spoken content.
        """)

    st_lottie(speech2text, height=200, key='speech2text')

    file_name = st.file_uploader('Upload the file', type=['mp3', 'wav'])

    r = sr.Recognizer()
    
    if file_name is not None:
        r = sr.Recognizer()

        audio = None
        with st.spinner('Transcribing...'):
            audio = sr.AudioFile(io.BytesIO(file_name.read()))

        if audio:
            with audio as source:
                try:
                    audio_data = r.record(source)
                    text = r.recognize_google(audio_data)
                    st.write("Transcription: ", text)
                except sr.UnknownValueError:
                    st.write("Google Speech Recognition could not understand the audio")
                except sr.RequestError as e:
                    st.write(f"Could not request results from Google Speech Recognition service; {e}")
    else:
        st.write("Please upload an audio file.")


# Go to text to speech page        

elif choose == 'Text to speech':

    st.title("Text to speech convertor")

    st.write('---')

    st.markdown("""
        
    Leveraging the power of pyttsx3, our platform effortlessly transmutes text into speech. 
    Simply input your text, and experience the instant echo as your words come to life in spoken form.
        """)

    st_lottie(text2speech, height=200, key='text2speech')

    text_to_speech = pyttsx3.init()

    user_input = st.text_input('Enter the text')

    if st.button('Convert to speech') and user_input is not None:

        text = user_input

        voices = text_to_speech.getProperty('voices')
        text_to_speech.setProperty('voice', voices[1].id)

        text_to_speech.say(text)

    #text_to_speech.save_to_file(text, 'test.mp3')

        text_to_speech.runAndWait()



# Go to pdf extractor page

elif choose == 'Pdf extracter':

    st.title('Pdf extractor')

    st.write('---')

    st.markdown("""
        
    This section serves as your PDF-to-Text converter, ingeniously extracting textual content from your PDF files, 
    and then seamlessly transforming it into audible speech, offering you a convenient and accessible way to 
    engage with your documents.
        """)

    st_lottie(pdf, height=250, key='pdf')

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if st.button("Extract to text") and uploaded_file is not None:
        pdf_reader = PyPDF2.PdfFileReader(uploaded_file)

        text = ''

        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            text += page.extractText()

        if text:
            st.write("Extracted text from the PDF:")
            st.write(text)

            # Set the voice (you can customize this)
            voices = text_to_speech.getProperty('voices')
            text_to_speech.setProperty('voice', voices[1].id)

            # Convert text to speech
            text_to_speech.say(text)

            # Save to a file (optional)
            # text_to_speech.save_to_file(text, 'test1.mp3')

            # Wait for the speech to finish
            # text_to_speech.runAndWait()

# Go to document conversion page

elif choose == "Document Conversion":

    st.title('Document Conversion')

    st.write('--')

    st.markdown("""
        
    In this dedicated section, you have the power to effortlessly convert your documents into PDF files, 
    ensuring compatibility, security, and professional presentation for your content.
        """)    

    st_lottie(conversion, height=250, key='Conversion')

    st.header('This is used to convert the document to PDF')

    file = st.file_uploader('Upload your DOCX file', type=['docx'])

    if st.button("Convert") and file is not None:
        input_docx = file
        input_docx_data = io.BytesIO(input_docx.read())  # Read the file as bytes

        # Create a temporary file for the DOCX data
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_docx:
            temp_docx.write(input_docx_data.getvalue())

        output_pdf = temp_docx.name.replace('.docx', '.pdf')  # Generate the PDF file name

        try:
            # Convert DOCX to PDF using python-docx2pdf
            convert(temp_docx.name, output_pdf)

            st.success(f'Conversion successful. Download the PDF [here]({output_pdf}).')

            # Display the PDF download link
            with open(output_pdf, 'rb') as pdf_file:
                pdf_bytes = pdf_file.read()
            st.download_button(
                label="Download PDF",
                data=pdf_bytes,
                key="download_pdf",
                on_click=None,  # You can specify a custom callback here
                args=(output_pdf,),
                file_name=output_pdf
            )
        except Exception as e:
            st.error(f"Error converting the file: {str(e)}")
# Go to translation page

elif choose == "Translation":

    st.title('Translation')

    st.write('--')

    st.markdown("""
        
    Utilizing Google Translate, our platform provides seamless and accurate translations from English into various native languages, 
    bridging linguistic gaps and fostering effective communication.
        """)

    st_lottie(translate, height=200, key='Translation')

    trans = st.text_input('Enter the input to translate')

    # Language Selection
    target_lang = st.selectbox("Select target language", ["English (en)", "Tamil (ta)", "French (fr)", "Spanish (es)", "German (de)", "Japanese (ja)"])  # You can add more languages

    # Translator
    translator = Translator()

    words = trans

    if st.button("Translate"):
        translation = translator.translate(words, dest=target_lang)
        st.write("Original Text:", trans)
        st.write("Translation:", translation.text)

# Go to text summarization page

elif choose == "Text Summarization": 
    st.title("Text Summarization")

    st.write('---')

    st.markdown("""
        This dedicated section employs advanced LLM (Large Language Model) technology to succinctly summarize provided text, 
        delivering concise yet informative summaries tailored to your specific needs.
        """)

    st_lottie(summarization, height=250, key='summarization')
    # Text Input
    text = st.text_area("Enter the text you want to summarize:")

    if st.button("Summarize"):
        model_name = "facebook/bart-large-cnn"
        tokenizer = BartTokenizer.from_pretrained(model_name)
        model = BartForConditionalGeneration.from_pretrained(model_name)
        inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = model.generate(**inputs)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        st.subheader("Summary:")
        st.write(summary)

elif choose == "Feedback":
        st.header(":postbox: Give your valuable feedback!!")

        st.write('##')
        left_col, right_col = st.columns((3,2))

        with left_col:
            contact_form = """
            <form action="https://formsubmit.co/archanas210603@gmail.com" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here"></textarea>
                <button type="submit">Send</button>
            </form>

            """
            local_css("Styles/styles.css")

            st.markdown(contact_form, unsafe_allow_html=True)

        with right_col:
            st_lottie(contact, height=250, key='contact')

        


        

   