from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///movies.db'
db=SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title=StringField("Movie Title",  validators=[DataRequired()]) 
    submit=SubmitField("Add Movie")   

@app.route("/")
def home():
    result=db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies=result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking=len(all_movies) - i
    db.session.commit()    
    return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def editMovie():
    form=RateMovieForm()
    movie_id=request.args.get('id')
    movie=db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating=float(form.rating.data)
        movie.review=form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie, form=form)

@app.route("/delete")
def deleteMovie():
    movie_id=request.args.get('id')
    movie_to_delete=db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def addMovie():
    form=AddMovieForm()

    if form.validate_on_submit():
        movie_title=form.title.data
        response=requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key":"0865eeb586b19c233eedcecd13e24fe8", "query": movie_title})
        data=response.json()["results"]
        return render_template("select.html", options=data)
    
    return render_template("add.html", form=form)

@app.route("/find")
def findMovie():
    movie_id=request.args.get('id')
    if movie_id:
        movie_api_url=f"https://api.themoviedb.org/3/movie/{movie_id}"
        response=requests.get(movie_api_url, params={"api_key":"0865eeb586b19c233eedcecd13e24fe8", "language":"en-US" })
        data=response.json()
        new_movie=Movie(
            title=data['title'],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('editMovie', id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
