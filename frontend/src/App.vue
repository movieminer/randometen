<template>
  <router-view />
</template>

<script></script>

<style>
body {
  background: rgb(255, 173, 0);
  background-repeat: no-repeat;
  background-size: cover;
  background: linear-gradient(
    0deg,
    rgba(255, 173, 0, 1) 0%,
    rgba(255, 229, 0, 1) 95%,
    rgba(255, 255, 255, 1) 99%
  );
  min-width: 100vw;
  min-height: 100vh;
  padding: env(safe-area-inset-top) env(safe-area-inset-right)
    env(safe-area-inset-bottom) env(safe-area-inset-left);
}
</style>
