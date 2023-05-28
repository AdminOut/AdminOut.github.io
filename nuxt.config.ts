// https://nuxt.com/docs/api/configuration/nuxt-config

export default defineNuxtConfig({
  css: ["@/assets/scss/main.scss"],
  nitro: {
    preset: "cloudflare-module",
  },
});
