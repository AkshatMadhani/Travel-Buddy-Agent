from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.youtube_tools import YouTubeTools
import os
from dotenv import load_dotenv
load_dotenv()
agent = Agent(
    name="YouTube summary Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[YouTubeTools(get_video_data=True)],
    show_tool_calls=True,
    instructions=[
        "You are a youtube summary agent , your task it to give user  detailed summary of video",
        "also mention key point in video or funny part in the video",
        " also give timestamp for start of act part[name of person,timestamp]"
    ],
)
agent.print_response(
    "Get the summary for this video https://youtu.be/n_E3bLYuQBo?si=qzFdQPJ9up21xJtf", stream=True
)