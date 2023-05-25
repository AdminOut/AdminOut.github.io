<script setup lang="ts">
import { useRoute } from "vue-router";
import BackToTop from "~/components/BackToTop.vue";

const route = useRoute();

const isRouteActive = (path: string) => {
  return route.path === path;
};
</script>

<template>
  <div>
    <BackToTop />

    <section class="hero hero-main light">
      <!-- HERO BODY -->
      <div class="hero-body">
        <div class="container">
          <div class="columns is-vcentered">
            <div class="column is-two-thirds">
              <p class="title has-text-grey-darker is-size-1">Lance Moore</p>
              <p class="subtitle has-text-grey-dark is-size-3">
                Senior software engineer and consultant
              </p>
              <p>
                Passionate software engineer with a diverse background in both
                pharmacy and software engineering, combining over 10 years of
                industry experience in each field. I've leveraged my unique
                skill set to deliver a fresh approach to developing innovative
                software solutions.
              </p>
            </div>
            <div class="column">
              <img
                src="~assets/img/lance_full.webp"
                height="500"
                width="235"
                alt="Lance"
              />
            </div>
          </div>
        </div>
      </div>

      <!-- HERO FOOTER -->
      <div class="hero-foot">
        <nav class="tabs is-boxed is-fullwidth">
          <div class="container">
            <ul>
              <li :class="{ 'is-active': isRouteActive('/resume/cv') }">
                <NuxtLink to="/resume/cv">Resume</NuxtLink>
              </li>
              <li :class="{ 'is-active': isRouteActive('/resume/portfolio') }">
                <NuxtLink to="/resume/portfolio">Portfolio</NuxtLink>
              </li>
            </ul>
          </div>
        </nav>
      </div>
    </section>
    <slot />
  </div>
</template>

<style scoped></style>
