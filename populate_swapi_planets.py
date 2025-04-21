import requests

GRAPHQL_URL = "https://swapi-graphql.netlify.app/graphql"
REST_API_URL = "http://localhost:8000/swapi/planets/"

query = """
query {
  allPlanets {
    planets {
      name
      population
      terrains
      climates
    }
  }
}
"""

headers = {"Content-Type": "application/json"}
response = requests.post(GRAPHQL_URL, json={"query": query}, headers=headers)

if response.status_code != 200:
    print("❌ Failed to fetch from GraphQL:", response.text)
    exit(1)

planets_data = response.json()["data"]["allPlanets"]["planets"]

planet_list = []

for planet in planets_data:
    name = planet.get("name", "Unknown")
    population = planet.get("population")
    terrains = planet.get("terrains") or []
    climates = planet.get("climates") or []

    # Clean population
    try:
        population = float(population.replace(",", "")) if population else 0.0
    except Exception:
        population = 0.0

    planet_list.append({
        "name": name,
        "population": population,
        "terrains": terrains,
        "climates": climates
    })

# Send all planets in one POST request
print(f"Sending {len(planet_list)} planets in a single POST request...")
res = requests.post(REST_API_URL, json=planet_list, headers=headers)

if res.status_code in [200, 201]:
    print("✅ Planets inserted successfully:")
    inserted_planets = res.json()
    for planet in inserted_planets:
        print(f"- {planet['name']}")
else:
    print(f"❌ Failed to insert planets: {res.status_code} - {res.text}")
