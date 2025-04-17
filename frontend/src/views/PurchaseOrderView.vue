<template>
    <v-container fluid class="pa-4" :style="{ backgroundColor: colors.background }">
      <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
        <v-card-title class="text-h5 d-flex justify-space-between align-center"
                      :style="{ backgroundColor: colors.header, color: colors.headerText }">
          {{ organizationName }}
          <v-btn color="teal" @click="openAddDialog">
            Create Purchase-Order
          </v-btn>
        </v-card-title>
  
        <v-card class="elevation-1 pa-4" :style="{ backgroundColor: colors.card, color: colors.text }">
          <table style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr>
                <th style="text-align: left; padding: 8px;">Order ID</th>
                <th style="text-align: left; padding: 8px;">Supplier</th>
                <th style="text-align: left; padding: 8px;">Date&Time</th>
                <th style="text-align: left; padding: 8px;">Payment Method</th>
                <th style="text-align: left; padding: 8px;">Total Amount</th>
                <th style="text-align: left; padding: 8px;">Items</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in purchaseorderList" :key="item.id">
                <td style="padding: 8px;">{{ item.id }}</td>
                <td style="padding: 8px;">{{ item.supplier }}</td>
                <td style="padding: 8px;">{{ item.purchase_date }}</td>
                <td style="padding: 8px;">{{ item.payment_method }}</td>
                <td style="padding: 8px;">₹ {{ item.total_amount_paid }}</td>
                <td style="padding: 8px;">
                  <v-btn style="background-color: #333; color: #00BFFF; border: 2px solid #00BFFF;"
                         @click="openModal(item.purchase_items)">
                    View Purchase Items
                  </v-btn>
                </td>
              </tr>
            </tbody>
          </table>
        </v-card>
  
        <!-- Purchase Items Dialog -->
        <v-dialog v-model="dialogVisible" max-width="800px">
          <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
            <v-card-title class="text-h5" :style="{ backgroundColor: colors.header, color: colors.headerText }">
              Purchase Items
            </v-card-title>
            <v-card-text>
              <v-simple-table dense class="my-4">
                <thead class="bg-[#800020] text-[#E8E8E8]">
                  <tr>
                    <th class="px-4 py-2">Product</th>
                    <th class="px-4 py-2">Quantity</th>
                    <th class="px-4 py-2">Unit Price</th>
                    <th class="px-4 py-2">Line Item Price</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(prod, index) in modalItems" :key="index" class="hover:bg-[#E8E8E8]">
                    <td class="border px-4 py-2">{{ prod.product_name }}</td>
                    <td class="border px-4 py-2">{{ prod.product_quantity }}</td>
                    <td class="border px-4 py-2">{{ prod.unit_price }}</td>
                    <td class="border px-4 py-2">{{ prod.line_item_price }}</td>
                  </tr>
                </tbody>
              </v-simple-table>
            </v-card-text>
            <v-card-actions>
              <v-btn @click="dialogVisible = false" color="secondary">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
  
        <!-- Create Purchase Order Dialog -->
        <v-dialog v-model="createDialogVisible" max-width="900px">
          <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
            <v-card-title class="text-h5" :style="{ backgroundColor: colors.header, color: colors.headerText }">
              Create Purchase Order
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                    <v-col cols="12" sm="6">
                    <v-text-field v-model="newOrder.organization" label="Organization"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field v-model="newOrder.supplier" label="Supplier"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select v-model="newOrder.payment_method"
                              :items="['Cash', 'Online']"
                              label="Payment Method"></v-select>
                  </v-col>
                </v-row>
  
                <v-divider class="my-4"></v-divider>
  
                <div class="text-h6 mb-2">Purchase Items</div>
                <v-row v-for="(item, index) in newOrder.items" :key="index">
                  <v-col cols="12" sm="4">
                    <v-text-field v-model="item.product_name" label="Product Name"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="2">
                    <v-text-field v-model="item.product_quantity" label="Quantity" type="number"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="2">
                    <v-text-field v-model="item.unit_price" label="Unit Price" type="number"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="2" class="d-flex align-center">
                    <v-btn icon @click="removeItem(index)">
                      <v-icon>mdi-delete</v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
  
                <v-btn color="primary" class="mt-2" @click="addItem">Add Item</v-btn>
              </v-container>
            </v-card-text>
  
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="secondary" @click="cancelOrder">Cancel</v-btn>
              <v-btn color="success" @click="submitOrder">Submit Order</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
  
      </v-card>
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const organizationName = ref('Purchase Order List')
  const dialogVisible = ref(false)
  const createDialogVisible = ref(false)
  const modalItems = ref([])
  const purchaseorderList = ref([])
  
  const colors = {
    background: '#0C0F0A',
    card: '#E8E8E8',
    text: '#0C0F0A',
    header: '#800020',
    headerText: '#E8E8E8'
  }
  
  const fetchInventory = async () => {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/purchase-orders/')
    purchaseorderList.value = response.data
  }
  
  onMounted(() => {
    fetchInventory()
  })
  
  function openModal(purchaseItems) {
    modalItems.value = purchaseItems
    dialogVisible.value = true
  }
  
  const newOrder = ref({
    organization: '',
    supplier: '',
    payment_method: '',
    items: [{ product_name: '', product_quantity: 1, unit_price: 0 }]
  })
  
  function openAddDialog() {
    createDialogVisible.value = true
  }
  
  function addItem() {
    newOrder.value.items.push({ product_name: '', product_quantity: 1, unit_price: 0 })
  }
  
  function removeItem(index) {
    newOrder.value.items.splice(index, 1)
  }
  
  function cancelOrder() {
    createDialogVisible.value = false
    resetForm()
  }
  
  function resetForm() {
    newOrder.value = {
        organization: '',
      supplier: '',
      payment_method: '',
      items: [{ product_name: '', product_quantity: 1, unit_price: 0 }]
    }
  }
  
  async function submitOrder() {
    const total_amount_paid = newOrder.value.items.reduce((sum, item) => {
      return sum + (Number(item.product_quantity) * Number(item.unit_price))
    }, 0)
  
    const payload = {
        organization: newOrder.value.organization,
      supplier: newOrder.value.supplier,
      payment_method: newOrder.value.payment_method,
      total_amount_paid,
      purchase_items: newOrder.value.items.map(item => ({
        product_name: item.product_name,
        product_quantity: Number(item.product_quantity),
        unit_price: Number(item.unit_price),
        line_item_price: Number(item.product_quantity * item.unit_price)
      })),
      purchase_date: new Date().toISOString()
    }
  
    try {
      await axios.post('http://127.0.0.1:8000/api/v1/purchase-orders/', payload)
      fetchInventory()
      createDialogVisible.value = false
      resetForm()
    } catch (error) {
      console.error('Failed to submit order:', error)
    }
  }
  </script>
  