from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite


app = Flask('Flask Blog', template_folder='template')
app.secret_key = ("secret key")


@app.route('/')
@app.route('/posts')
def blogs():
    if type(sqlite.selectData()) == list:
        TYPE = 'list'
    else:
        TYPE = 'noList'
    return render_template('posts.html', posts=sqlite.selectData(), TYPE=TYPE)


@app.route('/post_add', methods=['GET', 'POST'])
def post_add():
    if request.method == 'GET':
        return render_template('post_add.html')
    if request.method == 'POST':
        titleText = request.form['Editbox1']
        contentText = request.form['TextArea1']
        if titleText != '' or contentText != '':
            sqlite.insertDataIn(titleText, contentText)
            flash("Your post added!")
            return redirect(url_for('blogs'))
        else:
            flash("Your post don't added, Please fill all form!")
            return redirect(url_for('post_add'))


app.run(host='localhost', port=8080, debug=True)

