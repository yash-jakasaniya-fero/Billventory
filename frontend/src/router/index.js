import { createRouter, createWebHistory } from "vue-router";

import adminRoutes from "./admin";
import orgRoutes from "./org";
import DefaultLayout from "@/layouts/DefaultLayout.vue";

const routes = [
  // Landing Page
  {
    path: "/",
    component: DefaultLayout,
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
      {
        path: "/contact",
        name: "Contact",
        component: () => import("@/views/ContactUs.vue"),
        meta: { requiresAuth: false, title: "Contact Us" },
      },
    ],
  },
  // Auth Pages
  {
    path: "/auth",
    component: DefaultLayout,
    children: [
      {
        path: "login",
        name: "Login",
        component: () => import("@/views/Login.vue"),
        meta: { requiresAuth: false, title: "Login" },
      },
      {
        path: "admin-login",
        name: "AdminLogin",
        component: () => import("@/views/AdminLogin.vue"),
        meta: { requiresAuth: false, title: "AdminLogin" },
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
  ...adminRoutes,
  ...orgRoutes,
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
