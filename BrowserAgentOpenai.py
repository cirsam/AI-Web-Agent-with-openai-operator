import asyncio
import os
import webbrowser
from agents import Agent, Runner, WebSearchTool
WebSearchTool()


async def main():
    #first install openai dependencies using the terminal
    #using pip install openai-agents
    #pip install playwright browser-use
    #pip install playwright   
    # if you get the errorresult= await Runner.run( ^^^^^^^^^^^^^^^^^ SyntaxError: 'await' outside function
    #check your indentation
    #if you get the error modulenotfounderror: no module named 'openai_agents'
    #install the openai-agents package using pip install openai-agents
#install openai version  2.16.0 instead of 2.43.
#in vs code set your python interpreter to the one with openai 2.16.0 installed

    os.environ["OPENAI_API_KEY"] = "your_api_key_here"   
    print(os.environ["OPENAI_API_KEY"])

    FINANCIALS_PROMPT = ("You are a financial analyst focused on  fundamentals such as revenue, "
    "profit, margins and growth trajectory. Given this https://www.google.com/finance/beta/quote/MSFT:NASDAQ use the web search tool to find information about microsoft, write a concise analysis of its recent financial "
    "about microsoft,apple, write a concise analysis of its recent financial "
    "performance. Pull out key metrics or quotes. Keep it under 2 paragraphs."
    )
    #initialize the agent   and configure the openai agent
     
    investment_advisor_agent=Agent(
        name="Investment Advisor",
        instructions=FINANCIALS_PROMPT,
        model="gpt-4o-mini",
        tools=[WebSearchTool()]
    )
    #now run the agent by invoking the runner which will execute the agent with the given inputS
    result= await Runner.run(

    starting_agent =investment_advisor_agent,
                    input="OPen the brower and go to https://www.google.com/finance/beta/quote/MSFT:NASDAQ and search for microsoft's financial data and return asummaryof the Upcoming earnings information."
                    )

    print("it works")
    print(result.final_output)
    

asyncio.run(main())