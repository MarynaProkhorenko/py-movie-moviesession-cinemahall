from django.db.models import QuerySet

from db.models import MovieSession
import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    new_movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )
    return new_movie_session


def get_movies_sessions(session_date: str = None) -> QuerySet:
    movies_sessions_set = MovieSession.objects.all()

    if session_date is not None:
        movies_sessions_set = movies_sessions_set.filter(
            show_time__date=datetime.datetime.strptime(
                session_date, "%Y-%m-%d"
            )
        )
    return movies_sessions_set


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: datetime = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)
    if show_time is not None:
        movie_session.show_time = show_time
        movie_session.save()
    if movie_id is not None:
        movie_session.movie_id = movie_id
        movie_session.save()
    if cinema_hall_id is not None:
        movie_session.cinema_hall_id = cinema_hall_id
        movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session_to_delete = MovieSession.objects.get(id=session_id)
    movie_session_to_delete.delete()