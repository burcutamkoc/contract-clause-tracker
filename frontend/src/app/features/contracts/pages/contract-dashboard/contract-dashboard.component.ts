import { Component } from '@angular/core'
import { CommonModule } from '@angular/common'
import { RouterModule } from '@angular/router'
import { SelectModule } from 'primeng/select';
import { InputTextModule } from 'primeng/inputtext'
import { Observable } from 'rxjs'
import { ButtonModule } from 'primeng/button';
import { ToolbarModule } from 'primeng/toolbar';
import { CardModule } from 'primeng/card';

import { ContractsService } from '../../../../core/api/api/contracts.service'
import { ContractDashboard } from '../../../../core/api/model/contractDashboard'

import { ContractTableComponent } from '../../components/contract-table/contract-table.component'

@Component({
  selector: 'app-contract-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    RouterModule,
    SelectModule,
    ButtonModule,
    ToolbarModule,
    CardModule,
    ContractTableComponent
  ],
  templateUrl: './contract-dashboard.component.html'
})
export class ContractDashboardComponent {

  contracts$!: Observable<ContractDashboard[]>

  search = ''
  status = ''

  statusOptions = [
    { label: 'All', value: '' },
    { label: 'Completed', value: 'completed' },
    { label: 'In Progress', value: 'in_progress' },
    { label: 'Not Started', value: 'not_started' }
  ]

  constructor(private contractsApi: ContractsService) {
    this.loadContracts()
  }

  loadContracts() {
    this.contracts$ = this.contractsApi.listContractsContractsGet(
      this.status || undefined,
      this.search || undefined
    )
  }

  onSearch(value: string) {
    this.search = value
    this.loadContracts()
  }

  onStatusChange(value: string) {
    this.status = value
    this.loadContracts()
  }

  deleteContract(id: number) {

    if (!confirm('Delete this contract?')) return

    this.contractsApi.deleteContractContractsContractIdDelete(id)
      .subscribe(() => this.loadContracts())
  }
}