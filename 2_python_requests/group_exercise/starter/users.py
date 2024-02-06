
import requests
import json


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_users():
    """Retrieve list of all users"""

    endpoint = BASE_URL + "/users"
    res = requests.get(endpoint)

    if 200 <= res.status_code <= 299:
        return json.dumps(
            {"status_code": res.status_code, "data": res.json()}
        )
    else:
        return f"Request not successful. Received a {res.status_code} response."


def get_user(id: int):
    """Retrieve a user by a given ID"""

    endpoint = BASE_URL + f"/users/{id}"
    res = requests.get(endpoint)
    if 200 <= res.status_code <= 299:
        return json.dumps(
            {"status_code": res.status_code, "data": res.json()}
        )
    else:
        return f"Request not successful. Received a {res.status_code} response."


def post_user():
    """
    Add a new user to the API.

    params:
        id
        name
        username
        email
        address
            street
            suite
            city
            zipcode
            geo
                lat
                long
        phone
        website
        company
            name
            catchPhrase
            bs
    """

    user_dict = {
        "name": "Oliver Cadman",
        "username": "SirKnx",
        "email": "oliver.cadman@xandertalent.com",
        "address": {
            "street": "Deptford Church Street",
            "suite": 33,
            "city": "London",
            "zipcode": "SE8 4SF",
            "geo": {
                "lat": "33.10",
                "long": "192.93"
            }
        },
        "phone": "1234567890",
        "company": {
            "name": "Xander Talent",
            "catchPhrase": "Work with us",
            "bs": "data and software talents"
        }
    }

    res = requests.post(
        BASE_URL + "/users",
        data=json.dumps(user_dict),
        headers={
            'Content-type': 'application/json; charset=UTF-8'
        },
        )

    if 200 <= res.status_code <= 299:
        return json.dumps(
            {"status_code": res.status_code, "data": res.json()}
        )


def put_user(id: int):
    """Full update of a user."""
    user_dict = {
        "name": "Oliver Cadman",
        "email": "oliver.cadman@xandertalent.com",
        "address": {
            "street": "Deptford Church Street",
            "suite": 33,
            "city": "London",
            "zipcode": "SE8 4SF",
            "geo": {
                "lat": "33.10",
                "long": "192.93"
            }
        },
        "phone": "1234567890",
        "company": {
            "name": "Xander Talent",
            "catchPhrase": "Work with us",
            "bs": "data and software talents"
        }
    }

    res = requests.put(
        BASE_URL + f"/users/{id}",
        data=json.dumps(user_dict),
        headers={
            "Content-type": "application/json; charset=UTF-8 "
        }
    )

    if 200 <= res.status_code <= 299:
        return json.dumps(
            {"status_code": res.status_code, "data": res.json()}
        )


def patch_user(id: int):
    """Partially update a user"""

    update_dict = {
        "username": "New Username",
        "email": "the1calledbirdman@hotmail.co.uk"
    }

    res = requests.patch(
        BASE_URL + f"/users/{id}",
        data=json.dumps(update_dict),
        headers={
            "Content-type": "application/json; charset=UTF-8"
        }
    )

    if 200 <= res.status_code <= 299:
        return json.dumps(
            {"status_code": res.status_code, "data": res.json()}
        )


def delete_user(id: int):
    """Delete a user."""

    res = requests.delete(BASE_URL + f"/users/{id}")
    if 200 <= res.status_code <= 299:
        return json.dumps(
            {"status_code": res.status_code, "data": res.json()}
        )


if __name__ == "__main__":
    user = get_user(1)
    print(user)

    # users = get_users()
    # print(users)

    # new_user = post_user()
    # print(new_user)
    #
    # put_user = put_user(1)
    # print(put_user)

    # patched_user = patch_user(1)
    # print(patched_user)

    deleted_user = delete_user(1)
    print(deleted_user)
