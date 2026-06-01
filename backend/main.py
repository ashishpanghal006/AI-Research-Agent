from dotenv import load_dotenv

load_dotenv()

from graph.workflow import graph


query = input("Research Topic: ")
result = graph.invoke({
    "query": query
})

print("\n")
print("=" * 60)
print("RESEARCH REPORT")
print("=" * 60)

print(result["report"])