import Button from '@mui/material/Button';
import AddIcon from '@mui/icons-material/Add';
import MessageIcon from '@mui/icons-material/Message';
import List from '@mui/material/List';
import { Divider, IconButton, ListItemButton, ListItemIcon, ListItemText } from '@mui/material';
import { injector } from '../service/provider';
import { ChatService } from '../service/chat.service';
import { Link } from 'react-router-dom';
import StorageIcon from '@mui/icons-material/Storage';
import SchoolIcon from '@mui/icons-material/School';
import ExtensionIcon from '@mui/icons-material/Extension';
import { BsBoxes } from 'react-icons/bs';
import { TbPrompt } from 'react-icons/tb';
import DeleteIcon from '@mui/icons-material/Delete';
import { useSignal } from '../service/signal/use-signal';
export function Sidebar() {
  let chatService = injector.get(ChatService);
  let list = useSignal(chatService.sessionList)
  return (
    <>
      <div className="flex flex-col gap-4 m-4 w-[240px]">
        <div>
          <img src="./logo.png" alt="" />
        </div>
        <Link to={'/'}>
          <Button variant="contained" startIcon={<AddIcon />} className="w-full">
            创建会话
          </Button>
        </Link>
        <div className="flex-1">
          <List>
            {list.map((item, index) => {
              // todo 导航目前写死db
              return (
                <Link to={`/chat/db/${item.id}`} key={index}>
                  <ListItemButton className="chat-title-item flex items-center">
                    <ListItemIcon className="!min-w-[24px] mr-4">
                      <MessageIcon></MessageIcon>
                    </ListItemIcon>
                    <ListItemText primary={item.title} className="list-item-text-overflow" />
                    <div className=" hidden  chat-title-item-action overflow-hidden">
                      <IconButton
                        size="small"
                        color="error"
                        onClick={() => {
                          chatService.deleteItem(item.id);
                        }}
                        className="!p-0"
                      >
                        <DeleteIcon></DeleteIcon>
                      </IconButton>
                    </div>
                  </ListItemButton>
                </Link>
              );
            })}
          </List>
        </div>
        <Divider></Divider>

        <div>
          <List>
            <ListItemButton>
              <ListItemIcon>
                <BsBoxes className="text-[24px] " />
              </ListItemIcon>
              <ListItemText primary="模型管理" />
            </ListItemButton>
            <Link to={'/database'}>
              <ListItemButton>
                <ListItemIcon>
                  <StorageIcon />
                </ListItemIcon>
                <ListItemText primary="数据库" />
              </ListItemButton>
            </Link>
            <ListItemButton>
              <ListItemIcon>
                <SchoolIcon />
              </ListItemIcon>
              <ListItemText primary="知识库" />
            </ListItemButton>
            <ListItemButton>
              <ListItemIcon>
                <ExtensionIcon />
              </ListItemIcon>
              <ListItemText primary="插件列表" />
            </ListItemButton>
            <ListItemButton>
              <ListItemIcon>
                <TbPrompt className="text-[24px]" />
              </ListItemIcon>
              <ListItemText primary="提示语" />
            </ListItemButton>
          </List>
        </div>
        <div></div>
      </div>
    </>
  );
}
