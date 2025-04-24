<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12" md="3">
        <v-card>
          <v-card-title>
            <v-icon class="mr-2">mdi-package-variant</v-icon> Products
          </v-card-title>
          <v-card-text>120</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="3">
        <v-card>
          <v-card-title>
            <v-icon class="mr-2">mdi-account-multiple</v-icon> Suppliers
          </v-card-title>
          <v-card-text>8</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="3">
        <v-card>
          <v-card-title>
            <v-icon class="mr-2">mdi-file-document</v-icon> Purchase Orders
          </v-card-title>
          <v-card-text>25</v-card-text>
        </v-card>
      </v-col>

      <v-col cols="12" md="3">
        <v-card>
          <v-card-title>
            <v-icon class="mr-2">mdi-currency-inr</v-icon> Total Billings
          </v-card-title>
          <v-card-text>₹1,20,000</v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="6" md="6">
        <v-card>
          <v-card-title>Sales Overview</v-card-title>
          <v-card-text>
            <canvas id="sales-chart"></canvas>
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols="6" md="6">
        <v-card>
          <v-card-title>Inventory Summary</v-card-title>
          <v-card-text>
            <canvas id="inventory-chart"></canvas>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted } from "vue";
import Chart from "chart.js/auto";

onMounted(() => {
  const salesCtx = document.getElementById("sales-chart");
  new Chart(salesCtx, {
    type: "bar",
    data: {
      labels: ["Jan", "Feb", "Mar", "Apr"],
      datasets: [
        {
          label: "Sales",
          data: [1200, 1900, 3000, 2500],
          backgroundColor: "#16a34a",
        },
      ],
    },
  });

  const inventoryCtx = document.getElementById("inventory-chart");
  new Chart(inventoryCtx, {
    type: "doughnut",
    data: {
      labels: ["In Stock", "Low Stock", "Out of Stock"],
      datasets: [
        {
          data: [75, 15, 10],
          backgroundColor: ["#22c55e", "#facc15", "#ef4444"],
        },
      ],
    },
  });
});
</script>