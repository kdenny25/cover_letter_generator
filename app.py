from flask import Flask, request, render_template, url_for, redirect, flash
import os
from scripts.gpt_prompt import gen_text, obtainText
from werkzeug.utils import secure_filename

base_dir = '.'
app = Flask(__name__,
            static_folder=os.path.join(base_dir, 'static'),
            template_folder=os.path.join(base_dir, 'templates'),)


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    if request.method == 'GET':
        form_fill = {'your_name': '',
                     'hiring_name': '',
                     'resume': '',
                     'job_listing': ''}

        return render_template('index.html', results='', form_fill=form_fill)
    else:
        your_name = request.form.get('yourName')
        hiring_name = request.form.get('hiringName')
        resume = request.form.get('resume')
        job_listing = request.form.get('jobListing')
        resume_file = request.files.get("resumeFile", None)

        file_path = ''
        if resume_file.filename != '':
            filename = secure_filename(resume_file.filename)
            resume_file.save(filename)
            resume_contents = obtainText(filename)
            print('contents extracted successfully.')

        results = gen_text(resume_contents, job_listing, your_name, hiring_name)
        form_fill = {'your_name': your_name,
                     'hiring_name': hiring_name,
                     'resume': resume_contents,
                     'job_listing': job_listing,
                     'resume_file': resume_file}

        return render_template('index.html', results=results, form_fill=form_fill)



if __name__ == '__main__':
    app.run()
