import streamlit as st
import time
import pandas as pd
import random
from datetime import datetime

# ---- ACCESS CODES ---- #
access_codes = {
    "Adah": "255877",
    "Ruth": "779311",
    "Esther": "85996170",
    "Martha": "368421",
    "Electa": "147258"
}

# ---- HEROINE QUESTIONS ---- #
question_bank = {
    "Adah": [...],  # Full 15 questions for Adah
    "Ruth": [...],  # Full 15 questions for Ruth
    "Esther": [...],  # Full 15 questions for Esther
    "Martha": [...],  # Full 15 questions for Martha
    "Electa": [...]   # Full 15 questions for Electa
}

# ---- INITIAL STATE ---- #
for key, default in {
    'name': "",
    'heroine': "Adah",
    'quiz_started': False,
    'current_q': 0,
    'score': 0,
    'completed': False,
    'user_answers': [],
    'start_time': None,
    'shuffled_questions': None
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# ---- CONFIG ---- #
st.set_page_config(page_title="OES Five Heroines Proficiency Exam", layout="centered")

# ---- HEADER / LOGO ---- #
st.image("Images/banner.png", use_column_width=True)

st.title("⭐ Order of the Eastern Star - Five Heroines Quiz ⭐")
st.image("Images/star_symbol.png", width=300)

# ---- START FORM ---- #
if not st.session_state.quiz_started:
    with st.form("start_form"):
        st.sidebar.image("Images/phoenix_logo.png", use_column_width=True)

        st.session_state.name = st.text_input("Enter your name:")
        st.session_state.heroine = st.selectbox("Select Heroines Point:", list(question_bank.keys()))
        access_code = st.text_input("Enter access code for selected heroine:")
        start_clicked = st.form_submit_button("Start Quiz")

        if start_clicked and st.session_state.name:
            correct_code = access_codes.get(st.session_state.heroine)
            if access_code == correct_code:
                st.session_state.quiz_started = True
                st.session_state.start_time = time.time()
                st.session_state.shuffled_questions = {
                    heroine: random.sample(questions, len(questions)) for heroine, questions in question_bank.items()
                }
                st.success(f"Welcome {st.session_state.name}, let's begin the {st.session_state.heroine} quiz.")
                st.rerun()
            else:
                st.error("Invalid access code. Please try again.")

# ---- QUIZ LOOP ---- #
elif not st.session_state.completed:
    q_list = st.session_state.shuffled_questions[st.session_state.heroine]
    q_idx = st.session_state.current_q
    question_set = q_list[q_idx]

    st.progress(q_idx / len(q_list))
    st.subheader(f"Question {q_idx + 1} of {len(q_list)}")
    st.write(question_set['question'])

    selected = st.radio("Choose one:", list(question_set['options'].values()), index=None, key=f"q_{q_idx}")

    time_limit = 45
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(0, time_limit - elapsed)
    st.info(f"⏱️ Time remaining: {remaining} seconds")

    if remaining == 0:
        st.warning("Time's up! Moving to the next question...")
        selected = None

    if st.button("Submit Answer"):
        correct_letter = question_set['answer']
        correct_text = question_set['options'][correct_letter]
        is_correct = selected == correct_text

        explanation_text = question_set.get('explanation', "")

        st.session_state.user_answers.append({
            "question": question_set['question'],
            "selected": selected or "(No answer)",
            "correct": correct_text,
            "result": "✅ Correct" if is_correct else "❌ Incorrect",
            "explanation": explanation_text
        })

        if is_correct:
            st.session_state.score += 1

        st.session_state.current_q += 1
        st.session_state.start_time = time.time()

        if st.session_state.current_q >= len(q_list):
            st.session_state.completed = True

        st.rerun()

# ---- QUIZ COMPLETE ---- #
if st.session_state.completed:
    total = len(st.session_state.shuffled_questions[st.session_state.heroine])
    st.success(f"{st.session_state.name}, you scored {st.session_state.score} out of {total}.")

    if st.session_state.score == total:
        st.balloons()
        st.info("Perfect knowledge!")
    elif st.session_state.score >= total // 2:
        st.info("Well done, keep studying!")
    else:
        st.warning("Keep studying, you will master it!")

    score_data = {
        "Name": st.session_state.name,
        "Heroine": st.session_state.heroine,
        "Score": st.session_state.score,
        "Total": total,
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    df = pd.DataFrame([score_data])
    df.to_csv("oes_scores.csv", mode='a', index=False, header=not pd.io.common.file_exists("oes_scores.csv"))
    st.success("Your score has been saved.")

    st.markdown("### 🔍 Review Your Answers")
    for idx, ans in enumerate(st.session_state.user_answers):
        st.write(f"**Q{idx+1}:** {ans['question']}")
        st.write(f"- Your answer: {ans['selected']}")
        st.write(f"- Correct answer: {ans['correct']}")
        st.write(f"- Result: {ans['result']}")
        if ans['explanation']:
            st.info(f"📘 Explanation: {ans['explanation']}")
        st.markdown("---")

    if st.button("Restart Quiz"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
