import requests

def explain_status(code):
    messages = {
        200: "OK - Request completed successfully",
        201: "Created - Resource created successfully",
        400: "Bad Request - Invalid request",
        401: "Unauthorized - Authentication required",
        404: "Not Found - Resource does not exist",
        500: "Internal Server Error - Server encountered an error"
    }

    return messages.get(code, f"Unknown status code: {code}")


# ----------------------------------------
# 1. GET /users - Print first 5 users
# ----------------------------------------
try:
    response = requests.get(
        f"{"https://jsonplaceholder.typicode.com"}/users",
        timeout=10
    )
    response.raise_for_status()

    users = response.json()

    print("First 5 users:")
    for user in users[:5]:
        print(
            f"{user['id']} - {user['name']} - "
            f"{user['email']}"
        )

except requests.exceptions as error:
    print(f"GET /users failed: {error}")

# ----------------------------------------
# 2. POST /posts - Create a post
# ----------------------------------------
try:
    post_data = {
        "title": "Learning Python APIs",
        "body": "Practicing REST API requests",
        "userId": 1
    }

    response = requests.post(
        f"{"https://jsonplaceholder.typicode.com"}/posts",
        json=post_data,
        timeout=10
    )

    print("\nPOST status:", response.status_code)

    if response.status_code == 201:
        created_post = response.json()
        print("Created post ID:", created_post["id"])
    else:
        print("POST result:", explain_status(response.status_code))

except requests.exceptions as error:
    print(f"POST /posts failed: {error}")

# ----------------------------------------
# 3. PUT /posts/1
# ----------------------------------------
try:
    updated_data = {
        "id": 1,
        "title": "AJAY",
        "body": "hey man!",
        "userId": 1
    }

    response = requests.put(
        f"{"https://jsonplaceholder.typicode.com"}/posts/1",
        json=updated_data,
        timeout=10
    )

    print("\nPUT status:", response.status_code)

except requests.exceptions.RequestException as error:
    print(f"PUT /posts/1 failed: {error}")    

# ----------------------------------------
# 5. DELETE /posts/1
# ----------------------------------------
try:
    response = requests.delete(
        f"{"https://jsonplaceholder.typicode.com"}/posts/1",
        timeout=10
    )

    print("DELETE status:", response.status_code)

except requests.exceptions as error:
    print(f"DELETE /posts/1 failed: {error}")

# ----------------------------------------
# 6. GET a post that does not exist
# ----------------------------------------
try:
    response = requests.get(
        f"{"https://jsonplaceholder.typicode.com"}/posts/9999",
        timeout=10
    )

    if response.status_code == 404:
        print("GET /posts/9999 -> 404 Not found")
    else:
        print(
            "GET /posts/9999 ->",
            response.status_code,
            explain_status(response.status_code)
        )

except requests.exceptions as error:
    print(f"GET /posts/9999 failed: {error}")        