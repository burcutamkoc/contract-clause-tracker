import { Routes } from '@angular/router'

export const routes: Routes = [

  {
    path: '',
    loadComponent: () =>
      import('./features/contracts/pages/contract-dashboard/contract-dashboard.component')
      .then(m => m.ContractDashboardComponent)
  },

  {
    path: 'upload',
    loadComponent: () =>
      import('./features/contracts/pages/contract-upload/contract-upload.component')
      .then(m => m.ContractUploadComponent)
  },

  {
    path: 'contracts/:id/label',
    loadComponent: () =>
      import('./features/contracts/pages/contract-labeler/contract-labeler.component')
      .then(m => m.ContractLabelerComponent)
  }

]