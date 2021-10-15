<template>
<div class="table-container container-lg mt-5">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">Rank</th>
            <th scope="col">CV</th>
            <th scope="col">Score</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="item in cv" :key="item.id">
            <th scope="row">{{ item.ranking }}</th>
            <td>{{ item.name }}</td>
            <td>{{ item.score }}</td>
          </tr>
        </tbody>
      </table>
    </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Table",
  props: ["cv"],
  data() {
    return {
      jd: {
        name: "AI_intern.docx",
      },
    };
  },
  methods: {
    getCv() {
      const path = "http://localhost:5000/cv";
      axios
        .get(path)
        .then((res) => {
          this.cv = res.data.cv;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
   created() {
    this.getCv();
  },
};
</script>

<style lang="scss" scoped>
.table {
  color: #fff;
  margin-bottom: 50px;
}
thead {
  th {
    font-size: 21px;
    font-weight: 600;
  }
}
td {
  word-break: break-all;
}
</style>