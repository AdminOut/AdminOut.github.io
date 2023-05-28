<script setup lang="ts">
useHead({
  title: "Portfolio",
  meta: [
    {
      name: "description",
      content: "Adminout software portfolio.",
    },
  ],
});

definePageMeta({
  layout: "resume",
});
</script>

<template>
  <NuxtLayout>
    <div class="container">
      <!-- PORTFOLIO HEADING -->

      <section class="section">
        <div class="container has-text-centered">
          <h2 class="title is-size-2">Portfolio</h2>
          <h3 class="subtitle">A few of my featured projects</h3>
        </div>
      </section>

      <!-- PORTFOLIO CONTENT -->

      <section class="section portfolio">
        <!-- ITEMS 1 - 2 -->
        <div class="columns">
          <!-- BATCH MANUFACTURE SOFTWARE -->
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img
                    src="~assets/img/portfolio/batch_software.jpg"
                    alt="Batch manufacture software"
                    height="960"
                    width="1280"
                  />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">Pharmaceutical Batch Manufacturing</p>
                    <p class="subtitle is-6">PHP (Yii)</p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    I designed this Batch Manufacturing ERP software for a
                    complimentary medicine manufacturer. The system has has
                    replaced the previous paper system.
                  </p>

                  <h4 class="is-size-6">Key Features</h4>

                  <ul>
                    <li>Manage material stock levels and procurement</li>
                    <li>
                      Generate PDF batch documents and labels for materials
                    </li>
                    <li>
                      QR Scanning application ensures operators are adding the
                      correct raw materials
                    </li>
                    <li>Quickly flags expiring materials</li>
                    <li>Enforce FEFO (First expiring first out)</li>
                    <li>Staff login</li>
                    <li>Staff Clock In</li>
                    <li>Regulatory and compliance reporting</li>
                    <li>Full batch traceability</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- INVOICING SOFTWARE -->
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img
                    src="~assets/img/portfolio/invoice_system.jpg"
                    alt="Invoicing Software"
                    height="960"
                    width="1280"
                  />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">Invoicing and payment collection</p>
                    <p class="subtitle is-6">Django / VueJS</p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    I worked on this project as both an independent contributor
                    and Team Lead.
                  </p>

                  <h4 class="is-size-6">Key Features</h4>

                  <ul>
                    <li>
                      Multi-tenant platform with organization "White labelling"
                    </li>
                    <li>Track invoices, bills and payments</li>
                    <li>
                      Integrates with Quickbooks desktop and Quickbooks online
                    </li>
                    <li>
                      Add employees with fine grained permissions to carry out
                      finance tasks
                    </li>
                    <li>
                      Manage accounts for multiple organizations with a single
                      login
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ITEMS 3 - 4 -->
        <div class="columns">
          <!-- CHIVO -->
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img
                    src="~assets/img/portfolio/crypto_wallet.jpg"
                    alt="Crypto wallet"
                    height="960"
                    width="1280"
                  />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">National Crypto Rollout</p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    I worked with a team of contractors to address severe issues
                    related to the national rollout of crypto as legal tender. I
                    was responsible for assembling a team and providing support
                    to various project stake-holders.
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- ARBITRAGE RSS FEED -->
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img
                    src="~assets/img/portfolio/arbitrage_rss.jpg"
                    alt="Arbitrage RSS"
                    height="480"
                    width="640"
                  />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">Crypto Arbitrage RSS</p>
                    <p class="subtitle is-6">Python / Celery</p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    A personal project that I developed. The system aggregates
                    order books from several local and international exchanges
                    to determine the best arbitrage rates. I was able to
                    generate a handsome profit before the arbitrage gaps
                    eventually closed.
                  </p>

                  <h4 class="is-size-6">Key Features</h4>

                  <ul>
                    <li>Realtime RSS Feed of various arbitrage rates</li>
                    <li>
                      Aggregated data from platforms with and without public
                      API's
                    </li>
                    <li>Customizable email alerts</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ITEMS 5 - 6 -->
        <div class="columns">
          <!-- VIRTUAL INSPECTION -->
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img
                    src="~assets/img/portfolio/virtual_inspection.jpg"
                    alt="Virtual inspection"
                    height="960"
                    width="1280"
                  />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">Virtual Inspection Application</p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    A virtual inspection application that I designed and
                    implemented for the metal recycling association in South
                    Africa. The virtual inspection application was approved by
                    SAPS (The South African Police Service) and replaces
                    physical inspections to this day.
                  </p>

                  <h4 class="is-size-6">Key Features</h4>

                  <ul>
                    <li>
                      Automatically generates inspections for members on an
                      annual basis
                    </li>
                    <li>
                      Multi-tenant system with Member, Staff and SAPS logins
                    </li>
                    <li>Compliance Reports</li>
                    <li>
                      Secure/encrypted data uploads for member documentation
                    </li>
                    <li>Automated email reminders</li>
                    <li>Comprehensive member documentation and training</li>
                    <li>
                      Automatically Generates PDF documentation of completed
                      inspections and issues PDF certificates to compliant
                      members
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>

          <!-- ELECTRONIC PROCUREMENT AND ERP -->
          <div class="column is-half">
            <div class="card">
              <div class="card-image">
                <figure class="image is-4by3">
                  <img
                    src="~assets/img/portfolio/medical.jpg"
                    alt="Electronic medical procurement"
                    height="960"
                    width="1280"
                  />
                </figure>
              </div>
              <div class="card-content">
                <div class="media">
                  <div class="media-content">
                    <p class="title is-4">Electronic procurement and ERP</p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    Working together with a small team we rolled out a
                    Electronic procurement and ERP system for a pharmaceutical
                    supplier.
                  </p>

                  <h4 class="is-size-6">Key Features</h4>

                  <ul>
                    <li>Electronic ordering of medical supplies</li>
                    <li>
                      Multi-tenant logins for clinics, practitioners, staff and
                      sales representatives
                    </li>
                    <li>
                      Automated commission calculations based of very technical
                      business logic
                    </li>
                    <li>Payment collections</li>
                    <li>Meets regulatory requirements</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </NuxtLayout>
</template>

<style scoped lang="scss">
.portfolio {
  .card {
    height: 100%;
  }
}
</style>
