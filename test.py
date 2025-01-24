from phi.agent import Agent

agent = Agent(name="Test Agent")
response = agent.print_response("Hello, how can I help you?", stream=False)
print(response)
