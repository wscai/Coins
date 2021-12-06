from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
import random
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'l4sn8y194aaaacccc'
Bootstrap(app)
app.debug = True
gua_8 = {
    '000': '',
    '001': '',
    '010': '',
    '011': '',
    '100': '',
    '101': '',
    '110': '',
    '111': ''
}

class TossingForm(FlaskForm):
    choices = ['Head', 'Tail']
    coin1 = SelectField(label='coin1', id='coin1', choices=choices, default=choices[0])
    coin2 = SelectField(label='coin2', id='coin2', choices=choices, default=choices[0])
    coin3 = SelectField(label='coin3', id='coin3', choices=choices, default=choices[0])
    submit = SubmitField("Next")

def result_analyzer(outcome):
    gua = ''
    don = ''
    for i in range(len(outcome)//3):
        yang_count = outcome[i*3:i*3+3].count('1')
        if yang_count==1:
            gua+='1'
            don+='0'
        elif yang_count==2:
            gua+='0'
            don+='0'
        elif yang_count == 3:
            gua+='1'
            don+='1'
        else:
            gua+='0'
            don+='1'



@app.route('/')
def start():  # put application's code here
    return render_template(r'index.html')


@app.route('/toss_coin/<outcome>', methods=['GET', 'POST'])
def toss_coin(outcome):
    form = TossingForm()
    roundNum = outcome[0]
    if form.validate_on_submit():
        if form.coin1.data == 'Head':
            outcome+='1'
        else:
            outcome+='0'
        if form.coin2.data == 'Head':
            outcome+='1'
        else:
            outcome+='0'
        if form.coin3.data == 'Head':
            outcome+='1'
        else:
            outcome+='0'
        roundNum = str(int(roundNum)+1)
        outcome=roundNum+outcome[1:]
        if int(roundNum)>=7:
            return redirect(f'/result/{outcome}')
        return redirect(f'/toss_coin/{outcome}')
    return render_template(r'toss_coin.html',form=form,roundNum=roundNum)

@app.route('/result/<outcome>')
def result(outcome):
    print(outcome)
    return render_template(r'result.html',outcome=outcome)

@app.route('/about')
def about():
    return render_template(r'about.html')

if __name__ == '__main__':
    app.run()
