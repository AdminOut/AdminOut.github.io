<script setup lang="ts">
useHead({
  title: "Resume: Lance Moore",
  meta: [
    {
      name: "description",
      content:
        "Lance Moore, senior software engineer and integration specialist: skills and work history.",
    },
  ],
});

definePageMeta({
  layout: "resume",
});
</script>

<template>
  <NuxtLayout>
    <ResumeCvContent />
  </NuxtLayout>
</template>
