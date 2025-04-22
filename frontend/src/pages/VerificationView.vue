<template>
    <div>
      <v-img class="mx-auto my-6" max-width="228" src="/App_logo.ico"></v-img>
  
    <v-card class="mx-auto pa-12 pb-8" elevation="8" max-width="448" rounded="lg">
        <div class="text-subtitle-1 text-medium-emphasis">Email Id</div>
  
        <v-text-field
          v-model="email"
          density="compact"
          placeholder="Email address"
          prepend-inner-icon="mdi-email-outline"
          variant="outlined"
        ></v-text-field>
  
        <v-card class="mb-12" color="surface-variant" variant="tonal"></v-card>        
  
        <v-btn
          class="mb-8"
          color="#0C0F0A"
          size="large"
          variant="tonal"
          block
          @click="sendOtp"
        >
          send otp
        </v-btn>
        <v-card-text class="text-center">
        <router-link to="/login" class="text-blue text-decoration-none">
          Already Have Account? Log in <v-icon icon="mdi-chevron-right"></v-icon>
        </router-link>
      </v-card-text>
    </v-card>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  const email = ref('')
  const router = useRouter()
  
  const sendOtp = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/v1/auth/request-otp/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: email.value })
      })
  
      if (!response.ok) {
        const errorData = await response.json()
        console.error('Error sending OTP:', errorData)
        return
      }
  
      const data = await response.json()
      console.log('OTP sent successfully:', data)
  
      router.push('/register')
    } catch (error) {
      console.error('Network error:', error)
    }
  }
  </script>
  
  