from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.network.database import get_db
from app.network.models import NetworkSegment
from app.network.curd import create_network_segment,get_network_segments

router = APIRouter()

@router.post("/network-segments/")
def add_network_segment(segment: str, sensitive_info_enabled: bool, db: Session = Depends(get_db)):
    return create_network_segment(db, segment, sensitive_info_enabled)

@router.get("/network-segments/")
def list_network_segments(db: Session = Depends(get_db)):
    return get_network_segments(db)