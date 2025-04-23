export default [
  {
    path: "/org",
    component: () => import("@/layouts/OrgLayout.vue"),
    children: [
      {
        path: "dashboard",
        name: "OrgDashboard",
        component: () => import("@/pages/org/Dashboard.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
      {
        path: "products",
        name: "OrgProducts",
        component: () => import("@/pages/org/Products.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
      {
        path: "suppliers",
        name: "OrgSuppliers",
        component: () => import("@/pages/org/Suppliers.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
      {
        path: "purchase-orders",
        name: "OrgPurchaseOrders",
        component: () => import("@/pages/org/PurchaseOrders.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
      {
        path: "billings",
        name: "OrgBillings",
        component: () => import("@/pages/org/Billings.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
      {
        path: "reports",
        name: "OrgReports",
        component: () => import("@/pages/org/Reports.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
      {
        path: "support",
        name: "OrgSupport",
        component: () => import("@/pages/org/Support.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
      {
        path: "settings",
        name: "OrgSettings",
        component: () => import("@/pages/org/Settings.vue"),
        meta: { requiresAuth: true, role: "org" },
      },
    ],
  },
];
