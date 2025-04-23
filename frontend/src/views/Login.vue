<template>
  <v-container class="d-flex align-center justify-center fill-height">
    <v-card elevation="3" class="pa-6">
      <v-card-title class="text-h5 font-weight-bold mb-2">Login</v-card-title>

      <v-card-text>
        <v-form @submit.prevent="login">
          <v-text-field
            v-model="form.email"
            label="Email"
            type="email"
            required
            prepend-inner-icon="mdi-email"
          />
          <v-text-field
            v-model="form.password"
            label="Password"
            type="password"
            required
            prepend-inner-icon="mdi-lock"
          />
          <v-btn type="submit" color="green" class="mt-4" block> Login </v-btn>

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

      <v-card-actions class="justify-center">
        <router-link
          :to="{ name: 'Register' }"
          class="text-green text-decoration-none"
        >
          Don’t have an account? Register
        </router-link>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const form = ref({
  email: "",
  password: "",
});
const error = ref("");

const login = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form.value),
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Login failed");

    error.value = "";

    // Store user data in localStorage
    localStorage.setItem("user", JSON.stringify(data.user)); // Save user data

    // Redirect to Dashboard
    router.push({ name: "Dashboard" }); // Replace with your dashboard route name
  } catch (err) {
    error.value = err.message;
  }
};
</script>