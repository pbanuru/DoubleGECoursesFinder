import requests

QUERY_TEMPLATE = '''
query($ge: String, $quarter: String!) {
    schedule(year:2023, quarter: $quarter, ge: $ge) {
        course {
            id
            title
            description
            ge_text
        }
        meetings {
            building
        }
    }
}
'''

def run_query(query, variables=None):
    url = "https://api.peterportal.org/graphql/"
    headers = {
        "Content-Type": "application/json",
    }
    data = {"query": query, "variables": variables}
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(response.content) 
        raise Exception(f"Query failed with status code {response.status_code}.")

def extract_courses_from_result(result):
    if result["data"]["schedule"] is None:
        return {}
    return {course["course"]["id"]: course for course in result["data"]["schedule"] if course["course"] is not None}