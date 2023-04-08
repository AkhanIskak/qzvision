<template>
  <div>
    <section class="pb-5 bg-hero">
      <b-container class="pt-5">
        <b-row>
          <b-col cols="12" lg="6" md="6" sm="12">
            <h1>
              QazVision <br/>
              делаем город <br/>
              Умным
            </h1>
            <svg
              class="my-5"
              width="487"
              height="34"
              viewBox="0 0 487 34"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M4 30C73.6307 10.3798 266.914 -17.0885 483 30"
                stroke="#54BD95"
                stroke-width="8"
                stroke-linecap="round"
              />
            </svg>

            <p class="hero-description">
              Наша цель сделать города умными. С помощью компьютерного зрения , мы разрабатываем решения делающие город
              более удобным и оптимизированным для жителей
            </p>
          </b-col>
          <br class="d-none d-sm-block"/>
          <b-col cols="12" lg="6" md="6" sm="12">
            <b-img
              alt="hero image"
              class="img-fluid"
              :src="require(`~/assets/img/smartcity.png`)"
            ></b-img>
          </b-col>
        </b-row>
      </b-container>
    </section>
    <section class="bg-green-light py-5">
      <!--      <b-container>-->
      <!--        <b-row>-->
      <!--          <b-col cols="12" lg="6" md="6" sm="12">-->
      <!--            <h2>How we support our partner all over the world</h2>-->
      <!--            <div class="my-5">-->
      <!--              <p class="text-muted">-->
      <!--                SaaS become a common delivery model for many business-->
      <!--                application, including office software, messaging software,-->
      <!--                payroll processing software, DBMS software, management software-->
      <!--              </p>-->
      <!--            </div>-->
      <!--            <div class="d-flex flex-row">-->
      <!--              <div class="d-flex flex-column">-->
      <!--                <svg-->
      <!--                  width="142"-->
      <!--                  height="26"-->
      <!--                  viewBox="0 0 142 26"-->
      <!--                  fill="none"-->
      <!--                  xmlns="http://www.w3.org/2000/svg"-->
      <!--                >-->
      <!--                  <path-->
      <!--                    d="M13 0L15.9187 8.98278H25.3637L17.7225 14.5344L20.6412 23.5172L13 17.9656L5.35879 23.5172L8.27747 14.5344L0.636266 8.98278H10.0813L13 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M42 0L44.9187 8.98278H54.3637L46.7225 14.5344L49.6412 23.5172L42 17.9656L34.3588 23.5172L37.2775 14.5344L29.6363 8.98278H39.0813L42 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M71 0L73.9187 8.98278H83.3637L75.7225 14.5344L78.6412 23.5172L71 17.9656L63.3588 23.5172L66.2775 14.5344L58.6363 8.98278H68.0813L71 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M100 0L102.919 8.98278H112.364L104.723 14.5344L107.641 23.5172L100 17.9656L92.3588 23.5172L95.2775 14.5344L87.6363 8.98278H97.0813L100 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M129 0L131.919 8.98278H141.364L133.723 14.5344L136.641 23.5172L129 17.9656L121.359 23.5172L124.277 14.5344L116.636 8.98278H126.081L129 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                </svg>-->

      <!--                <h5>4.9 / 5 Rating</h5>-->
      <!--                <h5 class="text-muted">Databricks</h5>-->
      <!--              </div>-->
      <!--              <div class="d-flex flex-column ml-5">-->
      <!--                <svg-->
      <!--                  width="142"-->
      <!--                  height="26"-->
      <!--                  viewBox="0 0 142 26"-->
      <!--                  fill="none"-->
      <!--                  xmlns="http://www.w3.org/2000/svg"-->
      <!--                >-->
      <!--                  <path-->
      <!--                    d="M13 0L15.9187 8.98278H25.3637L17.7225 14.5344L20.6412 23.5172L13 17.9656L5.35879 23.5172L8.27747 14.5344L0.636266 8.98278H10.0813L13 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M42 0L44.9187 8.98278H54.3637L46.7225 14.5344L49.6412 23.5172L42 17.9656L34.3588 23.5172L37.2775 14.5344L29.6363 8.98278H39.0813L42 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M71 0L73.9187 8.98278H83.3637L75.7225 14.5344L78.6412 23.5172L71 17.9656L63.3588 23.5172L66.2775 14.5344L58.6363 8.98278H68.0813L71 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M100 0L102.919 8.98278H112.364L104.723 14.5344L107.641 23.5172L100 17.9656L92.3588 23.5172L95.2775 14.5344L87.6363 8.98278H97.0813L100 0Z"-->
      <!--                    fill="#FFC728"-->
      <!--                  />-->
      <!--                  <path-->
      <!--                    d="M129 0L131.919 8.98278H141.364L133.723 14.5344L136.641 23.5172L129 17.9656L121.359 23.5172L124.277 14.5344L116.636 8.98278H126.081L129 0Z"-->
      <!--                    fill="#BBBBBB"-->
      <!--                  />-->
      <!--                </svg>-->

      <!--                <h5>4.8 / 5 Rating</h5>-->
      <!--                <h5 class="text-muted">Chainalysis</h5>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--          </b-col>-->
      <!--          <b-col cols="12" lg="6" md="6" sm="12" class="mt-sm-5">-->
      <!--            <div class="d-flex flex-column">-->
      <!--              <div class="d-flex flex-row">-->
      <!--                <div class="d-fle align-items-start">-->
      <!--                  <svg-->
      <!--                    width="78"-->
      <!--                    height="78"-->
      <!--                    viewBox="0 0 78 78"-->
      <!--                    fill="none"-->
      <!--                    xmlns="http://www.w3.org/2000/svg"-->
      <!--                  >-->
      <!--                    <g filter="url(#filter0_d_0_1)">-->
      <!--                      <rect x="9" y="5" width="60" height="60" fill="white" />-->
      <!--                    </g>-->
      <!--                    <g clip-path="url(#clip0_0_1)">-->
      <!--                      <path-->
      <!--                        d="M51.5 35H46.5L42.75 46.25L35.25 23.75L31.5 35H26.5"-->
      <!--                        stroke="#54BD95"-->
      <!--                        stroke-width="2"-->
      <!--                        stroke-linecap="round"-->
      <!--                        stroke-linejoin="round"-->
      <!--                      />-->
      <!--                    </g>-->
      <!--                    <defs>-->
      <!--                      <filter-->
      <!--                        id="filter0_d_0_1"-->
      <!--                        x="0"-->
      <!--                        y="0"-->
      <!--                        width="78"-->
      <!--                        height="78"-->
      <!--                        filterUnits="userSpaceOnUse"-->
      <!--                        color-interpolation-filters="sRGB"-->
      <!--                      >-->
      <!--                        <feFlood-->
      <!--                          flood-opacity="0"-->
      <!--                          result="BackgroundImageFix"-->
      <!--                        />-->
      <!--                        <feColorMatrix-->
      <!--                          in="SourceAlpha"-->
      <!--                          type="matrix"-->
      <!--                          values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"-->
      <!--                          result="hardAlpha"-->
      <!--                        />-->
      <!--                        <feOffset dy="4" />-->
      <!--                        <feGaussianBlur stdDeviation="4.5" />-->
      <!--                        <feComposite in2="hardAlpha" operator="out" />-->
      <!--                        <feColorMatrix-->
      <!--                          type="matrix"-->
      <!--                          values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0"-->
      <!--                        />-->
      <!--                        <feBlend-->
      <!--                          mode="normal"-->
      <!--                          in2="BackgroundImageFix"-->
      <!--                          result="effect1_dropShadow_0_1"-->
      <!--                        />-->
      <!--                        <feBlend-->
      <!--                          mode="normal"-->
      <!--                          in="SourceGraphic"-->
      <!--                          in2="effect1_dropShadow_0_1"-->
      <!--                          result="shape"-->
      <!--                        />-->
      <!--                      </filter>-->
      <!--                      <clipPath id="clip0_0_1">-->
      <!--                        <rect-->
      <!--                          width="30"-->
      <!--                          height="30"-->
      <!--                          fill="white"-->
      <!--                          transform="translate(24 20)"-->
      <!--                        />-->
      <!--                      </clipPath>-->
      <!--                    </defs>-->
      <!--                  </svg>-->
      <!--                </div>-->
      <!--                <div>-->
      <!--                  <h5>Publishing</h5>-->
      <!--                  <p class="text-muted">-->
      <!--                    Plan, collaborate, and publishing your contetn that drivees-->
      <!--                    meaningful engagement and growth for your barnd-->
      <!--                  </p>-->
      <!--                </div>-->
      <!--              </div>-->
      <!--              <div class="d-flex flex-row my-lg-5">-->
      <!--                <div class="d-fle align-items-start">-->
      <!--                  <svg-->
      <!--                    width="78"-->
      <!--                    height="78"-->
      <!--                    viewBox="0 0 78 78"-->
      <!--                    fill="none"-->
      <!--                    xmlns="http://www.w3.org/2000/svg"-->
      <!--                  >-->
      <!--                    <g filter="url(#filter0_d_0_1)">-->
      <!--                      <rect x="9" y="5" width="60" height="60" fill="white" />-->
      <!--                    </g>-->
      <!--                    <path-->
      <!--                      d="M50.512 39.8626C49.7168 41.7432 48.473 43.4004 46.8894 44.6892C45.3057 45.9781 43.4305 46.8594 41.4276 47.2561C39.4247 47.6528 37.3551 47.5528 35.3997 46.9648C33.4444 46.3769 31.6628 45.3189 30.2108 43.8834C28.7588 42.4479 27.6805 40.6785 27.0703 38.73C26.4601 36.7815 26.3365 34.7132 26.7103 32.7059C27.0841 30.6986 27.9439 28.8134 29.2146 27.2151C30.4853 25.6169 32.1281 24.3542 33.9995 23.5376"-->
      <!--                      stroke="#54BD95"-->
      <!--                      stroke-width="2"-->
      <!--                      stroke-linecap="round"-->
      <!--                      stroke-linejoin="round"-->
      <!--                    />-->
      <!--                    <path-->
      <!--                      d="M51.5 35C51.5 33.3585 51.1767 31.733 50.5485 30.2165C49.9203 28.6999 48.9996 27.3219 47.8388 26.1612C46.6781 25.0004 45.3001 24.0797 43.7835 23.4515C42.267 22.8233 40.6415 22.5 39 22.5V35H51.5Z"-->
      <!--                      stroke="#54BD95"-->
      <!--                      stroke-width="2"-->
      <!--                      stroke-linecap="round"-->
      <!--                      stroke-linejoin="round"-->
      <!--                    />-->
      <!--                    <defs>-->
      <!--                      <filter-->
      <!--                        id="filter0_d_0_1"-->
      <!--                        x="0"-->
      <!--                        y="0"-->
      <!--                        width="78"-->
      <!--                        height="78"-->
      <!--                        filterUnits="userSpaceOnUse"-->
      <!--                        color-interpolation-filters="sRGB"-->
      <!--                      >-->
      <!--                        <feFlood-->
      <!--                          flood-opacity="0"-->
      <!--                          result="BackgroundImageFix"-->
      <!--                        />-->
      <!--                        <feColorMatrix-->
      <!--                          in="SourceAlpha"-->
      <!--                          type="matrix"-->
      <!--                          values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"-->
      <!--                          result="hardAlpha"-->
      <!--                        />-->
      <!--                        <feOffset dy="4" />-->
      <!--                        <feGaussianBlur stdDeviation="4.5" />-->
      <!--                        <feComposite in2="hardAlpha" operator="out" />-->
      <!--                        <feColorMatrix-->
      <!--                          type="matrix"-->
      <!--                          values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0"-->
      <!--                        />-->
      <!--                        <feBlend-->
      <!--                          mode="normal"-->
      <!--                          in2="BackgroundImageFix"-->
      <!--                          result="effect1_dropShadow_0_1"-->
      <!--                        />-->
      <!--                        <feBlend-->
      <!--                          mode="normal"-->
      <!--                          in="SourceGraphic"-->
      <!--                          in2="effect1_dropShadow_0_1"-->
      <!--                          result="shape"-->
      <!--                        />-->
      <!--                      </filter>-->
      <!--                    </defs>-->
      <!--                  </svg>-->
      <!--                </div>-->
      <!--                <div>-->
      <!--                  <h5>Analytics</h5>-->
      <!--                  <p class="text-muted">-->
      <!--                    Analyze your performance and create goegeous report-->
      <!--                  </p>-->
      <!--                </div>-->
      <!--              </div>-->
      <!--              <div class="d-flex flex-row">-->
      <!--                <div class="d-fle align-items-start">-->
      <!--                  <svg-->
      <!--                    width="78"-->
      <!--                    height="78"-->
      <!--                    viewBox="0 0 78 78"-->
      <!--                    fill="none"-->
      <!--                    xmlns="http://www.w3.org/2000/svg"-->
      <!--                  >-->
      <!--                    <g filter="url(#filter0_d_0_1)">-->
      <!--                      <rect x="9" y="5" width="60" height="60" fill="white" />-->
      <!--                    </g>-->
      <!--                    <path-->
      <!--                      d="M46.5 23.75C45.5054 23.75 44.5516 24.1451 43.8483 24.8483C43.1451 25.5516 42.75 26.5054 42.75 27.5V42.5C42.75 43.4946 43.1451 44.4484 43.8483 45.1517C44.5516 45.8549 45.5054 46.25 46.5 46.25C47.4946 46.25 48.4484 45.8549 49.1517 45.1517C49.8549 44.4484 50.25 43.4946 50.25 42.5C50.25 41.5054 49.8549 40.5516 49.1517 39.8483C48.4484 39.1451 47.4946 38.75 46.5 38.75H31.5C30.5054 38.75 29.5516 39.1451 28.8483 39.8483C28.1451 40.5516 27.75 41.5054 27.75 42.5C27.75 43.4946 28.1451 44.4484 28.8483 45.1517C29.5516 45.8549 30.5054 46.25 31.5 46.25C32.4946 46.25 33.4484 45.8549 34.1517 45.1517C34.8549 44.4484 35.25 43.4946 35.25 42.5V27.5C35.25 26.5054 34.8549 25.5516 34.1517 24.8483C33.4484 24.1451 32.4946 23.75 31.5 23.75C30.5054 23.75 29.5516 24.1451 28.8483 24.8483C28.1451 25.5516 27.75 26.5054 27.75 27.5C27.75 28.4946 28.1451 29.4484 28.8483 30.1517C29.5516 30.8549 30.5054 31.25 31.5 31.25H46.5C47.4946 31.25 48.4484 30.8549 49.1517 30.1517C49.8549 29.4484 50.25 28.4946 50.25 27.5C50.25 26.5054 49.8549 25.5516 49.1517 24.8483C48.4484 24.1451 47.4946 23.75 46.5 23.75Z"-->
      <!--                      stroke="#54BD95"-->
      <!--                      stroke-width="2"-->
      <!--                      stroke-linecap="round"-->
      <!--                      stroke-linejoin="round"-->
      <!--                    />-->
      <!--                    <defs>-->
      <!--                      <filter-->
      <!--                        id="filter0_d_0_1"-->
      <!--                        x="0"-->
      <!--                        y="0"-->
      <!--                        width="78"-->
      <!--                        height="78"-->
      <!--                        filterUnits="userSpaceOnUse"-->
      <!--                        color-interpolation-filters="sRGB"-->
      <!--                      >-->
      <!--                        <feFlood-->
      <!--                          flood-opacity="0"-->
      <!--                          result="BackgroundImageFix"-->
      <!--                        />-->
      <!--                        <feColorMatrix-->
      <!--                          in="SourceAlpha"-->
      <!--                          type="matrix"-->
      <!--                          values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"-->
      <!--                          result="hardAlpha"-->
      <!--                        />-->
      <!--                        <feOffset dy="4" />-->
      <!--                        <feGaussianBlur stdDeviation="4.5" />-->
      <!--                        <feComposite in2="hardAlpha" operator="out" />-->
      <!--                        <feColorMatrix-->
      <!--                          type="matrix"-->
      <!--                          values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0"-->
      <!--                        />-->
      <!--                        <feBlend-->
      <!--                          mode="normal"-->
      <!--                          in2="BackgroundImageFix"-->
      <!--                          result="effect1_dropShadow_0_1"-->
      <!--                        />-->
      <!--                        <feBlend-->
      <!--                          mode="normal"-->
      <!--                          in="SourceGraphic"-->
      <!--                          in2="effect1_dropShadow_0_1"-->
      <!--                          result="shape"-->
      <!--                        />-->
      <!--                      </filter>-->
      <!--                    </defs>-->
      <!--                  </svg>-->
      <!--                </div>-->
      <!--                <div>-->
      <!--                  <h5>Engagement</h5>-->
      <!--                  <p class="text-muted">-->
      <!--                    Quiuckly navigate you anda engage with your adience-->
      <!--                  </p>-->
      <!--                </div>-->
      <!--              </div>-->
      <!--            </div>-->
      <!--          </b-col>-->
      <!--        </b-row>-->
      <!--      </b-container>-->
    </section>
    <section>
      <b-container class="pt-5 mt-5">
        <b-row>
          <b-col cols="12" md="4" lg="4" sm="12">
            <h2
            >Наши решения </h2>
          </b-col>
          <b-col
            cols="12"
            md="5"
            lg="5"
            sm="12"
            class="d-flex align-items-center"
          >
            <p class="text-muted" id="solutions">
              Наши решения улучшают качество жизни и помогают сохранять время жителям
            </p>
          </b-col>
          <b-col
            cols="12"
            md="3"
            lg="3"
            sm="12"
            class="d-flex align-items-center"
          >
            <a href="">
              <b-button
                class="rounded-lg ml-lg-auto text-white"
                variant="primary"
                size="lg"
              >Начнем
              </b-button
              >
            </a>

          </b-col>
        </b-row>
        <b-row class="mt-5 p-lg-5">
          <b-col cols="12" lg="4" md="4" sm="4">
            <b-card class="rounded-lg border-0 card-feature">
              <b-img
                alt="feature"
                class="img-fluid img-feature"
                :src="require(`~/assets/img/light.png`)"
              >
              </b-img>
              <b-card-text class="pt-2">
                <h5>Динамический расчет времени светофора</h5>
                <p class="text-muted">
                  Анализирую фотографии с камер , мы анализируем загруженность на перекрестках и в зависимости от
                  количества машин с каждой стороны устанавливаем время светофора
                </p>
              </b-card-text>
            </b-card>
          </b-col>
          <b-col cols="12" lg="4" md="4" sm="4">
            <b-card class="rounded-lg border-0 card-feature">
              <b-img
                alt="feature"
                class="img-fluid img-feature"
                :src="require(`~/assets/img/bus.png`)"
              ></b-img>
              <b-card-text class="pt-2">
                <h5>Загруженность общественного транспорта</h5>
                <p class="text-muted">
                  Анализирую с помощью computer vision количество людей в автобусе , показываем гражданам загруженность

                </p>
              </b-card-text>
            </b-card>
          </b-col>
          <b-col cols="12" lg="4" md="4" sm="4">
            <b-card class="rounded-lg border-0 card-feature">
              <b-img
                alt="feature"
                class="img-fluid img-feature"
                :src="require(`~/assets/img/litter.png`)"
              >
              </b-img>
              <b-card-text class="pt-2">
                <h5>Штрафы за мусор и порчу общественного имущества</h5>
                <p class="text-muted">
                  В нашем городе много людей мусорят и портят общественное имущество , чтобы прекратить это нужны штрафы
                </p>
              </b-card-text>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </section>
    <section>
      <b-container class="pt-5 mt-5">
        <b-row>
          <b-col cols="12" md="4" lg="4" sm="12">
            <h2 id="about">
              Основатели </h2>
          </b-col>
          <b-col
            cols="12"
            md="5"
            lg="5"
            sm="12"
            class="d-flex align-items-center"
          >
          </b-col>
        </b-row>
        <b-row class="mt-5 p-lg-5">
          <b-col cols="12" lg="4" md="4" sm="4">
            <b-card class="rounded-lg border-0 card-feature">
              <b-img
                alt="feature"
                class="img-fluid img-feature"
                :src="require(`~/assets/img/nurbek.jpeg`)"
              >
              </b-img>
              <b-card-text class="pt-2">
                <h5>Нурбек Болат</h5>
                <p class="text-muted">
                  Python AI and Ml разработчик , python backend developer
                </p>
              </b-card-text>
            </b-card>
          </b-col>
          <b-col cols="12" lg="4" md="4" sm="4">
            <b-card class="rounded-lg border-0 card-feature">
              <b-img
                alt="feature"
                class="img-fluid img-feature"
                :src="require(`~/assets/img/akhan.jpg`)"
              ></b-img>
              <b-card-text class="pt-2">
                <h5>Искак Ахан</h5>
                <p class="text-muted">
                  AI and ML энтузиаст , мидл node.js developer
                </p>
              </b-card-text>
            </b-card>
          </b-col>
        </b-row>
      </b-container>
    </section>

