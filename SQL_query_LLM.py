from get_completion_1 import get_completion

def get_SQL_query(user_prompt):
    
    q1 = "Retrieve the count of candidates by gender (male and female) who contested in the Maharashtra state elections of 2019. Use the Maharashtra_elections_2019 table, specifically filtering the candidate_sex column for 'MALE' and 'FEMALE' values to determine the total number of male and female candidates" 
    ans1 = """   SELECT candidate_sex, COUNT(*) AS candidate_count
    FROM Maharashtra_elections_2019
    GROUP BY candidate_sex;
    """

    q2 = "Identify the top three political parties that received the highest total votes in the parliamentary elections of 2024. Use the parlimentary_elections_2024 table and aggregate the total votes for each party by summing the values in the secured_votes column. List the top three parties by their total votes in descending order, along with the number of votes each party received."
    ans2 = """
    SELECT party_name_expanded, SUM(secured_votes) AS total_votes
    FROM parlimentary_elections_2024
    GROUP BY party_name_expanded
    ORDER BY total_votes DESC
    LIMIT 3;
    """

    q3 = "Identify the political parties with the most female candidates in the 2019 Maharashtra elections. Use the Maharashtra_elections_2019 table to filter candidates where candidate_sex is 'FEMALE', then group the data by party_name. For each party, count the number of female candidates, and return the party name along with the count of female candidates, sorted in descending order to show the party with the maximum number of female candidates at the top."
    ans3 = """
    SELECT party_name, COUNT(*) AS female_candidate_count
    FROM Maharashtra_elections_2019
    WHERE candidate_sex = 'FEMALE'
    GROUP BY party_name
    ORDER BY female_candidate_count DESC;
    """

    q4 = """Count the number of constituencies in which the BJP party (specified in party_name as 'BJP') won in the 2019 elections but lost in the 2024 elections, and separately count the constituencies where the BJP won in 2024 but lost in 2019. To achieve this:

        Use the parlimentary_elections_2019 and parlimentary_elections_2024 tables.
        For each table, identify the winning party in each constituency_name by finding the row where the party_name is 'BJP' and secured_votes is the highest.
        Count constituencies where BJP won in 2019 but does not have the highest secured_votes in 2024.
        Count constituencies where BJP won in 2024 but does not have the highest secured_votes in 2019.
        Return two counts: (1) constituencies where BJP won in 2019 but lost in 2024, and (2) constituencies where BJP won in 2024 but lost in 2019."""
    ans4 = """SELECT 
        CASE 
            WHEN p2019.secured_votes > p2024.secured_votes THEN 'BJP Won in 2019 but Lost in 2024'
            WHEN p2024.secured_votes > p2019.secured_votes THEN 'BJP Won in 2024 but Lost in 2019'
        END AS result_type,
        COUNT(*) AS constituencies_count
    FROM 
        parlimentary_elections_2019 p2019
    JOIN 
        parlimentary_elections_2024 p2024
    ON 
        p2019.state_name = p2024.state_name 
        AND p2019.constituency_name = p2024.constituency_name
    WHERE 
        p2019.party_name = 'BJP' 
        AND (p2019.secured_votes != p2024.secured_votes)  -- Ensuring there's a change in vote share
    GROUP BY 
        result_type;
    """
    q5 = """Identify the political party that secured the most votes in Maharashtra in both the 2019 and 2024 parliamentary elections. For this, use the parlimentary_elections_2019 and parlimentary_elections_2024 tables and perform the following steps:

    Filter the records in each table where state_name is 'Maharashtra'.
    For each year (2019 and 2024), sum the secured_votes by party_name for all constituencies in Maharashtra.
    Identify the political party with the highest total secured_votes in Maharashtra for each year.
    Return the party_name, along with the total number of votes the party secured in both 2019 and 2024.
    If the same party won in both years, provide this party's name and the vote counts from each year."""
    ans5 = """
    SELECT 
        p2019.party_name AS party_name_2019,
        p2019.secured_votes AS votes_2019,
        p2024.party_name AS party_name_2024,
        p2024.secured_votes AS votes_2024
    FROM 
        parlimentary_elections_2019 p2019
    JOIN 
        parlimentary_elections_2024 p2024
    ON 
        p2019.state_name = p2024.state_name 
        AND p2019.constituency_name = p2024.constituency_name
    WHERE 
        p2019.party_name = p2024.party_name
    ORDER BY 
        p2019.secured_votes DESC
    LIMIT 1;

    """

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

    prompt = f"""
    You are an expert in generating SQL queries from natural language queries.
    
    I want you to generate SQL query for the input question, which needs to be executed in SQLite3 in python. 

    Please keep in mind the schema of my database and the correct spellings of the table and column names.
    
    Just Give me one SQL query, nothing else. 
    
    I don't want any introduction, NO explanation, NO conclusion, just the correct SQL query.
    
    Please dont output backslashes. Use this database schema as context for generating SQL Queries which will answer the input question:

    {schema_context}

    #####

    Here are some EXAMPLES : 

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
    JUST RETURN THE SQL QUERY AND NOTHING ELSE, NO INTRODUCTION, NO CONCLUSION , JUST THE SQL QUERY.

    Now generate the SQL query for the following question:

    Input : {user_prompt}

    """


    response = get_completion(prompt)

    if response.startswith("```sql"):
        response = response[6:]  # Remove "```sql" at the start
    if response.startswith("\n```sql"):
        response = response[8:]  # Remove "```sql" at the start
    if response.endswith("```"):
        response = response[:-3]  # Remove "```" at the end
        

    return response