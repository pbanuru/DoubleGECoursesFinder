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
    
    response.raise_for_status()
    
    return response.json()

def extract_courses_from_result(query_result):
    if query_result["data"]["schedule"] is None:
        raise ValueError("No schedule data found for the given parameters")
    return {course["course"]["id"]: course for course in query_result["data"]["schedule"] if course["course"] is not None}
