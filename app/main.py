# app/main.py

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)

# Configure PostgreSQL database connection
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/postgres'  # Update with your credentials
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define the InterviewData model
class InterviewData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(100))
    questions = db.Column(db.Text)
    answers = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    score = db.Column(db.Float)  # Add a column for score


# Function to load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Route to redirect to animation page
@app.route('/')
def animation_redirect():
    return redirect('/animation')


# Serve the animation page
@app.route('/animation')
def animation():
    lottie_url_hello = "https://lottie.host/61d09ce5-62a9-4c09-990a-18b4fa4ab4f9/HN0RNWoZg7.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    return render_template('animation.html', lottie_hello=lottie_hello)


# Serve the homepage
@app.route('/home')
def home():
    return render_template('home.html')


# Serve the role selection page
@app.route('/roles')
def roles():
    return render_template('role_selection.html')


# Serve the interview process and handle both role and answer mode
@app.route('/interview')
def interview():
    role = request.args.get('role')
    answer_mode = request.args.get('answer_mode', 'text')  # Default to text if no mode selected
    # Redirect to Streamlit or other interview handling logic
    streamlit_url = f"http://localhost:8501/?role={role}&answer_mode={answer_mode}"
    return redirect(streamlit_url)


# API endpoint to submit interview data
@app.route('/submit_interview', methods=['POST'])
def submit_interview():
    role = request.form['role']
    questions = request.form['questions']
    answers = request.form['answers']
    score = request.form['score']  # Assume score is sent from Streamlit

    # Create a new entry in the database
    new_entry = InterviewData(
        role=role,
        questions=questions,
        answers=answers,
        score=score
    )

    # Add and commit to the database
    db.session.add(new_entry)
    db.session.commit()

    return redirect('/home')  # Redirect to the homepage after submission


# Initialize the database (run this once to create the tables)
with app.app_context():
    db.create_all()


# Route to choose the answer method (text or voice) after role selection
@app.route('/choose_answer_method', methods=['GET'])
def choose_answer_method():
    role = request.args.get('role')
    return render_template('answer_choice.html', role=role)


# Route to start the interview based on the selected answer method
@app.route('/start_interview', methods=['GET'])
def start_interview():
    answer_mode = request.args.get('answer_mode', 'text')  # Default to text
    role = request.args.get('role')
    # Redirect to interview with the selected role and answer method
    return redirect(f"/interview?role={role}&answer_mode={answer_mode}")


if __name__ == '__main__':
    app.run(debug=True)
