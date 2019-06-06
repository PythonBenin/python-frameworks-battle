"""Review Model"""

from config.database import Model


class Review(Model):
    """Review Model"""
    __fillable__ = ['id', 'company', 'job', 'headline', 'pros', 'cons', 'user_id']

    @belongs_to('user_id', 'id')
    def user(self):
        from app.User import User
        return User