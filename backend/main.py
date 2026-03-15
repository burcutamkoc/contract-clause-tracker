from fastapi import FastAPI
from src.core.database import SessionLocal, Base, engine
from fastapi.middleware.cors import CORSMiddleware

from src.api.controller.contract_controller import router as contract_router
from src.api.controller.clause_type_controller import router as clause_router
from src.api.controller.sentence_controller import router as sentence_router

from src.infra.config.seed_data import seed_clause_types

# entity import (required for SQLAlchemy)
from src.infra.repository.entities.contract_entity import Contract
from src.infra.repository.entities.sentence_entity import Sentence
from src.infra.repository.entities.clause_type_entity import ClauseType
from src.infra.repository.entities.sentence_label_entity import SentenceLabel


app = FastAPI(
    title="Contract Clause Tracker API",
    description="API for uploading contracts and labeling legal clauses",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():

    # create tables
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    seed_clause_types(db)

    db.close()


app.include_router(contract_router)
app.include_router(clause_router)
app.include_router(sentence_router)