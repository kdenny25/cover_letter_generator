import openai
from settings import OPENAI_API_KEY
from docx import Document
import os

openai.api_key = OPENAI_API_KEY

def gen_text(resume, job_listing):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content": "You are a entry level data scientist creating cover letters."},
            {"role":"user", "content": f"Summarize the companies objectives, qualifications and requirements from the following job listing and pull the most relevent information to be addressed in a cover letter. {job_listing}"}],
        temperature=0,
        max_tokens=2048
    )
    result = response['choices'][0]['message']['content']

    return result

def obtainText(docFileName):
    document = Document(docFileName)
    finalText = []
    for line in document.paragraphs:
        finalText.append(line.text)

    # read table data
    if len(document.tables) > 0:
        for table in document.tables:
            for row in table.rows:
                for cell in row.cells:
                    finalText.append(cell.text)

    return '\n'.join(finalText)

def saveText(textData):
    document = Document()


# resume = obtainText(r'C:\Users\kdenn\PycharmProjects\cover_letter_generator\static\Kevin Resume_072223.docx')
# job_listing = obtainText(r'C:\Users\kdenn\PycharmProjects\cover_letter_generator\static\job_listing.docx')
#
# #print(response['choices'][0]['text'])
# print(gen_text(resume, job_listing))