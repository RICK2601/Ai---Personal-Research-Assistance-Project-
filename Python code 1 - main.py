from dotenv import load_dotenv
from crew import research_crew

# Load environment variables from .env
load_dotenv()


def run(topic: str):
    result = research_crew.kickoff(inputs={"topic": topic})

    print("-" * 50)
    print(result)
    print("-" * 50)


if __name__ == "__main__":
    topic = (
        "AI Agents"
    )

    run(topic)


{"topic": "AI Agents"}
