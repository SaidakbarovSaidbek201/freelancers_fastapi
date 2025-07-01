from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, routers.freelancers
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="🧑‍💻💻 Freelancer API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "🧑‍💻💻 Freelancer API ishga tushdi. Barcha Freelancer uchun /freelancers/ manziliga o'ting."}


@app.get("/freelancers", response_model=list[schemas.Freelancer])
def read_freelancers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    freelancers = routers.freelancers.get_freelancers(db, skip=skip, limit=limit)
    return freelancers

@app.get("/freelancers/{freelancer_id}", response_model=schemas.Freelancer)
def read_freelancer(freelancer_id: int, db: Session = Depends(get_db)):
    freelancer = routers.freelancers.get_freelancer(db, freelancer_id=freelancer_id)
    if freelancer is None:
        raise HTTPException(status_code=404, detail="Bunaqa freelancer topilmadi")
    return freelancer

@app.post("/freelancers", response_model=schemas.Freelancer)
def create_freelancer(freelancer: schemas.FreelancerCreate, db: Session = Depends(get_db)):
    return routers.freelancers.create_freelancer(db=db, freelancer=freelancer)

@app.put("/freelancers/{freelancer_id}", response_model=schemas.Freelancer)
def update_freelancer(freelancer_id: int, freelancer: schemas.FreelancerUpdate, db: Session = Depends(get_db)):
    db_freelancer = routers.freelancers.update_freelancer(db=db, freelancer_id=freelancer_id, freelancer=freelancer)
    if db_freelancer is None:
        raise HTTPException(status_code=404, detail="Bunaqa freelancer topilmadi")
    return db_freelancer

@app.delete("/freelancers/{freelancer_id}", response_model=schemas.Freelancer)
def delete_freelancer(freelancer_id: int, db: Session = Depends(get_db)):
    db_freelancer = routers.freelancers.delete_freelancer(db=db, freelancer_id=freelancer_id)
    if db_freelancer is None:
        raise HTTPException(status_code=404, detail="Bunaqa freelancer topilmadi")
    return db_freelancer

@app.get("/freelancers/skill/{skill}", response_model=list[schemas.Freelancer])
def read_freelancers_by_skill(skill: str, db: Session = Depends(get_db)):
    freelancers = db.query(models.Freelancer).filter(models.Freelancer.skills.contains(skill)).all()
    if not freelancers:
        raise HTTPException(status_code=404, detail="Bunaqa freelancer topilmadi")
    return freelancers

@app.put("/freelancers/{freelancer_id}/status", response_model=schemas.Freelancer)
def update_freelancer_status(freelancer_id: int, status: str, db: Session = Depends(get_db)):
    db_freelancer = routers.freelancers.get_freelancer(db, freelancer_id=freelancer_id)
    if db_freelancer is None:
        raise HTTPException(status_code=404, detail="Bunaqa freelancer topilmadi")
    
    db_freelancer.status = status
    db.commit()
    db.refresh(db_freelancer)
    return db_freelancer    


