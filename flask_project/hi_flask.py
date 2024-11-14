from flask import Flask, render_template, request, redirect, url_for
import pyjokes
import script

joke = script.joke()
weight_dict={}
app = Flask(__name__)
 
@app.route('/')
def home():
   return render_template('home_page.html')

@app.route('/html1')
def home_1():
   return render_template('hi_1.html') 

@app.route('/weather')
def weather():
   return render_template('weather.html')

@app.route('/jokes')
def jokes():
   return render_template('display_joke.html',joke = joke)

@app.route('/weight')
def weight():
   return render_template('weight_input.html')

@app.route('/weightvalue', methods=['POST'])
def weight_values():
   weight = request.form['weight']
   return redirect(url_for('display_weight',weight = weight))

@app.route('/displayweight/<weight>')
def display_weight(weight):
    weight_dict = script.calculate_weight_on_planets(weight)
    return render_template('display_weight.html', mercury=weight_dict.get('Mercury',''),venus = weight_dict.get('Venus',''),mars=weight_dict.get('Mars',''),
                           jupiter=weight_dict.get('Jupiter',''),saturn=weight_dict.get('Saturn',''),uranus=weight_dict.get('Uranus',''),
                           neptune=weight_dict.get('Neptune',''),pluto=weight_dict.get('Pluto',''))

@app.route('/submit', methods=['POST'])
def submit():
   value1 = request.form['value1']
   entered_time, current_time = script.time(value1)
   return redirect(url_for('display',current_time = current_time,entered_time=entered_time))

@app.route('/weatherupdate',methods=["POST"])
def weather_update():
   weather_value = request.form['weather_value']
   return redirect('https://wttr.in/{}'.format(weather_value))

@app.route('/display/<current_time>/<entered_time>')
def display(current_time,entered_time):
    return render_template('display_time.html', current_time=current_time,entered_time = entered_time)

if __name__ == '__main__':
   app.run()


