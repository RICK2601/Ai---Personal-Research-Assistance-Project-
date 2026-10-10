from crewai import Crew

from agents.research_specialist import research_specialist_agent
from tasks.research_task import research_task

research_crew=Crew(
    agents=[research_specialist_agent],
    tasks=[research_task],
    verbose=True
)
