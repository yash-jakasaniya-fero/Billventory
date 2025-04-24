<template>
    <v-card :style="{ backgroundColor: colors.card, color: colors.text }">
        <v-card-title class="text-h5 d-flex justify-space-between align-center"
          :style="{ backgroundColor: colors.header, color: colors.headerText }">
          {{ organizationName }}
        </v-card-title>
    </v-card>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const organizationName = ref('Reports')

const colors = {
card: '#f9fafb',
text: '#0C0F0A',
header: '#16a34a',
headerText: '#ffffff'
}
</script>