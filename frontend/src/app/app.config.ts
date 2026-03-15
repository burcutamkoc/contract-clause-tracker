import { ApplicationConfig } from '@angular/core'
import { provideRouter } from '@angular/router'
import { provideHttpClient } from '@angular/common/http'

import { providePrimeNG } from 'primeng/config'
import Lara from '@primeng/themes/lara'

import { routes } from './app.routes'
import { Configuration } from './core/api/configuration'

export const appConfig: ApplicationConfig = {

  providers: [

    provideRouter(routes),
    provideHttpClient(),

    providePrimeNG({
      theme: {
        preset: Lara
      }
    }),

    {
      provide: Configuration,
      useFactory: () =>
        new Configuration({
          basePath: 'http://localhost:8000'
        })
    }

  ]

}