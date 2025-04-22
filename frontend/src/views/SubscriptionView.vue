<template>
  <v-container class="py-10">
    <!-- Heading -->
    <v-row justify="center" class="mb-10">
      <v-col cols="12" md="8" class="text-center">
        <h1 class="text-h4 font-weight-bold mb-2">Choose Your Plan</h1>
        <p class="text-subtitle-1 text-grey-darken-1">
          Select the perfect subscription that fits your needs. Upgrade or downgrade anytime.
        </p>
      </v-col>
    </v-row>

    <!-- Plans -->
    <v-row justify="center" class="mb-10" dense>
      <!-- Lite Plan -->
      <v-col cols="12" md="4">
        <v-card outlined class="d-flex flex-column h-100">
          <v-card-title class="text-h6">Lite</v-card-title>
          <v-card-subtitle class="text-body-2 text-grey">Perfect for individuals and small projects</v-card-subtitle>
          <v-card-text>
            <div class="text-h5 font-weight-bold">$9 <span class="text-caption text-grey">/month</span></div>
            <v-list dense>
              <v-list-item v-for="(item, i) in litePlanFeatures" :key="i">
                <v-list-item-icon>
                  <v-icon color="green">mdi-check-circle</v-icon>
                </v-list-item-icon>
                <v-list-item-title>{{ item }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions class="mt-auto">
            <v-btn block outlined color="primary">Get Started</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <!-- Pro Plan -->
      <v-col cols="12" md="4">
        <v-card class="border border-primary d-flex flex-column h-100">
          <v-chip color="primary" text-color="white" small class="ma-2 float-right" label>Popular</v-chip>
          <v-card-title class="text-h6">Pro</v-card-title>
          <v-card-subtitle class="text-body-2 text-grey">Ideal for growing businesses and teams</v-card-subtitle>
          <v-card-text>
            <div class="text-h5 font-weight-bold">$29 <span class="text-caption text-grey">/month</span></div>
            <v-list dense>
              <v-list-item v-for="(item, i) in proPlanFeatures" :key="i">
                <v-list-item-icon>
                  <v-icon color="green">mdi-check-circle</v-icon>
                </v-list-item-icon>
                <v-list-item-title>{{ item }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions class="mt-auto">
            <v-btn block color="primary" dark>Get Started</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <!-- Diamond Plan -->
      <v-col cols="12" md="4">
        <v-card outlined class="d-flex flex-column h-100">
          <v-card-title class="text-h6">Diamond</v-card-title>
          <v-card-subtitle class="text-body-2 text-grey">For enterprises and large-scale operations</v-card-subtitle>
          <v-card-text>
            <div class="text-h5 font-weight-bold">$99 <span class="text-caption text-grey">/month</span></div>
            <v-list dense>
              <v-list-item v-for="(item, i) in diamondPlanFeatures" :key="i">
                <v-list-item-icon>
                  <v-icon color="green">mdi-check-circle</v-icon>
                </v-list-item-icon>
                <v-list-item-title>{{ item }}</v-list-item-title>
              </v-list-item>
            </v-list>
          </v-card-text>
          <v-card-actions class="mt-auto">
            <v-btn block outlined color="primary">Contact Sales</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- Footer Note -->
    <v-row justify="center">
      <v-col cols="12" md="8" class="text-center">
        <p class="text-body-2 text-grey">
          All plans include a 14-day free trial. No credit card required.
        </p>
        <p class="text-body-2 text-grey mt-2">
          Need a custom plan?
          <a href="#" class="text-primary text-decoration-underline font-weight-medium">
            Contact us
          </a>
          for enterprise pricing.
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue'

const litePlanFeatures = ref([
  '5 projects',
  'Up to 10GB storage',
  'Basic analytics',
  'Email support',
])

const proPlanFeatures = ref([
  '25 projects',
  'Up to 50GB storage',
  'Advanced analytics',
  'Priority email support',
  'Team collaboration tools',
  'API access',
])

const diamondPlanFeatures = ref([
  'Unlimited projects',
  'Up to 500GB storage',
  'Enterprise analytics',
  '24/7 dedicated support',
  'Advanced team management',
  'Custom integrations',
  'Dedicated account manager',
])
</script>
