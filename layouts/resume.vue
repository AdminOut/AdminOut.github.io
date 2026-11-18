<script setup lang="ts">
import { useRoute } from "vue-router";
import BackToTop from "~/components/BackToTop.vue";
import { profile } from "~/data/resume";
import { yearsSince } from "~/utils/period";

const route = useRoute();
const now = useNow();

const years = yearsSince(profile.softwareSince, now);
const bio = profile.bio.map((p) => p.replace("{years}", String(years)));

const isRouteActive = (path: string) => {
  return route.path === path;
};
</script>

<template>
  <div>
    <BackToTop />

    <section class="hero hero-main light resume-hero">
      <!-- HERO BODY -->
      <div class="hero-body">
        <div class="container">
          <div class="columns is-vcentered">
            <div class="column is-two-thirds">
              <h1 class="title has-text-grey-darker is-size-1">
                {{ profile.name }}
              </h1>
              <p class="subtitle has-text-grey-dark is-size-3">
                {{ profile.headline }}
              </p>
              <p class="contact">
                <ResumeProtectedEmail :encoded="profile.emailEncoded" />
                <span class="separator" aria-hidden="true">·</span>
                <span>{{ profile.location }}</span>
              </p>
              <p v-for="paragraph in bio" :key="paragraph" class="bio">
                {{ paragraph }}
              </p>
            </div>
            <div class="column photo">
              <img
                src="~assets/img/lance_full.webp"
                height="500"
                width="235"
                alt="Lance Moore"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- HERO FOOTER -->
      <div class="hero-foot no-print">
        <nav class="tabs is-boxed is-fullwidth">
          <div class="container">
            <ul>
              <li :class="{ 'is-active': isRouteActive('/resume/cv') }">
                <NuxtLink to="/resume/cv">Resume</NuxtLink>
              </li>
              <li :class="{ 'is-active': isRouteActive('/resume/portfolio') }">
                <NuxtLink to="/resume/portfolio">Portfolio</NuxtLink>
              </li>
              <li>
                <a href="/Lance-Moore-CV.pdf" download="Lance-Moore-CV.pdf">
                  Download CV (PDF)
                </a>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </section>
    <slot />
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/scss/variables";

.contact {
  margin-bottom: 1.25rem;
  font-weight: 500;

  .separator {
    margin: 0 0.5rem;
    color: #8a8a8a;
  }
}

.bio {
  max-width: 46rem;
  margin-bottom: 0.75rem;
  line-height: 1.6;
}

.photo {
  text-align: center;
}
</style>
