from sqlalchemy import Boolean, Column, Integer, String

from db.session import Base

# DAO MODEL


class Dao(Base):
    __tablename__ = "daos"

    id = Column(Integer, primary_key=True, index=True)
    dao_name = Column(String)
    dao_short_description = Column(String)
    dao_url = Column(String)
    governance_id = Column(Integer)
    tokenomics_id = Column(Integer)
    design_id = Column(Integer)
    is_draft = Column(Boolean)
    is_published = Column(Boolean)
    nav_stage = Column(Integer)
    is_review = Column(Boolean)
