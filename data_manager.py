from models import db, User, Movie


class DataManager:
    def create_user(self, name):
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_users(self):
        return User.query.all()

    def get_movies(self, user_id):
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        db.session.add(movie)
        db.session.commit()
        return movie

    def update_movie(self, movie_id, name=None, director=None, year=None, poster_url=None):
        movie = Movie.query.get(movie_id)

        if movie is None:
            return None

        if name is not None:
            movie.name = name

        if director is not None:
            movie.director = director

        if year is not None:
            movie.year = year

        if poster_url is not None:
            movie.poster_url = poster_url

        db.session.commit()
        return movie

    def delete_movie(self, movie_id):
        movie = Movie.query.get(movie_id)

        if movie is None:
            return False

        db.session.delete(movie)
        db.session.commit()
        return True