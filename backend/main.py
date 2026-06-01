from dotenv import load_dotenv
from graph.workflow import graph

load_dotenv()

query = input("Research Topic: ")
result = graph.invoke({
    "query": query
})

print("\n")
print("=" * 50)
print("PLAN")
print("=" * 50)

print(result["plan"])

print("\n")
print("=" * 50)
print("RESEARCH")
print("=" * 50)

print(result["research"])