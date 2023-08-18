#write a lamda function to find whether a given string starts with a given character
st=input('enter ')
s=input('enter ')
k=lambda s,st : st.startswith(s)
print(k(s,st))
