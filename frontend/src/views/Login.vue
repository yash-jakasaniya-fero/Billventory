<template>
  <div>
    <v-img class="mx-auto my-6" max-width="228" src="/App_logo.ico"></v-img>

    <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
      <div class="text-subtitle-1 text-medium-emphasis">Account</div>

      <v-text-field
        v-model="email"
        density="compact"
        placeholder="Email address"
        prepend-inner-icon="mdi-email-outline"
        variant="outlined"
      ></v-text-field>

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Password
      </div>

      <v-text-field
        v-model="password"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Enter your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>

      <v-card class="mb-12" color="surface-variant" variant="tonal"></v-card>

      <v-btn
        class="mb-8"
        color="#0C0F0A"
        size="large"
        variant="tonal"
        block
        @click="handleLogin"
      >
        Log In
      </v-btn>

      <v-card-text class="text-center">
        <router-link to="/verification" class="text-blue text-decoration-none">
          No Account...!Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
        </router-link>
      </v-card-text>
    </v-card>

    <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="2000">
      {{ snackbarMessage }}
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const visible = ref(false)

const email = ref('')
const password = ref('')

const snackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('success')

const handleLogin = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/api/v1/auth/login/', {
      email: email.value,
      password: password.value
    })

    snackbarMessage.value = 'Login successful! Redirecting...'
    snackbarColor.value = 'success'
    snackbar.value = true

    setTimeout(() => {
      router.push('/dashboard')
    }, 1500)
  } catch (error) {
    snackbarMessage.value = error.response?.data?.message || 'Login failed!'
    snackbarColor.value = 'error'
    snackbar.value = true
  }
}
</script>