<!--    <div class="bg-section-product">-->
<!--      <section>-->
<!--        <b-container class="pt-5 mt-5">-->
<!--          <b-row>-->
<!--            <b-col lg="6" md="6" sm="12">-->
<!--              <h2>-->
<!--                What benefit will <br class="d-none d-lg-block"/>-->
<!--                you get-->
<!--              </h2>-->
<!--              <div class="d-flex flex-column mt-5">-->
<!--                <div class="my-1 d-flex flex-row">-->
<!--                  <svg-->
<!--                    width="32"-->
<!--                    height="32"-->
<!--                    viewBox="0 0 32 32"-->
<!--                    fill="none"-->
<!--                    xmlns="http://www.w3.org/2000/svg"-->
<!--                  >-->
<!--                    <path-->
<!--                      fill-rule="evenodd"-->
<!--                      clip-rule="evenodd"-->
<!--                      d="M16 32C24.8366 32 32 24.8366 32 16C32 7.16344 24.8366 0 16 0C7.16344 0 0 7.16344 0 16C0 24.8366 7.16344 32 16 32ZM15.6318 19.8961L21.8379 13.4961L20.4021 12.1039L14.8858 17.7926L11.5695 14.6357L10.1905 16.0843L14.2245 19.9243L14.9421 20.6074L15.6318 19.8961Z"-->
<!--                      fill="#54BD95"-->
<!--                    />-->
<!--                  </svg>-->
<!--                  <p class="ml-2">Free Consulting With Experet Saving Money</p>-->
<!--                </div>-->
<!--                <div class="my-1 d-flex flex-row">-->
<!--                  <svg-->
<!--                    width="32"-->
<!--                    height="32"-->
<!--                    viewBox="0 0 32 32"-->
<!--                    fill="none"-->
<!--                    xmlns="http://www.w3.org/2000/svg"-->
<!--                  >-->
<!--                    <path-->
<!--                      fill-rule="evenodd"-->
<!--                      clip-rule="evenodd"-->
<!--                      d="M16 32C24.8366 32 32 24.8366 32 16C32 7.16344 24.8366 0 16 0C7.16344 0 0 7.16344 0 16C0 24.8366 7.16344 32 16 32ZM15.6318 19.8961L21.8379 13.4961L20.4021 12.1039L14.8858 17.7926L11.5695 14.6357L10.1905 16.0843L14.2245 19.9243L14.9421 20.6074L15.6318 19.8961Z"-->
<!--                      fill="#54BD95"-->
<!--                    />-->
<!--                  </svg>-->
<!--                  <p class="ml-2">Online Banking</p>-->
<!--                </div>-->
<!--                <div class="my-1 d-flex flex-row">-->
<!--                  <svg-->
<!--                    width="32"-->
<!--                    height="32"-->
<!--                    viewBox="0 0 32 32"-->
<!--                    fill="none"-->
<!--                    xmlns="http://www.w3.org/2000/svg"-->
<!--                  >-->
<!--                    <path-->
<!--                      fill-rule="evenodd"-->
<!--                      clip-rule="evenodd"-->
<!--                      d="M16 32C24.8366 32 32 24.8366 32 16C32 7.16344 24.8366 0 16 0C7.16344 0 0 7.16344 0 16C0 24.8366 7.16344 32 16 32ZM15.6318 19.8961L21.8379 13.4961L20.4021 12.1039L14.8858 17.7926L11.5695 14.6357L10.1905 16.0843L14.2245 19.9243L14.9421 20.6074L15.6318 19.8961Z"-->
<!--                      fill="#54BD95"-->
<!--                    />-->
<!--                  </svg>-->
<!--                  <p class="ml-2">Investment Report Every Month</p>-->
<!--                </div>-->
<!--                <div class="my-1 d-flex flex-row">-->
<!--                  <svg-->
<!--                    width="32"-->
<!--                    height="32"-->
<!--                    viewBox="0 0 32 32"-->
<!--                    fill="none"-->
<!--                    xmlns="http://www.w3.org/2000/svg"-->
<!--                  >-->
<!--                    <path-->
<!--                      fill-rule="evenodd"-->
<!--                      clip-rule="evenodd"-->
<!--                      d="M16 32C24.8366 32 32 24.8366 32 16C32 7.16344 24.8366 0 16 0C7.16344 0 0 7.16344 0 16C0 24.8366 7.16344 32 16 32ZM15.6318 19.8961L21.8379 13.4961L20.4021 12.1039L14.8858 17.7926L11.5695 14.6357L10.1905 16.0843L14.2245 19.9243L14.9421 20.6074L15.6318 19.8961Z"-->
<!--                      fill="#54BD95"-->
<!--                    />-->
<!--                  </svg>-->
<!--                  <p class="ml-2">Saving Money For The Future</p>-->
<!--                </div>-->
<!--                <div class="my-1 d-flex flex-row">-->
<!--                  <svg-->
<!--                    width="32"-->
<!--                    height="32"-->
<!--                    viewBox="0 0 32 32"-->
<!--                    fill="none"-->
<!--                    xmlns="http://www.w3.org/2000/svg"-->
<!--                  >-->
<!--                    <path-->
<!--                      fill-rule="evenodd"-->
<!--                      clip-rule="evenodd"-->
<!--                      d="M16 32C24.8366 32 32 24.8366 32 16C32 7.16344 24.8366 0 16 0C7.16344 0 0 7.16344 0 16C0 24.8366 7.16344 32 16 32ZM15.6318 19.8961L21.8379 13.4961L20.4021 12.1039L14.8858 17.7926L11.5695 14.6357L10.1905 16.0843L14.2245 19.9243L14.9421 20.6074L15.6318 19.8961Z"-->
<!--                      fill="#54BD95"-->
<!--                    />-->
<!--                  </svg>-->
<!--                  <p class="ml-2">Online Transection</p>-->
<!--                </div>-->
<!--              </div>-->
<!--            </b-col>-->
<!--            <b-col lg="6" md="6" sm="12">-->
<!--              <b-img-->
<!--                alt="hero"-->
<!--                :src="require(`~/assets/img/hero-img-2.png`)"-->
<!--                class="img-fluid"-->
<!--              ></b-img>-->
<!--            </b-col>-->
<!--          </b-row>-->
<!--        </b-container>-->
<!--      </section>-->
<!--      <section class="pb-5">-->
<!--        <b-container class="mt-5">-->
<!--          <div class="d-flex flex-column">-->
<!--            <h2 class="mx-auto">-->
<!--              Choose Plan <br/>-->
<!--              Thats's Right For Your-->
<!--            </h2>-->
<!--            <p class="text-muted mx-auto text-700 my-4">-->
<!--              Choose plan that works best for you, feel free to contact us-->
<!--            </p>-->
<!--            <b-col lg="3" md="4" sm="10" cols="12" class="mx-auto">-->
<!--              <div-->
<!--                class="bg-white p-2 rounded-lg d-flex justify-content-between align-items-center font-weight-bold shadow-lg"-->
<!--              >-->
<!--                <span>Bil Monthly</span>-->
<!--                <b-button-->
<!--                  variant="primary"-->
<!--                  size="lg"-->
<!--                  class="text-white rounded-lg"-->
<!--                >Bil Yearly-->
<!--                </b-button-->
<!--                >-->
<!--              </div>-->
<!--            </b-col>-->

