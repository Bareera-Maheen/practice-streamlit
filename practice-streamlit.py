import streamlit as st
# a simple streamlit app
# practice to know the what the purpose and how  it actually help in making projects?
st.title("this the first app") 
# fo heading or title basically streamit work as html or create the structure .
st.write("i am creating  a project for  utterance of stramlit with python")

#  now for simple as use input  or(user input)  we create the a variable to store  ,eans 
# if we the input of the name how it will be shown to you and when you enter the how result will be?
name= st.text_input("Enter your name here:")
if name :
    # embaded string in python we write with "f" like we use backtick in ts or
    #  js to embaded two strings or string with the text.
    st.write(f"Hello! {name}, welcome to streamlit journey.")

    # and now the button 
    if st.button("click me"):
        st.success("button is clicked")
        # success to show you a message in popup for that clicked on button  
        # as you are not setting and function in button 
        
        # same as for slider button 
age = st.slider("Select your age:",1,100,4)
st.write(f"you selected that you're {age} years old") 
# if i write the function of slider it will not work .why ?
# because in slider function with st we the values in the form min-Value=1 , max-Value=100, Value=4(the you to start fron it can be any value and aslo back values)
       

