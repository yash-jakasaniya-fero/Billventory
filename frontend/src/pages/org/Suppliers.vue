<template>
    <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
        <v-card-title class="text-h5 d-flex justify-space-between align-center" :style="{ backgroundColor: colors.header, color: colors.headerText }">
          {{ organizationName }}
          <v-btn color="teal" @click="openAddDialog">
            Add Supplier
          </v-btn>
        </v-card-title>

        <!-- Supplier Table -->
        <v-data-table
          v-model:items-per-page="itemsPerPage"
          :headers="headers"
          :items="supplierList"
          :items-length="supplierList.length"
          :loading="loading"
          item-value="id"
          class="elevation-1"
          :style="{ backgroundColor: colors.card, color: colors.text }"
        >
        </v-data-table>

        <!-- Create Supplier Dialog -->
        <v-dialog v-model="addDialog" max-width="600px">
          <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
            <v-card-title :style="{ backgroundColor: colors.header, color: colors.headerText }">Add Supplier</v-card-title>
            <v-card-text>
              <v-form ref="formRef" @submit.prevent="saveNewSupplier">
                <v-text-field v-model="newSupplier.email" label="Email" required />
                <v-text-field v-model="newSupplier.gst_number" label="GST Number" required />
                <v-text-field v-model="newSupplier.name" label="Name" required />
                <v-text-field v-model="newSupplier.contact_person" label="Contact Person" required />
                <v-text-field v-model="newSupplier.address" label="Address" required />
              </v-form>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn text @click="addDialog = false">Cancel</v-btn>
              <v-btn color="primary" @click="saveNewSupplier">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
  
      </v-card>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const supplierList = ref([])
  const organizationName = ref('Supplier List')
  const addDialog = ref(false)
  const itemsPerPage=ref(10)
  
  const newSupplier = ref({
    email: '',
    gst_number: '',
    name: '',
    contact_person: '',
    address: ''
  })
  
  const colors = {
  card: '#FFF5E5',
  text: '#0C0F0A',
  header: '#D7CFFF',
  headerText: '#7C6DD4'
}
  
  const fetchInventory = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/v1/supplier/')
      supplierList.value = response.data
    } catch (err) {
      console.error('Error fetching supplier list:', err)
    }
  }
  
  const openAddDialog = () => {
    newSupplier.value = {
      email: '',
      gst_number: '',
      name: '',
      contact_person: '',
      address: ''
    }
    addDialog.value = true
  }
  
  const saveNewSupplier = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/api/v1/supplier/', newSupplier.value)
      addDialog.value = false
      fetchInventory()
    } catch (err) {
      console.error('Error saving new supplier:', err)
    }
  }
  
  onMounted(() => {
    fetchInventory()
  })
  </script>
  