<script setup lang="ts">
import { earlierProjects, projects } from "~/data/resume";

const featured = projects.filter((p) => p.featured);
const rest = projects.filter((p) => !p.featured);
</script>

<template>
  <section class="section portfolio">
    <div class="container">
      <h2 class="title is-3">Portfolio</h2>
      <p class="subtitle is-6 note">
        Screenshots use demo data. Clients are named only where the work is
        already public.
      </p>

      <div
        v-for="project in featured"
        :key="project.title"
        class="featured-row"
      >
        <ResumeProjectCard :project="project" />
      </div>

      <div class="columns is-multiline">
        <div
          v-for="project in rest"
          :key="project.title"
          class="column is-half"
        >
          <ResumeProjectCard :project="project" />
        </div>
      </div>

      <h3 class="title is-5 earlier-heading">Earlier projects</h3>
      <ul class="earlier">
        <li v-for="item in earlierProjects" :key="item.title">
          <strong>{{ item.title }}</strong>
          <span v-if="item.stack" class="stack"> ({{ item.stack }})</span>.
          {{ item.line }}
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped lang="scss">
.note {
  color: #6b6b6b;
}

.featured-row {
  margin-bottom: 1.5rem;
}

.earlier-heading {
  margin-top: 2rem;
}

.earlier li {
  margin-bottom: 0.75rem;
}

.stack {
  color: #6b6b6b;
}
</style>
