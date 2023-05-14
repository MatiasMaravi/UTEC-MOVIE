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
      genre: "",
      genreId: null,
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
        this.genre = this.genres[0];

        // Calling the postGenre() method for each genre
        this.postGenre(genre);

        // Calling the postMovie() method to add each movie
        this.postMovie();
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {
    postGenre(genre) {
      const genreData = {
        name: genre.name,
      };

      fetch("https://ejemplo.com/api/genres", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(genreData),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (!this.firstGenreId) {
            this.firstGenreId = data.id;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
    postMovie() {
      const movieData = {
        title: this.movie.title,
        genre_id: this.genreId,
      };

      fetch("https://ejemplo.com/api/movies", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(movieData),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error(error);
        });
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
  width: 300px;
}

.genre {
  display: flex;
  justify-content: space-evenly;
}

.genre div {
  border: 2px solid #686868;
  font-size: 1.5em;
  padding: 0.4em 0.4em;
  border-radius: 0.4em;
  font-weight: 500;
  color: rgb(0, 212, 255);
}

.details {
  display: flex;
  justify-content: space-evenly;
  font-size: 1.5em;
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

@media (min-width: 1024px) {
}
</style>
