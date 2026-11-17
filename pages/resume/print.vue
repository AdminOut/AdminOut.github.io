<script setup lang="ts">
useHead({
  title: "Resume and portfolio: Lance Moore",
  meta: [
    {
      name: "description",
      content: "Printable resume and portfolio of Lance Moore.",
    },
    // The same content lives on /resume/cv and /resume/portfolio.
    { name: "robots", content: "noindex" },
  ],
});

definePageMeta({
  layout: "resume",
});

function print() {
  window.print();
}
</script>

<template>
  <NuxtLayout>
    <div class="container no-print print-actions">
      <button class="button is-primary" @click="print">
        Print or save as PDF
      </button>
    </div>
    <ResumeCvContent />
    <div class="print-page-break" />
    <ResumePortfolioContent />
  </NuxtLayout>
</template>

<style scoped>
.print-actions {
  padding: 1.5rem 1.5rem 0;
  text-align: right;
}
</style>
