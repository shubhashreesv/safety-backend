from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import AdminUser, Product, ProductViewEvent, EnquiryClickEvent
from app.routes.auth import router as auth_router
from app.routes.products import router as product_router
from app.routes.analytics import router as analytics_router
from app.routes import chatbot

app = FastAPI(title="Product Enquiry API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def create_tables():
    from app.database import Base
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(analytics_router)


app.include_router(chatbot.router)


#from fastapi import FastAPI
#from app.database import engine
#from app.models import AdminUser, Product, ProductViewEvent, EnquiryClickEvent
#from app.routes import auth
#from app.routes.auth import router as auth_router 
#from app.routes.products import router as product_router
#from app.routes.analytics import router as analytics_router

#app = FastAPI(title="Product Enquiry API")

#@app.on_event("startup")
#def create_tables():
#    from app.database import Base 
#    Base.metadata.create_all(bind=engine) 

#@app.get("/health")
#def health_check():
#    return {"status": "ok"}

#app.include_router(auth.router, prefix="/auth", tags=["Auth"])
#app.include_router(product_router)
#app.include_router(analytics_router)
