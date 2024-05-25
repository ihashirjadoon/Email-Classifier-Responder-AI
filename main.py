# pip install langchain-community
# pip install crewai


from langchain_community.llms import Ollama
from crewai import Agent, Task, Crew, Process

model = Ollama(model = "llama3")

email = input("Enter your email: ")  

# Create the agents for classifying emails 

classifier = Agent(
    role = 'Email classfifer',
    goal = 'Accurately classify email based on their importance give one of these following rationg: Important, Casual or Spam',
    backstory = 'Your AI Agent, which was developed by a team of data scientists and engineers to help users manage their email inboxes. It was trained on a diverse dataset of emails, allowing it to accurately classify emails as spam, important, or casual.',
    verbose = True,
    allow_delegation = False,
    llm = model
)

# Create agent for response

responder = Agent(
    role = "Email Responder",
    goal = "Based on the importance of the emal write a simple and consice response. If the email is rated 'important ' write a formal response and if the email is rated 'casual' write a causal response and if the email is rated 'spam' write a ignore the email no matter what be consice and simple",
    backstory = "You're an AI assistant who only job is to write short responses to email based on their importance. The importace will be provided you by the 'classifier' agent.",
    verbose = True,
    allow_delegation = False,
    llm = model
)

# Create task for classifier 

classify_email = Task(
    description = f"Classify the following email {email}",
    agent = classifier,
    expected_output = "One of these three options: 'important', 'casual', or 'spam'",
)

# Create task for responder 

respond_to_email = Task(
    description = f"Respond to the following email {email} based on the importance of the email provided by the 'classifier' agent.",
    agent = responder,
    expected_output = "A simple and consice response to the email based on the importance of the email provided by the 'classifier' agent."
)

# Create the crew 

crew = Crew(
    agents = [classifier, responder],
    tasks = [classify_email, respond_to_email],
    verbose = 2,
    process = Process.sequential
)

# Get the output or error if any 

try:
    print("[INFO] Starting the crew process")
    output = crew.kickoff()
    print("[INFO] Crew process completed successfully")
    print(output)
except Exception as e:
    print(f"[ERROR] An error occured during the crew process{e}")

