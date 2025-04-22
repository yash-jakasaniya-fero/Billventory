<template>
  <v-app>
    <!-- If the route is login or register, show only the router view -->
    <router-view v-if="isAuthPage" />
    
    <!-- Else, show the full layout with sidebar and top bar -->
    <template v-else>
      <v-navigation-drawer permanent>
        <v-list nav dense>
          <v-list-item class="justify-center">
            <img src="/App_logo.ico" style="width: 200px; border-radius: 8px;" />
          </v-list-item>
          <v-list-item
            v-for="(page, index) in pages"
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
          <v-toolbar-title class="font-weight-bold" style="color: #FFC542;">
            {{ getCurrentPageTitle }}
          </v-toolbar-title>
        </v-app-bar>

        <v-container fluid>
          <router-view />
        </v-container>
      </v-main>
    </template>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      pages: [
        { title: 'Dashboard', icon: 'mdi-view-dashboard', path: '/dashboard' },
        { title: 'Inventory', icon: 'mdi-cube-outline', path: '/inventory' },
        { title: 'Purchase-Order', icon: 'mdi-cart-plus', path: '/purchase-order' },
        { title: 'Sales-Order', icon: 'mdi-sale', path: '/sales-order' },
        { title: 'Supplier', icon: 'mdi-account-multiple-outline', path: '/supplier' },
        { title: 'Subscription', icon: 'mdi-credit-card', path: '/subscription' },
      ]
    }
  },
  computed: {
    getCurrentPageTitle() {
      const current = this.pages.find(p => p.path === this.$route.path)
      return current ? current.title : ''
    },
    isAuthPage() {
      return this.$route.path === '/login' || this.$route.path === '/register' || this.$route.path === '/verification';
    }
  }
}
</script>
