import streamlit as st

# Function to generate the HTML template
def generate_html(questions):
    html_template = """
    <div class="custom-quiz-container">
        <div class="container">
            <!-- Middle 50% - MCQ Questions -->
            <div class="panel middle-panel">
                <h3>MCQ Test</h3>
                <div id="quiz">
    """

    for i, question in enumerate(questions, start=1):
        html_template += f"""
                    <!-- Question {i} -->
                    <div class="question">
                        <p>{i}. {question['question']}</p>
                        <label><input type="radio" name="q{i}" value="a"> {question['options'][0]}</label>
                        <label><input type="radio" name="q{i}" value="b"> {question['options'][1]}</label>
                        <label><input type="radio" name="q{i}" value="c"> {question['options'][2]}</label>
                        <label><input type="radio" name="q{i}" value="d"> {question['options'][3]}</label>
                        <button onclick="checkAnswer('q{i}', '{question['correct']}', '{question['explanation']}')">Submit</button>
                        <p class="feedback" id="feedback-q{i}"></p>
                    </div>
        """

    html_template += """
                </div>
                <div id="score" style="margin-top: 20px; font-weight: bold; color: #1a1a1a;"></div>
            </div>

            <!-- Left 25% - Combined Concepts and Courses -->
            <div class="panel left-panel">
                <h3>Concepts</h3>
                <ul class="concepts-list">
                    <li><a href="https://www.codegrammer.com">Operating Systems</a></li>
                    <li><a href="https://www.codegrammer.com">DBMS</a></li>
                    <li><a href="https://www.codegrammer.com">Computer Networks</a></li>
                    <li><a href="https://www.codegrammer.com">Data Structures</a></li>
                    <li><a href="https://www.codegrammer.com">Algorithms</a></li>
                    <li><a href="https://www.codegrammer.com">Software Engineering</a></li>
                    <li><a href="https://www.codegrammer.com">Machine Learning</a></li>
                    <li><a href="https://www.codegrammer.com">Cloud Computing</a></li>
                </ul>

                <h3>Courses</h3>
                <ul class="courses-list">
                    <li><a href="https://www.codegrammer.com">Java</a></li>
                    <li><a href="https://www.codegrammer.com">Python</a></li>
                    <li><a href="https://www.codegrammer.com">SQL</a></li>
                    <li><a href="https://www.codegrammer.com">C</a></li>
                    <li><a href="https://www.codegrammer.com">C++</a></li>
                    <li><a href="https://www.codegrammer.com">Data Analytics</a></li>
                    <li><a href="https://www.codegrammer.com">Power BI</a></li>
                    <li><a href="https://www.codegrammer.com">Data Science</a></li>
                </ul>
            </div>
        </div>
    </div>

    <style>
        /* Scoped styles inside .custom-quiz-container to prevent affecting other elements */
        .custom-quiz-container {
            font-family: 'Poppins', sans-serif;
        }

        .custom-quiz-container .container {
            display: flex;
            flex-wrap: wrap;
            max-width: 1200px;
            margin: 20px auto;
            background: #ffffff;
            border-radius: 15px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.1);
        }

        .custom-quiz-container .panel {
            padding: 20px;
            border-radius: 10px;
            box-sizing: border-box;
        }

        .custom-quiz-container .left-panel {
            width: 25%;
            background: #1a1a1a;
            color: #ffffff;
            margin-right: 1%;
        }

        .custom-quiz-container .middle-panel {
            width: 74%;
        }

        .custom-quiz-container h3 {
            font-size: 20px;
            font-weight: 700;
            color: #d4af37;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .custom-quiz-container ul {
            list-style: none;
            padding: 0;
        }

        .custom-quiz-container ul li {
            margin: 12px 0;
        }

        .custom-quiz-container ul li a {
            color: #ffffff;
            text-decoration: none; /* Remove underline */
            font-size: 16px;
            font-weight: 500;
            padding: 10px 15px;
            border-radius: 8px;
            transition: all 0.3s ease;
            display: block; /* Make the entire area clickable */
        }

        .custom-quiz-container ul li a:hover {
            background: rgba(255, 255, 255, 0.1); /* Light hover effect */
        }

        .custom-quiz-container .question {
            margin-bottom: 20px;
        }

        .custom-quiz-container .question p {
            font-size: 16px;
            font-weight: 500;
            color: #1a1a1a;
        }

        .custom-quiz-container .question label {
            display: block;
            margin: 8px 0;
            font-size: 14px;
            color: #333;
        }

        .custom-quiz-container .question input[type="radio"] {
            margin-right: 10px;
        }

        .custom-quiz-container .question button {
            background: #d4af37;
            color: #1a1a1a;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.3s ease;
            margin-top: 10px;
        }

        .custom-quiz-container .question button:hover {
            background: #c0a037;
        }

        .custom-quiz-container .feedback {
            font-size: 14px;
            color: #1a1a1a;
            margin-top: 8px;
        }

        /* Mobile Layout */
        @media (max-width: 768px) {
            .custom-quiz-container .container {
                flex-direction: column;
            }

            .custom-quiz-container .left-panel,
            .custom-quiz-container .middle-panel {
                width: 100%;
                margin: 10px 0;
            }

            /* Reorder panels for mobile */
            .custom-quiz-container .middle-panel {
                order: 1; /* MCQ Test appears first */
            }

            .custom-quiz-container .left-panel {
                order: 2; /* Concepts and Courses appear at the bottom */
            }
        }
    </style>

    <script>
        let totalScore = 0;

        function checkAnswer(questionId, correctAnswer, explanation) {
            const selected = document.querySelector(`.custom-quiz-container input[name="${questionId}"]:checked`);
            const feedback = document.getElementById(`feedback-${questionId}`);

            if (selected && selected.value === correctAnswer) {
                feedback.innerHTML = `Correct! <br><small>${explanation}</small>`;
                feedback.style.color = "green";
                totalScore += 1;
            } else {
                feedback.innerHTML = `Incorrect. Correct answer: ${correctAnswer} <br><small>${explanation}</small>`;
                feedback.style.color = "red";
            }

            document.getElementById('score').textContent = `Total Score: ${totalScore}/6`;
        }
    </script>
    """
    return html_template

