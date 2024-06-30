import { useNavigate, useParams } from 'react-router-dom';
import { injector } from '../service/provider';
import { ChatService } from '../service/chat.service';
import AccountCircle from '@mui/icons-material/AccountCircle';
import ReactMarkdown from 'react-markdown';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import InputAdornment from '@mui/material/InputAdornment';
import IconButton from '@mui/material/IconButton';
import SendIcon from '@mui/icons-material/Send';
import { SubmitHandler, useForm } from 'react-hook-form';
import { DatabaseService } from '../service/database.service';
import { useSignal } from '../service/signal/use-signal';
import { DATABASE_OBJECT } from './const';
import Avatar from '@mui/material/Avatar';
import { useCallback, useEffect, useMemo, useState } from 'react';
import PrecisionManufacturingIcon from '@mui/icons-material/PrecisionManufacturing';
import remarkGfm from 'remark-gfm';
import { OutlinedInput, Paper } from '@mui/material';

export function UserChat(item: any) {
  return (
    <>
      <div className="flex p-4 rounded-[8px] gap-4">
        <div className="flex-1"></div>
        <span>{item.message_content}</span>
        <AccountCircle></AccountCircle>
      </div>
    </>
  );
}
export function SystemChat(item: any) {
  // todo 需要增加插件,直接复制,但是没接口先等着
  return (
    <>
      <div className="flex p-4 rounded-[8px] bg-slate-50 gap-4">
        <PrecisionManufacturingIcon></PrecisionManufacturingIcon>
        <div className="flex-1">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>{item.message_content}</ReactMarkdown>
        </div>
      </div>
    </>
  );
}
let chatService = injector.get(ChatService);
export function Chat() {
  const params = useParams();

  let historyList = useSignal(chatService.sessionHistory);
  useEffect(() => {
    if (params.id !== 'new') {
      chatService.getHistory(+params.id!);
    } else {
      chatService.sessionHistory.set([]);
    }
  }, [params.id]);
  let modelList = chatService.getModelList();
  let databaseService = injector.get(DatabaseService);
  databaseService.requestList();
  let databaseList = useSignal(databaseService.databaseList);
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
    reset,
  } = useForm<any>();
  let [modelValue, setModelChange] = useState(modelList[0]?.value || '');
  let [databaseValue, setDatabaseValue] = useState(databaseList[0]?.id || '');
  const onSubmit: SubmitHandler<any> = useCallback(
    async (data) => {
      let id = params.id!;
      if (params.id === 'new') {
        await chatService.saveSession({ input: data.input, model: modelValue, database_id: databaseValue }).then((v) => {
          id = v.data;
          navigate(`../${id}`, { relative: 'path', replace: true });
        });
        chatService.initList();
      }

      chatService.sessionHistory.set([
        ...chatService.sessionHistory.get(),
        { session_id: +id, message_content: data.input, message_type: 'user' },
      ]);
      reset();

      chatService.chat({ model: modelValue, database_id: databaseValue, input: data.input, session_id: +id }).then((result) => {
        if (params.id) {
          navigate(`../${id}`, { relative: 'path', replace: true });
        }
        chatService.sessionHistory.set([
          ...chatService.sessionHistory.get(),
          { session_id: +id, message_content: result.data, message_type: modelValue },
        ]);
      });
    },
    [modelValue, databaseValue, params, reset]
  );

  const navigate = useNavigate();

  return (
    <>
      <div className="flex flex-col h-full gap-4">
        <div className="flex gap-4 justify-center mt-2 chat-size">
          <FormControl size="small">
            <InputLabel>选择模型</InputLabel>
            <Select
              className="w-[200px]"
              label="选择模型"
              value={modelValue}
              onChange={(e) => {
                console.log(e);
                setModelChange(e.target.value);
              }}
            >
              {useMemo(
                () =>
                  modelList.map((item, i) => (
                    <MenuItem key={i} value={item.value}>
                      {item.label}
                    </MenuItem>
                  )),
                [modelList]
              )}
            </Select>
          </FormControl>
          <FormControl size="small">
            <InputLabel>选择数据库连接</InputLabel>

            <Select
              className="w-[200px]"
              label="选择数据库连接"
              value={databaseValue}
              onChange={(e) => {
                console.log(e);
                setDatabaseValue(e.target.value);
              }}
              renderValue={(value: any) => {
                let item = databaseList.find((item) => item.id === value);
                return item ? (
                  <div className="flex gap-4 items-center">
                    <div>{item.database_name}</div>
                  </div>
                ) : null;
              }}
            >
              {useMemo(
                () =>
                  databaseList.map((item, i) => (
                    <MenuItem value={item.id} key={i}>
                      <div className="flex gap-4 items-center">
                        <Avatar src={(DATABASE_OBJECT as any)[item.database_type].icon}></Avatar>
                        <div>{item.database_name}</div>
                      </div>
                    </MenuItem>
                  )),
                [databaseList]
              )}
            </Select>
          </FormControl>
        </div>
        <div className="flex-1 overflow-auto custom-scrollbar chat-size">
          {historyList.map((item, index) => {
            return (
              <div key={index}>{item.message_type === 'user' ? <UserChat {...item}></UserChat> : <SystemChat {...item}></SystemChat>}</div>
            );
          })}
        </div>
        <div className="chat-size pb-[36px]">
          <form onSubmit={handleSubmit(onSubmit)}>
            <Paper elevation={2} className="!bg-transparent">
              <FormControl variant="outlined" className="w-full">
                <OutlinedInput
                  {...register('input', { required: true })}
                  placeholder="请输入一条消息"
                  autoComplete="off"
                  endAdornment={
                    <InputAdornment position="end">
                      <IconButton type="submit">
                        <SendIcon />
                      </IconButton>
                    </InputAdornment>
                  }
                />
              </FormControl>
            </Paper>
          </form>
        </div>
      </div>
    </>
  );
}
