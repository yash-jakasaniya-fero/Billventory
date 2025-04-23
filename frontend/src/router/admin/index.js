export default [
  {
    path: "/admin",
    component: () => import("@/layouts/AdminLayout.vue"),
    children: [
      {
        path: "organizations",
        name: "AdminOrganizations",
        component: () => import("@/pages/admin/Organizations.vue"),
        meta: { requiresAuth: true, role: "admin" },
      },
      {
        path: "onboarding",
        name: "AdminOnboarding",
        component: () => import("@/pages/admin/Onboarding.vue"),
        meta: { requiresAuth: true, role: "admin" },
      },
      {
        path: "support",
        name: "AdminSupport",
        component: () => import("@/pages/admin/Support.vue"),
        meta: { requiresAuth: true, role: "admin" },
      },
      {
        path: "settings",
        name: "AdminSettings",
        component: () => import("@/pages/admin/Settings.vue"),
        meta: { requiresAuth: true, role: "admin" },
      },
    ],
  },
];
