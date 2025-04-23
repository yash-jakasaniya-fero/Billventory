<template>
  <v-container fluid class="ma-20">
    <v-row class="bg-white align-center pa-0 ma-0">
      <!-- Left Section -->
      <v-col cols="12" md="6" class="text-left px-10 py-16">
        <h1 class="text-4xl font-bold mb-2">Simplify your</h1>
        <h1 class="text-4xl font-bold text-green-600 mb-6">business operations</h1>
        <p class="text-gray-600 text-lg mb-8">
          BillInventory helps businesses effortlessly manage products, track stock,
          generate invoices, and monitor sales — all in one intuitive platform.
        </p>
        <v-btn color="green" class="me-4" size="large">Get started</v-btn>
        <v-btn color="green lighten-5" class="text-green-700" size="large" variant="outlined">
          Live demo
        </v-btn>
      </v-col>

      <!-- Right Section -->
      <v-col cols="12" md="6">
        <v-img src="https://images.unsplash.com/photo-1556761175-129418cb2dfe" alt="Team working on computer"
          class="rounded-lg" height="400px" cover />
      </v-col>
    </v-row>

    <!-- Features Section -->
    <v-row class="py-16 px-10 justify-center bg-gray-50 text-center">
      <v-col cols="12">
        <h3 class="text-green-600 font-semibold mb-2">FEATURES</h3>
        <h2 class="text-3xl font-bold mb-6">Everything you need to manage your business</h2>
        <p class="text-gray-600 text-lg">
          BillInventory provides a comprehensive suite of tools to streamline your inventory and billing processes.
        </p>
      </v-col>
    </v-row>
    <v-row class="justify-center bg-gray-50 text-center">
      <v-col cols="6" md="4" class="mt-10">
        <v-icon color="green" size="40">mdi-cube-outline</v-icon>
        <h4 class="font-bold mt-4">Inventory Management</h4>
        <p class="text-gray-600 mt-2">
          Track your stock levels in real-time, set up low stock alerts, and manage multiple warehouses with ease.
        </p>
      </v-col>

      <v-col cols="6" md="4" class="mt-10">
        <v-icon color="green" size="40">mdi-file-document-outline</v-icon>
        <h4 class="font-bold mt-4">Invoice Generation</h4>
        <p class="text-gray-600 mt-2">
          Create professional invoices in seconds, customize templates, and send them directly to your customers.
        </p>
      </v-col>
      <v-col cols="6" md="4" class="mt-10">
        <v-icon color="green" size="40">mdi-chart-box-outline</v-icon>
        <h4 class="font-bold mt-4">Inventory Management</h4>
        <p class="text-gray-600 mt-2">
          Get insights into your sales performance with detailed reports and customizable dashboards.
        </p>
      </v-col>
      <v-col cols="6" md="4" class="mt-10">
        <v-icon color="green" size="40">mdi-chart-box-outline</v-icon>
        <h4 class="font-bold mt-4">Customer Management</h4>
        <p class="text-gray-600 mt-2">
          Maintain a comprehensive database of your customers and their purchase history.
        </p>
      </v-col>
    </v-row>
  </v-container>




 
</template>

<style>
.text-green-700 {
  color: #16a34a;
}

.bg-gray-50 {
  background-color: #f9fafb;
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

.btn-link {
  color: #7C6DD4;
  font-weight: 600;
  font-size: 16px;
  transition: all 0.2s ease;
} */
</style>