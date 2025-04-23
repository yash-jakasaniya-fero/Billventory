<template>

    <v-container class="pa-0">
        <div class="svg-container">
            <!-- Left Pattern -->
            <svg width="404" height="384" fill="none" viewBox="0 0 404 384" class="pattern-left">
                <defs>
                    <pattern id="pattern-left" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                        <rect x="0" y="0" width="4" height="4" :fill="primaryColor" />
                    </pattern>
                </defs>
                <rect width="404" height="384" fill="url(#pattern-left)" />
            </svg>

            <!-- Right Pattern -->
            <!-- <svg width="404" height="384" fill="none" viewBox="0 0 404 384" class="pattern-right">
                <defs>
                    <pattern id="pattern-right" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                        <rect x="0" y="0" width="4" height="4" :fill="primaryColor" />
                    </pattern>
                </defs>
                <rect width="404" height="384" fill="url(#pattern-right)" />
            </svg> -->
        </div>
    </v-container>
    <v-container class="py-16 mt-10">
        <v-row justify="center">
            <v-col cols="12" md="8" lg="6" class="text-center">
                <span class="text-uppercase text-green-600 font-weight-medium">About Us</span>
                <h1 class="text-h3 font-weight-bold mt-2 mb-6">Our Story</h1>
                <p class="text-body-1">
                    Billventory was founded with a simple mission: to make inventory and billing management
                    accessible, efficient, and stress-free for businesses of all sizes.
                </p>
            </v-col>
        </v-row>
    </v-container>

    <!-- About Content -->
    <v-container>
        <v-row justify="center">
            <v-col cols="12" md="10" lg="8">
                <v-card variant="flat" class="bg-transparent">
                    <v-card-text>
                        <p class="text-body-1 mb-4">
                            In today's fast-paced business environment, managing inventory and billing efficiently is
                            crucial for success. Yet, many businesses struggle with outdated systems, manual processes,
                            and disconnected tools that lead to errors, wasted time, and lost revenue.
                        </p>
                        <p class="text-body-1 mb-4">
                            Our founder, a small business owner, experienced these challenges firsthand. After searching
                            for a solution that was both powerful and user-friendly, they decided to build one.
                            Billventory was born from the belief that businesses deserve better tools to manage their
                            operations.
                        </p>
                        <h2 class="text-h5 font-weight-bold mt-8 mb-4">Our Mission</h2>
                        <p class="text-body-1 mb-4">
                            At Billventory, our mission is to empower businesses with intuitive, comprehensive tools
                            that simplify inventory and billing management. We believe that with the right tools,
                            businesses can focus on what they do best: serving their customers and growing their
                            operations.
                        </p>
                        <p class="text-body-1 mb-4">
                            We're committed to continuous innovation, listening to our customers' needs, and evolving
                            our platform to meet the changing demands of modern business. Our goal is to be more than
                            just a software provider—we aim to be a trusted partner in your business journey.
                        </p>
                        <h2 class="text-h5 font-weight-bold mt-8 mb-4">Our Values</h2>
                        <p class="text-body-1 mb-2">
                            <strong>Simplicity:</strong> We believe powerful software doesn't have to be complicated. We
                            focus on creating intuitive interfaces that anyone can use without extensive training.
                        </p>
                        <p class="text-body-1 mb-2">
                            <strong>Reliability:</strong> Your business depends on accurate inventory and billing. Our
                            platform is built with reliability at its core, ensuring your data is always accurate and
                            accessible.
                        </p>
                        <p class="text-body-1 mb-2">
                            <strong>Customer-Centric:</strong> Everything we do starts with our customers. We actively
                            seek feedback and continuously improve our platform based on real-world needs.
                        </p>
                        <p class="text-body-1 mb-2">
                            <strong>Innovation:</strong> The business landscape is constantly evolving, and so are we.
                            We're committed to staying ahead of trends and incorporating new technologies that benefit
                            our users.
                        </p>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
    <v-container class="pa-0">
        <div class="svg-container">
            <!-- Left Pattern -->
            <!--<svg width="404" height="384" fill="none" viewBox="0 0 404 384" class="pattern-left">
                 <defs>
                    <pattern id="pattern-left" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                        <rect x="0" y="0" width="4" height="4" :fill="primaryColor" />
                    </pattern>
                </defs>
                <rect width="404" height="384" fill="url(#pattern-left)" />
            </svg> -->

            <!-- Right Pattern -->
            <svg width="404" height="384" fill="none" viewBox="0 0 404 384" class="pattern-right">
                <defs>
                    <pattern id="pattern-right" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
                        <rect x="0" y="0" width="4" height="4" :fill="primaryColor" />
                    </pattern>
                </defs>
                <rect width="404" height="384" fill="url(#pattern-right)" />
            </svg>
        </div>
    </v-container>

    <!-- Team Section -->
    <v-container fluid class="py-12 bg-primary-lighten-5">
        <v-row justify="center">
            <v-col cols="12" md="10" lg="8" class="text-center">
                <span class="text-uppercase text-primary font-weight-medium">Our Team</span>
                <h2 class="text-h4 font-weight-bold mt-2 mb-3">
                    The people behind Billventory
                </h2>
                <p class="text-body-1 mb-8">
                    Our diverse team of experts is passionate about creating the best inventory and billing solution for
                    your business.
                </p>
            </v-col>
        </v-row>

        <v-row justify="center">
            <v-col cols="12" sm="6" md="4">
                <v-card class="mx-auto" max-width="300">
                    <v-img
                        src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
                        height="300" cover></v-img>
                    <v-card-item>
                        <v-card-title>Emma Thompson</v-card-title>
                        <v-card-subtitle class="text-primary">CEO & Founder</v-card-subtitle>
                    </v-card-item>
                    <v-card-text>
                        With over 15 years of experience in business management, Emma founded Billventory to solve
                        real-world inventory challenges.
                    </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="12" sm="6" md="4">
                <v-card class="mx-auto" max-width="300">
                    <v-img
                        src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
                        height="300" cover></v-img>
                    <v-card-item>
                        <v-card-title>Michael Chen</v-card-title>
                        <v-card-subtitle class="text-primary">CTO</v-card-subtitle>
                    </v-card-item>
                    <v-card-text>
                        Michael leads our technical team, bringing his expertise in software architecture and cloud
                        infrastructure to build a robust platform.
                    </v-card-text>
                </v-card>
            </v-col>

            <v-col cols="12" sm="6" md="4">
                <v-card class="mx-auto" max-width="300">
                    <v-img
                        src="https://images.unsplash.com/photo-1517841905240-472988babdf9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60"
                        height="300" cover></v-img>
                    <v-card-item>
                        <v-card-title>Sophia Rodriguez</v-card-title>
                        <v-card-subtitle class="text-primary">Head of Product</v-card-subtitle>
                    </v-card-item>
                    <v-card-text>
                        Sophia ensures our product meets real user needs, with a focus on creating intuitive and
                        powerful features.
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>

    <!-- Why Choose Us Section -->
    <v-container class="py-12">
        <v-row justify="center">
            <v-col cols="12" md="10" lg="8" class="text-center">
                <span class="text-uppercase text-green-600 font-weight-medium">Why Choose Us</span>
                <h2 class="text-h4 font-weight-bold mt-2 mb-3">
                    The Billventory Difference
                </h2>
                <p class="text-body-1 mb-8">
                    What sets us apart from other inventory and billing solutions
                </p>
            </v-col>
        </v-row>

        <v-row>
            <v-col cols="12" md="6">
                <v-list>
                    <v-list-item>
                        <template v-slot:prepend>
                            <v-avatar color="primary" rounded>
                                <v-icon icon="mdi-flash" color="text-green-600"></v-icon>
                            </v-avatar>
                        </template>
                        <v-list-item-title class="text-h6">Lightning Fast Performance</v-list-item-title>
                        <v-list-item-subtitle>
                            Our platform is built for speed, allowing you to manage thousands of inventory items without
                            slowdowns.
                        </v-list-item-subtitle>
                    </v-list-item>
                </v-list>
            </v-col>

            <v-col cols="12" md="6">
                <v-list>
                    <v-list-item>
                        <template v-slot:prepend>
                            <v-avatar color="primary" rounded>
                                <v-icon icon="mdi-shield" color="text-green-600"></v-icon>
                            </v-avatar>
                        </template>
                        <v-list-item-title class="text-h6">Enterprise-Grade Security</v-list-item-title>
                        <v-list-item-subtitle>
                            Your data is protected with industry-leading security measures, including encryption and
                            regular
                            backups.
                        </v-list-item-subtitle>
                    </v-list-item>
                </v-list>
            </v-col>

            <v-col cols="12" md="6">
                <v-list>
                    <v-list-item>
                        <template v-slot:prepend>
                            <v-avatar color="primary" rounded>
                                <v-icon icon="mdi-cellphone" color="white"></v-icon>
                            </v-avatar>
                        </template>
                        <v-list-item-title class="text-h6">Mobile-Friendly Design</v-list-item-title>
                        <v-list-item-subtitle>
                            Access your inventory and billing information from anywhere, on any device, with our
                            responsive design.
                        </v-list-item-subtitle>
                    </v-list-item>
                </v-list>
            </v-col>

            <v-col cols="12" md="6">
                <v-list>
                    <v-list-item>
                        <template v-slot:prepend>
                            <v-avatar color="primary" rounded>
                                <v-icon icon="mdi-headphones" color="white"></v-icon>
                            </v-avatar>
                        </template>
                        <v-list-item-title class="text-h6">Dedicated Support</v-list-item-title>
                        <v-list-item-subtitle>
                            Our customer support team is always ready to help you get the most out of Billventory.
                        </v-list-item-subtitle>
                    </v-list-item>
                </v-list>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
const primaryColor = '#16a34a' // Replace with your Vuetify primary color
</script>


<style scoped>
.svg-container {
    position: relative;
}

.pattern-left {
    position: absolute;
    top: 3rem;
    /* similar to top-12 */
    left: 100%;
    transform: translateX(8rem);
    /* similar to translate-x-32 */
    z-index: 0;
}

.pattern-right {
    position: absolute;
    top: 50%;
    right: 100%;
    transform: translate(-8rem, -50%);
    z-index: 0;
}
</style>