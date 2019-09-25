# from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
import nexmo
import json
# from keys.json import NEXMO_API_KEY_P, NEXMO_API_SECRET_P, NEXMO_NUMBER_P
 
# from .util import env_var, extract_error
 
# Load environment variables from a .env file:
# load_dotenv('.env')

# loading json file
parsed_json = json.loads(open('keys.json', 'r').read())

# Load in configuration from environment variables:
NEXMO_API_KEY = parsed_json['NEXMO_API_KEY_P']
NEXMO_API_SECRET = parsed_json['NEXMO_API_SECRET_P']
NEXMO_NUMBER = parsed_json['NEXMO_NUMBER_P']
 
# Create a new Nexmo Client object:
nexmo_client = nexmo.Client(
    key=NEXMO_API_KEY,
    secret=NEXMO_API_SECRET
)
 
# Initialize Flask:
app = Flask(__name__)
app.config['SECRET_KEY'] = 'FLASK_SECRET_KEY'

@app.route('/')
def index():
    """ A view that renders the Send SMS form. """
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """ A POST endpoint that sends an SMS. """
 
    # Extract the form values:
    to_number = request.form['to_number']
    message = request.form['message']
 
    # Send the SMS message:
    result = nexmo_client.send_message({
        'from': NEXMO_NUMBER,
        'to': to_number,
        'text': message,
    })
 
    flash('sms sent')
    # Redirect the user back to the form:
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)