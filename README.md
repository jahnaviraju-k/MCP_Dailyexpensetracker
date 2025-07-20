# Model Context Protocol (MCP) Daily Expense Tracker Project
This project has been built and explained using the Model Context Protocol (MCP) format  often used in academic and enterprise environments to validate data solutions. It also simulates agent-like behaviour through modular pipelines.

Here, I  used a relational data model (SQLite schema) as the internal structure or model. Each expense is an event with attributes the agent cares about - Amount, Category, Note, Date.
- This acts like the agent’s memory base, storing and retrieving structured facts.
- The data is user-generated (manual input), and stored in a local SQLite database. This represents how an agent records observations about the world (spending).
- Simulation of an agent pipeline by implementing like this: User Input → Validation → Insert into DB → Visualisation/Action → Store Insights.
# Implemented as:
- main.py = control system
- db.py = persistence agent
- tracker.py = planner & executor
- matplotlib/pandas = visualiser agent
