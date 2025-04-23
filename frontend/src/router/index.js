import { createRouter, createWebHistory } from "vue-router";

import AuthLayout from "@/layouts/AuthLayout.vue";
import DefaultLayout from "@/layouts/DefaultLayout.vue";
import HomePageLayout from "@/layouts/HomePageLayout.vue";

const routes = [
  // Landing Page
  {
    path: "/",
    component: HomePageLayout,
    children: [
      {
        path: "",
        name: "HomePage",
        component: () => import("@/views/HomePage.vue"),
        meta: { requiresAuth: false, title: "Welcome" },
      },
      {
        path: "/about",
        name: "About Us",
        component: () => import("@/views/AboutUs.vue"),
        meta: { requiresAuth: false, title: "About Us" },
      },
      {
        path: "/subscriptions",
        name: "Subscriptions",
        component: () => import("@/views/Subscription.vue"),
        meta: { requiresAuth: false, title: "Subscriptions" },
      },
      {
        path: "/thank-you",
        name: "ThankYou",
        component: () => import("@/views/ThankYou.vue"),
      },
    ],
  },
  // Auth Pages
  {
    path: "/auth",
    component: HomePageLayout,
    children: [
      {
        path: "login",
        name: "Login",
        component: () => import("@/views/Login.vue"),
        meta: { requiresAuth: false, title: "Login" },
      },
      {
        path: "register",
        name: "Register",
        component: () => import("@/views/Register.vue"),
        meta: { requiresAuth: false, title: "Register" },
      },
    ],
  },
  // Authenticated Pages
  {
    path: "/dashboard",
    component: DefaultLayout,
    children: [
      {
        path: "",
        name: "Dashboard",
        component: () => import("@/pages/DashboardView.vue"),
        meta: { requiresAuth: true, title: "Dashboard" },
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
