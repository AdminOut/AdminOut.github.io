<script setup lang="ts">
/**
 * An email address that is never in the HTML or as plain text in the bundle.
 * The server renders a "Show email" button; the address is decoded in the
 * browser only when a visitor clicks it, or when the page is printed so the
 * printed or saved PDF still carries it. Scrapers that read the HTML, or run
 * the page without clicking, get nothing.
 */
const props = defineProps<{
  /** The address reversed, then base64-encoded. */
  encoded: string;
}>();

const address = ref("");

function reveal() {
  if (!address.value) {
    address.value = atob(props.encoded).split("").reverse().join("");
  }
}

onMounted(() => window.addEventListener("beforeprint", reveal));
onBeforeUnmount(() => window.removeEventListener("beforeprint", reveal));
</script>

<template>
  <a v-if="address" :href="`mailto:${address}`">{{ address }}</a>
  <button
    v-else
    type="button"
    class="button is-small is-primary is-outlined show-email"
    @click="reveal"
  >
    Show email address
  </button>
</template>

<style scoped>
.show-email {
  vertical-align: baseline;
}
</style>