<!--            <b-row class="mx-lg-5 mt-5">-->
<!--              <b-col cols="12" lg="4" md="4" sm="12" class="mt-2">-->
<!--                <b-card class="rounded-lg shadow">-->
<!--                  <div class="text-center d-flex flex-column">-->
<!--                    <h4>Free</h4>-->
<!--                    <p class="text-muted">Have a go test your superpowers</p>-->
<!--                    <span class="d-inline">-->
<!--                      <div class="money">&#36;0</div>-->
<!--                    </span>-->
<!--                  </div>-->
<!--                  <div class="light-green p-2 mt-4 rounded-lg">-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">2 Users</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">2 Files</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">Public Share & Comments</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">Chat & Support</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">New income apps</span>-->
<!--                    </div>-->
<!--                    <b-button block class="rounded-lg btn-white shadow-sm"-->
<!--                    >Signup for free-->
<!--                    </b-button-->
<!--                    >-->
<!--                  </div>-->
<!--                </b-card>-->
<!--              </b-col>-->
<!--              <b-col cols="12" lg="4" md="4" sm="12" class="mt-2">-->
<!--                <b-card-->
<!--                  class="rounded-lg primary-card shadow"-->
<!--                  bg-variant="primary"-->
<!--                >-->
<!--                  <div>-->
<!--                    <div-->
<!--                      class="text-center d-flex flex-column text-white position-relative"-->
<!--                    >-->
<!--                      <h4>Pro</h4>-->
<!--                      <p>-->
<!--                        Experientce the power<br/>-->
<!--                        of invinity posibilities-->
<!--                      </p>-->
<!--                      <span class="d-inline">-->
<!--                        <div class="money">&#36;8</div>-->
<!--                      </span>-->
<!--                      <div class="my-4">-->
<!--                        <div class="p-2 card-saving rounded-lg d-inline">-->
<!--                          Save $50 a year-->
<!--                        </div>-->
<!--                      </div>-->
<!--                    </div>-->
<!--                    <div class="bg-white p-3 rounded-lg">-->
<!--                      <div class="d-flex flex-row my-3">-->
<!--                        <svg-->
<!--                          width="26"-->
<!--                          height="26"-->
<!--                          viewBox="0 0 26 26"-->
<!--                          fill="none"-->
<!--                          xmlns="http://www.w3.org/2000/svg"-->
<!--                        >-->
<!--                          <path-->
<!--                            fill-rule="evenodd"-->
<!--                            clip-rule="evenodd"-->
<!--                            d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                            fill="#54BD95"-->
<!--                          />-->
<!--                        </svg>-->

