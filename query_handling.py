import requests

QUERY_TEMPLATE = '''
query($year: Float!, $ge: String, $quarter: String!) {
    schedule(year:$year, quarter: $quarter, ge: $ge) {
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
    
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        print(response.text)
        raise e
    
    return response.json()

def extract_courses_from_result(query_result):
    if query_result["data"]["schedule"] is None:
        raise ValueError("No schedule data found for the given parameters")
    return {course["course"]["id"]: course for course in query_result["data"]["schedule"] if course["course"] is not None}
