import Button from '@mui/material/Button';
import AddIcon from '@mui/icons-material/Add';
import MessageIcon from '@mui/icons-material/Message';
import List from '@mui/material/List';
import { ListItemButton, ListItemIcon, ListItemText } from '@mui/material';
import { injector } from '../service/provider';
import { ChatService } from '../service/chat.service';
import { Link } from 'react-router-dom';
export function Sidebar() {
  let list = injector.get(ChatService).getList();
  return (
    <>
      <div className="flex flex-col gap-4 m-4 w-[240px]">
        <Link to={'/'} >
          <Button variant="contained" startIcon={<AddIcon />} className='w-full'>
            创建会话
          </Button>
        </Link>
        <div className="flex-1">
          <List>
            {list.map((item, index) => {
              return (
                <Link to={`/chat/${item.type}/${item.id}`} key={index}>
                  <ListItemButton>
                    <ListItemIcon>
                      <MessageIcon></MessageIcon>
                    </ListItemIcon>
                    <ListItemText primary={item.title} />
                  </ListItemButton>
                </Link>
              );
            })}
          </List>
        </div>
        <div>
          <List>
            <ListItemButton>
              <ListItemText primary="模型管理" />
            </ListItemButton>
            <Link to={'/database'}>
              <ListItemButton>
                <ListItemText primary="数据库" />
              </ListItemButton>
            </Link>
            <ListItemButton>
              <ListItemText primary="知识库" />
            </ListItemButton>
            <ListItemButton>
              <ListItemText primary="插件列表" />
            </ListItemButton>
            <ListItemButton>
              <ListItemText primary="提示语" />
            </ListItemButton>
          </List>
        </div>
        <div></div>
      </div>
    </>
  );
}
