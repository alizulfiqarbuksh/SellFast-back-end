from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

# Controllers
from controllers.teas import router as TeasRouter
from controllers.comments import router as CommentsRouter
from controllers.users import router as UserRouter

app = FastAPI()

# CORS ✅ Allow your React dev server(s) to call the API
origins = [
    "*"
    # "http://localhost:5173",
    # "http://127.0.0.1:5173",
    # Later, add your deployed frontend origin, e.g.:
    # "https://your-frontend.example.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # Which sites can call this API
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],       # Allow all headers (e.g., Content-Type, Authorization)
)


# ROUTES

app.include_router(TeasRouter, prefix="/api")
app.include_router(CommentsRouter, prefix="/api")
app.include_router(UserRouter, prefix="/api")



# Example middleware
def help():
    return "SOS noooooow!!!!!"

@app.get("/")
def home(mamamia: str = Depends(help)):
    return {"message": mamamia}

@app.get("/health")
def health_check():
    return {"ok": True}