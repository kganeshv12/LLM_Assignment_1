import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def generate_response(chat_input):
    # Generate a sample response based on the chat input
    response_text = f"You said: {chat_input}. Here is a response."
    
    # Generate a sample plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    
    return response_text

st.title("Chat with Election Data")

# Get the chat input from the user
chat_input = st.text_input("Enter your Question :", "")

# Generate the response and plot
if chat_input:
    response_text = generate_response(chat_input)
    
    # Display the response text
    st.write(response_text)
    
    # Display the Matplotlib plot

    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [10, 15, 7, 12]
    })

    # Create a Streamlit app
    st.title("Bar Chart Example")

    # Display the dataframe
    st.dataframe(df)

    # Create the bar chart
    # st.bar_chart(df.set_index('Category'))
    st.bar_chart(df)
    # fig, ax = plt.subplots()
    # ax.plot(plot_data)
    # st.pyplot(fig)