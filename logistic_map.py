import streamlit as st

st.title('Logistic map')
st.write('ロジスティック写像をグラフ化します。')
st.write('')
st.latex(r'x_{n+1}=ax_{n}(1-x_{n})')
st.write('')


a = st.sidebar.slider('a:', 0.0, 4.0, 2.0)
start_num = st.sidebar.slider('x:', 0.0,1.0, 0.9)
n = st.sidebar.slider('n:', 50,300, 100)

x = [start_num]
for i in range(n):
    x.append(a * x[i] * (1-x[i]))

st.line_chart(x)
