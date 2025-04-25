import streamlit as st
import os
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
    "Adah": [
        {"question": "What does Adah's color blue represent?", "options": {"a": "Fidelity", "b": "Courage", "c": "Wisdom", "d": "Peace"}, "answer": "a", "explanation": "Blue symbolizes fidelity and faithfulness."},
        {"question": "Who was Adah's father?", "options": {"a": "Boaz", "b": "Jephthah", "c": "David", "d": "Jesse"}, "answer": "b", "explanation": "Jephthah was Adah’s father."},
        {"question": "What vow involved Adah?", "options": {"a": "To sacrifice enemies", "b": "Offer first to greet him", "c": "Build a temple", "d": "Become a priestess"}, "answer": "b", "explanation": "Jephthah vowed to sacrifice the first to greet him."},
        {"question": "What virtue does Adah teach?", "options": {"a": "Obedience", "b": "Love", "c": "Fidelity", "d": "Charity"}, "answer": "c", "explanation": "Adah teaches fidelity to duty and promise."},
        {"question": "Where is Adah's story found?", "options": {"a": "Judges", "b": "Ruth", "c": "Esther", "d": "Genesis"}, "answer": "a", "explanation": "Her story is in the Book of Judges."},
        {"question": "What emblem represents Adah?", "options": {"a": "Broken column", "b": "Sword and veil", "c": "Crown", "d": "Cup"}, "answer": "b", "explanation": "Sword and veil symbolize Adah’s fidelity."},
        {"question": "What is Adah’s sacrifice?", "options": {"a": "Wealth", "b": "Life for vow", "c": "Crown", "d": "Her home"}, "answer": "b", "explanation": "Adah sacrifices her life for her father's vow."},
        {"question": "What role does Adah fulfill?", "options": {"a": "Martyr", "b": "Judge", "c": "Queen", "d": "Teacher"}, "answer": "a", "explanation": "Adah is viewed as a martyr."},
        {"question": "What quality did Adah show?", "options": {"a": "Pride", "b": "Courage", "c": "Deceit", "d": "Anger"}, "answer": "b", "explanation": "She showed courage in the face of death."},
        {"question": "What lesson is learned from Adah?", "options": {"a": "Value wealth", "b": "Obey blindly", "c": "Honor promises", "d": "Avoid vows"}, "answer": "c", "explanation": "Honor sacred promises."},
        {"question": "Adah’s sword symbolizes what?", "options": {"a": "Attack", "b": "Protection", "c": "Sacrifice", "d": "Power"}, "answer": "c", "explanation": "The sword reminds of sacrifice."},
        {"question": "What does the veil symbolize?", "options": {"a": "Joy", "b": "Submission", "c": "Strength", "d": "Victory"}, "answer": "b", "explanation": "The veil shows humble submission to duty."},
        {"question": "Why did Adah submit?", "options": {"a": "Fear", "b": "Honor to God", "c": "Greed", "d": "Confusion"}, "answer": "b", "explanation": "Out of honor and reverence to God."},
        {"question": "How is Adah honored?", "options": {"a": "Songs", "b": "Star Point", "c": "Ceremonies", "d": "Temples"}, "answer": "b", "explanation": "She is honored as a point of the Star."},
        {"question": "Adah's story teaches loyalty to what?", "options": {"a": "Family only", "b": "Wealth", "c": "Sacred obligations", "d": "Community"}, "answer": "c", "explanation": "Sacred obligations are honored above all."}
    ],
    "Ruth": [
        {"question": "What color is associated with Ruth?", "options": {"a": "Yellow", "b": "Red", "c": "White", "d": "Blue"}, "answer": "a", "explanation": "Yellow for constancy and loyalty."},
        {"question": "What is Ruth’s relationship to Naomi?", "options": {"a": "Sister", "b": "Mother", "c": "Daughter-in-law", "d": "Servant"}, "answer": "c", "explanation": "She was Naomi’s daughter-in-law."},
        {"question": "Where did Ruth glean for food?", "options": {"a": "Temple", "b": "Boaz’s field", "c": "Market", "d": "City square"}, "answer": "b", "explanation": "In Boaz’s fields."},
        {"question": "What is Ruth’s emblem?", "options": {"a": "Broken column", "b": "Sheaf of wheat", "c": "Cup", "d": "Scepter"}, "answer": "b", "explanation": "The sheaf represents Ruth’s loyalty."},
        {"question": "Ruth married who?", "options": {"a": "Elimelech", "b": "David", "c": "Boaz", "d": "Jesse"}, "answer": "c", "explanation": "She married Boaz."},
        {"question": "Ruth’s story shows what virtue?", "options": {"a": "Charity", "b": "Constancy", "c": "Faith", "d": "Hope"}, "answer": "b", "explanation": "Constancy and loyalty are Ruth’s themes."},
        {"question": "What declaration did Ruth make?", "options": {"a": "\"I shall rule\"", "b": "\"Where you go, I will go\"", "c": "\"I will stay here\"", "d": "\"You must leave me\""}, "answer": "b", "explanation": "Famous words of loyalty to Naomi."},
        {"question": "Ruth’s nationality before conversion?", "options": {"a": "Egyptian", "b": "Moabite", "c": "Philistine", "d": "Hebrew"}, "answer": "b", "explanation": "She was a Moabite."},
        {"question": "Who is Ruth's great-grandson?", "options": {"a": "Solomon", "b": "David", "c": "Elijah", "d": "Moses"}, "answer": "b", "explanation": "David, King of Israel."},
        {"question": "Boaz described Ruth as?", "options": {"a": "Bold woman", "b": "Virtuous woman", "c": "Beautiful woman", "d": "Faithful priestess"}, "answer": "b", "explanation": "A virtuous woman."},
        {"question": "Which festival is tied to Ruth's story?", "options": {"a": "Passover", "b": "Sabbath", "c": "Pentecost", "d": "Feast of Weeks"}, "answer": "d", "explanation": "Feast of Weeks relates to harvest and loyalty."},
        {"question": "What does Ruth's sheaf symbolize?", "options": {"a": "Labor", "b": "Charity", "c": "Hope", "d": "Harvest and loyalty"}, "answer": "d", "explanation": "Harvest and loyalty."},
        {"question": "How did Ruth demonstrate loyalty?", "options": {"a": "Fought a battle", "b": "Followed Naomi", "c": "Built a temple", "d": "Saved a king"}, "answer": "b", "explanation": "She followed Naomi without obligation."},
        {"question": "Ruth trusted in which God?", "options": {"a": "Moab’s god", "b": "The God of Israel", "c": "Egyptian gods", "d": "Philistine gods"}, "answer": "b", "explanation": "She embraced the God of Israel."},
        {"question": "Ruth's decision teaches us about?", "options": {"a": "Power", "b": "Wealth", "c": "Constancy and loyalty", "d": "Fear"}, "answer": "c", "explanation": "Constancy and loyalty are key lessons."}
    ],


    # (Esther, Martha, Electa — posting in next chunk so I don't break mid-posting)
    "Esther": [
        {"question": "What color is associated with Esther?", "options": {"a": "White", "b": "Yellow", "c": "Red", "d": "Blue"}, "answer": "a", "explanation": "White symbolizes purity, joy, and light."},
        {"question": "In which book of the Bible is Esther’s story found?", "options": {"a": "Ruth", "b": "Esther", "c": "Kings", "d": "Samuel"}, "answer": "b", "explanation": "Her story is in the Book of Esther."},
        {"question": "What is Esther’s main virtue?", "options": {"a": "Patience", "b": "Justice", "c": "Courage", "d": "Charity"}, "answer": "c", "explanation": "She showed courage facing death for her people."},
        {"question": "Who was Esther’s cousin and protector?", "options": {"a": "Boaz", "b": "Mordecai", "c": "Solomon", "d": "Haman"}, "answer": "b", "explanation": "Mordecai guided and protected Esther."},
        {"question": "Who was Esther’s husband?", "options": {"a": "King Solomon", "b": "King David", "c": "King Ahasuerus", "d": "King Nebuchadnezzar"}, "answer": "c", "explanation": "She married King Ahasuerus (Xerxes)."},
        {"question": "What feast celebrates Esther’s bravery?", "options": {"a": "Passover", "b": "Purim", "c": "Hanukkah", "d": "Pentecost"}, "answer": "b", "explanation": "Purim celebrates Esther’s saving of the Jews."},
        {"question": "What plot did Esther expose?", "options": {"a": "Building a false temple", "b": "Killing the king", "c": "Killing the Jews", "d": "Stealing treasures"}, "answer": "c", "explanation": "She revealed Haman’s plot to kill the Jews."},
        {"question": "What object is associated with Esther?", "options": {"a": "Sheaf", "b": "Crown and scepter", "c": "Sword", "d": "Cup"}, "answer": "b", "explanation": "Crown and scepter symbolize her courage and royal favor."},
        {"question": "How did Esther approach the king?", "options": {"a": "By force", "b": "By invitation", "c": "Uninvited, risking death", "d": "Through a servant"}, "answer": "c", "explanation": "She approached uninvited risking her life."},
        {"question": "What did Esther request of her people before seeing the king?", "options": {"a": "To fight", "b": "To fast and pray", "c": "To give money", "d": "To leave the city"}, "answer": "b", "explanation": "She asked for fasting and prayers."},
        {"question": "What does Esther’s courage teach?", "options": {"a": "Pride", "b": "Caution", "c": "Stand for what’s right despite danger", "d": "Ambition"}, "answer": "c", "explanation": "Stand courageously even when it's dangerous."},
        {"question": "What evil man did Esther oppose?", "options": {"a": "Haman", "b": "Mordecai", "c": "Boaz", "d": "Jesse"}, "answer": "a", "explanation": "She opposed Haman’s plot."},
        {"question": "What feast did Esther invite the king and Haman to?", "options": {"a": "Pentecost", "b": "Her own banquet", "c": "Sabbath feast", "d": "Harvest festival"}, "answer": "b", "explanation": "She invited them to her banquet to reveal the truth."},
        {"question": "What was Esther’s Hebrew name?", "options": {"a": "Hadassah", "b": "Hannah", "c": "Ruth", "d": "Miriam"}, "answer": "a", "explanation": "Her Hebrew name was Hadassah."},
        {"question": "What does Esther symbolize in Eastern Star?", "options": {"a": "Justice", "b": "Purity", "c": "Courage and loyalty", "d": "Victory"}, "answer": "c", "explanation": "She represents courageous loyalty and sacrifice."}
    ],

    "Martha": [
        {"question": "What color represents Martha?", "options": {"a": "Green", "b": "Blue", "c": "White", "d": "Red"}, "answer": "c", "explanation": "White represents purity and hope."},
        {"question": "Martha's story is mainly found in which Gospel?", "options": {"a": "Matthew", "b": "Luke", "c": "John", "d": "Mark"}, "answer": "c", "explanation": "Martha’s story appears in John."},
        {"question": "What is Martha’s main virtue?", "options": {"a": "Hospitality", "b": "Endurance in trial", "c": "Wisdom", "d": "Charity"}, "answer": "b", "explanation": "She teaches endurance during trials."},
        {"question": "Who was Martha’s brother?", "options": {"a": "Solomon", "b": "David", "c": "Lazarus", "d": "Aaron"}, "answer": "c", "explanation": "Lazarus was Martha's brother."},
        {"question": "What miracle involved Martha?", "options": {"a": "Water to wine", "b": "Lazarus raised", "c": "Feeding 5,000", "d": "Walking on water"}, "answer": "b", "explanation": "Jesus raised Lazarus from the dead."},
        {"question": "How is Martha depicted during Lazarus' death?", "options": {"a": "Faithless", "b": "Angry", "c": "Faithful and patient", "d": "Hopeless"}, "answer": "c", "explanation": "She showed endurance and faith."},
        {"question": "What was Martha’s famous declaration?", "options": {"a": "\"You are a good man\"", "b": "\"You are the Christ\"", "c": "\"Raise Lazarus now\"", "d": "\"Let me serve\""}, "answer": "b", "explanation": "She declared Jesus was the Christ."},
        {"question": "What emblem represents Martha?", "options": {"a": "Broken column", "b": "Cup", "c": "Sword and veil", "d": "Crown and scepter"}, "answer": "a", "explanation": "The broken column symbolizes life interrupted but hope preserved."},
        {"question": "What city was Martha from?", "options": {"a": "Bethlehem", "b": "Nazareth", "c": "Bethany", "d": "Jericho"}, "answer": "c", "explanation": "Martha lived in Bethany."},
        {"question": "Martha is known for what trait?", "options": {"a": "Sloth", "b": "Hospitality and service", "c": "Warrior spirit", "d": "Prophecy"}, "answer": "b", "explanation": "Hospitality and service define Martha."},
        {"question": "What future hope did Martha express?", "options": {"a": "Victory", "b": "Wealth", "c": "Resurrection", "d": "Earthly rule"}, "answer": "c", "explanation": "Belief in final resurrection."},
        {"question": "What emotion did Martha show when Lazarus died?", "options": {"a": "Joy", "b": "Patience and sadness", "c": "Anger", "d": "Jealousy"}, "answer": "b", "explanation": "She patiently trusted even in sadness."},
        {"question": "What kind of faith did Martha show?", "options": {"a": "Weak", "b": "Practical and enduring", "c": "Easily shaken", "d": "Doubtful"}, "answer": "b", "explanation": "Her faith was practical and strong under pressure."},
        {"question": "What lesson can be learned from Martha?", "options": {"a": "Worry less", "b": "Trust God's promises", "c": "Act boldly", "d": "Take revenge"}, "answer": "b", "explanation": "Trusting God's promises even in loss."},
        {"question": "What attribute does Martha's broken column teach?", "options": {"a": "Strength", "b": "Wealth", "c": "Endurance and hope", "d": "Power"}, "answer": "c", "explanation": "It shows endurance through broken dreams and hope for eternal life."}
    ],
    "Electa": [
        {"question": "What color represents Electa?", "options": {"a": "Blue", "b": "Red", "c": "White", "d": "Yellow"}, "answer": "b", "explanation": "Red symbolizes fervent love and sacrifice."},
        {"question": "Electa stands for what virtue?", "options": {"a": "Justice", "b": "Charity", "c": "Courage", "d": "Hope"}, "answer": "b", "explanation": "Charity (love) is Electa's central virtue."},
        {"question": "Electa's story is associated with which Testament?", "options": {"a": "Old Testament", "b": "New Testament", "c": "Apocrypha", "d": "Psalms"}, "answer": "b", "explanation": "New Testament teachings inspire Electa’s story."},
        {"question": "Who persecuted Electa and early Christians?", "options": {"a": "Greeks", "b": "Romans", "c": "Egyptians", "d": "Persians"}, "answer": "b", "explanation": "Romans persecuted early Christians."},
        {"question": "What was Electa’s sacrifice?", "options": {"a": "Her wealth", "b": "Her home", "c": "Her life for Christ", "d": "Her family"}, "answer": "c", "explanation": "She gave her life rather than deny Christ."},
        {"question": "What is Electa's symbol?", "options": {"a": "Cup", "b": "Broken column", "c": "Crown", "d": "Sword"}, "answer": "a", "explanation": "The Cup symbolizes charity and sacrifice."},
        {"question": "Which apostle spoke about charity being the greatest virtue?", "options": {"a": "John", "b": "Peter", "c": "Paul", "d": "James"}, "answer": "c", "explanation": "Paul in Corinthians highlights charity."},
        {"question": "Electa showed kindness by doing what?", "options": {"a": "Feeding the Romans", "b": "Sheltering Christians", "c": "Serving kings", "d": "Gathering armies"}, "answer": "b", "explanation": "She sheltered persecuted Christians."},
        {"question": "How did Electa die?", "options": {"a": "Poisoned", "b": "Burned alive", "c": "Stoned", "d": "Crucified"}, "answer": "b", "explanation": "Tradition says Electa was burned alive."},
        {"question": "What does Electa teach us?", "options": {"a": "Obedience to kings", "b": "Charity and steadfast faith", "c": "Revenge", "d": "Patience"}, "answer": "b", "explanation": "Charity and unwavering faith are Electa’s lessons."},
        {"question": "Where in the Bible is the famous 'greatest of these is love' teaching?", "options": {"a": "Romans", "b": "1 Corinthians", "c": "Galatians", "d": "Hebrews"}, "answer": "b", "explanation": "1 Corinthians 13:13 speaks about charity being the greatest."},
        {"question": "What great act of faith did Electa show?", "options": {"a": "Building a temple", "b": "Refusing to deny Christ", "c": "Preaching in the temple", "d": "Traveling across seas"}, "answer": "b", "explanation": "She refused to renounce her faith."},
        {"question": "Electa is honored in the Star because of what?", "options": {"a": "Political power", "b": "Victory in war", "c": "Sacrificial love", "d": "Wealth and power"}, "answer": "c", "explanation": "Her sacrificial love is honored."},
        {"question": "The Cup symbol represents what for Electa?", "options": {"a": "Victory", "b": "Sacrifice", "c": "Power", "d": "Prosperity"}, "answer": "b", "explanation": "The cup symbolizes sacrifice and charity."},
        {"question": "Electa's story encourages members to act how?", "options": {"a": "With fear", "b": "With cunning", "c": "With steadfast love and sacrifice", "d": "With ambition"}, "answer": "c", "explanation": "Steadfast love and sacrifice are Electa’s examples."}
    ]
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
st.set_page_config(page_title="OES Five Heroines Quiz", layout="centered")
import os  # <-- Add this import at the top if you don't already have it


# Paths
main_banner = "Images/banner.png"
default_banner = "default_banner.png"  # Backup image

# Safe image loading
if os.path.exists(main_banner):
    st.image(main_banner, use_container_width=True)
elif os.path.exists(default_banner):
    st.image(default_banner, use_container_width=True)
    st.warning(f"Main banner image not found. Displaying default image instead.")
else:
    st.error("No banner image available. Please upload 'Images/banner.png' or 'default_banner.png'.")

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

