from app import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    platform = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="Not Started")
    added_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        """Convert object to dictionary format (for JSON responses)"""
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "platform": self.platform,
            "status": self.status,
            "added_at": self.added_at.strftime("%Y-%m-%d %H:%M:%S")
        }