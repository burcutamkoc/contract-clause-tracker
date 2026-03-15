import { Component, Input, Output, EventEmitter } from '@angular/core'
import { CommonModule } from '@angular/common'
import { ButtonModule } from 'primeng/button'
import { FormsModule } from '@angular/forms'
import { SelectModule } from 'primeng/select';

@Component({
  selector: 'app-sentence-labeler',
  standalone: true,
  imports: [
    CommonModule,
    ButtonModule,
    FormsModule,
    SelectModule
  ],
  templateUrl: './sentence-labeler.component.html',
  styleUrls: ['./sentence-labeler.component.scss']
})
export class SentenceLabelerComponent {

  @Input() sentence: any
  @Input() clauseTypes: any[] = []

  @Output() labelSelected = new EventEmitter<any>()

  selectedClause: any

  labelSentence() {

    this.labelSelected.emit({
      sentenceId: this.sentence.id,
      clauseTypeId: this.selectedClause
    })

  }

}