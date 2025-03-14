import requests
import csv

# Set your New Relic API key
API_KEY = "YOUR_API_KEY"
GRAPHQL_ENDPOINT = "https://api.newrelic.com/graphql"

# GraphQL query to fetch dashboards
QUERY = """
{
  actor {
    entitySearch(query: "type='DASHBOARD'") {
      results {
        entities {
          guid
          name
          accountId
          permalink
          tags {
            key
            values
          }
        }
      }
    }
  }
}
"""

# Function to send GraphQL request
def fetch_dashboards():
    headers = {
        "Content-Type": "application/json",
        "API-Key": API_KEY
    }
    
    response = requests.post(GRAPHQL_ENDPOINT, json={"query": QUERY}, headers=headers)
    response.raise_for_status()  # Raise error for failed requests
    
    data = response.json()
    return data["data"]["actor"]["entitySearch"]["results"]["entities"]

# Function to write dashboards to CSV
def save_to_csv(dashboards, filename="new_relic_dashboards.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        # Write header
        writer.writerow(["GUID", "Name", "Account ID", "Permalink", "Tags"])
        
        # Write each dashboard's details
        for dashboard in dashboards:
            tags = "; ".join([f"{tag['key']}={','.join(tag['values'])}" for tag in dashboard.get("tags", [])])
            writer.writerow([dashboard["guid"], dashboard["name"], dashboard["accountId"], dashboard["permalink"], tags])

# Main execution
if __name__ == "__main__":
    dashboards = fetch_dashboards()
    save_to_csv(dashboards)
    print(f"Dashboard data saved to new_relic_dashboards.csv")