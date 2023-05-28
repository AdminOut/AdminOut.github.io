<script setup lang="ts">
useHead({
  title: "Custom software development",
  meta: [
    {
      name: "description",
      content:
        "Custom software development house and payment solution specialist.",
    },
  ],
});
</script>

<template>
  <NuxtLayout>
    <section id="home-page-image" class="hero hero-main is-hidden-mobile">
      <!-- HERO TABLET - FULLHD -->
      <div class="hero-body">
        <div class="container">
          <div class="columns is-vcentered">
            <div class="column is-two-thirds">
              <p class="title has-text-grey-lighter is-size-1">
                Custom software artisans
              </p>
              <p class="subtitle has-text-grey-light is-size-3">
                Partner with a team that can get the job done. We craft custom
                software that empowers organizations to streamline their
                operations, enhance productivity, and achieve sustainable
                growth.
              </p>

              <a
                class="button is-large is-outlined is-inverted"
                href="#contact-us"
              >
                Get in touch
              </a>
            </div>
            <div class="column">
              <img
                src="~assets/img/adminout.svg"
                height="400"
                width="329"
                alt="Adminout"
              />
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- HERO MOBILE -->

    <section class="section dark is-hidden-tablet">
      <div class="container has-text-centered">
        <h2 class="title is-size-2">Custom Software Artisans</h2>
        <p class="body1">
          Partner with a team that can get the job done. We craft custom
          software that empowers organizations to streamline their operations,
          enhance productivity, and achieve sustainable growth.
        </p>
      </div>
    </section>

    <!-- SPELLS AND ENCHANTMENTS (SERVICES) HEADING -->

    <section class="light section">
      <div class="container has-text-centered">
        <span id="services" tabindex="-1"></span>
        <h2 class="title is-size-2">Our Services</h2>
        <p class="body1">Spells and enchantments for the digital age</p>
      </div>
    </section>

    <!-- SPELLS AND ENCHANTMENTS (SERVICES) CONTENT -->

    <section class="light section">
      <div class="container has-text-centered">
        <div class="columns">
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <img
                  src="~assets/img/predict.svg"
                  height="300"
                  width="300"
                  alt="Prediction"
                />
              </div>
              <div class="card-content">
                <h3 class="title">Prediction</h3>
                <p class="body2">
                  <strong>Enterprise resource planning (ERP)</strong>
                  systems can significantly improve your business operations by
                  streamlining processes, enhancing efficiency, and providing
                  valuable insights for informed decision-making.
                </p>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="card">
              <div class="card-image">
                <img
                  src="~assets/img/rune-craft.svg"
                  height="300"
                  width="300"
                  alt="Rune-Craft"
                />
              </div>

              <div class="card-content">
                <h3 class="title">Rune-script</h3>
                <p class="body2">
                  <strong>Custom software development.</strong>
                  Our team of highly skilled and experienced arcane masters are
                  dedicated to delivering tailored solutions that meet your
                  specific business needs.
                </p>
              </div>
            </div>
          </div>
        </div>

        <div class="columns">
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <img
                  src="~assets/img/summon.svg"
                  height="300"
                  width="300"
                  alt="Summon"
                />
              </div>
              <div class="card-content">
                <h3 class="title">Summon</h3>
                <p class="body2">
                  <strong>Outsource your development team.</strong>
                  Rally trustworthy allies to your banners. A fully managed and
                  white-labelled development team, assembled from the ether so
                  that you can focus on you core business.
                </p>
              </div>
            </div>
          </div>
          <div class="column">
            <div class="card">
              <div class="card-image">
                <img
                  src="~assets/img/transmute.svg"
                  height="300"
                  width="300"
                  alt="Transmute"
                />
              </div>
              <div class="card-content">
                <h3 class="title">Transmute</h3>
                <p class="body2">
                  <strong>Digital payment solutions</strong>
                  that facilitate B2B and B2C payments and convert your services
                  and products into money. Discover how your payment solution
                  can passively subsidise your development costs.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- HELMSMAN HEADING -->

    <section class="section">
      <div class="container has-text-centered">
        <h2 class="title is-size-2">Your guide</h2>
        <p class="body1">Every adventure requires a navigator</p>
      </div>
    </section>

    <!-- HELMSMAN CONTENT -->
    <section class="section">
      <div class="container has-text-centered">
        <div class="columns is-vcentered">
          <div class="column">
            <p class="subtitle is-size-2 has-text-grey-dark">
              I have been building business software for over a decade. I've
              failed again and again so that you don't have to.
            </p>
            <p class="subtitle is-size-4 has-text-grey">
              <i>- Founder, Lance Moore</i>
            </p>
          </div>

          <div class="column">
            <img
              src="~assets/img/helmsman.webp"
              height="600"
              width="467"
              alt="Lance Moore"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- CLIENTS HEADER -->

    <section class="section light">
      <span id="our-clients" tabindex="-1"></span>
      <div class="container has-text-centered">
        <h2 class="title is-size-2">You're in good company</h2>
        <p class="body1">Join our list of satisfied clients</p>
      </div>
    </section>

    <!-- CLIENTS CONTENT -->
    <section class="section light">
      <div class="container has-text-centered">
        <div class="columns is-vcentered">
          <div class="column is-one-fifth">
            <img
              src="~assets/img/clients/saxmoore.webp"
              height="100"
              width="200"
              alt="saxmoore"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/clients/accruvia.webp"
              height="46"
              width="200"
              alt="accurvia"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/clients/mra.webp"
              height="100"
              width="94"
              alt="metal recyclers association"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/clients/g2g.webp"
              height="100"
              width="200"
              alt="gift2give"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/clients/wlast.webp"
              height="100"
              width="200"
              alt="wlast"
            />
          </div>
        </div>
      </div>
    </section>

    <!-- CONTACT US HEADER -->

    <section class="section">
      <div class="container has-text-centered">
        <span id="contact-us" tabindex="-1"></span>
        <h2 class="title is-size-2">Contact Us</h2>
        <p class="body1">Take that first step</p>
      </div>
    </section>

    <!-- CONTACT US CONTENT -->

    <section class="section">
      <div class="container has-text-centered">
        <form>
          <div class="field is-horizontal">
            <div class="field-body">
              <div class="field">
                <p class="control">
                  <input
                    class="input is-large"
                    type="text"
                    placeholder="Name"
                  />
                </p>
              </div>
              <div class="field">
                <p class="control">
                  <input
                    class="input is-large"
                    type="email"
                    placeholder="Email"
                  />
                </p>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <textarea
                    class="textarea is-large"
                    placeholder="Explain how we can help you"
                  ></textarea>
                </div>
              </div>
            </div>
          </div>

          <div class="field is-horizontal">
            <div class="field-body">
              <div class="field">
                <div class="control">
                  <button class="button is-primary is-large">
                    Send message
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </section>

    <!-- TOOLS CONTENT -->
    <section class="section dark">
      <div class="container has-text-centered">
        <div class="columns">
          <div class="column is-one-fifth">
            <img
              src="~assets/img/languages/python_light.webp"
              height="100"
              width="100"
              alt="python"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/languages/javascript_light.webp"
              height="80"
              width="80"
              alt="javascript"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/languages/typescript_light.webp"
              height="80"
              width="80"
              alt="typescript"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/languages/php_light.webp"
              height="100"
              width="100"
              alt="php"
            />
          </div>

          <div class="column is-one-fifth">
            <img
              src="~assets/img/languages/golang_light.webp"
              height="100"
              width="100"
              alt="golang"
            />
          </div>
        </div>
      </div>
    </section>
  </NuxtLayout>
</template>

<style scoped>
#home-page-image {
  background-color: #2b2b2b;
}

.field {
  padding: 0.5rem;
}
</style>
