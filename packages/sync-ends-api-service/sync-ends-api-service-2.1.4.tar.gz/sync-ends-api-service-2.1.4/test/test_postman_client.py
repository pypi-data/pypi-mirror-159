from src.postman_client import PostmanClient
import responses


@responses.activate
def test_get_collections_schema():
    postman_client = PostmanClient("SAM-Key-123fg", "Postman API")
    collections_json = {
        "collections": [
            {
                "id": "adad789d-d8b4-4d0b-a98c-bc9f0d1d6991",
                "name": "Postman API",
                "owner": "21675201",
                "createdAt": "2022-07-01T03:10:45.000Z",
                "updatedAt": "2022-07-01T03:12:52.000Z",
                "uid": "21675201-adad789d-d8b4-4d0b-a98c-bc9f0d1d6991",
                "fork": {
                    "label": "postman api collection",
                    "createdAt": "2020-10-21T00:20:52.000Z",
                    "from": "12959542-c8142d51-e97c-46b6-bd77-52bb66712c9a",
                },
                "isPublic": False,
            },
            {
                "id": "689dfc9d-5581-436f-b0d7-b14d49617c5a",
                "name": "Sample Server",
                "owner": "21675201",
                "createdAt": "2022-06-28T04:05:48.000Z",
                "updatedAt": "2022-07-06T05:01:33.000Z",
                "uid": "21675201-689dfc9d-5581-436f-b0d7-b14d49617c5a",
                "isPublic": False,
            },
        ]
    }
    single_collection_json = {
        "collection": {
            "info": {
                "_postman_id": "21675201-adad789d-d8b4-4d0b-a98c-bc9f0d1d6991",
                "name": "Sample Server",
                "description": "This collection contains sample APIs that can be used to test the Sync Ends service.",
                "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
            },
            "item": [
                {
                    "name": "Get student details",
                    "id": "d6283288-0cde-443c-8bf6-82773810f164",
                    "request": {
                        "method": "GET",
                        "header": [],
                        "url": {
                            "raw": "http://127.0.0.1:5001/students?studentName=Test",
                            "protocol": "http",
                            "host": ["127", "0", "0", "1"],
                            "port": "5001",
                            "path": ["students"],
                            "query": [{"key": "studentName", "value": "Test"}],
                        },
                    },
                    "response": [],
                },
            ],
        }
    }
    responses.add(
        responses.GET,
        "https://api.getpostman.com/collections",
        json=collections_json,
        status=200,
    )
    responses.add(
        responses.GET,
        "https://api.getpostman.com/collections/21675201-adad789d-d8b4-4d0b-a98c-bc9f0d1d6991",
        json=single_collection_json,
        status=200,
    )

    resp = postman_client.get_collection_schema()
    assert len(responses.calls) == 2
    assert responses.calls[0].request.url == "https://api.getpostman.com/collections"
    assert responses.calls[0].response.json() == collections_json
    assert (
        responses.calls[1].request.url
        == "https://api.getpostman.com/collections/21675201-adad789d-d8b4-4d0b-a98c-bc9f0d1d6991"
    )
    assert responses.calls[1].response.json() == single_collection_json
    assert (
        postman_client.get_collection_id()
        == "21675201-adad789d-d8b4-4d0b-a98c-bc9f0d1d6991"
    )
