<template>
  <v-app>
    <v-navigation-drawer app>
      <v-list>
        <v-list-item
          v-for="item in orgLinks"
          :key="item.name"
          :to="{ name: item.name }"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
  
  <script setup>
const orgLinks = [
  { name: "OrgDashboard", title: "Dashboard" },
  { name: "OrgProducts", title: "Products" },
  { name: "OrgSuppliers", title: "Suppliers" },
  { name: "OrgPurchaseOrders", title: "Purchase Orders" },
  { name: "OrgBillings", title: "Billings" },
  { name: "OrgReports", title: "Reports" },
  { name: "OrgSupport", title: "Support" },
  { name: "OrgSettings", title: "Settings" },
];
</script>