# Streamlit app
def main():
    st.title("Quiz Generator")

    # Initialize session state to store questions and form data
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {
            "question": "",
            "option_a": "",
            "option_b": "",
            "option_c": "",
            "option_d": "",
            "correct_option": "a",
            "explanation": ""
        }

    # Progress bar
    progress = len(st.session_state.questions) / 6
    st.progress(progress)

    # Display current question number
    question_num = len(st.session_state.questions) + 1
    st.subheader(f"Please enter Question {question_num}")

    # Input form for questions
    with st.form("question_form"):
        question = st.text_input("Question", value=st.session_state.form_data["question"])
        option_a = st.text_input("Option A", value=st.session_state.form_data["option_a"])
        option_b = st.text_input("Option B", value=st.session_state.form_data["option_b"])
        option_c = st.text_input("Option C", value=st.session_state.form_data["option_c"])
        option_d = st.text_input("Option D", value=st.session_state.form_data["option_d"])
        correct_option = st.selectbox("Correct Option", ["a", "b", "c", "d"], index=["a", "b", "c", "d"].index(st.session_state.form_data["correct_option"]))
        explanation = st.text_area("Explanation", value=st.session_state.form_data["explanation"])

        submitted = st.form_submit_button("Add Question")
        if submitted:
            if len(st.session_state.questions) < 6:
                st.session_state.questions.append({
                    "question": question,
                    "options": [option_a, option_b, option_c, option_d],
                    "correct": correct_option,
                    "explanation": explanation
                })
                st.success(f"Question {question_num} added!")
                # Celebration effect
                st.balloons()  # You can also use st.snow() for a snow effect
                # Reset form data
                st.session_state.form_data = {
                    "question": "",
                    "option_a": "",
                    "option_b": "",
                    "option_c": "",
                    "option_d": "",
                    "correct_option": "a",
                    "explanation": ""
                }
                # Rerun the app to refresh the form
                st.experimental_rerun()
            else:
                st.error("You can only add 6 questions.")

    # Display the HTML code and provide a download button
    if st.session_state.questions and len(st.session_state.questions) == 6:
        st.subheader("Generated HTML Code")
        html_code = generate_html(st.session_state.questions)
        st.code(html_code, language="html")

        # Download button for the HTML code
        st.download_button(
            label="Download HTML as .txt",
            data=html_code,
            file_name="quiz_template.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()