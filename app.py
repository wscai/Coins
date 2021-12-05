from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'l4sn8y194aaaacccc'
Bootstrap(app)
app.debug = True


class TossingForm(FlaskForm):
    coin1 = SelectField(label='coin1',choices=['Head', 'Tail'])
    coin2 = SelectField(label='coin2',choices=['Head', 'Tail'])
    coin3 = SelectField(label='coin3',choices=['Head', 'Tail'])
    submit = SubmitField("Next")


@app.route('/')
def start():  # put application's code here
    return render_template(r'index.html')


@app.route('/toss_coin/<outcome>', methods=['GET', 'POST'])
def toss_coin(outcome):
    form = TossingForm()
    if form.validate_on_submit():
        print(form.coin1.data,form.coin2.data,form.coin3.data)
        outcome+='1'
        return redirect(f'/toss_coin/{outcome}')
    return render_template(r'toss_coin.html',form=form)



if __name__ == '__main__':
    app.run()