<!--                        <span class="ml-2">4 Users</span>-->
<!--                      </div>-->
<!--                      <div class="d-flex flex-row my-3">-->
<!--                        <svg-->
<!--                          width="26"-->
<!--                          height="26"-->
<!--                          viewBox="0 0 26 26"-->
<!--                          fill="none"-->
<!--                          xmlns="http://www.w3.org/2000/svg"-->
<!--                        >-->
<!--                          <path-->
<!--                            fill-rule="evenodd"-->
<!--                            clip-rule="evenodd"-->
<!--                            d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                            fill="#54BD95"-->
<!--                          />-->
<!--                        </svg>-->

<!--                        <span class="ml-2">All Apps</span>-->
<!--                      </div>-->
<!--                      <div class="d-flex flex-row my-3">-->
<!--                        <svg-->
<!--                          width="26"-->
<!--                          height="26"-->
<!--                          viewBox="0 0 26 26"-->
<!--                          fill="none"-->
<!--                          xmlns="http://www.w3.org/2000/svg"-->
<!--                        >-->
<!--                          <path-->
<!--                            fill-rule="evenodd"-->
<!--                            clip-rule="evenodd"-->
<!--                            d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                            fill="#54BD95"-->
<!--                          />-->
<!--                        </svg>-->

<!--                        <span class="ml-2">Unlimited editable exports</span>-->
<!--                      </div>-->
<!--                      <div class="d-flex flex-row my-3">-->
<!--                        <svg-->
<!--                          width="26"-->
<!--                          height="26"-->
<!--                          viewBox="0 0 26 26"-->
<!--                          fill="none"-->
<!--                          xmlns="http://www.w3.org/2000/svg"-->
<!--                        >-->
<!--                          <path-->
<!--                            fill-rule="evenodd"-->
<!--                            clip-rule="evenodd"-->
<!--                            d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                            fill="#54BD95"-->
<!--                          />-->
<!--                        </svg>-->

