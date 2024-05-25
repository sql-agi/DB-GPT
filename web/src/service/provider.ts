import { createContext } from 'react';
import { Injector } from 'static-injector';
import { ChatService } from './chat.service';
import { DatabaseService } from './database.service';
import { URL_PREFIX_TOKEN } from './token';

export const injector = Injector.create({
  providers: [ChatService, DatabaseService, { provide: URL_PREFIX_TOKEN, useValue: 'http://localhost:8000' }],
});
// export const INJECTOR_CONTEXT = createContext(injector);
// export const INJECTOR_PROVIDER = INJECTOR_CONTEXT.Provider;
