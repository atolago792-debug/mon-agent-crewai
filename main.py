import os
from crewai import Agent, Task, Crew, Process

# 1. Définition des Agents
chercheur = Agent(
  role='Chercheur de solutions',
  goal='Trouver les meilleures méthodes pour automatiser des tâches avec CrewAI',
  backstory="Tu es un expert en automatisation IA spécialisé dans GitHub Actions.",
  verbose=True,
  allow_delegation=False
)

redacteur = Agent(
  role='Rédacteur technique',
  goal='Rédiger un guide clair et court basé sur les recherches',
  backstory="Tu sais transformer des informations complexes en instructions simples.",
  verbose=True,
  allow_delegation=False
)

# 2. Définition des Tâches
tache_recherche = Task(
  description="Analyse comment faire tourner un agent CrewAI sur GitHub Actions gratuitement.",
  agent=chercheur,
  expected_output="Une liste de 3 points clés pour l'automatisation."
)

tache_redaction = Task(
  description="Rédige un court rapport final.",
  agent=redacteur,
  expected_output="Un rapport au format Markdown prêt à être lu.",
  output_file="rapport_final.md"  # Sauvegarde le résultat dans ce fichier
)

# 3. Lancement de l'équipe (Crew)
equipe = Crew(
  agents=[chercheur, redacteur],
  tasks=[tache_recherche, tache_redaction],
  process=Process.sequential
)

print("### Début de l'automatisation ###")
resultat = equipe.kickoff()
print("### Tâche terminée avec succès ! ###")
