import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Avatar from '@mui/material/Avatar';

import { DB_LIST } from '../const';
import Drawer from '@mui/material/Drawer';
import { useState } from 'react';
import Button from '@mui/material/Button';
import AddIcon from '@mui/icons-material/Add';
import Dialog from '@mui/material/Dialog';
import { DatabaseEdit } from './edit';

function DatabaseDetail(inputs: { dbType: string }) {
  const [dialogOpen, setDialogOpen] = useState(false);
  // todo 未知接口类型是一次性返回,还是按照类型按需返回
  return (
    <>
      <Dialog open={dialogOpen}>
        <DatabaseEdit dbType={inputs.dbType} setDialogOpen={setDialogOpen}></DatabaseEdit>
      </Dialog>
      <h2 className="m-4 text-center text-lg">{inputs.dbType}</h2>
      <div className="m-4 w-[400px]">
        {/** 通过列表请求或者读取服务 */}
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={() => {
            setDialogOpen(true);
          }}
          className="w-full"
        >
          创建连接
        </Button>
      </div>
    </>
  );
}

export function Database() {
  const [open, setOpen] = useState(false);
  let [dbType, setDbType] = useState('');
  const toggleDrawer = (newOpen: boolean, type?: string) => () => {
    if (type) {
      setDbType(type);
    }
    setOpen(newOpen);
  };
  return (
    <>
      <Drawer open={open} onClose={toggleDrawer(false)} anchor="right">
        {<DatabaseDetail dbType={dbType}></DatabaseDetail>}
      </Drawer>
      <div className="grid grid-cols-4 gap-4 w-[80%] mx-auto">
        {DB_LIST.map((item, index) => (
          <div key={index} onClick={toggleDrawer(true, item[0])}>
            <Card sx={{ '&:hover': { boxShadow: 6 } }}>
              <CardHeader title={item[1].label} avatar={<Avatar src={item[1].icon}></Avatar>}></CardHeader>
              <CardContent>{item[1].desc}</CardContent>
            </Card>
          </div>
        ))}
      </div>
    </>
  );
}
