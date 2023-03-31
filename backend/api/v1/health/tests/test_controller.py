from fastapi.testclient import TestClient

from api.v1.health.controller import router

client = TestClient(router)


def test_ヘルスチェックのjsonをチェック() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
