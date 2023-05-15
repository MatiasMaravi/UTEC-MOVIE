<script>
export default {
  name: "MovieView",
  components: {},
  data() {
    return {
      url: "",
      movie: {},
      imageStyle: {
        boxShadow: "0 0 25px rgba(0, 212, 255, 0.5)",
      },
      year: "",
      genres: [],
      genre_id: null,
      movie_id: null,
      favorite: false,
    };
  },
  created() {
    const apiKey = "c648045dfc27706ac42d6ac0ae9bffd1";
    const movieId = this.$route.params.code;

    fetch(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${apiKey}`)
      .then((response) => response.json())
      .then((data) => {
        this.movie = data;
        this.url = `https://image.tmdb.org/t/p/original${this.movie.poster_path}`;
        this.year = this.movie.release_date.slice(0, 4);
        this.genres = this.movie.genres;

        // Llama al método postGenre para el primer género encontrado en la lista de géneros
        this.postGenre(this.genres[0])
          .then(() => {
            // Llama a postMovie después de que se complete postGenre
            this.postMovie();
          })
          .catch((error) => {
            console.error(error);
          });
      })
      .catch((error) => {
        console.error(error);
      });
    const movieName = this.movie.title;
    fetch("http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8003/movies") // Reemplaza "https://ejemplo.com/api/peliculas" con la URL de tu API
      .then((response) => response.json()) // Convierte la respuesta en formato JSON
      .then((data) => {
        console.log("Data: ", data)
        // Verifica si la respuesta fue exitosa
        if (data.success) {
          // Verifica si hay películas en la respuesta
          if (data.movies && data.movies.length > 0) {
            // Busca la película por nombre
            const currentMovie = data.movies.find(
              (cMovie) => cMovie.title === this.movie.title
            );
            console.log("Current movie: ", currentMovie);
            if (currentMovie) {
              console.log("Movie ID:", currentMovie.id);
              console.log("Genre ID:", currentMovie.genre_id);
              this.movie_id = currentMovie.id;
              this.genre_id = currentMovie.genre_id;
            } else {
              console.log("No se encontró ninguna película con ese nombre.");
            }
          } else {
            console.log("No hay películas en la respuesta.");
          }
        } else {
          console.log("La solicitud no fue exitosa.");
        }
      })
      .catch((error) => {
        console.error("Ocurrió un error al obtener los datos:", error);
      });
  },
  methods: {
    postGenre(genre) {
      const genreData = {
        name: genre.name,
      };

      return new Promise((resolve, reject) => {
        fetch("http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8002/genres", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(genreData),
        })
          .then((response) => response.json())
          .then((data) => {
            console.log("Genre posted");
            console.log(data);
            if (!this.genre_id) {
              this.genre_id = data.genre.id;
              resolve(); // Resuelve la promesa después de asignar el genre_id
            }
          })
          .catch((error) => {
            reject(error); // Rechaza la promesa si ocurre un error
          });
      });
    },
    postMovie() {
      const movieData = {
        title: this.movie.title,
        genre_id: this.genre_id,
      };
      fetch("http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8003/movies", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(movieData),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log("Movie posted");
          this.movie_id = data.movies.id;
          console.log(data.movies.id);
        })
        .catch((error) => {
          console.error(error);
        });
    },
    async addFavorite() {
      try {
        console.log("Movie");
        console.log(this.movie_id);
        const response = await fetch(
          `http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8004/users/${this.$root.userId}/favorites`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              movie_id: this.movie_id,
            }),
          }
        );

        if (response.ok) {
          console.log("Película agregada a favoritos");
        } else {
          console.error("Error al agregar la película a favoritos");
        }
      } catch (error) {
        console.error(error);
      }
    },
    async deleteFavorite() {
      try {
        const response = await fetch(
          `http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8004/users/${this.$root.userId}/favorites/${this.movie_id}`,
          {
            method: "DELETE",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              movie_id: this.movie_id,
            }),
          }
        );

        if (response.ok) {
          console.log("Película eliminada de favoritos");
        } else {
          console.error("Error al eliminar la película de favoritos");
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<template>
  <div class="info">
    <img :src="url" :style="imageStyle" class="poster" />
    <div>
      <h1>{{ movie.title }}</h1>
      <div class="rating">
        <h4>{{ movie.vote_average }}</h4>
        <img src="@/assets/star-icon.svg" />
      </div>
      <div class="details">
        <p>Year: {{ year }}</p>
        <p>Runtime: {{ movie.runtime }} minutes</p>
      </div>
      <div class="genre">
        <div v-for="(genre, index) in movie.genres" :key="index">
          {{ genre.name }}
        </div>
      </div>
      <h3>Plot:</h3>
      <div class="summary">{{ movie.overview }}</div>
      <div class="button-container" v-if="$root.userId">
        <button class="addFavorite-button" @click="addFavorite">
          Add to your favorites
        </button>
      </div>
      <div class="button-container" v-if="$root.userId">
        <button class="addFavorite-button" @click="deleteFavorite">
          Delete from your favorites
        </button>
      </div>
      <div v-else>
        <h2>Sign in to add your favorite movies!</h2>
      </div>
    </div>
  </div>
</template>

<style scoped>
.info {
  position: relative;
  display: grid;
  grid-template-columns: 3fr 8fr;
  margin-top: 1.5em;
}

.poster {
  width: 310px;
}

.genre {
  display: flex;
  justify-content: space-evenly;
}

.genre div {
  border: 2px solid #686868;
  font-size: 1.25em;
  padding: 0.4em 0.4em;
  border-radius: 0.4em;
  font-weight: 500;
  color: rgb(0, 212, 255);
}

.details {
  display: flex;
  justify-content: space-evenly;
  font-size: 1.25em;
  color: #a0a0a0;
  margin: 0.6em 5em;
  font-weight: 300;
}

h1 {
  text-align: center;
  font-size: 4em;
  font-weight: bold;
  line-height: 1em;
  color: #00d4ff;
}

h2 {
  text-align: center;
  font-size: 2em;
  font-weight: bold;
  line-height: 1em;
  margin-top: 1em;
  color: #00d4ff;
}

h3 {
  display: flex;
  align-items: left;
  justify-content: left;
  font-size: 2em;
  margin: 10px;
  font-weight: 500;
  color: #00d4ff;
}

.summary {
  display: flex;
  align-items: left;
  justify-content: left;
  margin: 10px;
  font-size: 1.25em;
  font-weight: 700;
}

.rating {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.6em;
  margin: 0.6em 0 0.9em 0;
}

.rating img {
  width: 1.5em;
}

.rating h4 {
  display: inline-block;
  font-size: 1.5em;
  font-weight: 500;
}

.button-container {
  margin-top: 10px;
}

button {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 0.4em;
  font-weight: bolder;
  background-color: #00d4ff;
  color: white;
  border: none;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #00a7cc;
}

.addFavorite-button {
  width: 100%;
  max-width: 300px; /* Ajusta el valor según el ancho deseado */
  margin: 0 auto; /* Centra horizontalmente el botón */
}

@media (min-width: 1024px) {
}
</style>
