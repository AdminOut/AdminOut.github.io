<script setup lang="ts">
useHead({
  title: "Portfolio: Lance Moore",
  meta: [
    {
      name: "description",
      content:
        "Selected projects by Lance Moore: integration platforms, ERPs and multi-tenant business systems.",
    },
  ],
});

definePageMeta({
  layout: "resume",
});
</script>

<template>
  <NuxtLayout>
    <ResumePortfolioContent />
  </NuxtLayout>
</template>
