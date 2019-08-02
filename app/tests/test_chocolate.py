import json


def test_get_no_chocolates(client):
    res = client.get("/chocolates")
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == []

def test_create_chocolate(client):
    res = client.post("/chocolates", data={"name": "Kit Kat"})
    assert res.status_code == 200

def test_sample_chocolate(sample_chocolate):
    assert sample_chocolate.id == 1
    assert sample_chocolate.name == "Kit Kat"

def test_get_chocolate_by_id(client, sample_chocolate):
    res = client.get(f"/chocolates/{sample_chocolate.id}")
    chocolate_dict = json.loads(res.data.decode())
    assert chocolate_dict["name"] == "Kit Kat"

def test_create_chocolate_and_check(client):
    client.post("/chocolates", data = {"name": "Kit Kat"})
    res = client.get("/chocolates")
    chocolates = json.loads(res.data.decode())
    assert len(chocolates) == 1
    assert chocolates[0]["name"] == "Kit Kat"

def test_create_chocolate_and_fetch(client, sample_chocolate):
    res = client.get(f"/chocolates/{sample_chocolate.id}")
    assert res.status_code == 200

    chocolate_dict = json.loads(res.data.decode())
    assert chocolate_dict["name"] == "Kit Kat"

def test_update_chocolate(client, sample_chocolate):
    res = client.put(f"/chocolates/{sample_chocolate.id}", data = {"name": "Not Kit Kat"})
    assert res.status_code == 200
    assert json.loads(res.data.decode()) == sample_chocolate.id

    res = client.get(f"/chocolates/{sample_chocolate.id}")
    chocolate_dict = json.loads(res.data.decode())
    assert chocolate_dict["name"] == "Not Kit Kat"

def test_get_chocolate_with_wines(client, sample_wine):
    res = client.get(f"/chocolates/{sample_wine.chocolate_id}")
    chocolate_dict = json.loads(res.data.decode())
    assert chocolate_dict["wines"][0]["name"] == "Syrah"

def test_delete_chocolate(client, sample_chocolate):
    res = client.delete(f"/chocolates/{sample_chocolate.id}")
    assert res.status_code == 200

def test_get_chocolate_by_name(client, sample_chocolate):
    res = client.get("/chocolates/Kit Kat")
    assert res.status_code == 200
    
    chocolate_dict = json.loads(res.data.decode())
    assert chocolate_dict["name"] == "Kit Kat"
