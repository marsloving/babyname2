
import openai
import streamlit as st

# Set up OpenAI API key
openai.api_key =  'OPENAI_API_KEY_babyname'

def generate_names(model, parents_names, birth_date, language):
    completions = openai.Completion.create(
        engine=model,
        prompt=f"Generate baby names for parents with names {parents_names} born on {birth_date} in {language}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Use OpenAI's GPT-3 as the language model
model = "text-davinci-003"

st.title("Baby Name Generator")

parents_names = st.text_input("Enter both parents' names (e.g. John Doe & Jane Doe):")
birth_date = st.date_input("Enter birth date:")
language = st.selectbox("Choose language:", ["Chinese", "English"])

if st.button("Generate Names"):
    names = generate_names(model, parents_names, birth_date, language)
    st.success(names)
