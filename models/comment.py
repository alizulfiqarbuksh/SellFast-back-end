from .base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class CommentModel(BaseModel):

  __tablename__ = "comments"

  id = Column(Integer, primary_key=True, index=True)
  content = Column(String, nullable=False)

  # relationships
  tea_id = Column(Integer, ForeignKey('teas.id', ondelete="CASCADE"), nullable=False)
  tea = relationship('TeaModel', back_populates='comments', passive_deletes=True)