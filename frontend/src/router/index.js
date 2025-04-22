import { createRouter, createWebHistory } from 'vue-router'

import DashboardView from '../views/DashboardView.vue'
import InventoryView from '../views/InventoryView.vue'
import PurchaseOrderView from '../views/PurchaseOrderView.vue'
import SalesOrderView from '../views/SalesOrderView.vue'
import SupplierView from '../views/SupplierView.vue'
import SubscriptionView from '../views/SubscriptionView.vue'
import LoginView from '@/pages/LoginView.vue'
import RegisterView from '@/pages/RegisterView.vue'
import VerificationView from '@/pages/VerificationView.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/dashboard', component: DashboardView },
  { path: '/inventory', component: InventoryView },
  { path: '/purchase-order', component: PurchaseOrderView },
  { path: '/sales-order', component: SalesOrderView },
  { path: '/supplier', component: SupplierView },
  { path: '/subscription', component: SubscriptionView },
  { path: '/login', component: LoginView },
  { path: '/register', component: RegisterView },
  { path: '/verification', component: VerificationView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
