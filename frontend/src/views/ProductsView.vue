<template>
  <v-container fluid class="pa-4" :style="{ backgroundColor: colors.background }">
    <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
      <v-card-title class="text-h5 d-flex justify-space-between align-center" :style="{ backgroundColor: colors.header, color: colors.headerText }">
        {{ organizationName }}
        <v-btn color="teal" @click="openAddDialog">Add New Item</v-btn>
      </v-card-title>

      <v-card :style="{ backgroundColor: colors.card, color: colors.text }" class="elevation-1 pa-4">
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                <tr>
                  <th style="text-align: left; padding: 8px;">ID</th>
                    <th style="text-align: left; padding: 8px;">Product Name</th>
                    <th style="text-align: left; padding: 8px;">Unit Price</th>
                    <th style="text-align: left; padding: 8px;">Quantity</th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in inventoryList" :key="item.id">
                    <td style="padding: 8px;">{{ item.id }}</td>
                    <td style="padding: 8px;">{{ item.product_name }}</td>
                    <td style="padding: 8px;">₹ {{ item.unit_price }}</td>
                    <td style="padding: 8px;">{{ item.quantity_in_stock }}</td>
                </tr>
                </tbody>
            </table>
        </v-card>

      <!-- Add Item Dialog -->
      <v-dialog v-model="addDialog" max-width="600px">
        <v-card>
          <v-card-title class="text-h6">Add New Item</v-card-title>
          <v-card-text>
            <v-form ref="formRef" @submit.prevent="saveNewItem">
              <v-text-field v-model="newItem.organization" label="Organization" required />
              <v-text-field v-model="newItem.product_name" label="Product Name" required />
              <v-text-field v-model="newItem.unit_price" label="Unit Price" type="number" required />
              <v-text-field v-model="newItem.quantity_in_stock" label="Quantity In Stock" type="number" required />
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer />
            <v-btn text @click="addDialog = false">Cancel</v-btn>
            <v-btn color="primary" @click="saveNewItem">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const inventoryList = ref([])
const organizationName = ref('My Organization')
const detailDialog = ref(false)
const addDialog = ref(false)
const selectedItem = ref(null)
const formRef = ref(null)

const newItem = ref({
  product_name: '',
  unit_price: null,
  quantity_in_stock: null
})

const colors = {
  background: '#0C0F0A',
  card: '#E8E8E8',
  text: '#0C0F0A',
  header: '#800020',
  headerText: '#E8E8E8'
}

const fetchInventory = async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/inventory/')
    inventoryList.value = response.data
  } catch (err) {
    console.error(err)
  }
}

const openAddDialog = () => {
  newItem.value = {
    product_name: '',
    unit_price: null,
    quantity_in_stock: null
  }
  addDialog.value = true
}

const saveNewItem = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/api/v1/inventory/', newItem.value)
    addDialog.value = false
    fetchInventory()
  } catch (err) {
    console.error(err)
  }
}

onMounted(() => {
  fetchInventory()
})
</script>
