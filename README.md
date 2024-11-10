# SkillMitra - Interview-Preparation with AI

Skill Mitra is an AI-powered application designed to help users prepare for interviews by offering real-time feedback, dynamic question generation, and a personalized, interactive experience. Using advanced NLP models, Skill Mitra provides a comprehensive interview practice environment that caters to various roles and experience levels.

## Features

- **Role Selection**: Choose from multiple roles, such as Data Scientist, Product Manager, Business Analyst, and more.
- **Dynamic Question Generation**: AI-driven questions tailored to the selected role.
- **Real-Time Feedback**: Immediate evaluation and constructive feedback on responses.
- **Answer Options**: Flexibility to answer via text or voice for a real interview-like experience.
- **Progress Tracking**: Track progress over time, allowing for focused improvement.
- **User Authentication**: Secure login system to access personalized interview data.
- **Data Storage**: All user interview data is securely stored in a PostgreSQL database for easy retrieval and analysis.

## Project Structure

```
project_root/
│
├── app/
│   ├── templates/
│   │   ├── home.html
│   │   ├── role_selection.html
│   │   └── answer_choice.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css
│   │   │   └── role_selection.css
│   │   └── images/
│   │       └── logo.png
│   └── main.py
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── secrets.toml
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/HeenaGagwani/skillmitra---Interview-Preparation.git
   cd skill-mitra
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**
   Ensure you have a PostgreSQL database set up with the parameters stored in `secrets.toml` (or update these directly in your codebase if needed).

4. **Run the Application**
   Start the main Flask and Streamlit applications:
   ```bash
   python app/main.py
   streamlit run streamlit_app.py
   ```

## Usage

1. Open the application in your web browser by navigating to the provided localhost URL.
2. Select the desired role and choose a preferred method (typing or speaking) for answering interview questions.
3. Receive real-time feedback and track your progress.

## Future Scope

- Expand to support various experience levels for more personalized interviews.
- Introduce AI avatars or AR/VR features for immersive interview preparation.
- Incorporate Reinforcement Learning and other approaches for an enhanced, interactive experience.
- Comparative studies on different machine learning models and NLP techniques for question generation and feedback.

## Limitations

- Limited scalability for large-scale simultaneous user sessions.
- Absence of a GPU limits real-time voice processing capabilities.
- Feedback, while accurate, may not capture the full nuance of user responses.

## Contributing

Contributions are welcome! Please follow the guidelines in `CONTRIBUTING.md` for submitting issues or pull requests.


Skill Mitra empowers users to refine their skills and build confidence through tailored, dynamic interview preparation.
