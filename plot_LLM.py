import os
import tempfile
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from get_completion_1 import get_completion


def generate_bar_plot_code(df):
    """
    Prompt the LLM to generate code to plot a bar graph for the given DataFrame.
    """
    prompt = f"""

    I need you to generate a python code to plot a graph for the given dataframe, somewhat similar like the example given below.
    It needs to be specific to the dataframe I give you. 

    Just Give me the code itself, don't give me any explanation or anything else.

    Don't include "plt.show()" in the code.

    Make sure to include a "KEY" for the Plot generated.

    Ensure the code saves the figure as : 'output_plot.png'

    I need you to decide the kind of plot, it can be either a bar chart, or a scatter plot or a Line graph. 
    The decision must be taken with regards to what suits the dataframe the best.

    
    Please generate the code in python to create the A SUITABLE plot for the given dataframe. Don't give me anything else other than the code itself.

    INPUT DATAFRAME : {df}   
    
    """

    response = get_completion(prompt)
    if response.startswith("```python"):
            response = response[9:]  
    if response.startswith("\n```python"):
        response = response[11:]  
    if response.endswith("```"):
        response = response[:-3]  
    return response

def render_plot(df):
    """
    Generate the bar plot code using the LLM, save the plot, and render it in Streamlit.
    """

    try: 
        code = generate_bar_plot_code(df)
        print(code)
        if code:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp_file:
                tmp_file.write(code.encode())
                tmp_file.flush()
                exec(open(tmp_file.name).read())
                os.remove(tmp_file.name)

            # if os.path.exists("output_plot.png"):
            #     st.title("Bar Plot")
            #     st.image("output_plot.png")
            #     os.remove("output_plot.png")
            # else:
            #     st.error("Failed to generate plot.")
        else:
            print("Failed to generate plot code.")
    except Exception as e:
        print(f"An error occurred: {e}")

"""
#####

    EXAMPLE OUTPUT : 

    ```python
    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.DataFrame({df.to_dict()})

    # Create a bar plot for the dataframe
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar')
    plt.title('Bar Plot')
    plt.xlabel('{df.columns[0]}')
    plt.ylabel('{df.columns[1]}')
    plt.grid()
    plt.savefig('output_plot.png')
    ```

    ##### 
"""