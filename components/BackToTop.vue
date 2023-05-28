<script setup lang="ts">
import { ref } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const isAtTop = ref(false);
const pathToTop = ref(`${route.path}#top`);
</script>

<template>
  <span id="top" tabindex="-1"></span>
  <a
    v-if="!isAtTop"
    id="back-to-top"
    title="Back to top"
    class="button is-rounded is-transparent"
    :href="pathToTop"
  >
    <span class="icon is-large"> &#8679; </span>
  </a>
</template>

<style scoped>
#back-to-top {
  position: fixed;
  bottom: 10px;
  float: right;
  right: 2%;
  left: 94%;
  color: #2b2b2b;
}
</style>
