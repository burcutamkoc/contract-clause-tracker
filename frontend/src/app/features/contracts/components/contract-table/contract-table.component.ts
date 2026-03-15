import { Component, Input, Output, EventEmitter } from '@angular/core'
import { CommonModule } from '@angular/common'
import { TableModule } from 'primeng/table'
import { ButtonModule } from 'primeng/button'
import { RouterModule } from '@angular/router'
import { ProgressBarModule } from 'primeng/progressbar'

import { ContractDashboard } from '../../../../core/api/model/contractDashboard'

@Component({
  selector: 'app-contract-table',
  standalone: true,
  imports: [
    CommonModule,
    TableModule,
    ButtonModule,
    RouterModule,
    ProgressBarModule
  ],
  templateUrl: './contract-table.component.html',
  styleUrls: ['./contract-table.component.scss']
})
export class ContractTableComponent {

  Math = Math

  @Input() contracts: ContractDashboard[] = []

  @Output() delete = new EventEmitter<number>()

  deleteContract(id: number) {
    this.delete.emit(id)
  }

}