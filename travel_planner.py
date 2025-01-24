import streamlit as st
from phi.agent import Agent
from phi.tools.exa import ExaTools
from phi.model.groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
<<<<<<< HEAD
groq_api_key = st.secrets["groq_api_key"]
exa_api_key=st.secrets["exa_api_key"]
=======
groq_api_key = st.secrets["groq_api_key"].strip('"')
exa_api_key=st.secrets["exa_api_key"].strip('"')
>>>>>>> 78755cd95f0437ce69897baf2e420a85db8f0fe7


# Initialize the travel agent
travel_recommender_agent = Agent(
    name="Travel recommender",
    model=Groq(id='llama-3.1-8b-instant'),
    tools=[ExaTools()],
    markdown=True,
    description="You are an expert itinerary planning agent. Your role is to assist users in creating detailed, customized travel plans tailored to their preferences and needs.",
    instructions=[
        "Use Exa to search and extract relevant data from reputable travel platforms.",
        "Collect information on flights, accommodations, local attractions, and estimated costs from these sources.",
        "Ensure that the gathered data is accurate and tailored to the user's preferences, such as destination, group size, and budget constraints.",
        "Create a clear and concise itinerary that includes: detailed day-by-day travel plan, suggested transportation and accommodation options, activity recommendations (e.g., sightseeing, dining, events), an estimated cost breakdown (covering transportation, accommodation, food, and activities).",
        "If a particular website or travel option is unavailable, provide alternatives from other trusted sources.",
        "Do not include direct links to external websites or booking platforms in the response."
    ]
)


st.title("Travel Buddy Agent")
destination = st.text_input("Destination")
group_size = st.number_input("Group size", min_value=1, max_value=10000, value=4)
start_date = st.date_input("Start Date", value="2025-06-01")
end_date = st.date_input("End Date", value="2025-06-05")
budget = st.number_input("Budget (INR)", min_value=5000, max_value=1000000, value=100000)
activities = st.text_input("what activites you wanna enjoy?")

if st.button('"Generate Plan"'):
    # Preparing the prompt for the agent
    user_plan = f"""
    I want to plan an international/national trip of {group_size} people for {start_date} to {end_date} from Mumbai to {destination} and back. 
    My budget is {budget} INR. 
    Suggested activities: {activities}. 
    Please suggest options for places to stay, activities, co-working spaces, and a detailed itinerary with transportation (flights) and activities.
    """
    
    with st.spinner("processing"):
        response = travel_recommender_agent.run(user_plan)
    
        st.write(response.content)
