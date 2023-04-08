<template>
  <div>
    <b-navbar toggleable="md">
      <b-container class="d-flex align-items-center">
        <b-navbar-brand tag="h1" class="mb-4 mt-0">

        </b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-item active to="/">Домой</b-nav-item>
            <b-nav-item href="#solutions">Наши решения</b-nav-item>
            <b-nav-item href="#about">О нас</b-nav-item>
<!--            <div class="mx-lg-5 d-lg-flex flex-lg-row">-->
<!--              <b-nav-item href="/">Login</b-nav-item>-->
<!--              <b-button class="rounded-lg text-white" variant="primary" href="#"-->
<!--                >Sign Up</b-button-->
<!--              >-->
<!--            </div>-->
          </b-navbar-nav>
        </b-collapse>
      </b-container>
    </b-navbar>
    <nuxt />
  </div>
</template>

<script>
export default {
  name: 'DefaultLayout',
}
</script>

<style lang="scss" scoped></style>
