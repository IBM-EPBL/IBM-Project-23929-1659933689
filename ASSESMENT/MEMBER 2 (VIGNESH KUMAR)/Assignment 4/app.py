from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feba25506'

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            name = "Shrruthi"
            return redirect(url_for('index', messages=name ))

    return render_template('create.html')


messages = [{'title': 'Sample Message',
            'content': 'This is a sample message'},
          
        ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)