<script setup lang="ts">
import type { Role } from "~/data/resume";
import { formatPeriod } from "~/utils/period";

const props = defineProps<{ role: Role }>();
const now = useNow();
const period = computed(() =>
  formatPeriod(props.role.start, props.role.end, now)
);
</script>

<template>
  <article class="card role-card">
    <div class="card-content">
      <div class="media">
        <div class="media-left">
          <figure v-if="role.logo" class="image is-48x48">
            <img
              :src="role.logo"
              :alt="role.organisation"
              width="48"
              height="48"
            />
          </figure>
          <span v-else class="initials" aria-hidden="true">
            {{ role.initials }}
          </span>
        </div>
        <div class="media-content">
          <h3 class="title is-5">{{ role.organisation }}</h3>
          <p class="role-title">{{ role.title }}</p>
          <p class="period">{{ period }}</p>
        </div>
      </div>

      <div class="content">
        <p class="summary">{{ role.summary }}</p>
        <ul>
          <li v-for="item in role.highlights" :key="item">{{ item }}</li>
        </ul>
      </div>
    </div>
  </article>
</template>

<style scoped lang="scss">
@import "@/assets/scss/variables";

.role-card {
  margin-bottom: 1.5rem;
}

.initials {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 48px;
  height: 48px;
  border-radius: 8px;
  background: $primary;
  color: #fff;
  font-weight: 700;
  letter-spacing: 0.05em;
}

.role-title {
  font-weight: 600;
  color: $primary;
  text-transform: uppercase;
  font-size: 0.85rem;
  letter-spacing: 0.04em;
}

.period {
  color: #6b6b6b;
  font-size: 0.9rem;
}

.summary {
  font-style: italic;
  color: #4a4a4a;
}
</style>
