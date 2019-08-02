import json

def test_get_no_wines(client):
    res = client.get("/wines")
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == []

def test_sample_wine_fixture(sample_wine):
    assert sample_wine.id == 1
    assert sample_wine.name == "Syrah"

def test_solo_wine_fixture(solo_wine):
    assert solo_wine.id == 1
    assert solo_wine.name == "Chardonnay"

def test_create_wine_with_chocolate(client, sample_chocolate):
    wine_info = {"name": "Syrah", "chocolate": sample_chocolate.id}
    res = client.post("/wines", data=wine_info)
    assert res.status_code == 200

def test_create_solo_wine(client):
    wine_info = {"name": "Chardonnay"}
    res = client.post("/wines", data=wine_info)
    assert res.status_code == 200

    res = client.get("/wines")
    wines = json.loads(res.data.decode())
    assert len(wines) == 1
    assert wines[0]['name'] == "Chardonnay"
    assert wines[0].get('chocolate') is None

def test_get_one_wine(client, sample_wine):
    res = client.get(f"/wines/{sample_wine.id}")
    wine_dict = json.loads(res.data.decode())
    assert wine_dict["name"] == "Syrah"