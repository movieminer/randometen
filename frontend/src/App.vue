<template>
  <router-view />
</template>

<script></script>

<style>
body {
  background-repeat: no-repeat;
  background-size: cover;
  background: linear-gradient(
    0deg,
    rgb(70, 141, 46) 0%,
    rgb(228, 223, 148) 75%,
    rgb(225, 145, 145) 99%
  );
  min-width: calc(
    100vw - env(safe-area-inset-right) - env(safe-area-inset-left)
  );
  min-height: calc(
    100vh - env(safe-area-inset-bottom) - env(safe-area-inset-top)
  );
  min-height: -webkit-fill-available;
  padding: env(safe-area-inset-top) env(safe-area-inset-right)
    env(safe-area-inset-bottom) env(safe-area-inset-left);
}
</style>
