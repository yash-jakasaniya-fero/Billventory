<template>
  
    <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
      <v-card-title
        class="text-h5 d-flex justify-space-between align-center"
        :style="{ backgroundColor: colors.header, color: colors.headerText }"
      >
        {{ organizationName }}
        <v-btn color="teal" @click="openAddDialog">Add New Item</v-btn>
      </v-card-title>


      <!-- Inventory Item Table -->
        <v-data-table
          v-model:items-per-page="itemsPerPage"
          :headers="headers"
          :items="inventoryList"
          :items-length="inventoryList.length"
          :loading="loading"
          item-value="id"
          class="elevation-1"
          :style="{ backgroundColor: colors.card, color: colors.text }"
        >
          <template #item.unit_price="{ item }">
            ₹ {{ item.unit_price }}
          </template>
        </v-data-table>

      
      <!-- Add Item Dialog -->
      <v-dialog v-model="addDialog" max-width="600px">
        <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
          <v-card-title :style="{ backgroundColor: colors.header, color: colors.headerText }">Add New Item</v-card-title>
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
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const inventoryList = ref([])
const organizationName = ref('Inventory')
const addDialog = ref(false)
const formRef = ref(null)
const itemsPerPage = ref(10)
const loading = ref(false)

const newItem = ref({
  organization: '',
  product_name: '',
  unit_price: null,
  quantity_in_stock: null
})

const colors = {
  card: '#FFF5E5',
  text: '#0C0F0A',
  header: '#D7CFFF',
  headerText: '#7C6DD4'
}


const fetchInventory = async () => {
  loading.value = true
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/inventory/')
    inventoryList.value = response.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}

const openAddDialog = () => {
  newItem.value = {
    organization: '',
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
