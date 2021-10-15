<template>
  <div class="home">
    <div class="post-container container-lg">
      <div class="post-container__header">
        <div class="page-logo"></div>
        <h3 class="post-title">Find the right candidate</h3>
      </div>
      <form
        id="fileForm"
        ref="fileForm"
        @submit.prevent="matching"
        class="post-container__form"
        enctype="multipart/form-data"
      >
        <div class="post-container__file">
          <div class="cv-box">
            <div class="cv-icon"></div>
            <div class="cv-box__file file-loading">
              <label for="cv-input">Upload a cv folder</label>
              <input
                class="cv--choose"
                id="cv-input"
                type="file"
                name="cvFile"
                webkitdirectory
                @change="uploadCV($event)"
                required
              />
            </div>
          </div>
          <div class="jd-box">
            <div class="jd-icon"></div>
            <div class="jd-box__file file-loading">
              <label for="jd-input">Upload a jd file</label>
              <input
                class="jd--choose"
                id="jd-input"
                type="file"
                name="jdFile"
                webkitdirectory
                @change="uploadJD($event)"
                required
              />
            </div>
          </div>
        </div>
        <div class="select_jd">
          <label for="">Select a JD</label><br/>
          <select v-model="jdIndex" id="" required>
            <option selected="selected">Select a JD</option>
            <option v-for="(jd, index) in jdFile" :key="index" :value=index >JD {{jd.name}}</option>
          </select>
        </div>
        <div class="post-container__submit">
          <button type="submit" class="btn-submit"></button>
        </div>
      </form>
    </div>
    <Table :cv=cv v-show="!loading"></Table>
    <loading v-show="loading"></loading>
  </div>
</template>

<script>
import Table from "../components/Table.vue";
import axios from "axios";
import Loading from '../components/Loading.vue';

export default {
  name: "Home",
  components: { Table, Loading },
  data() 
    {
    return {
      loading: false,
      cv: [],
      cvFile: [],
      jdFile: [],
      jdIndex: 0,
    };
  },
  methods: {
    uploadCV(event) {
      this.cvFile = event.target.files;

    },
    uploadJD(event) {
      this.jdFile = event.target.files;
    },
    getCv() {
      this.loading = true;
      const path = "http://localhost:5000/cv";
      axios
        .get(path)
        .then((res) => {
          this.cv = res.data.cv;
          this.loading = false;
        })
        .catch((error) => {
          console.error(error);
          this.loading = false;
        });
    },
    async matching() {
      this.loading = true;
      const data = new FormData();

      data.append("name", "my-file");
      data.append("jdIndex", this.jdIndex);
      this.cvFile.forEach(element => {
        data.append("cvFile", element);
      });
      this.jdFile.forEach(element => {
        data.append("jdFile", element);
      });

      let config = {
        header: {
          "Content-Type": "multipart/form-data",
        },
      };

      console.log(...data.entries());
      const path = "http://localhost:5000/cv";
      axios
        .post(path, data, config)
        .then(() => {
          this.getCv();
          this.loading = false;
        })
        .catch((error) => {
          alert(error);
          this.loading = false;
        });
    },
  },
  created() {
    this.getCv();
  },
};
</script>

<style lang="scss" scoped>
@import "../assets/scss/style.scss";

.home {
  display: flex;
  flex-direction: column;
  position: relative;
  background-image: url(../assets/images/cover.jpg);
  z-index: 1;
  min-height: 100vh;
}

.home * {
  z-index: 3;
}

.home::before {
  z-index: 2;
  content: "";
  width: 100%;
  height: 100%;
  background-color: #555;
  position: absolute;
  opacity: 0.7;
  top: 0;
  left: 0;
}

.post-container {
  display: flex;
  flex-direction: column;
}
.post-container__header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-top: 30px;

  .post-title {
    font-size: 28px;
    font-weight: 500;
    margin: 0;
    padding-left: 10px;
    font-family: $font-1;
    color: #fff;
  }
  .page-logo {
    height: 60px;
    width: 60px;
    background-color: #fff;
    color: #fff;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background-size: cover;
    background-image: url(../assets/images/logo-bap.png);
  }
}
.post-container__form {
  margin-top: 80px;
  display: flex;
  flex-direction: column;
}

.post-container__file {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  height: 200px;
}

.cv-box {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: 0 10px;

  .cv-icon {
    padding: 5px;
    height: 75px;
    width: 50px;
    background-size: 100%;
    background-image: url(../assets/icons/cv.svg);
    background-repeat: no-repeat;
    margin-left: 47%;
  }
  .cv-box__file {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    width: 100%;
    margin-top: 20px;
    height: 100%;
    border-radius: 8px;
    padding: 10px;
    background-color: rgb(224, 224, 224);
    label {
      cursor: pointer;
      font-family: $font-1;
      padding: 5px;
      margin-bottom: 10px;
      width: 50%;
      text-align: center;
      border-radius: 8px;
      background-color: #fff2cc;
    }
    label:hover {
      background-color: #f3de9f;
    }
  }
  .cv-box__file::before {
    content: "";
    display: block;
    position: absolute;
    top: -15px;
    left: 49%;

    @include triangle(15px, rgb(224, 224, 224));
  }
}

.cv--input {
  border: none;
  outline: none;
  padding: 10px;
  padding-top: 0;
  color: rgb(71, 71, 71);
  border-radius: 8px;
  width: 100%;
  height: 100%;
  background-color: transparent;
}

.jd-box {
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: 0 10px;

  .jd-icon {
    padding: 5px;
    height: 75px;
    width: 50px;
    margin-left: 20px;
    background-size: 100%;
    background-image: url(../assets/icons/job.svg);
    background-repeat: no-repeat;
    margin-left: 48%;
  }
  .jd-box__file {
    display: flex;
    flex-direction: column;
    align-items: center;
    position: relative;
    width: 100%;
    margin-top: 20px;
    height: 100%;
    border-radius: 8px;
    padding: 10px;
    background-color: rgb(224, 224, 224);
    label {
      cursor: pointer;
      font-family: $font-1;
      padding: 5px;
      margin-bottom: 10px;
      width: 50%;
      text-align: center;
      border-radius: 8px;
      background-color: #fff2cc;
    }
    label:hover {
      background-color: #f3de9f;
    }
    #preview {
      text-align: center;
      max-height: 230px;
      margin-top: 20px;
      object-fit: contain;
    }
  }
  .jd-box__file::before {
    content: "";
    display: block;
    position: absolute;
    top: -15px;
    left: 49%;

    @include triangle(15px, rgb(224, 224, 224));
  }
}

.post-box__image::before {
  content: "";
  display: block;
  position: absolute;
  top: -15px;
  left: 70px;

  @include triangle(15px, rgb(224, 224, 224));
}
.post-box__image--choose {
  display: none;
}

.select_jd {
  margin-top: 20px;
  label {
    font-family: $font-1;
    color: #fff;
    font-size: 19px;
    font-weight: 400;
  }
  select {
    outline: none;
    border-radius: 5px;
    padding: 5px;
  }
}

.post-container__submit {
  display: flex;
  justify-content: center;
  .btn-submit {
    background-color: transparent;
    border: none;
    padding: 5px;

    height: 70px;
    width: 70px;
    margin: 20px 20px;
    background-size: 100%;
    background-image: url(../assets/icons/start-button.svg);
  }

  .btn-submit:hover {
    box-shadow: rgba(255, 255, 255, 0.56) 0px 22px 70px 4px;
  }
}

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
