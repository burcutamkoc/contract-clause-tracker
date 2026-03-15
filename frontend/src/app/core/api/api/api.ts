export * from './clauseTypes.service';
import { ClauseTypesService } from './clauseTypes.service';
export * from './contracts.service';
import { ContractsService } from './contracts.service';
export * from './sentences.service';
import { SentencesService } from './sentences.service';
export const APIS = [ClauseTypesService, ContractsService, SentencesService];
