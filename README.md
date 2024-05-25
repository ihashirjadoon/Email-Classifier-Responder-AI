# Email-Classifier-Responder-AI

This project uses `langchain-community` and `crewai` libraries to create an AI agent that classifies emails based on their importance and generates appropriate responses. The agents are powered by the `Ollama` language model.

## Installation

First, ensure you have Python installed on your system. Then, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ihashirjadoon/Email-Classifier-Responder-AI.git
    cd Email-Classifier-Responder-AI
    ```

2. **Create a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install langchain-community
    pip install crewai
    ```

4. **Download the `llama3` model**:
    - Visit [Ollama Llama3 Model](https://ollama.com/library/llama3) to download the latest version of the model.

## Usage

1. **Run the script**:
    ```sh
    python main.py
    ```

2. **Enter your email** when prompted.

The script will classify the email as "important", "casual", or "spam" and generate an appropriate response based on the classification.

## Steps to Create this AI

1. **Define the Language Model**:
    - Use the `Ollama` model to handle natural language understanding and generation.

2. **Create Agents**:
    - **Classifier Agent**: This agent classifies emails into categories: Important, Casual, or Spam.
    - **Responder Agent**: This agent generates a response based on the classification provided by the classifier agent.

3. **Define Tasks**:
    - **Classify Email Task**: Task for the classifier agent to classify the email.
    - **Respond to Email Task**: Task for the responder agent to generate a response based on the classification.

4. **Create the Crew**:
    - Combine the agents and tasks into a `Crew` object, specifying the process type and verbosity.

5. **Run the Process**:
    - Execute the crew process and handle any potential errors.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request. We welcome all contributions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Langchain Community](https://github.com/langchain-community)
- [CrewAI](https://github.com/crewai)
- [Ollama](https://ollama.com/)

---

Feel free to customize this `README.md` further to better fit your project's specifics and requirements.
