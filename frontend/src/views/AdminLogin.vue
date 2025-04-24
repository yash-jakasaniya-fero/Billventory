<template>
    <v-container class="d-block align-center justify-center fill-height mt-15" max-width="700">
      <v-card class="pa-6 border" elevation="1" v-if="!loggedIn">
        <v-card-title class="text-h5 font-weight-bold mb-2">Admin Login</v-card-title>
  
        <v-card-text>
          <v-form @submit.prevent="login">
            <v-text-field
              v-model="form.username"
              label="Username"
              type="text"
              required
              prepend-inner-icon="mdi-account"
            />
            <v-text-field
              v-model="form.password"
              label="Password"
              type="password"
              required
              prepend-inner-icon="mdi-lock"
            />
            <v-btn type="submit" color="green" class="mt-4" block>Login</v-btn>
  
            <v-alert
              v-if="error"
              type="error"
              class="mt-4"
              border="start"
              color="red-lighten-4"
            >
              {{ error }}
            </v-alert>
          </v-form>
        </v-card-text>
      </v-card>
  
      <!-- Embed Django Admin -->
      <v-card v-else>
        <v-card-title class="text-h6 font-weight-bold">Django Admin Panel</v-card-title>
        <v-card-text>
          <iframe
            src="http://127.0.0.1:8000/admin/"
            style="width: 100%; height: 80vh; border: none"
          ></iframe>
        </v-card-text>
      </v-card>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const form = ref({
    username: '',
    password: ''
  })
  const error = ref('')
  const loggedIn = ref(false)
  
  const login = async () => {
    try {
      if (form.value.username === 'admin' && form.value.password === 'admin') {
        loggedIn.value = true
        error.value = ''
      } else {
        throw new Error('Invalid credentials')
      }
    } catch (err) {
      error.value = err.message
    }
  }
  </script>
  