from sqlalchemy.orm import Session

from src.infra.repository.entities.clause_type_entity import ClauseType


def seed_clause_types(db: Session):

    existing = db.query(ClauseType).count()

    if existing > 0:
        return

    default_types = [
        "Limitation of Liability",
        "Termination for Convenience",
        "Non-Compete"
    ]

    for name in default_types:
        clause = ClauseType(name=name)
        db.add(clause)

    db.commit()