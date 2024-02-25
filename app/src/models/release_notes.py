import uuid
from datetime import datetime
from sqlmodel import SQLModel,Field,Session
from feed import feed, entry

class ReleaseNote(SQLModel, table=True):
    __tablename__ = "release_notes"
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    title: str
    url: str
    created_at: datetime = Field(default_factory=datetime.now, nullable=False)

    def getEntryString(self, db:Session)->str:
        return entry.format(id=self.id,title=self.title,url=self.url,updated_at=self.created_at.isoformat(),summary="*")
