<script>
import MovieComponent from "../components/MovieComponent.vue";

export default {
  name: "FavoritesView",
  components: {
    MovieComponent,
  },
  data() {
    return {
      popularMovies: [],
      favoriteMovies: [],
      movies: [],
      arrMovie: [],
      intersectedMovies: [],
    };
  },
  mounted() { // Cambio: Usa el evento mounted en lugar de created
    fetch(
      "https://api.themoviedb.org/3/movie/popular?api_key=c648045dfc27706ac42d6ac0ae9bffd1"
    )
      .then((response) => {
        response.json().then((res) => (this.popularMovies = res.results));
      })
      .catch((err) => {
        console.error(err);
      });
    fetch(
      `http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8004/users/${this.$root.userId}/favorites`
    )
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          if (data.favorites && data.favorites.length > 0) {
            this.favoriteMovies = data.favorites;
          }
        } else {
          console.log("La solicitud no fue exitosa.");
        }
      })
      .catch((error) => {
        console.error("Ocurrió un error al obtener los datos:", error);
      });
    fetch(
      "http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8003/movies"
    )
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          if (data.movies && data.movies.length > 0) {
            this.movies = data.movies;
            this.getIntersection();
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
    getIntersection() {
      this.intersectedMovies = this.movies.find((movie) =>
        movie.id === 5,
      );
    },
  },
};
</script>
<template>
  <div>Favorite: {{ this.favoriteMovies }}</div>
  <div>Movie: {{ this.movies }}</div>
  <div>Intersected: {{ this.intersectedMovies }}</div>
  <div class="movies-container" v-if="$root.isLoggedIn">
    <MovieComponent
      v-for="(movie, index) in intersectedMovies"
      :key="index"
      :title="movie.title"
      :imageurl="movie.poster_path"
      :released="movie.release_date"
      :rating="movie.vote_average"
      :imdbid="movie.id"
      :clickable="true"
    ></MovieComponent>
  </div>
  <div class="notLogin" v-else>Sign in to watch your favorites movies!</div>
</template>

<style scoped>
@media (min-width: 1024px) {
  input {
    line-height: 2em;
  }

  .movies-container {
    text-align: center;
    overflow-y: auto;
    vertical-align: middle;
    display: grid;
    grid-template-columns: auto auto auto;
    grid-gap: 10px;
    padding: 10px;
  }

  .notLogin {
    font-weight: bold;
    font-size: larger;
    margin: 20px;
  }
}
</style>
