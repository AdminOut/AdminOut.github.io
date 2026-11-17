<script setup lang="ts">
import { earlierCareer, education, roles, skills } from "~/data/resume";
import { formatMonth } from "~/utils/period";
</script>

<template>
  <div class="cv">
    <!-- SKILLS -->
    <section class="section">
      <div class="container is-max-desktop">
        <h2 class="title is-3">Skills</h2>
        <div class="skills">
          <div v-for="group in skills" :key="group.name" class="skill-group">
            <h3 class="title is-6">{{ group.name }}</h3>
            <ul>
              <li v-for="item in group.items" :key="item">{{ item }}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- WORK HISTORY -->
    <section class="section light">
      <div class="container is-max-desktop">
        <h2 class="title is-3">Work history</h2>
        <ResumeRoleCard
          v-for="role in roles"
          :key="role.organisation"
          :role="role"
        />

        <h3 class="title is-5 earlier-heading">Earlier career: pharmacy</h3>
        <ul class="earlier">
          <li v-for="item in earlierCareer" :key="item.organisation">
            <strong>{{ item.organisation }}</strong
            >, {{ item.title }}
            <span class="dates">
              ({{ formatMonth(item.start) }} to {{ formatMonth(item.end) }})
            </span>
            <br />
            {{ item.line }}
          </li>
        </ul>
      </div>
    </section>

    <!-- EDUCATION -->
    <section class="section">
      <div class="container is-max-desktop">
        <h2 class="title is-3">Education</h2>
        <div class="media education">
          <div class="media-left">
            <figure class="image is-48x48">
              <img
                src="~assets/img/resume/wits.webp"
                :alt="education.institution"
                height="48"
                width="48"
              />
            </figure>
          </div>
          <div class="media-content">
            <p class="title is-5">
              {{ education.qualification }} ({{ education.year }})
            </p>
            <p class="subtitle is-6">{{ education.institution }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/scss/variables";

.skills {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem 2rem;
}

.skill-group {
  h3 {
    color: $primary;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.5rem;
  }

  li {
    margin-bottom: 0.25rem;
  }
}

.earlier-heading {
  margin-top: 2.5rem;
}

.earlier li {
  margin-bottom: 0.75rem;
}

.dates {
  color: #6b6b6b;
}
</style>