<!--                        <span class="ml-2">Folder and Callobration</span>-->
<!--                      </div>-->
<!--                      <div class="d-flex flex-row my-3">-->
<!--                        <svg-->
<!--                          width="26"-->
<!--                          height="26"-->
<!--                          viewBox="0 0 26 26"-->
<!--                          fill="none"-->
<!--                          xmlns="http://www.w3.org/2000/svg"-->
<!--                        >-->
<!--                          <path-->
<!--                            fill-rule="evenodd"-->
<!--                            clip-rule="evenodd"-->
<!--                            d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                            fill="#54BD95"-->
<!--                          />-->
<!--                        </svg>-->

<!--                        <span class="ml-2">All incomming apps</span>-->
<!--                      </div>-->
<!--                      <b-button-->
<!--                        block-->
<!--                        variant="primary text-white"-->
<!--                        class="rounded-lg"-->
<!--                      >Go to pro-->
<!--                      </b-button-->
<!--                      >-->
<!--                    </div>-->
<!--                  </div>-->
<!--                </b-card>-->
<!--              </b-col>-->
<!--              <b-col cols="12" lg="4" md="4" sm="12" class="mt-2">-->
<!--                <b-card class="rounded-lg shadow">-->
<!--                  <div class="text-center d-flex flex-column">-->
<!--                    <h4>Business</h4>-->
<!--                    <p class="text-muted">-->
<!--                      Unveil new superpowers and join the Design Leaque-->
<!--                    </p>-->
<!--                    <span class="d-inline">-->
<!--                      <div class="money">&#36;16</div>-->
<!--                    </span>-->
<!--                  </div>-->
<!--                  <div class="light-green p-3 mt-4 rounded-lg">-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">2 Users</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">2 Files</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">Public Share & Comments</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">Chat & Support</span>-->
<!--                    </div>-->
<!--                    <div class="d-flex flex-row my-3">-->
<!--                      <svg-->
<!--                        width="26"-->
<!--                        height="26"-->
<!--                        viewBox="0 0 26 26"-->
<!--                        fill="none"-->
<!--                        xmlns="http://www.w3.org/2000/svg"-->
<!--                      >-->
<!--                        <path-->
<!--                          fill-rule="evenodd"-->
<!--                          clip-rule="evenodd"-->
<!--                          d="M13 26C20.1797 26 26 20.1797 26 13C26 5.8203 20.1797 0 13 0C5.8203 0 0 5.8203 0 13C0 20.1797 5.8203 26 13 26ZM12.8355 16.2959L17.8779 11.0959L16.4421 9.70358L12.0894 14.1923L9.5295 11.7554L8.15054 13.204L11.4281 16.324L12.1458 17.0072L12.8355 16.2959Z"-->
<!--                          fill="#54BD95"-->
<!--                        />-->
<!--                      </svg>-->

<!--                      <span class="ml-2">New income apps</span>-->
<!--                    </div>-->
<!--                    <b-button block class="rounded-lg btn-white shadow-sm"-->
<!--                    >Goto Business-->
<!--                    </b-button-->
<!--                    >-->
<!--                  </div>-->
<!--                </b-card>-->
<!--              </b-col>-->
<!--            </b-row>-->
<!--          </div>-->
<!--        </b-container>-->
<!--      </section>-->
<!--    </div>-->

<!--    <section class="bg-dark text-white pt-5">-->
<!--      <b-container>-->
<!--        <b-row>-->
<!--          <b-col cols="12" lg="6" sm="12" md="6">-->
<!--            <h2>People are Saying about it</h2>-->
<!--            <p>-->
<!--              Everiting you need to accept payment and grow your money of manage-->
<!--              anywhere on plan-->
<!--            </p>-->
<!--            <div class="d-flex flex-column">-->
<!--              <div class="my-5">-->
<!--                <svg-->
<!--                  width="45"-->
<!--                  height="38"-->
<!--                  viewBox="0 0 45 38"-->
<!--                  fill="none"-->
<!--                  xmlns="http://www.w3.org/2000/svg"-->
<!--                >-->
<!--                  <path d="M11.5 0H21.5L14.5 38H0L11.5 0Z" fill="#D9D9D9"/>-->
<!--                  <path d="M35 0H45L38 38H23.5L35 0Z" fill="#D9D9D9"/>-->
<!--                </svg>-->
<!--              </div>-->
<!--              <p>-->
<!--                I'm very helped by this E-wallet application, my days are very-->
<!--                easy to use this application and its very helpfull in my live,-->
<!--                even i can pay a short time-->
<!--              </p>-->
<!--              <p class="my-4">_ Aria Zinanrio</p>-->

