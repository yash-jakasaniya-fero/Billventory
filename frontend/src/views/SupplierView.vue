<template>
    <v-container fluid class="pa-4" :style="{ backgroundColor: colors.background }">
      <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
        <v-card-title class="text-h5 d-flex justify-space-between align-center" :style="{ backgroundColor: colors.header, color: colors.headerText }">
          {{ organizationName }}
          <v-btn color="teal" @click="openAddDialog">
            Add Supplier
          </v-btn>
        </v-card-title>
  
        <v-card class="elevation-1 pa-4" :style="{ backgroundColor: colors.card, color: colors.text }">
          <table style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr>
                <th style="text-align: left; padding: 8px;">Supplier ID</th>
                <th style="text-align: left; padding: 8px;">Email</th>
                <th style="text-align: left; padding: 8px;">GST Number</th>
                <th style="text-align: left; padding: 8px;">Supplied Name</th>
                <th style="text-align: left; padding: 8px;">Contact Person</th>
                <th style="text-align: left; padding: 8px;">Address</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in supplierList" :key="item.id">
                <td style="padding: 8px;">{{ item.supplier_code }}</td>
                <td style="padding: 8px;">{{ item.email }}</td>
                <td style="padding: 8px;">{{ item.gst_number }}</td>
                <td style="padding: 8px;">{{ item.name }}</td>
                <td style="padding: 8px;">{{ item.contact_person }}</td>
                <td style="padding: 8px;">{{ item.address }}</td>
              </tr>
            </tbody>
          </table>
        </v-card>
  
        <v-dialog v-model="addDialog" max-width="600px">
          <v-card>
            <v-card-title class="text-h6">Add Supplier</v-card-title>
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
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import axios from 'axios'
  
  const supplierList = ref([])
  const organizationName = ref('Your Organization')
  const addDialog = ref(false)
  
  const newSupplier = ref({
    email: '',
    gst_number: '',
    name: '',
    contact_person: '',
    address: ''
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
  