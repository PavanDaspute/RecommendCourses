from fastapi import FastAPI
from fastapi.responses import JSONResponse
from users.routes import router as guest_router, user_router
from auth.route import router as auth_router
from starlette.middleware.authentication import AuthenticationMiddleware
from core.security import JWTAuth
import logging
from fastapi.middleware.cors import CORSMiddleware





app = FastAPI()
app.include_router(guest_router)
app.include_router(user_router)
app.include_router(auth_router)

logging.info("application starting")





# add Middelware
app.add_middleware(AuthenticationMiddleware, backend = JWTAuth())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to match your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def health_check():
    return JSONResponse(content={"status": "Running"})

