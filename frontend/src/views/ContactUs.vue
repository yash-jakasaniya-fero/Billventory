<template>
  <v-container class="py-10">
    <v-card class="pa-6" elevation="2">
      <h2 class="text-h5 font-weight-bold mb-4">Contact Us</h2>
      <v-form ref="formRef" @submit.prevent="submitContactForm">
        <v-text-field
          v-model="contactForm.name"
          label="Your Name"
          required
        ></v-text-field>
        <v-text-field
          v-model="contactForm.email"
          label="Email"
          type="email"
          required
        ></v-text-field>
        <v-textarea
          v-model="contactForm.message"
          label="Your Message"
          required
          rows="5"
        ></v-textarea>
        <v-btn type="submit" color="green" class="mt-4" :loading="loading">
          Submit
        </v-btn>
        <v-alert
          v-if="responseMessage"
          :type="responseType"
          class="mt-4"
          dense
          border="start"
        >
          {{ responseMessage }}
        </v-alert>
      </v-form>
    </v-card>
  </v-container>
</template>
  
  <script setup>
import { ref, reactive } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const formRef = ref(null);
const loading = ref(false);
const responseMessage = ref("");
const responseType = ref("success");

const contactForm = reactive({
  name: "",
  email: "",
  message: "",
});

const submitContactForm = async () => {
  loading.value = true;
  responseMessage.value = "";

  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/contact/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(contactForm),
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to send message");

    // Reset form and redirect
    formRef.value.reset();
    await router.push({ name: "ThankYou" });

    setTimeout(() => {
      router.push({ name: "Home" });
    }, 10000);
  } catch (err) {
    responseMessage.value = err.message;
    responseType.value = "error";
  } finally {
    loading.value = false;
  }
};
</script>