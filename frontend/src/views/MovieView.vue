<script>
export default {
  name: "MovieView",
  components: {},
  data() {
    return {
      url: "",
      movie: {},
      imageStyle: {
        boxShadow: '0 0 25px rgba(0, 212, 255, 0.5)',
      },
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
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {},
};
</script>

<template>
  <div class="info">
    <img :src=url :style=imageStyle class="poster" />
    <div>
      <h1> {{ movie.title }} </h1>
      <div class="rating">
        <h4>{{ movie.vote_average }}</h4>
        <img src="@/assets/star-icon.svg" />
      </div>
      <h3>Plot:</h3>
      <div class="summary">{{ movie.overview }}</div>
    </div>
  </div>
</template>

<style scoped>
.info{
    position: relative;
    display: grid;
    grid-template-columns: 3fr 8fr;
    margin-top: 1.5em;
}

.poster{
    width: 300px;
}

h1{
    text-align: center;
    font-size: 4em;
    font-weight: bold;
    line-height: 1em;
    color: #00d4ff;
}

h3{
  display: flex;
  align-items: left;
  justify-content: left;
  font-size: 2em;
  margin: 10px;
  font-weight: 500;
  color: #00d4ff;
}

.summary{
  display: flex;
  align-items: left;
  justify-content: left;
  margin: 10px;
  font-size: 1.25em;
  font-weight: 700;
}

.rating{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.6em;
    margin: 0.6em 0 0.9em 0;
}

.rating img{
    width: 2em;
}

.rating h4{
    display: inline-block;
    font-size: 2em;
    font-weight: 500;
}

@media (min-width: 1024px) {
}
</style>
