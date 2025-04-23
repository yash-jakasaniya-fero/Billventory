<template>
  <div>
    <v-img class="mx-auto my-6" max-width="228" src="/App_logo.ico"></v-img>

    <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
      <div class="text-subtitle-1 text-medium-emphasis">Email Address</div>
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

      <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
        Confirm Password
      </div>
      <v-text-field
        v-model="confirmPassword"
        :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'"
        :type="visible ? 'text' : 'password'"
        density="compact"
        placeholder="Confirm your password"
        prepend-inner-icon="mdi-lock-outline"
        variant="outlined"
        @click:append-inner="visible = !visible"
      ></v-text-field>

      <v-card class="mb-12" color="surface-variant" variant="tonal"></v-card>

      <h3 class="text-h5">Verification Code</h3>
      <div class="text-subtitle-2 font-weight-light mb-3">
        Please enter the verification code sent to your Email
      </div>

      <v-sheet color="surface">
      <v-otp-input
        v-model="otp"
        type="password"
        variant="solo"
        color="grey"
      ></v-otp-input>
    </v-sheet>

      <v-btn
        class="mb-8"
        color="#0C0F0A"
        size="large"
        variant="tonal"
        block
        @click="handleRegister"
      >
        Sign up
      </v-btn>

      <v-card-text class="text-center">
        <router-link to="/login" class="text-blue text-decoration-none">
          Already Have Account? Log in <v-icon icon="mdi-chevron-right"></v-icon>
        </router-link>
      </v-card-text>
    </v-card>

    <v-snackbar v-model="snackbar" :color="snackbarColor" timeout="50">
      {{ snackbarMessage }}
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const otp = ref('')
const visible = ref(false)

const snackbar = ref(false)
const snackbarMessage = ref('')
const snackbarColor = ref('success')

const router = useRouter()

const handleRegister = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/api/v1/auth/register/', {
      email: email.value,
      password: password.value,
      confirm_password: confirmPassword.value,
      otp: otp.value,
    })

    snackbarMessage.value = 'Registration successful! Redirecting to login...'
    snackbarColor.value = 'success'
    snackbar.value = true

    setTimeout(() => {
      router.push('/login')
    }, 60)
  } catch (error) {
    snackbarMessage.value = error.response?.data?.message || 'Registration failed!'
    snackbarColor.value = 'error'
    snackbar.value = true
  }
}
</script>
