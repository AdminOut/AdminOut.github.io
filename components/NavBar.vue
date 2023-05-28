<script setup lang="ts"></script>

<template>
  <nav
    id="main-navbar"
    class="navbar"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="container">
      <div class="navbar-brand">
        <NuxtLink class="navbar-item logo-font brand-font" to="/">
          Admin<span>Out</span>
        </NuxtLink>

        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start"></div>

        <div class="navbar-end">
          <div class="navbar-item">
            <a class="navbar-item" href="#services"> Services </a>
          </div>
          <div class="navbar-item">
            <a class="navbar-item" href="#our-clients"> Clients </a>
          </div>
          <div class="navbar-item">
            <NuxtLink class="navbar-item" to="/resume/portfolio">
              Portfolio
            </NuxtLink>
          </div>
          <div class="navbar-item">
            <a class="navbar-item" href="#contact-us"> Contact Us </a>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.brand-font {
  font-size: 2rem;
}

#main-navbar {
  border-bottom: 1px #ebeaeb;
}
</style>
