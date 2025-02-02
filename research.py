import streamlit as st
from phi.model.groq import Groq
from phi.tools.exa import ExaTools
from phi.tools.arxiv_toolkit import ArxivToolkit
from phi.agent import Agent
from dotenv import load_dotenv
research_analytics_agents=Agent(
    name='research agent',
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[ExaTools(),ArxivToolkit(read_arxiv_papers=True)],
    instructions=["you are research agent ,your task is to find research paper from top publications",
    "research paper suggested should align with user inputs and suggest recent publication for better understanding",
    "use ArxivToolkit for giving detailed information about each research paper suggested"
    "also show in format[name,author,year,publisher]"
    ],
    markdown=True,
)
research_analytics_agents.print_response("suggest me 10 research paper of nlp",stream=True)
