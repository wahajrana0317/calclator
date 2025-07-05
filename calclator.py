import streamlit as st

# Set page config
st.set_page_config(page_title="Calculater design by Wahaj", page_icon="🧮")

st.markdown("<h1 style='text-align: center;'>Calculater design by Wahaj 🧮</h1>", unsafe_allow_html=True)

# Session state for input display
if "input" not in st.session_state:
    st.session_state.input = ""

# Function to update input
def add_to_input(val):
    st.session_state.input += str(val)

# Function to clear input
def clear():
    st.session_state.input = ""

# Function to delete last character
def backspace():
    st.session_state.input = st.session_state.input[:-1]

# Function to evaluate the expression
def evaluate():
    try:
        st.session_state.input = str(eval(st.session_state.input))
    except:
        st.session_state.input = "Error"

# Display area
st.text_input("Input/Output", value=st.session_state.input, key="display", disabled=True)

# Button layout using columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=add_to_input, args=("7",))
    st.button("4", on_click=add_to_input, args=("4",))
    st.button("1", on_click=add_to_input, args=("1",))
    st.button("0", on_click=add_to_input, args=("0",))

with col2:
    st.button("8", on_click=add_to_input, args=("8",))
    st.button("5", on_click=add_to_input, args=("5",))
    st.button("2", on_click=add_to_input, args=("2",))
    st.button(".", on_click=add_to_input, args=(".",))

with col3:
    st.button("9", on_click=add_to_input, args=("9",))
    st.button("6", on_click=add_to_input, args=("6",))
    st.button("3", on_click=add_to_input, args=("3",))
    st.button("Enter", on_click=evaluate)

with col4:
    st.button("clear", on_click=clear)
    st.button("backspace", on_click=backspace)
    st.button("++", on_click=add_to_input, args=("+",))
    st.button("--", on_click=add_to_input, args=("-",))
    st.button("**", on_click=add_to_input, args=("*",))
    st.button("/", on_click=add_to_input, args=("/",))

st.markdown("""
    <style>
        body {
            background-color: #1565c0 !important;
        } 
        .stApp {
            background-color: #1565c0 !important;
        }
        /* Make +, -, * buttons red */
        button[title="+"], button[title="-"], button[title="*"] {
            background-color: #d32f2f !important;
            color: #fff !important;
            border: 2px solid #b71c1c !important;
        }
    </style>
""", unsafe_allow_html=True)