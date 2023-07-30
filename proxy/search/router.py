from fastapi import APIRouter, Request

from proxy.reverse_proxy import ReverseProxy
from proxy.search.schemas import SUserData

router = APIRouter(
    prefix="/search",
    tags=["search"],
)


reverse_proxy = ReverseProxy(host="127.0.0.1", port="4001")


@router.post("/", response_model=list[SUserData])
async def search(request: Request, user_data: SUserData):
    return await reverse_proxy(request)
