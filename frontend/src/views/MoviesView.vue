<script>
import MovieComponent from "../components/MovieComponent.vue";

export default {
  name: "MoviesView",
  components: {
    MovieComponent,
  },
  data() {
    return {
      popularMovies: [],
    };
  },
  created() {
    fetch(
      "https://api.themoviedb.org/3/movie/popular?api_key=c648045dfc27706ac42d6ac0ae9bffd1"
    )
      .then((response) => {
        response.json().then((res) => (this.popularMovies = res.results));
      })
      .catch((err) => {
        console.error(err);
      });
  },
  methods: {},
};
</script>
<template>
  <div class="movies-container">
    <MovieComponent
      v-for="(movie, index) in popularMovies"
      :key="index"
      :title="movie.title"
      :imageurl="movie.poster_path"
      :released="movie.release_date"
      :rating="movie.vote_average"
      :imdbid="movie.id"
      :clickable="true"
    ></MovieComponent>
  </div>
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
}
</style>
