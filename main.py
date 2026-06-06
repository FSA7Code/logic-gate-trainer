import streamlit as st
import random

# --- THE LOGIC GATES ---
def and_gate(input1, input2):
    return 1 if (input1 == 1 and input2 == 1) else 0

def or_gate(input1, input2):
    return 1 if (input1 == 1 or input2 == 1) else 0

def not_gate(input_value):
    return 0 if (input_value == 1) else 1

def generate_question():
    gate_type = random.choice(["AND", "OR", "NOT"])
    in1 = random.randint(0, 1)
    in2 = random.randint(0, 1)
    
    if gate_type == "AND":
        ans = and_gate(in1, in2)
    elif gate_type == "OR":
        ans = or_gate(in1, in2)
    else:
        ans = not_gate(in1)
        
    return {"gate": gate_type, "in1": in1, "in2": in2, "answer": ans}

# --- INITIALIZE STATE ---
if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "current_question" not in st.session_state:
    st.session_state.current_question = generate_question()
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# --- WEB PAGE LAYOUT ---
st.title("🔌 ECE Logic Gate Trainer")
st.write("Test your electrical engineering digital logic skills! Select your answer below.")

col1, col2 = st.columns(2)
col1.metric("Score", st.session_state.score)
col2.metric("Total Questions", st.session_state.total_questions)

st.markdown("---")

q = st.session_state.current_question
if q["gate"] == "NOT":
    st.subheader(f"What is the output of a **{q['gate']}** gate if the input is `{q['in1']}`?")
else:
    st.subheader(f"What is the output of an **{q['gate']}** gate if the inputs are `{q['in1']}` and `{q['in2']}`?")

user_guess = st.selectbox("Your Answer:", options=["Select an option", "0", "1"])

if st.button("Submit Answer"):
    if user_guess == "Select an option":
        st.warning("Please select an answer (0 or 1) before submitting!")
    else:
        # Check the user guess against the CURRENT active question answer
        if int(user_guess) == q["answer"]:
            st.session_state.feedback = "✅ Correct! Excellent job."
            st.session_state.score += 1
        else:
            st.session_state.feedback = f"❌ Wrong. The correct answer was {q['answer']}."
        
        st.session_state.total_questions += 1
        
        # Move to the next question for the upcoming rerun
        st.session_state.current_question = generate_question()
        st.rerun()

if st.session_state.feedback:
    st.info(st.session_state.feedback)