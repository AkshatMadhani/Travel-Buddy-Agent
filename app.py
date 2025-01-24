from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
load_dotenv()


web_search_agent=Agent(
    name="web search agent",
    role="search web for information",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    instruction=["always include sources"],
    show_tools_calls=True,
    markdown=True,
)
#financial agent

finance_agent=Agent(
    name="finance research agent",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[YFinanceTools(stock_price=True,stock_fundamentals=True,company_news=True,analyst_recommendations=True)],
    instruction=["always shows prices in table "],
    show_tools_calls=True,
    markdown=True,
)
multi_agents=Agent(
    team=[finance_agent,web_search_agent],
    model=Groq(id='llama-3.3-70b-versatile'),
    instructions=("always shows prices in table ","always include sources"),
    show_tools_calls=True,
    markdown=True,


)
multi_agents.print_response("summarise analyst recommendation and share latest news for titagarh wagons",stream =True)