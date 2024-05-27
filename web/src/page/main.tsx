import { Outlet } from 'react-router-dom';
import { Sidebar } from './sidebar';

export function Main() {
  return (
    <>
      <div className="flex h-[100vh]">
        <Sidebar></Sidebar>
        <div className="p-4 flex-1 bg-gray-100 overflow-auto">
          <Outlet />
        </div>
      </div>
    </>
  );
}
