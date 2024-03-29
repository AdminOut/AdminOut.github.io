<script setup lang="ts">
useHead({
  title: "Resume: Lance",
  meta: [
    {
      name: "description",
      content: "Senior software engineer resume",
    },
  ],
});

definePageMeta({
  layout: "resume",
});
</script>

<template>
  <NuxtLayout>
    <!-- SKILLS HEADING -->

    <section class="section">
      <div class="container has-text-centered">
        <h2 class="title is-size-2">Skills</h2>
      </div>
    </section>

    <!-- SKILLS CONTENT -->
    <section class="section">
      <div class="container">
        <div class="columns">
          <div class="column">
            <div class="content is-normal">
              <h3>Languages and Frameworks</h3>
              <ul>
                <li>PHP, Python, Javascript</li>
                <li>Django, Laravel, React, Vue, Angular</li>
              </ul>

              <h3>DevOps</h3>
              <ul>
                <li>Jenkins, Terraform, Nginx, Docker, AWS, Git</li>
              </ul>
            </div>
          </div>

          <div class="column">
            <div class="content is-normal">
              <h3>Project Management</h3>
              <ul>
                <li>Agile methodologies</li>
                <li>Prioritization and Continuous Planning</li>
                <li>Customer collaboration</li>
                <li>Continuous Integration and Delivery</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- WORK HISTORY HEADING -->

    <section class="section light">
      <div class="container has-text-centered">
        <h2 class="title is-size-2">Work History</h2>
      </div>
    </section>

    <!-- WORK HISTORY CONTENT -->
    <section class="section work-history light">
      <div class="container">
        <div class="columns">
          <div class="column is-half">
            <!-- ADMIN-OUT -->
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <img
                        src="~assets/img/logo-mini.webp"
                        alt="Adminout Logo"
                        fill
                      />
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">AdminOut (PTY) LTD</p>
                    <p class="subtitle is-5">
                      DIRECTOR AND INDEPENDENT CONTRIBUTOR
                    </p>
                    <p class="subtitle is-6">
                      2017 to Present (6 years, 4 months)
                    </p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    My technology consulting firm. I operate in the capacity of
                    an independent contributor and consultant
                  </p>
                  <ul>
                    <li>
                      I secured several international clients from various
                      industries.
                    </li>
                    <li>
                      Maintained a high client retention rate with virtually all
                      my clients pursuing follow-up contracts.
                    </li>
                    <li>
                      Generated the continuous revenue necessary for me to exit
                      the pharmaceutical industry and pursue a career in
                      software development as a manager and independent
                      contributor.
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <!-- ACCRUVIA -->
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <img
                        src="~assets/img/resume/accruvia.jpg"
                        alt="Accruvia"
                        fill
                      />
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">Accruvia | ROI Developers</p>
                    <p class="subtitle is-5">
                      SENIOR SOFTWARE ENGINEERING LEAD
                    </p>
                    <p class="subtitle is-6">
                      2018 to Present (5 years, 1 month)
                    </p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    Accruvia is a custom software development house. The company
                    has recently focused its efforts as an API integration
                    specialist.
                  </p>
                  <ul>
                    <li>
                      Responsible for the planning, implementation, deployment,
                      and maintenance of a host of custom software solutions for
                      our clients
                    </li>
                    <li>
                      Designed and implemented agile workflows and standard
                      operating procedures focussed on increasing development
                      velocity and improving estimation.
                    </li>
                    <li>
                      Introduced and enforced code quality standards and
                      practices that contributed to a significant decrease in
                      end-user downtime
                    </li>
                    <li>
                      Introduced automated CI/CD pipelines to facilitate rapid
                      daily releases
                    </li>
                    <li>
                      Introduced and implemented hiring processes that resulted
                      in a significant reduction in developer churn.
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="columns">
          <div class="column is-half">
            <!-- WLAST -->
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <img
                        src="~assets/img/resume/wlast.webp"
                        alt="W.LAST"
                        fill
                      />
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">W.LAST Manufacturing</p>
                    <p class="subtitle is-5">ACTING RESPONSIBLE PHARMACIST</p>
                    <p class="subtitle is-6">
                      Sept 2009 to August 2019 (10 years)
                    </p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    W.LAST is a complementary and alternate medicine
                    manufacturing facility.
                  </p>
                  <ul>
                    <li>Stock procurement and product formulation</li>
                    <li>
                      Introduction of GMP standards in the form of SOPs to
                      ensure compliance with regulations
                    </li>
                    <li>Project budgeting and estimation</li>
                    <li>
                      Responsible for regulatory concerns and maintaining FDA
                      and SAHPRA registrations.
                    </li>
                    <li>
                      Designed and implemented a custom ERP software system to
                      facilitate GMP compliance and inventory management. The
                      software significantly reduced operational overhead and is
                      still in use by the company on a daily basis.
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <!-- GIFT2GIVE -->
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <img
                        src="~assets/img/resume/g2g.webp"
                        alt="Gift2Give"
                        fill
                      />
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">Gift2Give</p>
                    <p class="subtitle is-5">FREELANCE SOFTWARE ENGINEER</p>
                    <p class="subtitle is-6">
                      February 2015 to January 2018 (3 years)
                    </p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    Gift2Give provides third-party gift voucher issuing and
                    redemption for a chain of malls and retailers
                  </p>
                  <ul>
                    <li>
                      Designed and implemented a gift voucher redemption proxy
                      server and UI for terminals
                    </li>
                    <li>Configured linux and apache web servers.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="columns">
          <div class="column is-half">
            <!-- SPRINGBOK PHARMACY -->
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <img
                        src="~assets/img/resume/springbok.webp"
                        alt="Springbok"
                        fill
                      />
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">Springbok Pharmacy</p>
                    <p class="subtitle is-5">LOCUM RETAIL PHARMACIST</p>
                    <p class="subtitle is-6">
                      Oct 2005 to August 2017 (12 years)
                    </p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    Springbok Pharmacy remained one of the biggest single-store
                    pharmacies in South Africa for decades until it was recently
                    acquired by a competitor.
                  </p>
                  <ul>
                    <li>Dispensing medical prescriptions</li>
                    <li>Compounding of medicine</li>
                    <li>Patient counselling</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
          <div class="column">
            <!-- FEZILE DABI DISTRICT -->
            <div class="card">
              <div class="card-content">
                <div class="media">
                  <div class="media-left">
                    <figure class="image is-48x48">
                      <img
                        src="~assets/img/resume/fezile-dabi.webp"
                        alt="Fezile Dabi"
                        fill
                      />
                    </figure>
                  </div>
                  <div class="media-content">
                    <p class="title is-4">Fezile Dabi District Municipality</p>
                    <p class="subtitle is-5">
                      PHARMACY MANAGER (COMMUNITY SERVICE)
                    </p>
                    <p class="subtitle is-6">June 2008 to June 2009 (1 year)</p>
                  </div>
                </div>

                <div class="content">
                  <p>
                    As part of my post-graduation community service, I was
                    required to work for a state for one year.
                  </p>
                  <ul>
                    <li>Stock procurement</li>
                    <li>Supervising pharmacy assistants</li>
                    <li>Visiting and managing surrounding satellite clinics</li>
                    <li>
                      Maintained and improved experimental stock management
                      software that significantly improved district efficiency
                      and expenditure.
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- EDUCATION HEADING -->

    <section class="section">
      <div class="container has-text-centered">
        <h2 class="title is-size-2">Education</h2>
      </div>
    </section>

    <!-- EDUCATION CONTENT -->

    <section class="section">
      <div class="container">
        <div class="card light">
          <div class="card-content">
            <div class="media">
              <div class="media-left">
                <figure class="image is-48x48">
                  <img
                    src="~assets/img/resume/wits.webp"
                    alt="WITS"
                    height="48"
                    width="48"
                  />
                </figure>
              </div>
              <div class="media-content">
                <p class="title is-4">BACHELOR OF PHARMACY (2006)</p>
                <p class="subtitle is-6">University of the Witwatersrand</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </NuxtLayout>
</template>

<style scoped lang="scss">
@import "@/assets/scss/variables";

.work-history {
  .card {
    height: 100%;
  }
}

.card.light {
  background-color: $light;
}
</style>