<!--              <div class="d-flex flex-row my-4">-->
<!--                <b-avatar-->
<!--                  size="66px"-->
<!--                  class="mx-2"-->
<!--                  :src="require(`~/assets/img/avatar/avatar_01.png`)"-->
<!--                />-->
<!--                <b-avatar-->
<!--                  size="66px"-->
<!--                  class="mx-2"-->
<!--                  :src="require(`~/assets/img/avatar/avatar_02.png`)"-->
<!--                />-->
<!--                <b-avatar-->
<!--                  size="66px"-->
<!--                  class="mx-2"-->
<!--                  :src="require(`~/assets/img/avatar/avatar_03.png`)"-->
<!--                />-->
<!--                <b-avatar-->
<!--                  size="66px"-->
<!--                  class="mx-2"-->
<!--                  :src="require(`~/assets/img/avatar/avatar_04.png`)"-->
<!--                />-->
<!--                <b-avatar size="66px" class="mx-2">-->
<!--                  <b-icon-play-fill scale="2"/>-->
<!--                </b-avatar>-->
<!--              </div>-->
<!--            </div>-->
<!--          </b-col>-->
<!--          <b-col cols="12" lg="6" sm="12" md="6">-->
<!--            <b-card bg-variant="monocrhome" class="p-lg-5">-->
<!--              <div class="d-flex flex-column">-->
<!--                <div class="d-flex mx-auto">-->
<!--                  <svg-->
<!--                    width="73"-->
<!--                    height="86"-->
<!--                    viewBox="0 0 73 86"-->
<!--                    fill="none"-->
<!--                    xmlns="http://www.w3.org/2000/svg"-->
<!--                  >-->
<!--                    <path-->
<!--                      d="M72.0585 20.8486V20.4268H72.0234C71.8125 15.2245 68.2974 10.0574 61.4255 6.103C47.3302 -2.03433 24.4824 -2.03433 10.4749 6.103C3.46239 10.1805 -0.017509 15.5233 6.62377e-05 20.8662V31.8859V32.0792V42.9055V43.0989V53.9252V54.1185V65.1382C0.0352167 70.4811 3.58541 75.8239 10.6331 79.8838C17.6983 83.9613 26.9253 86 36.1347 86C45.3617 86 54.5536 83.9613 61.5837 79.8838C68.5962 75.8064 72.0761 70.4635 72.0585 65.1382V54.1185V53.5034V43.0989V42.4486V32.044V31.4289V20.8486C72.0585 20.8486 72.0585 20.8662 72.0585 20.8486ZM17.8038 14.2403L19.7546 13.1155C20.2467 12.8343 21.02 12.8343 21.5297 13.1155L23.9375 14.504C24.4648 14.1876 25.0096 13.8888 25.5369 13.5725L23.1291 12.184C22.637 11.9028 22.637 11.4459 23.1291 11.1647L25.0799 10.0399C25.572 9.75865 26.3629 9.75865 26.855 10.0399L29.9307 11.8149L30.3349 11.6919C33.7797 10.6374 37.4353 10.1629 41.337 10.4441C44.3951 10.6726 47.1368 11.3931 49.6501 12.4477C50.6343 12.8519 51.5482 13.3088 52.3743 13.7834C54.5536 15.0488 56.2232 16.5251 57.5238 18.1948L57.7874 18.6517C58.0862 19.2668 57.7347 19.6887 56.6978 19.9347C55.6081 20.2159 54.5009 20.462 53.3936 20.708C52.6203 20.8662 52.0755 20.831 51.6009 20.5498C51.4779 20.4795 51.3725 20.3917 51.2494 20.3038C50.5113 19.6184 49.8434 18.8802 49.0525 18.2123C48.3495 17.5972 47.5762 17.0172 46.6975 16.5075C45.5375 15.8397 44.2018 15.2773 42.6024 14.8906C40.2122 14.2931 37.8747 14.4337 35.5196 14.9785L35.4317 14.9961L41.3897 18.4408C41.8818 18.722 41.8818 19.179 41.3897 19.4602L39.4389 20.585C38.9468 20.8662 38.1559 20.8662 37.6638 20.585L30.827 16.6481C30.3173 16.9469 29.7725 17.2633 29.2277 17.5796L36.0644 21.5165C36.5565 21.7977 36.5565 22.2546 36.0644 22.5358L34.1136 23.6607C33.6215 23.9419 32.8482 23.9419 32.3385 23.6607L26.0993 20.0577C24.7108 21.745 24.2715 23.4146 25.8357 25.1546C26.5035 25.8927 27.3647 26.543 28.3665 27.123C29.2453 27.6327 30.2119 28.072 31.2488 28.4763C32.4088 28.8981 33.6391 29.2847 34.8342 29.7241C35.0275 29.7944 35.1857 29.8647 35.3263 29.9526C35.8008 30.2338 35.8711 30.5501 35.5899 30.9895C35.1857 31.6574 34.7287 32.3077 34.2366 32.9404C33.8324 33.5204 33.0767 33.7313 31.987 33.5204C30.8973 33.2743 29.8252 32.9755 28.7707 32.6416C26.8374 32.0089 25.0975 31.2707 23.586 30.392C22.0043 29.4781 20.6685 28.4235 19.5964 27.2284C17.0832 24.3812 17.1359 21.4813 19.1922 18.5638C19.5964 17.9839 20.1589 17.4742 20.651 16.9293L17.7335 15.2421C17.3117 14.9785 17.3117 14.5215 17.8038 14.2403ZM10.6331 35.6118C24.746 43.7667 47.5586 43.7667 61.5837 35.6118C63.763 34.3464 65.5732 32.9404 67.0671 31.4641V32.0792C67.0847 35.7348 64.1672 39.5487 59.0704 42.5013C53.0245 46.0163 44.8872 47.9496 36.1347 47.9496C27.3823 47.9496 19.1922 46.0163 13.1112 42.5013C7.96165 39.5311 4.99143 35.6997 4.95628 32.0616V31.341C6.52048 32.8525 8.38345 34.3112 10.6331 35.6118ZM59.088 64.5231C53.0421 68.0381 44.9048 69.9714 36.1523 69.9714C27.3999 69.9714 19.2098 68.0381 13.1288 64.5231C7.97922 61.5529 5.00901 57.7215 4.97386 54.0834V53.5561C6.52048 55.0852 8.36588 56.5263 10.6331 57.8269C17.6983 61.9044 26.9253 63.9431 36.1347 63.9431C45.3617 63.9431 54.5536 61.9044 61.5837 57.8269C63.763 56.5615 65.5732 55.1555 67.0671 53.6791V54.1185C67.1023 57.7742 64.1848 61.5704 59.088 64.5231ZM59.088 53.521C53.0421 57.036 44.9048 58.9693 36.1523 58.9693C27.3999 58.9693 19.2098 57.036 13.1288 53.521C7.97922 50.5508 5.00901 46.7194 4.97386 43.0813V42.554C6.52048 44.0831 8.36588 45.5242 10.6331 46.8248C17.6983 50.9023 26.9253 52.941 36.1347 52.941C45.3617 52.941 54.5536 50.9023 61.5837 46.8248C63.763 45.5594 65.5732 44.1534 67.0671 42.6771V43.1164C67.1023 46.7545 64.1848 50.5508 59.088 53.521ZM59.088 75.5427C53.0421 79.0578 44.9048 80.9911 36.1523 80.9911C27.3999 80.9911 19.2098 79.0578 13.1288 75.5427C7.97922 72.5725 5.00901 68.7411 4.97386 65.1031V64.5758C6.52048 66.1048 8.36588 67.546 10.6331 68.8466C17.6983 72.924 26.9253 74.9628 36.1347 74.9628C45.3617 74.9628 54.5536 72.924 61.5837 68.8466C63.763 67.5812 65.5732 66.1751 67.0671 64.6988V65.1382C67.1023 68.7763 64.1848 72.5901 59.088 75.5427Z"-->
<!--                      fill="#54BD95"-->
<!--                    />-->
<!--                  </svg>-->
<!--                </div>-->

