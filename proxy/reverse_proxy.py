import httpx
from fastapi import Request
from starlette.background import BackgroundTask
from starlette.responses import StreamingResponse


class ReverseProxy:
    def __init__(self, host, port):
        self.client = httpx.AsyncClient(base_url=f"http://{host}:{port}")

    async def __call__(self, request: Request):
        url = httpx.URL(path=request.url.path, query=request.url.query.encode("utf-8"))
        rp_req = self.client.build_request(
            request.method, url, headers=request.headers.raw, content=await request.body()
        )
        rp_resp = await self.client.send(rp_req, stream=True)
        return StreamingResponse(
            rp_resp.aiter_raw(),
            status_code=rp_resp.status_code,
            headers=rp_resp.headers,
            background=BackgroundTask(rp_resp.aclose),
        )
