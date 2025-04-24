<template>
  <v-app>
    <v-app-bar class="app-bar">
      <v-row class="ma-0" justify="space-between" align="center">
        <v-col>
          <v-icon
            icon="mdi-package-variant-closed"
            color="black"
            size="32"
            @click="$router.push({ name: 'HomePage' })"
          ></v-icon>
          <span
            class="font-weight-bold text-xl"
            @click="$router.push({ name: 'HomePage' })"
          >
            Billventory
          </span>
        </v-col>

        <v-col cols="auto">
          <v-menu location="bottom end">
            <template #activator="{ props }">
              <v-avatar v-bind="props" class="cursor-pointer">
                <v-icon color="black" large icon="mdi-account-circle"></v-icon>
              </v-avatar>
            </template>

            <v-list>
              <v-list-item @click="$router.push({ name: 'ProfilePage' })">
                <v-list-item-title>Profile</v-list-item-title>
              </v-list-item>
              <v-list-item
                @click="$router.push({ name: 'ChangePasswordPage' })"
              >
                <v-list-item-title>Change Password</v-list-item-title>
              </v-list-item>
              <v-list-item @click="logout">
                <v-list-item-title>Logout</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-menu>
        </v-col>
      </v-row>
    </v-app-bar>

    <v-navigation-drawer class="app-bar">
      <v-list nav>
        <v-list-item
          v-for="(page, index) in adminLinks"
          :key="page.name"
          :to="{ name: page.name }"
          :active="isActiveRoute(page.name)"
          class="flat-nav"
        >
          <template #prepend>
            <v-icon color="black">{{ page.icon }}</v-icon>
          </template>
          <v-list-item-title class="font-weight-bold text-xl">{{
            page.title
          }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main class="d-flex justify-center bg-cover">
      <v-container>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const isActiveRoute = (routeName) => {
  return router.name === routeName;
};

const logout = () => {
  // Clear user info from localStorage
  localStorage.removeItem("user");
  localStorage.removeItem("token"); // or any other keys you store

  // Redirect to login page
  router.push({ name: "Login" });
};

const adminLinks = [
  {
    name: "AdminOrganizations",
    title: "Organizations",
    icon: "mdi-account-group",
  },
  {
    name: "AdminOnboarding",
    title: "Onboarding Requests",
    icon: "mdi-account-plus",
  },
  { name: "AdminSupport", title: "Support", icon: "mdi-headset" },
  { name: "AdminSettings", title: "Settings", icon: "mdi-cogs" },
];
</script>

<style scoped>
.app-bar {
  background-color: white;
  color: #16a34a;
}

.flat-nav {
  background-color: transparent !important;
  transition: none;
}

.flat-nav:hover {
  background-color: transparent !important;
}

.flat-nav.v-list-item--active {
  background-color: #e0f2f1 !important; /* light green or your theme */
  font-weight: bold;
}
</style>