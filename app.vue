<script setup>
useHead({
  htmlAttrs: {
    lang: "en",
  },
  titleTemplate: (titleChunk) => {
    return titleChunk
      ? `${titleChunk} | Adminout`
      : "Custom software development | Adminout";
  },
  meta: [
    {
      name: "description",
      content:
        "Custom software development house and payment solution specialist.",
    },
  ],
});
</script>
<template>
  <div>
    <NuxtPage />
  </div>
</template>
