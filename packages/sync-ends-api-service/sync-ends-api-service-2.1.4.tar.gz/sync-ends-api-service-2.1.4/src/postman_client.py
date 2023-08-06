import requests


class PostmanClient:
    def __init__(self, api_key, collection_name):
        self.COLLECTIONS_ROUTE = "/collections"
        self.POSTMAN_API_URL = "api.getpostman.com"
        self.api_key = api_key
        self.collection_name = collection_name
        self.collection_id = 0

    def get_collection_schema(self):
        """
        Fetches the APIs schemas from the Postman collection
        """

        boundary = ""
        headers = {
            "X-Api-Key": self.api_key,
            "Content-type": "multipart/form-data; boundary={}".format(
                boundary
            ),  # noqa: E501
        }

        # create a HTTPS connection object
        HTTPS_PREFIX = "https://"
        collections_url = HTTPS_PREFIX + self.POSTMAN_API_URL + self.COLLECTIONS_ROUTE
        response = requests.get(
            collections_url,
            headers=headers,
        )
        collections = response.json()
        collection = list(
            filter(
                lambda x: self.collection_name == x["name"],
                collections.get("collections"),
            )
        )

        # if collection is empty, it is an invalid connection
        if len(collection) == 0:
            raise NameError("Invalid collection name !!!")

        self.collection_id = collection[0]["uid"]
        response = requests.get(
            collections_url + "/" + self.get_collection_id(), headers=headers
        )

        # fetch the response and load the API schema as a JSON
        collection_schema = response.json()
        return collection_schema

    def get_collection_id(self) -> str:
        return str(self.collection_id)
