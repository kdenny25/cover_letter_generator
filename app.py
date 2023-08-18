from flask import Flask, request, render_template, url_for, redirect, flash
import os
from scripts.gpt_prompt import gen_text

base_dir = '.'
app = Flask(__name__,
            static_folder=os.path.join(base_dir, 'static'),
            template_folder=os.path.join(base_dir, 'templates'),)


@app.route('/', methods=['GET', 'POST'])
def home():  # put application's code here
    if request.method == 'GET':
        return render_template('index.html', results='')
    else:
        role = request.form.get('role')
        job_listing = request.form.get('jobListing')

        results = gen_text('', job_listing)

        return render_template('index.html', results=results)



if __name__ == '__main__':
    app.run()
