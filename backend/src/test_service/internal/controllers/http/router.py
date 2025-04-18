from fastapi import APIRouter

from internal.controllers.http.products.router import router as products_router

router = APIRouter(prefix="")
router.include_router(products_router)