<!--                <h3 class="text-center">Get Started</h3>-->
<!--                <div>-->
<!--                  <label>Email</label>-->
<!--                  <b-form-input placeholder="Enter your email"/>-->
<!--                </div>-->
<!--                <div class="my-2">-->
<!--                  <label>Message</label>-->
<!--                  <b-form-textarea rows="2" placeholder="What are you say!"/>-->
<!--                </div>-->
<!--                <div class="my-2">-->
<!--                  <b-button block variant="primary" class="text-white"-->
<!--                  >Request Demo-->
<!--                  </b-button-->
<!--                  >-->
<!--                </div>-->
<!--                <div class="clearfix">-->
<!--                  <span class="float-right"-->
<!--                  >or-->
<!--                    <b-link href="#" class="text-white"-->
<!--                    >Start Free Trial</b-link-->
<!--                    >-->
<!--                  </span>-->
<!--                </div>-->
<!--              </div>-->
<!--            </b-card>-->
<!--          </b-col>-->
<!--        </b-row>-->
<!--      </b-container>-->
<!--    </section>-->
<!--    <section class="bg-dark text-white pt-5">-->
<!--      <b-container>-->
<!--        <b-row>-->
<!--          <b-col cols="12" lg="6" md="6">-->
<!--            <div>-->
<!--              <div>-->
<!--                <svg-->
<!--                  width="155"-->
<!--                  height="40"-->
<!--                  viewBox="0 0 155 40"-->
<!--                  fill="none"-->
<!--                  xmlns="http://www.w3.org/2000/svg"-->
<!--                >-->
<!--                  <path-->
<!--                    d="M0.586648 39V2.63636H14.5071C17.1349 2.63636 19.3189 3.05066 21.0589 3.87926C22.8108 4.69602 24.1188 5.81463 24.983 7.23508C25.8589 8.65554 26.2969 10.2654 26.2969 12.0646C26.2969 13.5443 26.0128 14.8108 25.4446 15.8643C24.8764 16.906 24.1129 17.7524 23.1541 18.4034C22.1953 19.0544 21.1241 19.522 19.9403 19.8061V20.1612C21.2306 20.2322 22.4676 20.6288 23.6513 21.3509C24.8468 22.0611 25.8234 23.0672 26.581 24.3693C27.3385 25.6714 27.7173 27.2457 27.7173 29.0923C27.7173 30.9744 27.2616 32.6671 26.3501 34.1705C25.4387 35.6619 24.0656 36.8397 22.2308 37.7038C20.3961 38.5679 18.0878 39 15.3061 39H0.586648ZM7.17401 33.4957H14.2585C16.6496 33.4957 18.3719 33.04 19.4254 32.1286C20.4908 31.2053 21.0234 30.0215 21.0234 28.5774C21.0234 27.5002 20.7571 26.5296 20.2244 25.6655C19.6918 24.7895 18.9342 24.103 17.9517 23.6058C16.9692 23.0968 15.7973 22.8423 14.4361 22.8423H7.17401V33.4957ZM7.17401 18.1016H13.6903C14.8267 18.1016 15.8506 17.8944 16.7621 17.4801C17.6735 17.054 18.3897 16.4562 18.9105 15.6868C19.4432 14.9055 19.7095 13.9822 19.7095 12.9169C19.7095 11.5083 19.2124 10.3482 18.218 9.43679C17.2356 8.52533 15.7737 8.0696 13.8324 8.0696H7.17401V18.1016ZM33.1639 39V11.7273H39.5914V39H33.1639ZM36.3954 7.85653C35.3774 7.85653 34.5015 7.51918 33.7676 6.84446C33.0337 6.15791 32.6667 5.33523 32.6667 4.37642C32.6667 3.40578 33.0337 2.58309 33.7676 1.90838C34.5015 1.22183 35.3774 0.87855 36.3954 0.87855C37.4252 0.87855 38.3012 1.22183 39.0233 1.90838C39.7572 2.58309 40.1241 3.40578 40.1241 4.37642C40.1241 5.33523 39.7572 6.15791 39.0233 6.84446C38.3012 7.51918 37.4252 7.85653 36.3954 7.85653ZM58.0973 39.5327C55.3748 39.5327 53.0369 38.9349 51.0838 37.7393C49.1425 36.5438 47.6451 34.8925 46.5916 32.7855C45.55 30.6667 45.0291 28.2282 45.0291 25.4702C45.0291 22.7003 45.5618 20.2559 46.6271 18.1371C47.6925 16.0064 49.1958 14.3492 51.1371 13.1655C53.0902 11.9699 55.3984 11.3722 58.0618 11.3722C60.2753 11.3722 62.2344 11.7805 63.9389 12.5973C65.6553 13.4022 67.0225 14.5445 68.0405 16.0241C69.0585 17.492 69.6385 19.2083 69.7805 21.1733H63.6371C63.3885 19.8594 62.7966 18.7644 61.8615 17.8885C60.9382 17.0007 59.7012 16.5568 58.1506 16.5568C56.8366 16.5568 55.6825 16.9119 54.6882 17.6222C53.6939 18.3205 52.9186 19.3267 52.3622 20.6406C51.8177 21.9545 51.5455 23.5289 51.5455 25.3636C51.5455 27.2221 51.8177 28.8201 52.3622 30.1577C52.9067 31.4834 53.6702 32.5073 54.6527 33.2294C55.647 33.9396 56.813 34.2947 58.1506 34.2947C59.0975 34.2947 59.9439 34.1172 60.6896 33.7621C61.4472 33.3951 62.0805 32.8684 62.5895 32.1818C63.0985 31.4953 63.4477 30.6607 63.6371 29.6783H69.7805C69.6267 31.6077 69.0585 33.3182 68.076 34.8097C67.0935 36.2893 65.7559 37.4493 64.0632 38.2898C62.3705 39.1184 60.3819 39.5327 58.0973 39.5327ZM86.9547 39.5327C84.2322 39.5327 81.8944 38.9349 79.9412 37.7393C77.9999 36.5438 76.5025 34.8925 75.449 32.7855C74.4074 30.6667 73.8865 28.2282 73.8865 25.4702C73.8865 22.7003 74.4192 20.2559 75.4846 18.1371C76.5499 16.0064 78.0532 14.3492 79.9945 13.1655C81.9476 11.9699 84.2559 11.3722 86.9192 11.3722C89.1328 11.3722 91.0918 11.7805 92.7963 12.5973C94.5127 13.4022 95.8799 14.5445 96.8979 16.0241C97.9159 17.492 98.4959 19.2083 98.638 21.1733H92.4945C92.2459 19.8594 91.6541 18.7644 90.7189 17.8885C89.7956 17.0007 88.5587 16.5568 87.008 16.5568C85.6941 16.5568 84.54 16.9119 83.5456 17.6222C82.5513 18.3205 81.776 19.3267 81.2196 20.6406C80.6751 21.9545 80.4029 23.5289 80.4029 25.3636C80.4029 27.2221 80.6751 28.8201 81.2196 30.1577C81.7641 31.4834 82.5276 32.5073 83.5101 33.2294C84.5044 33.9396 85.6704 34.2947 87.008 34.2947C87.955 34.2947 88.8013 34.1172 89.5471 33.7621C90.3046 33.3951 90.9379 32.8684 91.4469 32.1818C91.9559 31.4953 92.3051 30.6607 92.4945 29.6783H98.638C98.4841 31.6077 97.9159 33.3182 96.9334 34.8097C95.9509 36.2893 94.6133 37.4493 92.9206 38.2898C91.2279 39.1184 89.2393 39.5327 86.9547 39.5327ZM111.764 39.5504C110.036 39.5504 108.479 39.2427 107.094 38.6271C105.721 37.9998 104.632 37.0765 103.827 35.8572C103.034 34.638 102.637 33.1347 102.637 31.3473C102.637 29.8085 102.922 28.536 103.49 27.5298C104.058 26.5237 104.833 25.7188 105.816 25.1151C106.798 24.5114 107.905 24.0556 109.136 23.7479C110.379 23.4283 111.663 23.1974 112.989 23.0554C114.587 22.8897 115.883 22.7417 116.877 22.6115C117.872 22.4695 118.594 22.2564 119.044 21.9723C119.505 21.6764 119.736 21.2206 119.736 20.6051V20.4986C119.736 19.161 119.34 18.1252 118.547 17.3913C117.753 16.6574 116.611 16.2905 115.12 16.2905C113.545 16.2905 112.297 16.6338 111.373 17.3203C110.462 18.0069 109.846 18.8177 109.527 19.7528L103.525 18.9006C103.999 17.2434 104.78 15.8584 105.869 14.7457C106.958 13.6212 108.29 12.7808 109.864 12.2244C111.438 11.6562 113.178 11.3722 115.084 11.3722C116.398 11.3722 117.706 11.526 119.008 11.8338C120.31 12.1416 121.5 12.6506 122.577 13.3608C123.654 14.0592 124.518 15.0121 125.169 16.2195C125.832 17.4268 126.164 18.9361 126.164 20.7472V39H119.985V35.2536H119.772C119.381 36.0111 118.831 36.7214 118.12 37.3842C117.422 38.0353 116.54 38.562 115.475 38.9645C114.421 39.3551 113.184 39.5504 111.764 39.5504ZM113.433 34.8274C114.723 34.8274 115.842 34.5729 116.789 34.0639C117.736 33.5431 118.464 32.8565 118.973 32.0043C119.493 31.152 119.754 30.2228 119.754 29.2166V26.0028C119.553 26.1686 119.209 26.3224 118.724 26.4645C118.251 26.6065 117.718 26.7308 117.126 26.8374C116.534 26.9439 115.948 27.0386 115.368 27.1214C114.788 27.2043 114.285 27.2753 113.859 27.3345C112.9 27.4647 112.042 27.6778 111.284 27.9737C110.527 28.2696 109.929 28.6839 109.491 29.2166C109.053 29.7375 108.834 30.4122 108.834 31.2408C108.834 32.4245 109.266 33.3182 110.13 33.9219C110.994 34.5256 112.095 34.8274 113.433 34.8274ZM154.182 18.9361L148.323 19.5753C148.157 18.9834 147.867 18.4271 147.453 17.9062C147.05 17.3854 146.506 16.9652 145.819 16.6456C145.133 16.326 144.292 16.1662 143.298 16.1662C141.96 16.1662 140.836 16.4562 139.924 17.0362C139.025 17.6162 138.581 18.3679 138.593 19.2912C138.581 20.0843 138.871 20.7294 139.463 21.2266C140.066 21.7237 141.061 22.1321 142.446 22.4517L147.098 23.446C149.678 24.0024 151.596 24.8842 152.85 26.0916C154.117 27.299 154.756 28.8793 154.768 30.8324C154.756 32.5488 154.253 34.0639 153.259 35.3778C152.276 36.6799 150.909 37.6979 149.157 38.4318C147.405 39.1657 145.393 39.5327 143.12 39.5327C139.782 39.5327 137.095 38.8343 135.059 37.4375C133.023 36.0289 131.81 34.0698 131.419 31.5604L137.687 30.9567C137.971 32.1877 138.575 33.117 139.498 33.7443C140.422 34.3717 141.623 34.6854 143.103 34.6854C144.63 34.6854 145.855 34.3717 146.778 33.7443C147.713 33.117 148.181 32.3416 148.181 31.4183C148.181 30.6371 147.879 29.992 147.275 29.483C146.683 28.974 145.76 28.5833 144.505 28.3111L139.853 27.3345C137.237 26.79 135.302 25.8726 134.047 24.5824C132.792 23.2803 132.171 21.6349 132.183 19.6463C132.171 17.9654 132.627 16.5095 133.55 15.2784C134.485 14.0355 135.781 13.0767 137.439 12.402C139.108 11.7154 141.031 11.3722 143.209 11.3722C146.405 11.3722 148.921 12.0528 150.755 13.4141C152.602 14.7753 153.744 16.616 154.182 18.9361Z"-->
<!--                    fill="#54BD95"-->
<!--                  />-->
<!--                </svg>-->
<!--              </div>-->
<!--              <p class="my-3">Get Started now try our product</p>-->
<!--              <div-->
<!--                class="d-flex flex-row align-items-center absolute border border-white pl-3 py-1 pr-1 box-subsctibe w-75"-->
<!--              >-->
<!--                <b-form-input-->
<!--                  placeholder="Enter your email here"-->
<!--                  size="sm"-->
<!--                  class="rounded-lg bg-dark text-white border-0 input-subscribe"-->
<!--                >-->
<!--                </b-form-input>-->
<!--                <b-avatar class="text-white ml-2" variant="primary">-->
<!--                  <b-icon-arrow-right scale="1.6"/>-->
<!--                </b-avatar>-->
<!--              </div>-->
<!--            </div>-->
<!--          </b-col>-->
<!--          <b-col cols="12" lg="6" md="6">-->
<!--            <b-row>-->
<!--              <b-col-->
<!--                lg="4"-->
<!--                md="4"-->
<!--                sm="6"-->
<!--                cols="12"-->
<!--                class="d-flex flex-column mt-3"-->
<!--              >-->
<!--                <h6 class="mt-2 mb-4">Support</h6>-->
<!--                <b-link href="#" class="text-white">Help Center</b-link>-->
<!--                <b-link href="#" class="text-white">Account Information</b-link>-->
<!--                <b-link href="#" class="text-white">About</b-link>-->
<!--                <b-link href="#" class="text-white">Contact Us</b-link>-->
<!--              </b-col>-->
<!--              <b-col-->
<!--                lg="4"-->
<!--                md="4"-->
<!--                sm="6"-->
<!--                cols="12"-->
<!--                class="d-flex flex-column mt-3"-->
<!--              >-->
<!--                <h6 class="mt-2 mb-4">Help and Solution</h6>-->
<!--                <b-link href="#" class="text-white">Talk to support</b-link>-->
<!--                <b-link href="#" class="text-white">Support docs</b-link>-->
<!--                <b-link href="#" class="text-white">System status</b-link>-->
<!--                <b-link href="#" class="text-white">Covid Response</b-link>-->
<!--              </b-col>-->
<!--              <b-col-->
<!--                lg="4"-->
<!--                md="4"-->
<!--                sm="12"-->
<!--                cols="12"-->
<!--                class="d-flex flex-column mt-3"-->
<!--              >-->
<!--                <h6 class="mt-2 mb-4">Product</h6>-->

