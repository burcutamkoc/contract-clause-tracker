import { Component, OnInit } from '@angular/core'
import { CommonModule } from '@angular/common'
import { ActivatedRoute, RouterModule } from '@angular/router'
import { Observable } from 'rxjs'
import { Router } from '@angular/router'
import { ButtonModule } from 'primeng/button'

import { SentencesService } from '../../../../core/api/api/sentences.service'
import { ClauseTypesService } from '../../../../core/api/api/clauseTypes.service'

import { SentenceWithLabel } from '../../../../core/api/model/sentenceWithLabel'
import { ClauseTypeResponse } from '../../../../core/api/model/clauseTypeResponse'

import { SentenceLabelerComponent } from '../../components/sentence-labeler/sentence-labeler.component'
import { SentenceLabelRequest } from '../../../../core/api/model/sentenceLabelRequest'

@Component({
  selector: 'app-contract-labeler',
  standalone: true,
  imports: [CommonModule, RouterModule, SentenceLabelerComponent, ButtonModule],
  templateUrl: './contract-labeler.component.html'
})
export class ContractLabelerComponent implements OnInit {

  contractId!: number

  sentences$!: Observable<SentenceWithLabel[]>
  clauseTypes$!: Observable<ClauseTypeResponse[]>

  constructor(
    private route: ActivatedRoute,
    private sentencesApi: SentencesService,
    private clauseTypesApi: ClauseTypesService,
  ) {}

  ngOnInit() {

    this.contractId = Number(this.route.snapshot.paramMap.get('id'))

    this.sentences$ =
      this.sentencesApi
        .listSentencesContractsContractIdSentencesGet(this.contractId)

    this.clauseTypes$ =
      this.clauseTypesApi
        .listClauseTypesClauseTypesGet()

  }

  onLabel(event: any) {

    const payload: SentenceLabelRequest = {
      clause_type_id: event.clauseTypeId
    }

    this.sentencesApi
      .labelSentenceSentencesSentenceIdLabelPost(
        event.sentenceId,
        payload
      )
      .subscribe()

  }

}