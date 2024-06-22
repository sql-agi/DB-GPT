import { createContext } from 'react';
import { Injector } from 'static-injector';
import { ChatService } from './chat.service';
import { DatabaseService } from './database.service';
import { URL_PREFIX_TOKEN } from './token';
console.log(import.meta.env.URL_PREFIX);
console.log(import.meta.env);

export const injector = Injector.create({
  providers: [ChatService, DatabaseService, { provide: URL_PREFIX_TOKEN, useValue: import.meta.env.VITE_URL_PREFIX }],
});
// export const INJECTOR_CONTEXT = createContext(injector);
// export const INJECTOR_PROVIDER = INJECTOR_CONTEXT.Provider;
