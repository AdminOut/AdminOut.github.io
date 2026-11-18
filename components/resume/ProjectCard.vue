<script setup lang="ts">
import type { Project } from "~/data/resume";

const props = defineProps<{ project: Project }>();

const [lead, ...thumbs] = props.project.screenshots ?? [];
</script>

<template>
  <article class="card project-card" :class="{ featured: project.featured }">
    <div class="project-media">
      <template v-if="lead">
        <figure class="browser-frame">
          <span class="browser-bar" aria-hidden="true"><i /><i /><i /></span>
          <img
            :src="lead.src"
            :alt="lead.alt"
            width="1280"
            height="720"
            loading="lazy"
          />
        </figure>
        <div v-if="thumbs.length" class="thumbs">
          <figure v-for="shot in thumbs" :key="shot.src" class="browser-frame">
            <span class="browser-bar" aria-hidden="true"><i /><i /><i /></span>
            <img
              :src="shot.src"
              :alt="shot.alt"
              width="1280"
              height="720"
              loading="lazy"
            />
          </figure>
        </div>
      </template>
      <figure v-else-if="project.illustration" class="illustration">
        <img
          :src="project.illustration.src"
          :alt="project.illustration.alt"
          width="1280"
          height="720"
          loading="lazy"
        />
      </figure>
      <div v-else class="illustration placeholder" aria-hidden="true" />
    </div>

    <div class="card-content">
      <p v-if="project.featured" class="eyebrow">Featured project</p>
      <h3 class="title is-4">{{ project.title }}</h3>
      <p class="client">{{ project.client }}</p>
      <p class="role">{{ project.role }}</p>

      <div class="content">
        <p>{{ project.summary }}</p>
        <ul>
          <li v-for="feature in project.features" :key="feature">
            {{ feature }}
          </li>
        </ul>
        <p v-if="project.outcome" class="outcome">{{ project.outcome }}</p>
      </div>

      <div class="tags">
        <span v-for="tech in project.stack" :key="tech" class="tag stack-tag">
          {{ tech }}
        </span>
      </div>
    </div>
  </article>
</template>

<style scoped lang="scss">
@import "@/assets/scss/variables";

.project-card {
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.project-media {
  padding: 1.25rem 1.25rem 0;
}

.browser-frame {
  margin: 0;
  border: 1px solid #dcdcdc;
  border-radius: 6px;
  overflow: hidden;
  background: #fff;

  img {
    display: block;
    width: 100%;
    height: auto;
    aspect-ratio: 16 / 9;
    object-fit: cover;
  }
}

.browser-bar {
  display: flex;
  gap: 5px;
  padding: 6px 8px;
  background: #ececec;
  border-bottom: 1px solid #dcdcdc;

  i {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #c4c4c4;
  }
}

.thumbs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.75rem;
  margin-top: 0.75rem;
}

.illustration {
  margin: 0;
  border-radius: 6px;
  overflow: hidden;
  aspect-ratio: 16 / 9;

  img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  &.placeholder {
    background: radial-gradient(
        circle at 25% 35%,
        rgba(255, 255, 255, 0.18) 0 6%,
        transparent 6.5%
      ),
      radial-gradient(
        circle at 70% 60%,
        rgba(255, 255, 255, 0.14) 0 9%,
        transparent 9.5%
      ),
      radial-gradient(
        circle at 55% 25%,
        rgba(255, 255, 255, 0.1) 0 4%,
        transparent 4.5%
      ),
      linear-gradient(135deg, darken($primary, 8%), lighten($primary, 12%));
  }
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;

  .content {
    flex: 1;
  }
}

.eyebrow {
  color: $primary;
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  margin-bottom: 0.25rem;
}

.title {
  margin-bottom: 0.25rem;
}

.client {
  color: #4a4a4a;
}

.role {
  color: $primary;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.outcome {
  font-weight: 600;
}

.stack-tag {
  background: lighten($primary, 62%);
  color: darken($primary, 6%);
  font-weight: 500;
}

@media print, screen and (min-width: 1024px) {
  .project-card.featured {
    flex-direction: row;

    .project-media {
      flex: 0 0 58%;
      padding: 1.5rem;
    }

    .card-content {
      padding: 1.5rem 1.5rem 1.5rem 0.5rem;
    }
  }
}

@media print {
  .thumbs {
    display: none;
  }

  .project-media {
    padding: 0.75rem 0.75rem 0;
  }

  .card-content {
    padding: 0.75rem;
  }
}
</style>
