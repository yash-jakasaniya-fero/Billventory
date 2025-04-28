<template>
  <v-container
    class="d-block align-center justify-center fill-height mt-15"
    max-width="500"
  >
    <v-card class="pa-6 border" elevation="o">
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
    const { email, password } = form.value;

    let role = null;

    if (email === "admin" && password === "admin") {
      role = "admin";
    } else if (email === "org_admin" && password === "org_admin") {
      role = "org";
    } else {
      throw new Error("Invalid credentials");
    }

    // Store user data in localStorage
    const userData = { email, role };
    localStorage.setItem("user", JSON.stringify(userData));

    // Redirect based on role
    if (role === "admin") {
      router.push({ name: "AdminOrganizations" }); // or your actual admin dashboard route
    } else if (role === "org") {
      router.push({ name: "OrgDashboard" });
    }

    error.value = "";
  } catch (err) {
    error.value = err.message;
  }
};
</script>