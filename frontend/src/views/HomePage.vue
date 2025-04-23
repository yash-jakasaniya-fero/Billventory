<template>
  <v-container fluid class="ma-20">
    <v-container fluid class="pa-0 fill-height bg-white">
      <v-row no-gutters>
        <!-- Left Section -->
        <v-col cols="12" lg="6" class="d-flex align-center">
          <v-container>
            <v-row>
              <v-col cols="12" class="text-center text-lg-left">
                <h1 class="text-h2 font-weight-bold mb-4">
                  <div>Simplify your</div>
                  <div class="text-green-700">business operations</div>
                </h1>
                <p class="text-body-1 text-grey-darken-1 mb-6">
                  BillInventory helps businesses effortlessly manage products,
                  track stock, generate invoices, and monitor sales — all in one
                  intuitive platform.
                </p>
                <div
                  class="d-flex flex-column flex-sm-row justify-center justify-lg-start"
                >
                  <v-btn
                    color="#16a34a"
                    class="mb-3 mb-sm-0 mr-sm-3"
                    size="large"
                    variant="flat"
                  >
                    Get started
                  </v-btn>
                  <v-btn
                    color="#16a34a"
                    class="bg-primary-50 text-green-700"
                    size="large"
                    variant="outlined"
                  >
                    Live demo
                  </v-btn>
                </div>
              </v-col>
            </v-row>
          </v-container>
        </v-col>

        <!-- Right Image Section -->
        <v-col cols="12" lg="6" class="d-none d-lg-flex">
          <v-img
            src="https://images.unsplash.com/photo-1551434678-e076c223a692?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2850&q=80"
            class="h-100"
            cover
          />
        </v-col>
      </v-row>
    </v-container>

    <!-- Features Section -->
    <v-container>
      <v-row justify="center" class="py-10">
        <v-col cols="12" lg="8" class="text-center">
          <h2
            class="text-subtitle-1 text-green-700 font-weight-bold text-uppercase text-green-700"
          >
            Features
          </h2>
          <h3 class="text-h4 font-weight-bold mt-2 black">
            Everything you need to manage your business
          </h3>
          <p class="text-body-1 text-green-700 mt-4">
            BillInventory provides a comprehensive suite of tools to streamline
            your inventory and billing processes.
          </p>
        </v-col>
      </v-row>

      <v-row class="mt-10" dense>
        <v-col cols="12" md="6" v-for="(feature, i) in features" :key="i">
          <div class="d-flex">
            <v-icon color="#16a34a" size="48" class="me-4">{{
              feature.icon
            }}</v-icon>
            <div>
              <h4 class="text-subtitle-1 font-weight-medium">
                {{ feature.title }}
              </h4>
              <p class="text-body-2 text-grey-darken-1 mt-1">
                {{ feature.description }}
              </p>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>

    <!-- Testimonials Section -->
    <v-container class="bg-green-lighten-5">
      <v-row justify="center" class="pa-10">
        <v-col cols="12" md="8" class="text-center">
          <h2 class="text-h4 font-weight-bold">
            Trusted by businesses worldwide
          </h2>
          <p class="text-body-1 text-grey-darken-1 mt-3">
            See what our customers have to say about BillInventory
          </p>
        </v-col>
      </v-row>

      <v-row class="mt-12" dense>
        <v-col
          cols="12"
          md="6"
          lg="4"
          v-for="(testimonial, i) in testimonials"
          :key="i"
        >
          <v-card class="pa-6">
            <div class="d-flex align-center">
              <v-avatar size="48" class="me-4">
                <v-img :src="testimonial.avatar" />
              </v-avatar>
              <div>
                <h4 class="text-subtitle-1 font-weight-medium">
                  {{ testimonial.name }}
                </h4>
                <p class="text-body-2 text-grey-darken-1">
                  {{ testimonial.role }}
                </p>
              </div>
            </div>
            <p class="text-body-2 text-grey-darken-2 mt-4">
              "{{ testimonial.quote }}"
            </p>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script setup>
const features = [
  {
    title: "Inventory Management",
    description:
      "Track your stock levels in real-time, set up low stock alerts, and manage multiple warehouses with ease.",
    icon: "mdi-package",
  },
  {
    title: "Invoice Generation",
    description:
      "Create professional invoices in seconds, customize templates, and send them directly to your customers.",
    icon: "mdi-file-arrow-left-right-outline",
  },
  {
    title: "Sales Analytics",
    description:
      "Get insights into your sales performance with detailed reports and customizable dashboards.",
    icon: "mdi-poll",
  },
  {
    title: "Customer Management",
    description:
      "Maintain a comprehensive database of your customers and their purchase history.",
    icon: "mdi-account-group",
  },
];

const testimonials = [
  {
    name: "Sarah Johnson",
    role: "Retail Store Owner",
    avatar:
      "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    quote:
      "BillInventory has transformed how we manage our inventory. We've reduced stockouts by 75% and saved countless hours on manual inventory counts.",
  },
  {
    name: "Tom Wilson",
    role: "E-commerce Manager",
    avatar:
      "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    quote:
      "The billing system is incredibly intuitive. We can generate professional invoices in seconds and our customers love the clean, professional look.",
  },
  {
    name: "Maria Garcia",
    role: "Small Business Owner",
    avatar:
      "https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80",
    quote:
      "As a small business, we needed an affordable solution that could grow with us. BillInventory has been perfect - easy to use yet powerful enough for all our needs.",
  },
];
</script>

<style>
.text-green-700 {
  color: #16a34a;
}

.bg-gray-50 {
  background-color: #f9fafb;
}

.text-primary {
  color: var(--v-theme-primary);
}
.bg-primary-lighten-5 {
  background-color: #f0f5ff;
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