<!--                <b-link href="#" class="text-white">Update</b-link>-->
<!--                <b-link href="#" class="text-white">Security</b-link>-->
<!--                <b-link href="#" class="text-white">Beta Test</b-link>-->
<!--                <b-link href="#" class="text-white">Pricing product</b-link>-->
<!--              </b-col>-->
<!--            </b-row>-->
<!--          </b-col>-->
<!--        </b-row>-->
<!--      </b-container>-->
<!--    </section>-->
<!--    <section class="py-5 bg-dark text-white">-->
<!--      <b-container>-->
<!--        <b-row>-->
<!--          <b-col cols="12" lg="6" md="6" sm="6">-->
<!--            <h6>@ 2022 Biccas Ink. Copywrite and right reserved</h6>-->
<!--          </b-col>-->
<!--          <b-col cols="12" lg="6" md="6" sm="6">-->
<!--            <div class="clearfix">-->
<!--              <h6 class="float-lg-right float-md-right">-->
<!--                Terms and Conditions . Privacy Policy-->
<!--              </h6>-->
<!--            </div>-->
<!--          </b-col>-->
<!--          <b-col cols="12" lg="12" md="12" sm="12" class="d-flex flex-column">-->
<!--            <div class="mx-auto">-->
<!--              <b-link-->
<!--                class="text-white"-->
<!--                href="https://github.com/silvesterwali/saas-landing-page"-->
<!--              >-->
<!--                <b-icon-github-->
<!--                  class="mr-1"-->
<!--                />-->
<!--                https://github.com/silvesterwali/saas-landing-page-->
<!--              </b-link>-->
<!--            </div>-->
<!--            <div class="mx-auto">-->
<!--              <b-link class="text-white" href="https://uikit.to/saas-landing-pages/">-->
<!--                <b-icon-globe class="mr-1"/>-->
<!--                https://uikit.to/saas-landing-pages/-->
<!--              </b-link>-->
<!--            </div>-->
<!--          </b-col>-->
<!--        </b-row>-->
<!--      </b-container>-->
<!--    </section>-->
  </div>
</template>

<script>
import {} from 'bootstrap-vue'

export default {
  name: 'IndexPage',
  components: {
    // BIconPlayFill,
    // BIconArrowRight,
    // BIconGithub,
    // BIconGlobe,
  },
}
</script>
