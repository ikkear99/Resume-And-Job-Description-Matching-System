<template>
  <div class="body-container">
    <div class="loading-container">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.body-container {
  margin-top: 20px;
  margin-bottom: 50px;
  background-color: transparent;
  padding: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;

  .loading-container {
    height: 60px;
    width: 60px;
    animation-name: rotate1;
    animation-duration: 2.5s;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
    position: relative;

    .dot {
      height: 100%;
      width: 100%;
      position: absolute;
      animation-name: rotate1;
      animation-duration: 2s;
      animation-timing-function: ease-in-out;
      animation-iteration-count: infinite;
    }

    .dot::before {
      content: "";
      height: 25%;
      width: 25%;
      border-radius: 50%;
      position: absolute;
      animation-name: scale;
      animation-duration: 2s;
      animation-delay: inherit;
      animation-iteration-count: infinite;
      background-color: #fff;
    }

    .dot:nth-of-type(1) {
      animation-delay: -1.1s;
    }

    .dot:nth-of-type(2) {
      animation-delay: -1s;
    }

    .dot:nth-of-type(3) {
      animation-delay: -0.9s;
    }

    .dot:nth-of-type(4) {
      animation-delay: -0.8s;
    }

    .dot:nth-of-type(5) {
      animation-delay: -0.7s;
    }

    .dot:nth-of-type(6) {
      animation-delay: -0.6s;
    }
  }
}

@keyframes rotate1 {
  100% {
    transform: rotate(360deg);
  }
}

@keyframes scale {
  50% {
    transform: scale(0.5);
  }
  100% {
    transform: scale(1);
  }
}
</style>