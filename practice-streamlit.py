import streamlit as st
import emoji
# a simple streamlit app
# practice to know the what the purpose and how  it actually help in making projects?
st.title( "🌙✨ Eid Mubarak! ❤") 
# fo heading or title basically streamit work as html or create the structure .
st.write("Get your wishes with your name")

#  now for simple as use input  or(user input)  we create the a variable to store  ,eans 
# if we the input of the name how it will be shown to you and when you enter the how result will be?
name= st.text_input("Enter your name here: 'and press enter'")
if name :
    # embaded string in python we write with "f" like we use backtick in ts or
    #  js to embaded two strings or string with the text.
    st.write(f"Hello! {name}, Eid Mubarak to you, and your family with a lot of blessings ✨🎉.")


    # and now the button 
    if st.button("click me, for wishes too"):
        st.success("Thank you ❤,Khair Mubarik")
        # success to show you a message in popup for that clicked on button  
        # as you are not setting and function in button 
        
        # same as for slider button 
eidi = st.slider("Select your Eidi:",50,200,100)
st.write(f"here is your Eidi  {eidi} rupess 🎉") 
# if i write the function of slider it will not work .why ?
# because in slider function with st we the values in the form min-Value=1 , max-Value=100, Value=4(the you to start fron it can be any value and aslo back values)
       

