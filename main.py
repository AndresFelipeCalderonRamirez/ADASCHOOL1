from fastapi import FastAPI
from api.carbon_controller import router as carbon_router
from middleware.error_handler import app_exception_handler
from errors.custom_exceptions import BaseAppException

app = FastAPI(title="Carbon Tracker Service")

app.include_router(carbon_router, prefix="/carbon")

app.add_exception_handler(BaseAppException, app_exception_handler)