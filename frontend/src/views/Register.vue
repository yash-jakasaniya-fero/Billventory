<template>
  <v-container class="py-10" max-width="600px">
    <v-row justify="center">
      <v-col cols="12">
        <v-stepper alt-labels v-model="step" class="custom-stepper">
          <v-stepper-header>
            <v-stepper-item :complete="step > 1" :value="1" color="success">
              Email Details
            </v-stepper-item>
            <v-divider></v-divider>
            <v-stepper-item :complete="step > 2" :value="2" color="success">
              Verification
            </v-stepper-item>
            <v-divider></v-divider>
            <v-stepper-item :value="3"> Organization Details </v-stepper-item>
          </v-stepper-header>

          <v-stepper-window>
            <!-- Step 1 -->
            <v-stepper-window-item :value="1">
              <v-card flat class="pa-6">
                <v-card-title class="text-h6">Step 1: Enter Email</v-card-title>
                <v-text-field
                  v-model="email"
                  label="Email"
                  type="email"
                  required
                />
                <v-btn color="success" @click="sendOtp">Send OTP</v-btn>

                <v-alert v-if="error" type="error" class="mt-3">
                  {{ error }}
                </v-alert>

                <v-snackbar v-model="snackbar" :timeout="5000" color="success">
                  {{ snackbarMessage }}
                </v-snackbar>
              </v-card>
            </v-stepper-window-item>

            <!-- Step 2 -->
            <v-stepper-window-item :value="2">
              <v-card flat class="pa-6">
                <v-card-title class="text-h6">Step 2: Verify OTP</v-card-title>

                <div class="d-flex justify-space-between mt-4 mb-4">
                  <v-text-field
                    v-model="otp"
                    label="Enter OTP"
                    maxlength="6"
                    hide-details
                    class="otp-input"
                  ></v-text-field>
                </div>

                <v-btn color="success" @click="verifyOtp">Verify</v-btn>

                <v-alert v-if="error" type="error" class="mt-3">
                  {{ error }}
                </v-alert>

                <v-dialog v-model="otpSuccess" max-width="300">
                  <v-card>
                    <v-card-text class="text-center">
                      ✅ OTP Verified Successfully!
                    </v-card-text>
                  </v-card>
                </v-dialog>
              </v-card>
            </v-stepper-window-item>

            <!-- Step 3 -->
            <v-stepper-window-item :value="3">
              <v-card flat class="pa-6">
                <v-card-title class="text-h6"
                  >Step 3: Organization Details</v-card-title
                >
                <v-text-field
                  v-model="form.user_first_name"
                  label="First Name"
                />
                <v-text-field v-model="form.user_last_name" label="Last Name" />
                <v-text-field
                  v-model="form.org_name"
                  label="Organization Name"
                />
                <v-text-field
                  v-model="form.org_address"
                  label="Organization Address"
                />
                <v-text-field v-model="form.gst_number" label="GST Number" />
                <v-text-field
                  v-model="form.organization"
                  label="Organization ID"
                />

                <v-btn color="success" class="mt-4" @click="submitForm">
                  Submit
                </v-btn>

                <v-alert v-if="error" type="error" class="mt-3">
                  {{ error }}
                </v-alert>
              </v-card>
            </v-stepper-window-item>
          </v-stepper-window>
        </v-stepper>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref, reactive } from "vue";

import { useRouter } from "vue-router";

const router = useRouter();

const step = ref(1);
const email = ref("");
const otp = ref("");
const error = ref("");
const snackbar = ref(false);
const snackbarMessage = ref("");
const otpSuccess = ref(false);

const form = reactive({
  user_first_name: "",
  user_last_name: "",
  org_name: "",
  org_address: "",
  gst_number: "",
  organization: "",
});

const sendOtp = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/request-otp/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email.value }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to send OTP");

    error.value = "";
    snackbarMessage.value = "OTP sent successfully!";
    snackbar.value = true;

    setTimeout(() => {
      step.value = 2;
    }, 1000);
  } catch (err) {
    error.value = err.message;
  }
};

const verifyOtp = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/verify-otp/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email.value, otp: otp.value }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Invalid OTP");

    error.value = "";
    otpSuccess.value = true;

    setTimeout(() => {
      otpSuccess.value = false;
      step.value = 3;
    }, 1500);
  } catch (err) {
    error.value = err.message;
  }
};

const submitForm = async () => {
  try {
    const res = await fetch("http://127.0.0.1:8000/api/v1/onboarding/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email.value, ...form }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Submission failed");

    error.value = "";
    // Redirect to thank-you page
    router.push("/thank-you");

    // Wait for 10 seconds, then go to login
    setTimeout(() => {
      router.push("/login");
    }, 10000);
  } catch (err) {
    error.value = err.message;
  }
};
</script>

<style scoped>
.otp-input input {
  text-align: center;
  letter-spacing: 8px;
  font-size: 1.5rem;
}
</style>