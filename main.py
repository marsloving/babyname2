
import openai
import streamlit as st

# Set up OpenAI API key
print("a",OPENAI_API_KEY_babyname)
if  "OPENAI_API_KEY_babyname" in locals().keys(): #判断本地是否有定义
    openai.api_key = OPENAI_API_KEY_babyname

print(openai.api_key)
# else:
#     import setting                               #无则读取本地环境
#     openai.api_key = setting.get_key()

def generate_names(model, last_names,sex):
    completions = openai.Completion.create(
        engine=model,
        prompt=f"Generate three chinese and english baby names for the last name they choice  {last_names} "
               f"and the baby's sex {sex}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.8,
    )

    message = completions.choices[0].text
    return message

# Use OpenAI's GPT-3 as the language model
model = "text-davinci-003"

st.title("AI BB取名神器")

last_names = st.text_input("输入你想要BB的姓氏 (e.g. 陈 & Jane Doe):")
sex = st.selectbox("性别:", ["男", "女"])

if st.button("Generate Names"):
    names = generate_names(model, last_names,sex)
    st.success(names)
