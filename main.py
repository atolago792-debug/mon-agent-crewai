import os
from crewai import Agent, Task, Crew, Process

# Configuration pour Gemini
# (Remplace 'gemini-1.5-flash' par 'gemini-1.5-pro' si tu préfères)
mon_llm = "gemini/gemini-1.5-flash"

# Ajoute 'llm=mon_llm' à chaque agent
chercheur = Agent(
  role='Chercheur',
  goal='Trouver des infos',
  backstory="Expert en data.",
  llm=mon_llm,  # <--- TRÈS IMPORTANT
  verbose=True
)
