import os
from crewai import Agent, Task, Crew, LLM

# On définit le modèle Gemini
mon_llm = LLM(model="gemini/gemini-1.5-flash", api_key=os.environ.get("GEMINI_API_KEY"))

# On donne ce modèle à l'agent
chercheur = Agent(
  role='Chercheur',
  goal='Trouver des infos',
  backstory="Expert IA.",
  llm=mon_llm,  # <--- NE PAS OUBLIER CETTE LIGNE
  verbose=True
)
# 1. On définit la mission (Task)
ma_tache = Task(
    description="Explique en 3 points pourquoi CrewAI est génial avec Gemini.",
    expected_output="Un résumé court en français.",
    agent=chercheur
)

# 2. On crée l'équipe et on lance le travail
equipe = Crew(
    agents=[chercheur],
    tasks=[ma_tache],
    verbose=True
)

print("### L'agent commence son travail... ###")
equipe.kickoff()
