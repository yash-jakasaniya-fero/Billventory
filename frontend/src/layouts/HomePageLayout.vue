<template>
  <v-app>
    <v-app-bar app fixed flat height="75" class="shared-bar border">
      <v-list-item class="justify-center">
        <!-- <img src="/App_logo.ico" style="width: 200px;" /> -->

      </v-list-item>
      <div class="d-flex align-center">
        <v-icon icon="mdi-package-variant-closed" class="mr-2 text-green-700" size="32"></v-icon>
        <span class="font-weight-bold text-green-700 text-xl">BillInventory</span>
      </div>
      <v-spacer></v-spacer>
      <router-link to="/" class="text-green-700 text-decoration-none">
        <v-btn text class="btn-link" elevation="0">Home</v-btn>
      </router-link>
      <router-link :to="{ name: 'About Us' }" class="text-green-700 text-decoration-none">
        <v-btn text class="btn-link" elevation="0">About Us</v-btn>
      </router-link>
      <router-link :to="{ name: 'Subscriptions' }" class="text-green-700 text-decoration-none">
        <v-btn text class="btn-link" elevation="0">Subscriptions</v-btn>
      </router-link>
      <router-link :to="{ name: 'Login' }" class="text-green-700 text-decoration-none">
        <v-btn text class="btn-link mr-2" color="green" variant="elevated">Login</v-btn>
      </router-link>
      <router-link :to="{ name: 'Register' }" class="text-green-700 text-decoration-none">
        <v-btn text class="btn-link mr-2" variant="outlined">Register</v-btn>
      </router-link>
    </v-app-bar>

    <v-main class="pa-0 ma-0">
      <router-view />
    </v-main>
    <!-- CTA Section -->
    <v-container fluid class="highter-primary">
      <v-row align="center" justify="space-between" class="pa-5">
        <v-col cols="12" md="7">
          <h2 class="text-h4 font-weight-bold text-white mb-2">
            Ready to transform your business?
          </h2>
          <p class="text-h6 text-white-lighten-2">
            Join thousands of satisfied customers today.
          </p>
        </v-col>
        <v-col cols="12" md="5" class="d-flex flex-column flex-sm-row justify-md-end mt-4 mt-md-0">
          <v-btn color="white" class="mr-sm-4 mb-4 mb-sm-0">
            Get started
          </v-btn>
          <v-btn variant="outlined" color="white">
            Contact sales
          </v-btn>
        </v-col>
      </v-row>
    </v-container>
    <v-footer app fixed height="75" class="shared-bar d-flex justify-space-between border">
      <div class="text-subtitle-2 text-green-700">
        © {{ currentYear }} Billventory. All rights reserved.
      </div>
      <div class="pa-1 ga-1 ">
        <v-btn icon variant="text">
          <v-icon>mdi-facebook</v-icon>
        </v-btn>
        <v-btn icon variant="text">
          <v-icon>mdi-instagram</v-icon>
        </v-btn>
        <v-btn icon variant="text">
          <v-icon>mdi-twitter</v-icon>
        </v-btn>
        <v-btn icon variant="text">
          <v-icon>mdi-linkedin</v-icon>
        </v-btn>
      </div>
    </v-footer>
  </v-app>
</template>

<script setup>
const currentYear = new Date().getFullYear()
</script>

<style>
.text-green-700 {
  color: #16a34a;
}

.bg-gray-50 {
  background-color: #f9fafb;
}

.text-xl {
  font-size: 1.5rem;
}

.highter-primary {
  background-color: #16a34a;
  color: #f9fafb;
  font-family: sans-serif;
  font-size: 14px;
  margin-bottom: 75px;
  padding: 20px;
}

.shared-bar {
  color: #16a34a;
  background-color: #f9fafb;
  /* or any consistent text/icon color */
  font-family: sans-serif;
  font-size: 14px;
}

/* .main-background {
  background-color: #D7CFFF;
  min-height: 100vh;
}

.hero-content {
  padding-top: 140px;
}

.feature-card {
  min-height: 280px;
  border-radius: 12px;
  transition: all 0.3s ease;
}

.feature-card:hover {
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
}

.trusted-section {
  background-color: #D7CFFF;
}

.navbar {
  position: fixed;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  z-index: 10;
}

.navbar-content {
  padding: 0 20px;
  border-radius: 14px;
}
*/
.btn-link {
  color: #7C6DD4;
  font-weight: 600;
  font-size: 16px;
  transition: all 0.2s ease;
}
</style>