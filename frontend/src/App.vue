<template>
  <v-app>
    <v-navigation-drawer app permanent color="#0C0F0A" width="180">
      <v-list dense>
        <v-list-item class="justify-center">
          <img
            src="/logo.ico"
            style="width: 80px; border-radius: 8px;"
          />
        </v-list-item>

        <v-list-item
          v-for="(page, index) in pages"
          :key="index"
          @click="currentPage = page.component"
          :class="{ 'active-item': currentPage === page.component }"
        >
          <v-list-item-icon>
            <v-icon color="#800020">{{ page.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-title class="black--text">{{ page.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <v-app-bar color="#0C0F0A" flat app>
        <v-toolbar-title class="font-weight-bold" style="color: #800020;">
          {{ getCurrentPageTitle }}
        </v-toolbar-title>
      </v-app-bar>

      <v-container fluid style="background-color: #E8E8E8;">
        <component :is="currentPage" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import DashboardView from './views/DashboardView.vue'
import ProductsView from './views/ProductsView.vue'
import PurchaseOrderView from './views/PurchaseOrderView.vue'
import SalesOrderView from './views/SalesOrderView.vue'
import SignInSignUpView from './views/SignInSignUpView.vue'
import SupplierView from './views/SupplierView.vue'

export default {
  name: 'MainLayout',
  components: {
    DashboardView,
    ProductsView,
    PurchaseOrderView,
    SalesOrderView,
    SupplierView,
    SignInSignUpView
  },
  data() {
    return {
      pages: [
        { component: 'DashboardView', title: 'Dashboard', icon: 'mdi-view-dashboard' },
        { component: 'ProductsView', title: 'Products', icon: 'mdi-cube-outline' },
        { component: 'PurchaseOrderView', title: 'Purchase-Order', icon: 'mdi-cart-plus'},
        { component: 'SalesOrderView', title: 'Sales-Order', icon: 'mdi-sale'},
        { component: 'SupplierView', title: 'Supplier', icon: 'mdi-account-multiple-outline'},
        { component: 'SignInSignUpView', title: 'SignInSignUp', icon: 'mdi-account-key'}
      ],
      currentPage: ''
    }
  },
  computed: {
    getCurrentPageTitle() {
      const page = this.pages.find(p => p.component === this.currentPage)
      return page ? page.title : ''
    }
  }
}
</script>

<style scoped>
.v-navigation-drawer {
  border-right: 1px solid #e0e0e0;
}

.v-app-bar {
  height: 64px;
}

.active-item {
  background-color: #008080;
  border-radius: 6px;
  margin: 4px;
}

.v-list-item-title {
  font-weight: 500;
}

.v-main {
  padding-top: 64px;
}
</style>


