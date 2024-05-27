import { Form, useLoaderData, useParams } from 'react-router-dom';
import { injector } from '../service/provider';
import { ChatService } from '../service/chat.service';
import AccountCircle from '@mui/icons-material/AccountCircle';
import ReactMarkdown from 'react-markdown';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import Input from '@mui/material/Input';
import InputAdornment from '@mui/material/InputAdornment';
import IconButton from '@mui/material/IconButton';
import SendIcon from '@mui/icons-material/Send';
import { SubmitHandler, useForm } from 'react-hook-form';
import { DatabaseService } from '../service/database.service';
import { useSignal } from '../service/signal/use-signal';
import { dbMapper } from './const';
import Avatar from '@mui/material/Avatar';
export function UserChat(item: any) {
  return (
    <>
      <div className="flex p-4 rounded-full gap-4">
        <div className="flex-1"></div>
        <span>{item.context}</span>
        <AccountCircle></AccountCircle>
      </div>
    </>
  );
}
export function SystemChat(item: any) {
  // todo 需要增加插件,直接复制,但是没接口先等着
  return (
    <>
      <div className="flex p-4 rounded-full bg-slate-50 gap-4">
        <AccountCircle></AccountCircle>
        <ReactMarkdown>{item.context}</ReactMarkdown>
      </div>
    </>
  );
}
let chatService = injector.get(ChatService);
export function Chat() {
  const data = useParams();
  console.log(data);
  // todo 根据mode/id/模型/数据库请求数据
  let list = chatService.requestHistory(data);
  let modelList = chatService.getModelList();
  // todo 切换模型和数据库后是重载还是接着?
  let databaseService = injector.get(DatabaseService);
  databaseService.requestList();
  let databaseList = useSignal(databaseService.databaseList);
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<any>();
  const onSubmit: SubmitHandler<any> = (data) => console.log('发送', data);
  return (
    <>
      <div className="flex flex-col h-full">
        <div className="flex gap-4 justify-center">
          <FormControl>
            <InputLabel>选择模型</InputLabel>

            <Select className="w-[200px]" label="选择模型">
              {modelList.map((item) => (
                <MenuItem value={item.label}>{item.label}</MenuItem>
              ))}
            </Select>
          </FormControl>
          <FormControl>
            <InputLabel>选择数据库连接</InputLabel>

            <Select
              className="w-[200px]"
              label="选择数据库连接"
              renderValue={(value: any) => {
                let item = databaseList.find((item) => item.id === value);
                return (
                  <div className="flex gap-4 items-center">
                    <div>{item.database_name}</div>
                  </div>
                );
              }}
            >
              {databaseList.map((item) => (
                <MenuItem value={item.id}>
                  <div className="flex gap-4 items-center">
                    <Avatar src={(dbMapper as any)[item.database_type].icon}></Avatar>
                    <div>{item.database_name}</div>
                  </div>
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        </div>
        <div className="flex-1">
          {list.map((item, index) => {
            return <div key={index}>{item.role === 'user' ? <UserChat {...item}></UserChat> : <SystemChat {...item}></SystemChat>}</div>;
          })}
        </div>
        <div>
          <form onSubmit={handleSubmit(onSubmit)}>
            <FormControl variant="standard" className="w-full">
              <Input
                {...register('input', { required: true })}
                endAdornment={
                  <InputAdornment position="end">
                    <IconButton type="submit">
                      <SendIcon />
                    </IconButton>
                  </InputAdornment>
                }
              />
            </FormControl>
          </form>
        </div>
      </div>
    </>
  );
}
