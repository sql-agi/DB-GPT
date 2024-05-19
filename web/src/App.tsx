import './App.css';
import { RouterProvider } from 'react-router-dom';
import { router } from './router';
import { injector } from './service/provider';
import { ChatService } from './service/chat.service';

function App() {
  injector.get(ChatService).initList();
  return (
    <>
      <RouterProvider router={router}></RouterProvider>
    </>
  );
}

export default App;
