from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
]

bookings = []

# -------------------- Movies APIs --------------------

@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200


@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie_by_id(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    movies.append(data)
    return jsonify({"message": "Movie added successfully"}), 201


@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    data = request.json
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(data)
            return jsonify({"message": "Movie updated"}), 200
    return jsonify({"error": "Movie not found"}), 404


@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404


# -------------------- Booking API --------------------

@app.route("/api/bookings", methods=["POST"])
def book_tickets():
    data = request.json

    movie_id = data.get("movie_id")
    seats = data.get("seats")

    if not movie_id or not seats:
        return jsonify({"error": "Invalid booking data"}), 400

    for movie in movies:
        if movie["id"] == movie_id:
            booking = {
                "movie_id": movie_id,
                "seats": seats,
                "total_price": seats * movie["price"]
            }
            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Movie not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
