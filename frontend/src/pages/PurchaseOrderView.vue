<template>
      <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
        <v-card-title class="text-h5 d-flex justify-space-between align-center"
                      :style="{ backgroundColor: colors.header, color: colors.headerText }">
          {{ organizationName }}
          <v-btn color="teal" @click="openAddDialog">
            Create Purchase-Order
          </v-btn>
        </v-card-title>


        <!-- Purchase Orders Table -->
      <v-data-table
        :headers="tableHeaders"
        :items="purchaseorderList"
        item-value="id"
        class="elevation-1"
        :style="{ backgroundColor: colors.card, color: colors.text }"
      >
        <template #item.total_amount_paid="{ item }">
          ₹ {{ item.total_amount_paid }}
        </template>

        <template #item.purchase_items="{ item }">
          <v-btn
            style="background-color: #333; color: #00BFFF; border: 2px solid #00BFFF;"
            @click="openModal(item.purchase_items)"
          >
            View Purchase Items
          </v-btn>
        </template>
      </v-data-table>

      <!-- Purchase Items Dialog -->
      <v-dialog v-model="ListDialogVisible" max-width="800px">
        <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
          <v-card-title :style="{ backgroundColor: colors.header, color: colors.headerText }">
            Purchase Items
          </v-card-title>
          <v-card-text>
            <v-data-table
              :headers="header"
              :items="purchasemodalItems"
              dense
              class="my-4"
              hide-default-footer
            />   
          </v-card-text>
          <v-card-actions>
            <v-btn @click="ListDialogVisible = false" color="secondary">Close</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
  
        <!-- Create Purchase Order Dialog -->
        <v-dialog v-model="createpurchaseDialogVisible" max-width="900px">
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
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
const organizationName = ref('Purchase Order List')
const ListDialogVisible = ref(false)
const createpurchaseDialogVisible = ref(false)
const purchasemodalItems = ref([])
const purchaseorderList = ref([])

const colors = {
  card: '#FFF5E5',
  text: '#0C0F0A',
  header: '#D7CFFF',
  headerText: '#7C6DD4'
}
  
  const fetchPurchaseorder = async () => {
    const response = await axios.get('http://127.0.0.1:8000/api/v1/purchase-orders/')
    purchaseorderList.value = response.data
  }
  
  onMounted(() =>{
    fetchPurchaseorder()
  })

  function openModal(purchaseItems) {
    purchasemodalItems.value = purchaseItems
    ListDialogVisible.value = true
  }
  
  const newOrder = ref({
    organization: '',
    supplier: '',
    payment_method: '',
    items: [{ product_name: '', product_quantity: 1, unit_price: 0 }]
  })
  
  function openAddDialog() {
    createpurchaseDialogVisible.value = true
  }
  
  function addItem() {
    newOrder.value.items.push({ product_name: '', product_quantity: 1, unit_price: 0 })
  }
  
  function removeItem(index) {
    newOrder.value.items.splice(index, 1)
  }
  
  function cancelOrder() {
    createpurchaseDialogVisible.value = false
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
      fetchPurchaseorder()
      createpurchaseDialogVisible.value = false
      resetForm()
    } catch (error) {
      console.error('Failed to submit order:', error)
    }
  }
  </script>
  