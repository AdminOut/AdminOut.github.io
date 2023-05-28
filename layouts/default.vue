<script setup lang="ts">
import BackToTop from "~/components/BackToTop.vue";
import NavBar from "~/components/NavBar.vue";
import AppFooter from "~/components/AppFooter.vue";
</script>

<template>
  <div>
    <BackToTop />
    <NavBar />
    <slot />
    <AppFooter />
  </div>
</template>

<style scoped></style>
