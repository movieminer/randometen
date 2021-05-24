<template>
  <Bubbles></Bubbles>
  <div class="home p-6">

  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Bubbles from "@/components/Bubbles.vue";

@Options({
  components: {
    Bubbles,
  },
})
export default class Index extends Vue {}
</script>
