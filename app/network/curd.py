from app.network.models import NetworkSegment
from sqlalchemy.orm import Session

def create_network_segment(db: Session, segment: str, sensitive_info_enabled: bool):
    new_segment = NetworkSegment(segment=segment, sensitive_info_enabled=sensitive_info_enabled)
    db.add(new_segment)
    db.commit()
    db.refresh(new_segment)
    print("-----new_segment-----:", new_segment)
    return new_segment

def get_network_segments(db: Session):
    return db.query(NetworkSegment).all()
