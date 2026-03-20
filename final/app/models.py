from app import db

class Report(db.Model):
    __tablename__ = 'reports'
    
    id = db.Column(db.String(20), primary_key=True) 
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default='Pending')
    email = db.Column(db.String(120), nullable=True)
    upvotes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Report {self.id}>'
