<template>
    <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
        <v-card-title class="text-h5 d-flex justify-space-between align-center"
          :style="{ backgroundColor: colors.header, color: colors.headerText }">
          {{ organizationName }}
          <v-btn color="teal" @click="openAddDialog">Create Sales-Order</v-btn>
        </v-card-title>

        <!-- Sales Orders Table -->
        <v-data-table
        :headers="tableHeaders"
        :items="salesorderList"
        item-value="id"
        class="elevation-1"
        :style="{ backgroundColor: colors.card, color: colors.text }"
      >
        <template #item.final_amount="{ item }">
          ₹ {{ item.final_amount }}
        </template>

        <template #item.billing_items="{ item }">
          <v-btn
            style="background-color: #333; color: #00BFFF; border: 2px solid #00BFFF;"
            @click="openModal(item.billing_items)"
          >
            View Sales Items
          </v-btn>
        </template>
      </v-data-table>
  
        <!-- Billing Item Dialog -->
        <v-dialog v-model="ListDialogVisible" max-width="800px">
        <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
          <v-card-title :style="{ backgroundColor: colors.header, color: colors.headerText }">
            Sales Items
          </v-card-title>
          <v-card-text>
            <v-data-table
              :headers="header"
              :items="billingModalItems"
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
  
        <!-- Create Sales Order Dialog -->
        <v-dialog v-model="createbillingDialogVisible" max-width="900px">
          <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
            <v-card-title class="text-h5" :style="{ backgroundColor: colors.header, color: colors.headerText }">
              Create Sales Order
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="6">
                    <v-text-field v-model="newOrder.organization" label="Organization"></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-select v-model="newOrder.payment_method" :items="['Cash', 'Online']" label="Payment Method"></v-select>
                  </v-col>
                  <v-col cols="12" sm="6">
                    <v-text-field v-model="newOrder.gst_number" label="GST Number"></v-text-field>
                  </v-col>
                </v-row>
  
                <v-divider class="my-4"></v-divider>
  
                <div class="text-h6 mb-2">Billing Items</div>
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
  
  const organizationName = ref('Sales Order List')
  const ListDialogVisible = ref(false)
  const createbillingDialogVisible = ref(false)
  const billingModalItems = ref([])
  const salesorderList = ref([])
  
  const colors = {
  card: '#FFF5E5',
  text: '#0C0F0A',
  header: '#D7CFFF',
  headerText: '#7C6DD4'
}
  
  const fetchSalesOrders = async () => {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/sales-order/')
      salesorderList.value = response.data
    }
  
  onMounted(() => {
    fetchSalesOrders()
  })
  
  function openModal(billingItems) {
    billingModalItems.value = billingItems
    ListDialogVisible.value = true
  }
  
  const newOrder = ref({
    organization: '',
    gst_number: '',
    payment_method: '',
    items: [{ product_name: '', product_quantity: 1, unit_price: 0 }]
  })
  
  function openAddDialog() {
    createbillingDialogVisible.value = true
  }
  
  function addItem() {
    newOrder.value.items.push({ product_name: '', product_quantity: 1, unit_price: 0 })
  }
  
  function removeItem(index) {
    newOrder.value.items.splice(index, 1)
  }
  
  function cancelOrder() {
    createbillingDialogVisible.value = false
    resetForm()
  }
  
  function resetForm() {
    newOrder.value = {
      organization: '',
      gst_number: '',
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
      gst_number: newOrder.value.gst_number,
      payment_method: newOrder.value.payment_method,
      total_amount_paid,
      billing_items: newOrder.value.items.map(item => ({
        product_name: item.product_name,
        product_quantity: Number(item.product_quantity),
        unit_price: Number(item.unit_price),
        line_item_price: Number(item.product_quantity * item.unit_price)
      })),
      billing_date: new Date().toISOString()
    }
  
    try {
      await axios.post('http://127.0.0.1:8000/api/v1/sales-order/', payload)
      await fetchSalesOrders()
      createbillingDialogVisible.value = false
      resetForm()
    } catch (error) {
      console.error('Failed to submit order:', error)
    }
  }
</script>