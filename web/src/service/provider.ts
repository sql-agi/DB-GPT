import { createContext } from 'react';
import { Injector } from 'static-injector';
import { ChatService } from './chat.service';

export const injector = Injector.create({ providers: [ChatService] });
// export const INJECTOR_CONTEXT = createContext(injector);
// export const INJECTOR_PROVIDER = INJECTOR_CONTEXT.Provider;
