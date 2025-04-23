<template>
  <v-app>
    <v-navigation-drawer app permanent>
      <v-list nav dense>
        <v-list-item class="justify-center">
          <img src="/App_logo.ico" style="width: 200px; border-radius: 8px" />
        </v-list-item>
        <v-list-item
          v-for="(page, index) in adminLinks"
          :key="index"
          :to="page.path"
          exact
          :active-class="'active-item'"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ page.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ page.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-app-bar color="#A88AF3" flat app>
        <v-toolbar-title class="font-weight-bold" style="color: #ffc542">
          {{ currentPageTitle }}
        </v-toolbar-title>
      </v-app-bar>

      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>
  
  <script setup>
const adminLinks = [
  { name: "AdminOrganizations", title: "Organizations" },
  { name: "AdminOnboarding", title: "Onboarding Requests" },
  { name: "AdminSupport", title: "Support" },
  { name: "AdminSettings", title: "Settings" },
];
</script>