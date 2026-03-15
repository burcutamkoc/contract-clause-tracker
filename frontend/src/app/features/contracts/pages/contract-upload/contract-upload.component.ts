import { Component } from '@angular/core'
import { CommonModule } from '@angular/common'
import { Router } from '@angular/router'
import { HttpClient } from '@angular/common/http'
import { ButtonModule } from 'primeng/button'
import { ContractsService } from '../../../../core/api'
import { ContractResponse } from '../../../../core/api'
import { CardModule } from 'primeng/card';

@Component({
  selector: 'app-contract-upload',
  standalone: true,
  imports: [CommonModule, ButtonModule, CardModule],
  templateUrl: './contract-upload.component.html'
})
export class ContractUploadComponent {

  selectedFile?: File
  errorMessage?: string

  constructor(
    private http: HttpClient,
    private contractsApi: ContractsService,
    private router: Router
  ) {}

  onFileSelected(event: Event) {

    const input = event.target as HTMLInputElement
    const file = input.files?.[0]

    if (!file) return

    if (!file.name.endsWith('.txt') && !file.name.endsWith('.md')) {
      this.errorMessage = 'Only .txt or .md files are supported'
      return
    }

    this.errorMessage = undefined
    this.selectedFile = file
  }

  upload() {

    if (!this.selectedFile) return

    const formData = new FormData()
    formData.append('file', this.selectedFile)

    const url = `${this.contractsApi.configuration.basePath}/contracts/upload`

    this.http.post<ContractResponse>(url, formData)
      .subscribe(contract => {
        this.router.navigate([`/contracts/${contract.id}/label`])
      })
  }
}