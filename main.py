import streamlit as st
import time


st.title('Streamlit 超入門')
st.write('プログレスバーの表示')
'Start！！'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    time.sleep(0.1)
    bar.progress(i + 1)
'Dooone！！！'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('これは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容を書く1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容を書く2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容を書く4')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの調子は？', 0 , 100, 50)

# 'あなたの趣味は', text
# 'コンディション', condition

# if st.checkbox('show Image'):
#     img = Image.open('image_ichinomiya.jpeg')
#     st.image(img, caption='Ichinomiya Kaigan', use_column_width=True)


