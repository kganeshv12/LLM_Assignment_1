# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# import os
# from critique_LLM import get_enhanced_prompt
# from SQL_query_LLM import get_SQL_query
# from SQL_runtime_1 import sql_and_dataframe
# from insight_LLM import get_insights
# from plot_LLM import render_plot

# def generate_response(question):
#     enhanced_prompt = get_enhanced_prompt(question)
#     print("Enhanced Prompt: ", enhanced_prompt)

#     SQL_query = get_SQL_query(enhanced_prompt)
#     print(SQL_query)

#     dataframe = sql_and_dataframe(SQL_query)
#     print(dataframe)

#     Inference = get_insights(question, dataframe)
#     print(Inference)

    
    
#     return Inference, dataframe

# st.title("Chat with Election Data")

# # Get the chat input from the user
# chat_input = st.text_input("Enter your Question : ", "")

# # Generate the response and plot
# if chat_input:
#     response_text, df = generate_response(chat_input)
    
#     # Display the response text
#     st.write(response_text)


#     # Display the dataframe
#     st.dataframe(df)

#     render_plot(df)
#     if os.path.exists("output_plot.png"):
#         st.title("Visualization Plot")
#         st.image("output_plot.png")
#         os.remove("output_plot.png")
#     else:
#         st.error("Failed to generate plot.")


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from critique_LLM import get_enhanced_prompt
from SQL_query_LLM import get_SQL_query
from SQL_runtime_1 import sql_and_dataframe
from insight_LLM import get_insights
from plot_LLM import render_plot

def generate_response(question):
    enhanced_prompt = get_enhanced_prompt(question)
    print("Enhanced Prompt: ", enhanced_prompt)
    SQL_query = get_SQL_query(enhanced_prompt)
    print(SQL_query)
    dataframe = sql_and_dataframe(SQL_query)
    print(dataframe)
    Inference = get_insights(question, dataframe)
    print(Inference)
    
    return Inference, dataframe

st.title("Chat with Election Data")

# Define example questions organized by categories with proper nesting
example_categories = {
    "Demographics Analysis": [
        {
            "name": "Gender Distribution - Contestants",
            "question": "Give me count of all the male candidates who have contested the elections and count of all female candidates who have contested the Maharashtra 2019 elections"
        }
    ],
    "Party Performance": [
        {
            "name": "Overall Performance",
            "question": "How did BJP political party perform in the parlimentary elections 2024?"
        }
    ],
    "Electoral Statistics": [
        {
            "name": "Winning Margins",
            "question": "Which constituencies had the closest winning margins in the 2019 parlimentary elections?"
        },
        {
            "name": "Voter Turnout",
            "question": "What was the average voter turnout across different regions in Maharashtra 2019 elections?"
        }
    ]
}

# Create a list of all options including custom question
options = ["Custom Question"]
for category, questions in example_categories.items():
    for q in questions:
        options.append(f"{category} - {q['name']}")

# Create two columns
col1, col2 = st.columns([2, 1])

with col1:
    # Add a select box for example questions
    selected_option = st.selectbox(
        "Select a question or choose 'Custom Question':",
        options
    )

    # Initialize chat input
    if selected_option == "Custom Question":
        chat_input = st.text_input("Enter your Question:", "")
    else:
        # Parse the selected option
        category = selected_option.split(" - ")[0]
        question_name = selected_option.split(" - ")[1]
        
        # Find the matching question
        question_text = ""
        for questions in example_categories[category]:
            if questions["name"] == question_name:
                question_text = questions["question"]
                break
        
        chat_input = st.text_input(
            "Enter your Question:", 
            value=question_text
        )

with col2:
    # Add a help button with information
    with st.expander("ℹ️ Help"):
        st.markdown("""
        **How to use:**
        1. Select a category and question or choose 'Custom Question'
        2. Modify the question if needed
        3. The analysis will show:
           - Insights from the data
           - Relevant data table
           - Visualization (if applicable)
        
        **Available Categories:**
        - Demographics Analysis
        - Party Performance
        - Electoral Statistics
        """)

# Generate the response and plot
if chat_input:
    # Add a spinner while processing
    with st.spinner('Analyzing your question...'):
        try:
            response_text, df = generate_response(chat_input)
            
            # Create sections for different outputs
            st.subheader("📊 Analysis")
            st.write(response_text)
            
            st.subheader("🔢 Data")
            st.dataframe(df)
            
            # Visualization section
            render_plot(df)
            if os.path.exists("output_plot.png"):
                st.subheader("📈 Visualization")
                st.image("output_plot.png")
                os.remove("output_plot.png")
            else:
                st.warning("No visualization available for this query.")
        except Exception as e:
            st.error(f"An error occurred while processing your request: {str(e)}")

# Add footer
st.markdown("---")
st.markdown("*Powered by Election Data Analytics*")
