from get_completion_1 import get_completion

def get_insights(user_prompt, dataframe):

    
    prompt = f"""
        You are expert in understanding , interpretting and explaining data fetched from an SQL database.
        
        Given a natural language question and the Corresponding data fetched from the SQL Database, you need to understand, interpret and explain the data retrieved in accordance to the question asked.


        #####

        Input Question : {user_prompt}

        Data Fetched From SQL Database : {dataframe}

        Now provide the Analysis, interpretation and explanation :

        """
    
    response = get_completion(prompt)

    return response

