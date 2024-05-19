import { createBrowserRouter } from 'react-router-dom';
import { Chat } from './page/chat';
import { ChatSelect } from './page/chat-select';
import { Main } from './page/main';
import { Database } from './page/database/database';
export const router = createBrowserRouter([
  {
    path: '',
    element: <Main />,
    children: [
      {
        path: '',
        element: <ChatSelect />,
      },
      {
        path: '/chat/:mode/:id',
        element: <Chat />,
      },
      {
        path: '/database',
        element: <Database />,
      },
    ],
  },
]);
