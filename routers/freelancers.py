from sqlalchemy.orm import Session
import models, schemas


def get_freelancers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Freelancer).offset(skip).limit(limit).all()


def get_freelancer(db: Session, freelancer_id: int):
    return db.query(models.Freelancer).filter(models.Freelancer.id == freelancer_id).first()


def create_freelancer(db: Session, freelancer: schemas.FreelancerCreate):
    db_freelancer = models.Freelancer(
        full_name=freelancer.full_name,
        phone_number=freelancer.phone_number,
        skills=freelancer.skills,
        status=freelancer.status,

    )
    db.add(db_freelancer)
    db.commit()
    db.refresh(db_freelancer)
    return db_freelancer


def update_freelancer(db: Session, freelancer_id: int, freelancer: schemas.FreelancerUpdate):   
    db_freelancer = db.query(models.Freelancer).filter(models.Freelancer.id == freelancer_id).first()
    if db_freelancer:
        if freelancer.full_name is not None:
            db_freelancer.full_name = freelancer.full_name
        if freelancer.phone_number is not None:
            db_freelancer.phone_number = freelancer.phone_number
        if freelancer.skills is not None:
            db_freelancer.skills = freelancer.skills
        if freelancer.status is not None:
            db_freelancer.status = freelancer.status
        if freelancer.joined_at is not None:
            db_freelancer.joined_at = freelancer.joined_at
        db.commit()
        db.refresh(db_freelancer)
    return db_freelancer

def delete_freelancer(db: Session, freelancer_id: int):
    db_freelancer = db.query(models.Freelancer).filter(models.Freelancer.id == freelancer_id).first()
    if db_freelancer:
        db.delete(db_freelancer)
        db.commit()
    return db_freelancer

