from get_completion_1 import get_completion

def get_enhanced_prompt(user_prompt):

    schema_context = """
        Database Schema:
        1. Table Name: parlimentary_elections_2019
        Columns: state_name (TEXT), constituency_name (TEXT), assembly_constituency_name (TEXT), nota_votes (INTEGER), candidate_name (TEXT), party_name (TEXT), secured_votes (INTEGER)
        Data : 

        Andhra Pradesh,Aruku ,Palakonda (ST),3736,KISHORE CHANDRA DEO,TDP,54056
        Andhra Pradesh,Aruku ,Palakonda (ST),3736,Dr. KOSURI KASI VISWANADHA VEERA VENKATA SATYANARAYANA REDDY,BJP,1753
        Andhra Pradesh,Aruku ,Palakonda (ST),3736,GODDETI. MADHAVI,YSRCP,69588
        Andhra Pradesh,Aruku ,Palakonda (ST),3736,SHRUTI DEVI VYRICHERLA,INC,1327
        Andhra Pradesh,Aruku ,Palakonda (ST),3736,GANGULAIAH VAMPURU.,JnP,2987


        2. Table Name: Maharashtra_elections_2019
        Columns: state_name (TEXT), assembly_constituency_number (INTEGER), assembly_constituency_name (TEXT), candidate_name (TEXT), candidate_sex (TEXT), candidate_age (INTEGER), candidate_category (TEXT), party_name (TEXT), secured_votes (INTEGER), percentage_of_votes (REAL), total_voters (INTEGER), total_votes_in_state (INTEGER), PERCENT_VOTES_POLLED (REAL), candidate_position (INTEGER)
        Data : 

        Maharashtra,1,Akkalkuwa ,ADV. K. C. PADAVI,MALE,61,ST,INC,82770,41.25545786,278888,200628,71.93855598,1
        Maharashtra,1,Akkalkuwa ,AAMSHYA FULJI PADAVI,MALE,51,ST,SHS,80674,40.21073828,278888,200628,71.93855598,2
        Maharashtra,1,Akkalkuwa ,NAGESH DILVARSING PADVI,MALE,44,ST,IND,21664,10.79809398,278888,200628,71.93855598,3
        Maharashtra,1,Akkalkuwa ,NOTA,NOTA,0,NOTA,NOTA,4857,2.420898379,278888,200628,71.93855598,4
        Maharashtra,1,Akkalkuwa ,ADV. KAILAS PRATAPSING VASAVE,MALE,28,ST,AAAP,4055,2.021153578,278888,200628,71.93855598,5


        3. Table Name: parlimentary_elections_2024
        Columns: candidate_name (TEXT), party_name_expanded (TEXT), secured_votes (INTEGER), percentage_of_votes (REAL), state_name (TEXT), constituency_name (TEXT), party_name (TEXT)
        Data : 

        BISHNU PADA RAY,Bharatiya Janata Party,102436,50.58,Andaman & Nicobar Islands,Andaman & Nicobar Islands,BJP
        KULDEEP RAI SHARMA,Indian National Congress,78040,38.54,Andaman & Nicobar Islands,Andaman & Nicobar Islands,INC
        MANOJ PAUL,Andaman Nicobar Democratic Congress,8254,4.08,Andaman & Nicobar Islands,Andaman & Nicobar Islands,ANDC
        D AYYAPPAN,Communist Party of India (Marxist),6017,2.97,Andaman & Nicobar Islands,Andaman & Nicobar Islands,CPI (M)
        V.K. ABDUL AZIZ,Independent,2203,1.09,Andaman & Nicobar Islands,Andaman & Nicobar Islands,IND

    """

    q1 = "what was the count of the male candidates and female candidates who contested the 2019 maharashtra elections?"
    ans1 = "Retrieve the count of candidates by gender (male and female) who contested in the Maharashtra state elections of 2019. Use the Maharashtra_elections_2019 table, specifically filtering the candidate_sex column for 'MALE' and 'FEMALE' values to determine the total number of male and female candidates"

    q2 = "what were the top three political prties which got the maximum number of votes, and how many votes did they get with respect to the parlimentary elections of 2024?"
    ans2 = "Identify the top three political parties that received the highest total votes in the parliamentary elections of 2024. Use the parlimentary_elections_2024 table and aggregate the total votes for each party by summing the values in the secured_votes column. List the top three parties by their total votes in descending order, along with the number of votes each party received."

    q3 = "find the political parties with the maximum number of female candidates and the count of female candidates in the 2019 Maharashtra elections"
    ans3 = "Identify the political parties with the most female candidates in the 2019 Maharashtra elections. Use the Maharashtra_elections_2019 table to filter candidates where candidate_sex is 'FEMALE', then group the data by party_name. For each party, count the number of female candidates, and return the party name along with the count of female candidates, sorted in descending order to show the party with the maximum number of female candidates at the top."

    q4 = "count constituencies where BJP won in 2019 but lost in 2024 and where BJP won in 2024 but lost in 2019."
    ans4 = """Count the number of constituencies in which the BJP party (specified in party_name as 'BJP') won in the 2019 elections but lost in the 2024 elections, and separately count the constituencies where the BJP won in 2024 but lost in 2019. To achieve this:

        Use the parlimentary_elections_2019 and parlimentary_elections_2024 tables.
        For each table, identify the winning party in each constituency_name by finding the row where the party_name is 'BJP' and secured_votes is the highest.
        Count constituencies where BJP won in 2019 but does not have the highest secured_votes in 2024.
        Count constituencies where BJP won in 2024 but does not have the highest secured_votes in 2019.
        Return two counts: (1) constituencies where BJP won in 2019 but lost in 2024, and (2) constituencies where BJP won in 2024 but lost in 2019."""

    q5 = "find the name of the political party that won the parliamentary elections in Maharashtra in both 2019 and 2024, along with the number of votes secured by the party in each year"
    ans5 = """Identify the political party that secured the most votes in Maharashtra in both the 2019 and 2024 parliamentary elections. For this, use the parlimentary_elections_2019 and parlimentary_elections_2024 tables and perform the following steps:

    Filter the records in each table where state_name is 'Maharashtra'.
    For each year (2019 and 2024), sum the secured_votes by party_name for all constituencies in Maharashtra.
    Identify the political party with the highest total secured_votes in Maharashtra for each year.
    Return the party_name, along with the total number of votes the party secured in both 2019 and 2024.
    If the same party won in both years, provide this party's name and the vote counts from each year."""

    prompt = f"""
        You are expert in expanding the input question such that it is easier to undertand the question and arrive at the solution.
        
        Given a natural language question, you need to expand it to make it clear to another LLM by specifying details such as 
        which tables and columns to reference from the provided database schema.
        
        You need to ensure that the question is simplified and explicit.


        HERE IS THE SCHEMA CONTEXT:
        {schema_context}

        #####

        EXAMPLES : 

        Input : {q1}
        Output : {ans1}

        Input : {q2}
        Output : {ans2}

        Input : {q3}
        Output : {ans3}

        Input : {q4}
        Output : {ans4}

        Input : {q5}
        Output : {ans5}

        #####

        I NEED YOU TO ENSURE THAT EACH AND EVERY TABLE NAME AND COLUMN NAME THAT IS THERE IN THE OUTPUT SQL QUERY NEEDS TO BE VALID AND PRESENT IN MY SCHEMA.
        JUST RETURN THE ENHANCED TEXT AND NOTHING ELSE, NO INTRODUCTION, NO CONCLUSION , JUST THE TEXT.

        Now provide the enhanced question for the following question:

        {user_prompt}
        
        
        """
    
    response = get_completion(prompt)

    return response

