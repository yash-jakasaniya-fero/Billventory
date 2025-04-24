<template>
  <v-app>
    <v-app-bar>
      <v-row class="ma-0" justify="space-between" align="center">
        <v-col>
          <v-icon
            icon="mdi-package-variant-closed"
            color="black"
            size="32"
            @click="$router.push({ name: 'HomePage' })"
          ></v-icon>
          <span
            class="font-weight-bold text-green-700 text-xl"
            @click="$router.push({ name: 'HomePage' })"
          >
            Billventory
          </span>
        </v-col>

        <v-col cols="auto">
          <v-menu location="bottom end">
            <template #activator="{ props }">
              <v-avatar color="black" v-bind="props" class="cursor-pointer">
                <v-icon color="white" icon="mdi-account-circle"></v-icon>
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

    <v-navigation-drawer>
      <v-list nav>
        <v-list-item
          v-for="(page, index) in adminLinks"
          :key="page.name"
          :to="{ name: page.name }"
          class="nav-item"
          :class="{ 'active-item': isActive(index) }"
        >
          <v-list-item
            :prepend-icon="page.icon"
            :title="page.title"
            value="inbox"
          ></v-list-item>
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

const activeLinkIndex = ref(null);

const isActive = (index) => activeLinkIndex.value === index;

const onMouseOver = (index) => {
  activeLinkIndex.value = index;
};

const onMouseLeave = () => {
  activeLinkIndex.value = null;
};
</script>

