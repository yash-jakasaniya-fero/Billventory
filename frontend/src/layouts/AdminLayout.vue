<template>
  <v-app>
    <v-navigation-drawer app permanent class="elevation-4">
      <v-row class="pa-4" align="center">
        <v-icon icon="mdi-package-variant-closed" class="mr-2" size="36"></v-icon>
        <span class="font-weight-bold text-green-700 text-xl">Billventory</span>
      </v-row>
      <v-divider></v-divider>
      <v-list nav dense>
        <v-list-item
          v-for="(page, index) in adminLinks"
          :key="page.name"
          :to="{name: page.name}"
          link
          class="nav-item"
          @mouseover="onMouseOver(index)"
          @mouseleave="onMouseLeave"
          :class="{'active-item': isActive(index)}"
        >
          <v-list-item-icon>
            <v-icon>{{ page.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title>{{ page.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from 'vue';

const adminLinks = [
  { name: "AdminOrganizations", title: "Organizations", icon: "mdi-account-group" },
  { name: "AdminOnboarding", title: "Onboarding Requests", icon: "mdi-account-plus" },
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

<style scoped>
.nav-item {
  transition: background-color 0.3s ease, transform 0.2s ease;
  padding: 12px 24px;
}

.nav-item:hover {
  background-color: #f4f7f6;
  transform: scale(1.05);
}

.active-item {
  background-color: #16a34a;
  color: white !important;
}

.v-navigation-drawer .v-row {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding-bottom: 16px;
}

.v-navigation-drawer {
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.v-icon {
  font-size: 24px;
  color: #16a34a;
}

.v-list-item-title {
  font-size: 16px;
  font-weight: 500;
  color: #333;
}

.v-main {
  background-color: #f9fafb;
}

.v-list-item-title {
  transition: transform 0.3s ease;
}

.v-app-bar-title {
  font-weight: bold;
  font-size: 20px;
}

.v-divider {
  margin: 20px 0;
}
</style>
