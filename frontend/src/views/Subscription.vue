<template>
  <!-- Pricing Header -->
  <v-container class="py-16">
    <v-row justify="center">
      <v-col cols="12" md="8" class="text-center">
        <span class="text-uppercase text-primary font-weight-medium">Pricing</span>
        <h1 class="text-h3 font-weight-bold mt-2 mb-4">
          Take control of your business
        </h1>
        <p class="text-body-1 mb-8">
          Choose the plan that's right for your business and scale as you grow.
        </p>
      </v-col>
    </v-row>
  </v-container>

  <!-- Pricing Toggle -->
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8" lg="6" class="text-center">
        <v-btn-toggle v-model="billingInterval" color="primary" mandatory rounded="pill" density="comfortable">
          <v-btn value="monthly">Monthly</v-btn>
          <v-btn value="annual">Annual <span class="text-primary-darken-2">(-20%)</span></v-btn>
        </v-btn-toggle>
      </v-col>
    </v-row>
  </v-container>

  <!-- Pricing Cards -->
  <v-container class="py-12">
    <v-row>
      <!-- Starter Plan -->
      <v-col cols="12" md="4">
        <v-card class="h-100" variant="outlined">
          <v-card-item>
            <v-card-title class="text-h5">Starter</v-card-title>
            <v-card-subtitle>
              Perfect for small businesses just getting started with inventory management.
            </v-card-subtitle>
          </v-card-item>
          <v-card-text>
            <div class="text-h3 font-weight-bold mb-4">
              {{ billingInterval === 'monthly' ? '$29' : '$279' }}
              <span class="text-body-1 font-weight-regular">/{{ billingInterval === 'monthly' ? 'mo' : 'yr' }}</span>
            </div>
            <v-btn block color="primary" size="large" class="mb-6">
              Start your trial
            </v-btn>
            <h3 class="text-subtitle-1 font-weight-bold mb-4">What's included</h3>
            <v-list lines="two">
              <v-list-item prepend-icon="mdi-check" title="Up to 1,000 inventory items"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Basic reporting"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Invoice generation"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Email support"></v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Professional Plan -->
      <v-col cols="12" md="4">
        <v-card class="h-100" color="primary-lighten-5" variant="outlined" border>
          <v-card-item>
            <div class="position-absolute" style="top: -12px; right: 24px;">
              <v-chip color="primary" label>Most Popular</v-chip>
            </div>
            <v-card-title class="text-h5">Professional</v-card-title>
            <v-card-subtitle>
              For growing businesses with more complex inventory needs.
            </v-card-subtitle>
          </v-card-item>
          <v-card-text>
            <div class="text-h3 font-weight-bold mb-4">
              {{ billingInterval === 'monthly' ? '$79' : '$759' }}
              <span class="text-body-1 font-weight-regular">/{{ billingInterval === 'monthly' ? 'mo' : 'yr' }}</span>
            </div>
            <v-btn block color="primary" size="large" class="mb-6">
              Start your trial
            </v-btn>
            <h3 class="text-subtitle-1 font-weight-bold mb-4">What's included</h3>
            <v-list lines="two">
              <v-list-item prepend-icon="mdi-check" title="Up to 10,000 inventory items"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Advanced reporting"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Custom invoice templates"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Priority email support"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Multiple user accounts"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="API access"></v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>

      <!-- Enterprise Plan -->
      <v-col cols="12" md="4">
        <v-card class="h-100" variant="outlined">
          <v-card-item>
            <v-card-title class="text-h5">Enterprise</v-card-title>
            <v-card-subtitle>
              For large businesses with complex inventory and billing requirements.
            </v-card-subtitle>
          </v-card-item>
          <v-card-text>
            <div class="text-h3 font-weight-bold mb-4">
              {{ billingInterval === 'monthly' ? '$199' : '$1,919' }}
              <span class="text-body-1 font-weight-regular">/{{ billingInterval === 'monthly' ? 'mo' : 'yr' }}</span>
            </div>
            <v-btn block color="primary" size="large" class="mb-6">
              Contact sales
            </v-btn>
            <h3 class="text-subtitle-1 font-weight-bold mb-4">What's included</h3>
            <v-list lines="two">
              <v-list-item prepend-icon="mdi-check" title="Unlimited inventory items"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Custom reporting"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Advanced invoice customization"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="24/7 phone and email support"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Unlimited user accounts"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Advanced API access"></v-list-item>
              <v-list-item prepend-icon="mdi-check" title="Dedicated account manager"></v-list-item>
            </v-list>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>

  <!-- Feature Comparison -->
  <v-container fluid class="py-12 bg-grey-lighten-4">
    <v-row justify="center">
      <v-col cols="12" md="10" lg="8" class="text-center">
        <h2 class="text-h4 font-weight-bold mb-3">
          Compare plans in detail
        </h2>
        <p class="text-body-1 mb-8">
          Find the perfect plan for your business needs
        </p>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" md="10" xl="8">
        <v-table>
          <thead>
            <tr>
              <th class="text-left">Feature</th>
              <th class="text-center">Starter</th>
              <th class="text-center">Professional</th>
              <th class="text-center">Enterprise</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Inventory Items</td>
              <td class="text-center">1,000</td>
              <td class="text-center">10,000</td>
              <td class="text-center">Unlimited</td>
            </tr>
            <tr>
              <td>User Accounts</td>
              <td class="text-center">2</td>
              <td class="text-center">10</td>
              <td class="text-center">Unlimited</td>
            </tr>
            <tr>
              <td>Invoice Templates</td>
              <td class="text-center">Basic</td>
              <td class="text-center">Custom</td>
              <td class="text-center">Advanced Custom</td>
            </tr>
            <tr>
              <td>Reporting</td>
              <td class="text-center">Basic</td>
              <td class="text-center">Advanced</td>
              <td class="text-center">Custom</td>
            </tr>
            <tr>
              <td>API Access</td>
              <td class="text-center">
                <v-icon color="error">mdi-close</v-icon>
              </td>
              <td class="text-center">
                <v-icon color="success">mdi-check</v-icon>
              </td>
              <td class="text-center">
                <v-icon color="success">mdi-check</v-icon>
              </td>
            </tr>
            <tr>
              <td>Support</td>
              <td class="text-center">Email</td>
              <td class="text-center">Priority Email</td>
              <td class="text-center">24/7 Phone & Email</td>
            </tr>
            <tr>
              <td>Dedicated Account Manager</td>
              <td class="text-center">
                <v-icon color="error">mdi-close</v-icon>
              </td>
              <td class="text-center">
                <v-icon color="error">mdi-close</v-icon>
              </td>
              <td class="text-center">
                <v-icon color="success">mdi-check</v-icon>
              </td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
    </v-row>
  </v-container>

  <!-- FAQ Section -->
  <v-container class="py-12">
    <v-row justify="center">
      <v-col cols="12" md="10" lg="8" class="text-center">
        <h2 class="text-h4 font-weight-bold mb-8">
          Frequently asked questions
        </h2>
      </v-col>
    </v-row>

    <v-row justify="center">
      <v-col cols="12" md="10" lg="8">
        <v-expansion-panels variant="accordion">
          <v-expansion-panel>
            <v-expansion-panel-title>
              Can I try Billventory before subscribing?
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              Yes, all plans come with a 14-day free trial. No credit card required to start.
            </v-expansion-panel-text>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-title>
              Can I change plans later?
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              You can upgrade or downgrade your plan at any time. Changes take effect at the start of your next billing
              cycle.
            </v-expansion-panel-text>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-title>
              Is there a setup fee?
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              No, there are no setup fees for any of our plans. You only pay the subscription fee.
            </v-expansion-panel-text>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-title>
              How secure is my data?
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              We use industry-standard encryption and security practices to keep your data safe. All data is backed up
              daily.
            </v-expansion-panel-text>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-title>
              Can I cancel my subscription?
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              Yes, you can cancel your subscription at any time. You'll continue to have access until the end of your
              current billing period.
            </v-expansion-panel-text>
          </v-expansion-panel>

          <v-expansion-panel>
            <v-expansion-panel-title>
              Do you offer discounts for non-profits?
            </v-expansion-panel-title>
            <v-expansion-panel-text>
              Yes, we offer special pricing for non-profit organizations. Please contact our sales team for more
              information.
            </v-expansion-panel-text>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </v-container>
</template>